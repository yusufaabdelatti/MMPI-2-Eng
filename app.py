import streamlit as st
import requests, smtplib, os, datetime, math
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table,
    TableStyle, HRFlowable, Image as RLImage, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

from scoring_keys import (
    L_SCALE, F_SCALE, FB_SCALE, FP_SCALE, K_SCALE, S_SCALE,
    K_CORRECTIONS,
    HS_SCALE, D_SCALE, HY_SCALE, PD_SCALE, MF_MALE, MF_FEMALE,
    PA_SCALE, PT_SCALE, SC_SCALE, MA_SCALE, SI_SCALE,
    ANX_SCALE, FRS_SCALE, OBS_SCALE, DEP_SCALE, HEA_SCALE, BIZ_SCALE,
    ANG_SCALE, CYN_SCALE, ASP_SCALE, TPA_SCALE, LSE_SCALE, SOD_SCALE,
    FAM_SCALE, WRK_SCALE, TRT_SCALE,
    AGGR_SCALE, PSYC_SCALE, DISC_SCALE, NEGE_SCALE, INTR_SCALE,
    A_SCALE, R_SCALE, MACR_SCALE, ES_SCALE, DO_SCALE, RE_SCALE,
    MT_SCALE, OH_SCALE, APS_SCALE, AAS_SCALE, MDS_SCALE, HO_SCALE, PK_SCALE,
    GM_SCALE, GF_SCALE,
    D1_SUB, D2_SUB, D3_SUB, D4_SUB, D5_SUB,
    HY1_SUB, HY2_SUB, HY3_SUB, HY4_SUB, HY5_SUB,
    PD1_SUB, PD2_SUB, PD3_SUB, PD4_SUB, PD5_SUB,
    PA1_SUB, PA2_SUB, PA3_SUB,
    SC1_SUB, SC2_SUB, SC3_SUB, SC4_SUB, SC5_SUB, SC6_SUB,
    MA1_SUB, MA2_SUB, MA3_SUB, MA4_SUB,
    SI1_SUB, SI2_SUB, SI3_SUB,
    NORMATIVE_DATA, CRITICAL_ITEMS_KB, CRITICAL_ITEMS_LW,
    VRIN_PAIRS, TRIN_TRUE_PAIRS, TRIN_FALSE_PAIRS,
)

# ══════════════════════════════════════════════════════════════
#  CONFIGURATION
# ══════════════════════════════════════════════════════════════

GMAIL_ADDRESS   = "Wijdan.psyc@gmail.com"
GMAIL_PASSWORD  = "rias eeul lyuu stce"
THERAPIST_EMAIL = "Wijdan.psyc@gmail.com"
LOGO_FILE       = "logo.png"

ITEMS_PER_PAGE = 50

# ══════════════════════════════════════════════════════════════
#  MMPI-2 QUESTIONS (567 items, True/False)
# ══════════════════════════════════════════════════════════════

MMPI2_QUESTIONS = [
    "I like mechanics magazines.",
    "I have a good appetite.",
    "I wake up fresh and rested most mornings.",
    "I think I would enjoy the work of a librarian.",
    "I am easily awakened by noise.",
    "My father is a good man (or if your father is dead) my father was a good man.",
    "I like to read newspaper articles on crime.",
    "My hands and feet are usually warm enough.",
    "My daily life is full of things that keep me interested.",
    "I am about as able to work as I ever was.",
    "There seems to be a lump in my throat much of the time.",
    "My sex life is satisfactory.",
    "People should try to understand their dreams and be guided by or take warning from them.",
    "I enjoy detective or mystery stories.",
    "I work under a great deal of tension.",
    "Once in a while I think of things too bad to talk about.",
    "I am sure I get a raw deal from life.",
    "I am troubled by attacks of nausea and vomiting.",
    "When I take a new job, I like to find out whom it is important to be nice to.",
    "I am very seldom bothered by constipation.",
    "At times I have very much wanted to leave home.",
    "No one seems to understand me.",
    "At times I have fits of laughing and crying that I cannot control.",
    "Evil spirits possess me at times.",
    "I would like to be a singer.",
    "I feel that it is certainly best to keep my mouth shut when I am in trouble.",
    "When people do me wrong, I feel I should pay them back, just for the principle of the thing.",
    "I am bothered by an upset stomach several times a week.",
    "At times I feel like swearing.",
    "I have nightmares every few nights.",
    "I find it hard to keep my mind on a task or job.",
    "I have had very peculiar and strange experiences.",
    "I seldom worry about my health.",
    "I have never been in trouble because of my sexual behavior.",
    "Sometimes when I was young I stole things.",
    "I have a cough most of the time.",
    "At times I feel like smashing things.",
    "I have had periods of days, weeks, or months when I couldn't take care of things because I couldn't \"get going\".",
    "My sleep is fitful and disturbed.",
    "Much of the time, my head seems to hurt all over.",
    "I do not always tell the truth.",
    "If people had not had it in for me, I would have been much more successful.",
    "My judgment is better than it ever was.",
    "Once a week (or more often) I suddenly feel hot all over, for no reason.",
    "I am in just as good physical health as most of my friends.",
    "I prefer to pass by school friends, or people I know but have not seen for a long time, unless they speak to me first.",
    "I am almost never bothered by pains over my heart or in my chest.",
    "Most anytime I would rather sit and daydream than do anything else.",
    "I am a very sociable person.",
    "I have often had to take orders from someone who did not know as much as I did.",
    "I do not read every editorial in the newspaper every day.",
    "I have not lived the right kind of life.",
    "Parts of my body often have feelings like burning, tingling, crawling, or like \"going to sleep\".",
    "My family does not like the work I have chosen (or the work I intend to choose for my lifework).",
    "I sometimes keep on at a thing until others lose their patience with me.",
    "I wish I could be as happy as others seem to be.",
    "I hardly ever feel pain in the back of my neck.",
    "I think a great many people exaggerate their misfortunes in order to gain the sympathy and help of others.",
    "I am troubled by discomfort in the pit of my stomach every few days or so.",
    "When I am with people I am bothered by hearing very strange things.",
    "I am an important person.",
    "I have often wished I were a girl. (or if you are a girl) I have never been sorry that I am a girl.",
    "My feelings are not easily hurt.",
    "I enjoy reading love stories.",
    "Most of the time I feel blue.",
    "It would be better if almost all laws were thrown away.",
    "I like poetry.",
    "I sometimes tease animals.",
    "I think I would like the kind of work a forest ranger does.",
    "I am easily downed in an argument.",
    "These days I find it hard not to give up hope of amounting to something.",
    "My soul sometimes leaves my body.",
    "I am certainly lacking in self-confidence.",
    "I would like to be a florist.",
    "I usually feel that life is worthwhile.",
    "It takes a lot of argument to convince most people of the truth.",
    "Once in a while I put off until tomorrow what I ought to do today.",
    "Most people that know me like me.",
    "I do not mind being made fun of.",
    "I would like to be a nurse.",
    "I think most people would lie to get ahead.",
    "I do many things that I regret afterwards. (I regret things more than others seem to.)",
    "I have very few quarrels with members of my family.",
    "I was suspended from school one or more times for bad behavior.",
    "At times, I have a strong urge to do something harmful or shocking.",
    "I like to go to parties and other affairs where there is a lot of loud fun.",
    "I have met problems so full of possibilities that I have been unable to make up my mind about them.",
    "I believe that women ought to have as much sexual freedom as men.",
    "My hardest battles are with myself.",
    "I love my father, or (if your father is dead) I loved my father.",
    "I have little or no trouble with my muscles twitching or jumping.",
    "I don't seem to care what happens to me.",
    "Sometimes when I am not well I am irritable.",
    "Much of the time I feel as if I have done something wrong or evil.",
    "I am happy most of the time.",
    "I see things or animals or people around me that others do not see.",
    "There seems to be a fullness in my head or nose most of the time.",
    "Some people are so bossy that I feel like doing the opposite of what they request, even though I know they are right.",
    "Someone has it in for me.",
    "I have never done anything dangerous just for the thrill of it.",
    "Often I feel as if there is a tight band around my head.",
    "I get angry sometimes.",
    "I enjoy a race or game more when I bet on it.",
    "Most people are honest chiefly because they are afraid of being caught.",
    "In school I was sometimes sent to the principal for bad behavior.",
    "My speech is the same as always (not faster or slower, no slurring or hoarseness).",
    "My table manners are not quite as good at home as when I am out in company.",
    "Anyone who is able and willing to work hard has a good chance of succeeding.",
    "I seem to be about as capable and smart as most others around me.",
    "Most people will use somewhat unfair means to gain profit or an advantage rather than to lose it.",
    "I have a great deal of stomach trouble.",
    "I like dramatics.",
    "I know who is responsible for most of my troubles.",
    "Sometimes I am so strongly attracted by the personal articles of others, such as shoes, gloves, etc., that I want to handle or steal them, even though I have no use for them.",
    "The sight of blood does not frighten me or make me sick.",
    "Often I can't understand why I have been so irritable or grouchy.",
    "I have never vomited blood or coughed up blood.",
    "I do not worry about catching diseases.",
    "I like collecting flowers or growing houseplants.",
    "I frequently find it necessary to stand up for what I think is right.",
    "I have never indulged in unusual sex practices.",
    "At times my thoughts have raced ahead faster than I could speak them.",
    "If I could get into the movies without paying and be sure I was not seen, I would probably do it.",
    "I often wonder what hidden reason another person may have for doing something nice for me.",
    "I believe that my home life is as pleasant as that of most people I know.",
    "I believe in law enforcement.",
    "Criticism or scolding hurts me terribly.",
    "I like to cook.",
    "My conduct is largely controlled by the behavior of those around me.",
    "I certainly feel useless at times.",
    "When I was a child, I belonged to a group of friends that tried to be loyal through all kinds of trouble.",
    "I believe in life hereafter.",
    "I would like to be a soldier.",
    "At times I feel like picking a fistfight with someone.",
    "I have often lost out on things because I couldn't make my mind up soon enough.",
    "It makes me impatient to have people ask my advice or otherwise interrupt me when I am working on something important.",
    "I used to keep a diary.",
    "I believe I am being plotted against.",
    "I would rather win than lose in a game.",
    "Most nights I go to sleep without thoughts or ideas bothering me.",
    "During the past few years I have been well most of the time.",
    "I have never had a fit or convulsion.",
    "I am neither gaining nor losing weight.",
    "I believe I am being followed.",
    "I feel that I have often been punished without cause.",
    "I cry easily.",
    "I cannot understand what I read as often as I used to.",
    "I have never felt better in my life than I do now.",
    "The top of my head sometimes feels tender.",
    "Sometimes I feel as if I must injure either myself or someone else.",
    "I resent having anyone trick me so cleverly that I have to admit that I was fooled.",
    "I do not tire quickly.",
    "I like to know some important people because it makes me feel important.",
    "I am afraid when I look down from a high place.",
    "It wouldn't make me nervous if any members of my family got into trouble with the law.",
    "I am never happy unless I am roaming or traveling around.",
    "What others think of me does not bother me.",
    "It makes me uncomfortable to pull a stunt at a party even when others are doing the same sort of things.",
    "I have never had a fainting spell.",
    "I liked school.",
    "I frequently have to fight against showing that I am bashful.",
    "Someone has been trying to poison me.",
    "I do not have a great fear of snakes.",
    "I seldom or never have dizzy spells.",
    "My memory seems to be all right.",
    "I am worried about sex.",
    "I find it hard to make small talk when I meet new people.",
    "I have had periods in which I carried on activities without knowing later what I had been doing.",
    "When I get bored I like to stir up some excitement.",
    "I am afraid of losing my mind.",
    "I am against giving money to beggars.",
    "I frequently notice my hand shakes when I try to do something.",
    "I can read a long while without tiring my eyes.",
    "I like to study and read about things that I am working at.",
    "I feel weak all over much of the time.",
    "I have very few headaches.",
    "My hands have not become clumsy or awkward.",
    "Sometimes, when embarrassed, I break out in a sweat, which annoys me greatly.",
    "I have had no difficulty in keeping my balance while walking.",
    "There is something wrong with my mind.",
    "I do not have spells of hay fever or asthma.",
    "I have had attacks in which I could not control my movements or speech, but in which I knew what was going on around me.",
    "I do not like everyone I know.",
    "I daydream very little.",
    "I wish I were not so shy.",
    "I am not afraid to handle money.",
    "If I were a reporter, I would very much like to report news of the theater.",
    "I enjoy many different kinds of play and recreation.",
    "I like to flirt.",
    "Many people treat me more like a child than a grown-up.",
    "I would like to be a journalist.",
    "My mother is a good woman, or (if your mother is dead) my mother was a good woman.",
    "In walking, I am very careful to step over sidewalk cracks.",
    "I have never had any breaking out on my skin that has worried me.",
    "There is very little love and companionship in my family as compared to other homes.",
    "I frequently find myself worrying about something.",
    "I think I would like the work of a building contractor.",
    "I often hear voices without knowing where they come from.",
    "I like science.",
    "It is not hard for me to ask for help from my friends even though I cannot return the favor.",
    "I very much like hunting.",
    "My parents often objected to the kind of people I went around with.",
    "I gossip a little at times.",
    "My hearing is apparently as good as that of most people.",
    "Some members of my family have habits that bother and annoy me very much.",
    "At times I feel that I can make up my mind with unusually great ease.",
    "I would like to belong to several clubs.",
    "I hardly ever notice my heart pounding and I am seldom short of breath.",
    "I like to talk about sex.",
    "I like to visit places where I have never been before.",
    "I have been inspired to a program of life based on duty which I have since carefully followed.",
    "I have, at times stood in the way of people who were trying to do something, not because it amounted to much, but because of the principle of the thing.",
    "I get mad easily and then get over it soon.",
    "I have been quite independent and free from family rule.",
    "I brood a great deal.",
    "Someone has been trying to rob me.",
    "My relatives are nearly all in sympathy with me.",
    "I have periods of such great restlessness that I cannot sit long in a chair.",
    "I have been disappointed in love.",
    "I never worry about my looks.",
    "I dream frequently about things that are best kept to myself.",
    "Children should be taught all the main facts of sex.",
    "I believe I am no more nervous than most others.",
    "I have few or no pains.",
    "My way of doing things is apt to be misunderstood by others.",
    "Sometimes without any reason or even when things are going wrong, I feel excitedly happy or \"on top of the world\".",
    "I don't blame people for trying to grab everything they can get in this world.",
    "There are persons who are trying to steal my thoughts and ideas.",
    "I have had blank spells in which my activities were interrupted and I did not know what was going on around me.",
    "I can be friendly with people who do things that I consider wrong.",
    "I like to be with a crowd who play jokes on one another.",
    "Sometimes in elections, I vote for people about whom I know very little.",
    "I have difficulty in starting to do things.",
    "I believe I am a condemned person.",
    "I was a slow learner in school.",
    "If I were an artist, I would like to draw flowers.",
    "It does not bother me that I am not better looking.",
    "I sweat very easily, even on cool days.",
    "I'm entirely self-confident.",
    "At times it has been impossible for me to stop from stealing or shoplifting something.",
    "It is safer to trust nobody.",
    "Once a week or more, I become very excited.",
    "When in a group of people, I have trouble thinking of the right thing to say.",
    "Something exciting will almost always pull me out of it when I am feeling low.",
    "When I leave home, I do not worry about whether the door is locked and the windows are closed.",
    "I believe my sins are unpardonable.",
    "I have numbness in one or more places on my skin.",
    "I do not blame a person for taking advantage of people who leave themselves open to it.",
    "My eyesight is as good as it has been for years.",
    "At times I have been so entertained by the cleverness of some criminals that I have hopes they would get away with it.",
    "I have often felt that strangers were looking at me critically.",
    "Everything tastes the same.",
    "I drink an unusually large amount of water every day.",
    "Most people make friends because friends are likely to be useful to them.",
    "I do not often notice my ears ringing or buzzing.",
    "Once in a while I feel hate toward members of my family whom I usually love.",
    "If I were a reporter I would very much like to report sporting news.",
    "I can sleep during the day, but not at night.",
    "I am sure I am being talked about.",
    "Once in a while, I laugh at a dirty joke.",
    "I have very few fears compared to my friends.",
    "In a group of people, I would not be embarrassed to be called upon to start a discussion or give an opinion about something I know well.",
    "I am always disgusted with the law when a criminal is freed through the arguments of a smart lawyer.",
    "I have used alcohol excessively.",
    "I am likely not to speak to people until they speak to me.",
    "I have never been in trouble with the law.",
    "I have periods in which I feel unusually cheerful without any special reason.",
    "I wish I were not bothered by thoughts about sex.",
    "If several people find themselves in trouble, the best thing for them to do is agree upon a story and stick to it.",
    "It does not bother me particularly to see animals suffer.",
    "I think that I feel more intensely than most people do.",
    "There was never a time in my life when I liked to play with dolls.",
    "Life is a strain for me much of the time.",
    "I am so touchy on some subjects that I can't talk about them.",
    "In school I found it very hard to talk in front of the class.",
    "I love my mother, or (if your mother is dead) I loved my mother.",
    "Even when I am with people I feel lonely much of the time.",
    "I get all the sympathy I should.",
    "I refuse to play some games because I am not good at them.",
    "I seem to make friends about as quickly as others do.",
    "I dislike having people around me.",
    "I have been told that I walk during sleep.",
    "The person who provides temptation by leaving valuable property unprotected is about as much to blame for its theft as the one who steals it.",
    "I think nearly anyone would tell a lie to keep out of trouble.",
    "I am more sensitive than most people.",
    "Most people inwardly dislike putting themselves out to help other people.",
    "Many of my dreams are about sex.",
    "My parents and family find more fault with me than they should.",
    "I am easily embarrassed.",
    "I worry over money and business.",
    "I have never been in love with anyone.",
    "The things that some of my family have done have frightened me.",
    "I almost never dream.",
    "My neck spots with red often.",
    "I have never been paralyzed or had any unusual weakness of any of my muscles.",
    "Sometimes my voice leaves me or changes even though I have no cold.",
    "My mother or father often made me obey even when I thought it was unreasonable.",
    "Peculiar odors come to me at times.",
    "I cannot keep my mind on one thing.",
    "I have reason for feeling jealous of one or more members of my family.",
    "I feel anxiety about something or someone almost all the time.",
    "I easily become impatient with people.",
    "Most of the time I wish I were dead.",
    "Sometimes I become so excited that I find it hard to get to sleep.",
    "I have certainly had more than my share of things to worry about.",
    "No one cares much about what happens to you.",
    "At times I hear so well that it bothers me.",
    "I forget right away what people say to me.",
    "I usually have to stop and think before I act, even in small matters.",
    "Often I cross the street in order not to meet someone I see.",
    "I often feel as if things are not real.",
    "The only interesting part of newspapers is the comic strips.",
    "I have a habit of counting things that are not important, such as bulbs on electric signs and so forth.",
    "I have no enemies who really wish to harm me.",
    "I tend to be on my guard with people who are somewhat friendlier than I had expected.",
    "I have strange and peculiar thoughts.",
    "I get anxious and upset when I have to make a short trip away from home.",
    "I usually expect to succeed in things I do.",
    "I hear strange things when I am alone.",
    "I have been afraid of things or people that I knew could not hurt me.",
    "I have no dread of going into a room by myself where other people have already gathered and are talking.",
    "I am afraid of a knife or anything very sharp or pointed.",
    "Sometimes I enjoy hurting persons I love.",
    "I can easily make other people afraid of me, and sometimes do it for the fun of it.",
    "I have more trouble concentrating than others seem to have.",
    "I have several times given up doing a thing because I thought too little of my ability.",
    "Bad words, often terrible words, come into my mind and I cannot get rid of them.",
    "Sometimes some unimportant thought will run through my mind and bother me for days.",
    "Almost every day something happens to frighten me.",
    "At times I am all full of energy.",
    "I am inclined to take things hard.",
    "At times I have enjoyed being hurt by someone I loved.",
    "People say insulting and vulgar things about me.",
    "I feel uneasy indoors.",
    "I am not usually self-conscious.",
    "Someone has control over my mind.",
    "At parties I am more likely to sit by myself or with just one other person than to join in with the crowd.",
    "People often disappoint me.",
    "I have sometimes felt that difficulties were piling up so high that I could not overcome them.",
    "I love to go to dances.",
    "At periods, my mind seems to work more slowly than usual.",
    "While in trains, busses, etc., I often talk with strangers.",
    "I enjoy children.",
    "I enjoy gambling for small stakes.",
    "If given the chance, I could do some things that would be of great benefit to the world.",
    "I have often met people who were supposed to be experts who were no better than I.",
    "It makes me feel like a failure when I hear of the success of someone I know well.",
    "I often think: \"I wish I were a child again.\"",
    "I am never happier than when alone.",
    "If given the chance I would make a good leader of people.",
    "I am embarrassed by dirty stories.",
    "People generally demand more respect for their own rights than they are willing to allow for others.",
    "I enjoy social gatherings just to be with people.",
    "I try to remember good stories to pass them on to other people.",
    "At one or more times in my life I felt that someone was making me do things by hypnotizing me.",
    "I find it hard to set aside a task that I have undertaken, even for a short time.",
    "I am quite often not in on the gossip and talk of the group that I belong to.",
    "I have often found people jealous of my good ideas, just because they had not thought of them first.",
    "I enjoy the excitement of a crowd.",
    "I do not mind meeting strangers.",
    "Someone has been trying to influence my mind.",
    "I can remember \"playing sick\" to get out of something.",
    "My worries seem to disappear when I get into a crowd of lively friends.",
    "I feel like giving up quickly when things go wrong.",
    "I like to let people know where I stand on things.",
    "I have had periods when I felt so full of pep that sleep did not seem necessary for days at a time.",
    "Whenever possible I avoid being in a crowd.",
    "I shrink from facing a crisis or difficulty.",
    "I am apt to pass up something I want to do when others feel that it isn't worth doing.",
    "I like parties and socials.",
    "I have often wished I were a member of the opposite sex.",
    "I am not easily angered.",
    "I have done some bad things in the past that I never tell anybody about.",
    "Most people will use somewhat unfair means to get ahead in life.",
    "It makes me nervous when people ask me personal questions.",
    "I do not feel I can plan my own future.",
    "I am not happy with myself the way I am.",
    "I get angry when my friends or family give me advice on how to live my life.",
    "I got many beatings when I was a child.",
    "It bothers me when people say nice things about me.",
    "I don't like hearing other people give their opinions about life.",
    "I often have serious disagreements with people who are close to me.",
    "When things get really bad, I know I can count on my family for help.",
    "I liked playing \"house\" when I was a child.",
    "I am not afraid of fire.",
    "I have sometimes stayed away from another person because I feared doing or saying something I might regret afterwards.",
    "I can express my true feelings only when I drink.",
    "I very seldom have spells of the blues.",
    "I am often said to be hotheaded.",
    "I wish I could get over worrying about things I have said that may have injured other people's feelings.",
    "I feel unable to tell anyone all about myself.",
    "Lightning is one of my fears.",
    "I like to keep people guessing what I am going to do next.",
    "My plans have frequently seemed so full of difficulties that I have had to give them up.",
    "I am afraid to be alone in the dark.",
    "I have often felt bad about being misunderstood when trying to keep someone from making a mistake.",
    "A windstorm frightens me.",
    "I frequently ask people for advice.",
    "The future is too uncertain for a person to make serious plans.",
    "Often, even though everything is going fine for me, I feel that I don't care about anything.",
    "I have no fear of water.",
    "I often must sleep over a matter before I decide what to do.",
    "People have often misunderstood my intentions when I was trying to put them right and be helpful.",
    "I have no trouble swallowing.",
    "I am usually calm and not easily upset.",
    "I would certainly enjoy beating criminals at their own game.",
    "I deserve severe punishment for my sins.",
    "I am apt to take disappointments so keenly that I can't put them out of my mind.",
    "It bothers me to have someone watch me at work even though I know I can do it well.",
    "I am often so annoyed when someone tries to get ahead of me in a line of people that I speak to that person about it.",
    "At times I think I am no good at all.",
    "When I was young I often did not go to school even when I should have gone.",
    "One or more members of my family are very nervous.",
    "I have at times had to be rough with people who were rude or annoying.",
    "I worry quite a bit over possible misfortunes.",
    "I have strong political opinions.",
    "I would like to be an auto racer.",
    "It is all right to get around the law if you don't actually break it.",
    "There are certain people whom I dislike so much that I am inwardly pleased when they are catching it for something that they have done.",
    "It makes me nervous to have to wait.",
    "I am apt to pass up something I want to do because others feel that I am not going about it in the right way.",
    "I was fond of excitement when I was young.",
    "I am often inclined to go out of my way to win a point with someone who has opposed me.",
    "I am bothered by people outside, on the streets, in stores, etc., watching me.",
    "The man who had most to do with me when I was a child (such as my father, stepfather, etc.) was very strict with me.",
    "I used to like to play hopscotch and jump rope.",
    "I have never seen a vision.",
    "I have several times had a change of heart about my lifework.",
    "Except by doctor's orders I never take drugs or sleeping pills.",
    "I am often sorry because I am so irritable and grouchy.",
    "In school my marks in classroom behavior were quite regularly bad.",
    "I am fascinated by fire.",
    "When I am cornered I tell that portion of the truth which is not likely to hurt me.",
    "If I were in trouble with several friends who were as guilty as I was, I would rather take the whole blame than give them away.",
    "I am often afraid of the dark.",
    "When a man is with a woman he is usually thinking about things related to her sex.",
    "I am usually very direct with people I am trying to correct or improve.",
    "I dread the thought of an earthquake.",
    "I readily become one hundred percent sold on a good idea.",
    "I usually work things out for myself rather than get someone to show me how.",
    "I am afraid of finding myself in a closet or small closed space.",
    "I must admit that I have at times been worried beyond reason over something that really did not matter.",
    "I do not try to cover up my poor opinion or pity of people so that they won't know how I feel.",
    "I am a high-strung person.",
    "I have frequently worked under people who seem to have things arranged so that they get credit for good work but are able to pass mistakes onto those under them.",
    "I sometimes find it hard to stick up for my rights because I am so reserved.",
    "Dirt frightens or disgusts me.",
    "I have a daydream life about which I do not tell other people.",
    "Some of my family members have quick tempers.",
    "I cannot do anything well.",
    "I often feel guilty because I pretend to feel more sorry about something than I really do.",
    "I strongly defend my own opinions as a rule.",
    "I have no fear of spiders.",
    "The future seems hopeless to me.",
    "The members of my family and my close relatives get along quite well.",
    "I would like to wear expensive clothes.",
    "People can pretty easily change my mind, even when I have made a decision about something.",
    "I am made nervous by certain animals.",
    "I can stand as much pain as others can.",
    "Several times I have been the last to give up trying to do a thing.",
    "It makes me angry to have people hurry me.",
    "I am not afraid of mice.",
    "Several times a week I feel as if something dreadful is about to happen.",
    "I feel tired a good deal of the time.",
    "I like repairing a door latch.",
    "Sometimes I am sure that other people can tell what I am thinking.",
    "I like to read about science.",
    "I am afraid of being alone in a wide-open place.",
    "I sometimes feel that I am about to go to pieces.",
    "A large number of people are guilty of bad sexual conduct.",
    "I have often been frightened in the middle of the night.",
    "I am greatly bothered by forgetting where I put things.",
    "The one to whom I was most attached and whom I most admired as a child was a woman (mother, sister, aunt, or other woman).",
    "I like adventure stories better than romantic stories.",
    "Often I get confused and forget what I want to say.",
    "I am very awkward and clumsy.",
    "I really like playing sports (such as soccer or football).",
    "I hate my whole family.",
    "Some people think it's hard to get to know me.",
    "I spend most of my spare time by myself.",
    "When people do something that makes me angry, I let them know how I feel about it.",
    "I usually have a hard time deciding what to do.",
    "People do not find me attractive.",
    "People are not very kind to me.",
    "I often feel that I'm not as good as other people.",
    "I am very stubborn.",
    "I have enjoyed using marijuana.",
    "Mental illness is a sign of weakness.",
    "I have a drug or alcohol problem.",
    "Ghost or spirits can influence people for good or bad.",
    "I feel helpless when I have to make some important decisions.",
    "I always try to be pleasant even when others are upset or critical.",
    "When I have a problem it helps to talk it over with someone.",
    "My main goals in life are within my reach.",
    "I believe that people should keep personal problems to themselves.",
    "I am not feeling much pressure or stress these days.",
    "It bothers me greatly to think of making changes in my life.",
    "My greatest problems are caused by the behavior of someone close to me.",
    "I hate going to doctors, even when I'm sick.",
    "Although I am not happy with my life, there is nothing I can do about it.",
    "Talking over problems and worries with someone is often more helpful than taking drugs or medicine.",
    "I have habits that are really harmful.",
    "When problems need to be solved, I usually let other people take charge.",
    "I recognize several faults in myself that I will not be able to change.",
    "I am so sick of what I have to do every day that I just want to get out of it all.",
    "I have recently considered killing myself.",
    "I often become very irritable when people interrupt my work.",
    "I often feel I can read other people's minds.",
    "Having to make important decisions makes me nervous.",
    "Others tell me I eat too fast.",
    "Once a week or more I get high or drunk.",
    "I have had a tragic loss in my life that I know I will never get over.",
    "Sometimes I get so angry and upset I don't know what comes over me.",
    "When people ask me to do something I have a hard time saying no.",
    "I am never happier than when I am by myself.",
    "My life is empty and meaningless.",
    "I find it difficult to hold down a job.",
    "I have made lots of bad mistakes in my life.",
    "I get angry with myself for giving in to other people so much.",
    "Lately I have thought a lot about killing myself.",
    "I like making decisions and assigning jobs to others.",
    "Even without my family I know there will always be someone there to take care of me.",
    "At movies, restaurants, or sporting events, I hate to stand in line.",
    "No one knows it but I have tried to kill myself.",
    "Everything is going on too fast around me.",
    "I know I am a burden to others.",
    "After a bad day, I need a few drinks to relax.",
    "Much of the trouble I'm having is due to bad luck.",
    "At times I can't seem to stop talking.",
    "Sometimes I cut or injure myself on purpose without knowing why.",
    "I work very long hours, even though my job doesn't require this.",
    "I usually feel better after a good cry.",
    "I forget where I leave things.",
    "If I could live my life over again, I would not change much.",
    "I get very irritable when people I depend on don't get their work done on time.",
    "If I get upset, I'm sure to get a headache.",
    "I like to drive a hard bargain.",
    "Most men are unfaithful to their wives now and then.",
    "Lately I have lost my desire to work out my problems.",
    "I have gotten angry and broken furniture or dishes when I was drinking.",
    "I work best when I have a definite deadline.",
    "I have become so angry with someone that I have felt as if I would explode.",
    "Terrible thoughts about my family come to me at times.",
    "People tell me I have a problem with alcohol, but I disagree.",
    "I always have too little time to get things done.",
    "My thoughts these days turn more and more to death and the hereafter.",
    "I often keep and save things that I will probably never use.",
    "I have been so angry at times that I've hurt someone in a physical fight.",
    "In everything I do lately, I feel that I am being tested.",
    "I have very little to do with my relatives now.",
    "I sometimes seem to hear my thoughts being spoken out loud.",
    "When I am sad, visiting with friends can always pull me out of it.",
    "Much of what is happening to me now seems to have happened to me before.",
    "When my life gets difficult, it makes me want to just give up.",
    "I can't go into a dark room alone, even in my own home.",
    "I worry a great deal over money.",
    "The man should be the head of the family.",
    "The only place where I feel relaxed is in my own home.",
    "The people I work with are not sympathetic with my problems.",
    "I am satisfied with the amount of money I make.",
    "I usually have enough energy to do my work.",
    "It is hard for me to accept compliments.",
    "In most marriages one or both partners are unhappy.",
    "I almost never lose self-control.",
    "It takes a great deal of effort for me to remember what people tell me these days.",
    "When I am sad or blue, it is my work that suffers.",
    "Most married couples don't show much affection for each other.",
]

# ══════════════════════════════════════════════════════════════
#  SCORING ENGINE
# ══════════════════════════════════════════════════════════════

def score_scale(responses: dict, scale_key: dict) -> int:
    """Count items scored in the keyed direction."""
    total = 0
    for item, keyed_true in scale_key.items():
        if item in responses:
            answered_true = responses[item]  # True or False
            if answered_true == keyed_true:
                total += 1
    return total

def raw_to_t(raw, scale_name: str, gender: str) -> int:
    """Convert raw score to approximate T-score using linear conversion."""
    if raw is None:
        return 50
    if scale_name not in NORMATIVE_DATA:
        return 50
    norm = NORMATIVE_DATA[scale_name]
    if len(norm) < 4:
        return 50
    m, sd, f_m, f_sd = norm
    mean = m if gender == "Male" else f_m
    sd_v = sd if gender == "Male" else f_sd
    if not sd_v:
        return 50
    t = 50 + 10 * (raw - mean) / sd_v
    return max(20, min(120, round(t)))

def compute_vrin(responses: dict) -> int:
    """Compute VRIN raw score."""
    score = 0
    for pair in VRIN_PAIRS:
        i1, i2, pattern = pair
        if i1 in responses and i2 in responses:
            r1 = responses[i1]
            r2 = responses[i2]
            if pattern == "TF" and r1 is True and r2 is False:
                score += 1
            elif pattern == "FT" and r1 is False and r2 is True:
                score += 1
    return score

def compute_trin(responses: dict) -> int:
    """Compute TRIN raw score (base 9, add for TT pairs, subtract for FF pairs)."""
    score = 9
    for i1, i2 in TRIN_TRUE_PAIRS:
        if i1 in responses and i2 in responses:
            if responses[i1] is True and responses[i2] is True:
                score += 1
    for i1, i2 in TRIN_FALSE_PAIRS:
        if i1 in responses and i2 in responses:
            if responses[i1] is False and responses[i2] is False:
                score -= 1
    return max(0, score)

def compute_all_scores(responses: dict, gender: str) -> dict:
    """Compute all MMPI-2 scores from raw responses."""
    r = responses

    # Validity
    cannot_say = sum(1 for v in r.values() if v is None)
    l_raw  = score_scale(r, L_SCALE)
    f_raw  = score_scale(r, F_SCALE)
    fb_raw = score_scale(r, FB_SCALE)
    fp_raw = score_scale(r, FP_SCALE)
    k_raw  = score_scale(r, K_SCALE)
    s_raw  = score_scale(r, S_SCALE)
    vrin_raw = compute_vrin(r)
    trin_raw = compute_trin(r)

    # Clinical (raw, pre-K)
    hs_raw = score_scale(r, HS_SCALE)
    d_raw  = score_scale(r, D_SCALE)
    hy_raw = score_scale(r, HY_SCALE)
    pd_raw = score_scale(r, PD_SCALE)
    mf_key = MF_MALE if gender == "Male" else MF_FEMALE
    mf_raw = score_scale(r, mf_key)
    pa_raw = score_scale(r, PA_SCALE)
    pt_raw = score_scale(r, PT_SCALE)
    sc_raw = score_scale(r, SC_SCALE)
    ma_raw = score_scale(r, MA_SCALE)
    si_raw = score_scale(r, SI_SCALE)

    # K-corrected raws
    hs_k = hs_raw + round(K_CORRECTIONS["Hs"] * k_raw)
    pd_k = pd_raw + round(K_CORRECTIONS["Pd"] * k_raw)
    pt_k = pt_raw + round(K_CORRECTIONS["Pt"] * k_raw)
    sc_k = sc_raw + round(K_CORRECTIONS["Sc"] * k_raw)
    ma_k = ma_raw + round(K_CORRECTIONS["Ma"] * k_raw)

    # T-scores for clinical (using K-corrected where applicable)
    def ct(raw, name): return raw_to_t(raw, name, gender)

    scores = {
        # Validity raw
        "cannot_say": cannot_say,
        "L_raw": l_raw, "F_raw": f_raw, "Fb_raw": fb_raw,
        "Fp_raw": fp_raw, "K_raw": k_raw, "S_raw": s_raw,
        "VRIN_raw": vrin_raw, "TRIN_raw": trin_raw,
        # Validity T
        "L_T":   ct(l_raw,   "L"),
        "F_T":   ct(f_raw,   "F"),
        "Fb_T":  ct(fb_raw,  "Fb"),
        "Fp_T":  ct(fp_raw,  "Fp"),
        "K_T":   ct(k_raw,   "K"),
        "S_T":   ct(s_raw,   "S"),
        "VRIN_T": ct(vrin_raw, "VRIN"),
        "TRIN_T": ct(trin_raw, "TRIN"),
        # Clinical raw
        "Hs_raw": hs_raw, "D_raw": d_raw, "Hy_raw": hy_raw,
        "Pd_raw": pd_raw, "Mf_raw": mf_raw, "Pa_raw": pa_raw,
        "Pt_raw": pt_raw, "Sc_raw": sc_raw, "Ma_raw": ma_raw,
        "Si_raw": si_raw,
        # K-corrected raw
        "Hs_k": hs_k, "Pd_k": pd_k, "Pt_k": pt_k,
        "Sc_k": sc_k, "Ma_k": ma_k,
        # Clinical T (K-corrected where appropriate)
        "Hs_T": ct(hs_k, "Hs"), "D_T":  ct(d_raw,  "D"),
        "Hy_T": ct(hy_raw,"Hy"), "Pd_T": ct(pd_k,   "Pd"),
        "Mf_T": ct(mf_raw, "Mf_M" if gender=="Male" else "Mf_F"),
        "Pa_T": ct(pa_raw, "Pa"), "Pt_T": ct(pt_k,   "Pt"),
        "Sc_T": ct(sc_k,   "Sc"), "Ma_T": ct(ma_k,   "Ma"),
        "Si_T": ct(si_raw, "Si"),
        # F-K index
        "FK_index": f_raw - k_raw,
    }

    # Content scales
    for name, key in [
        ("ANX",ANX_SCALE),("FRS",FRS_SCALE),("OBS",OBS_SCALE),
        ("DEP",DEP_SCALE),("HEA",HEA_SCALE),("BIZ",BIZ_SCALE),
        ("ANG",ANG_SCALE),("CYN",CYN_SCALE),("ASP",ASP_SCALE),
        ("TPA",TPA_SCALE),("LSE",LSE_SCALE),("SOD",SOD_SCALE),
        ("FAM",FAM_SCALE),("WRK",WRK_SCALE),("TRT",TRT_SCALE),
    ]:
        raw = score_scale(r, key)
        scores[f"{name}_raw"] = raw
        scores[f"{name}_T"]   = ct(raw, name)

    # PSY-5
    for name, key in [
        ("AGGR",AGGR_SCALE),("PSYC",PSYC_SCALE),("DISC",DISC_SCALE),
        ("NEGE",NEGE_SCALE),("INTR",INTR_SCALE),
    ]:
        raw = score_scale(r, key)
        scores[f"{name}_raw"] = raw
        scores[f"{name}_T"]   = ct(raw, name)

    # Supplementary
    for name, key in [
        ("A",A_SCALE),("R",R_SCALE),("MAC_R",MACR_SCALE),
        ("Es",ES_SCALE),("Do",DO_SCALE),("Re",RE_SCALE),
        ("Mt",MT_SCALE),("OH",OH_SCALE),("APS",APS_SCALE),
        ("AAS",AAS_SCALE),("MDS",MDS_SCALE),("Ho",HO_SCALE),
        ("PK",PK_SCALE),("GM",GM_SCALE),("GF",GF_SCALE),
    ]:
        raw = score_scale(r, key)
        scores[f"{name}_raw"] = raw
        scores[f"{name}_T"]   = ct(raw, name)

    # Harris-Lingoes
    for name, key in [
        ("D1",D1_SUB),("D2",D2_SUB),("D3",D3_SUB),("D4",D4_SUB),("D5",D5_SUB),
        ("Hy1",HY1_SUB),("Hy2",HY2_SUB),("Hy3",HY3_SUB),("Hy4",HY4_SUB),("Hy5",HY5_SUB),
        ("Pd1",PD1_SUB),("Pd2",PD2_SUB),("Pd3",PD3_SUB),("Pd4",PD4_SUB),("Pd5",PD5_SUB),
        ("Pa1",PA1_SUB),("Pa2",PA2_SUB),("Pa3",PA3_SUB),
        ("Sc1",SC1_SUB),("Sc2",SC2_SUB),("Sc3",SC3_SUB),
        ("Sc4",SC4_SUB),("Sc5",SC5_SUB),("Sc6",SC6_SUB),
        ("Ma1",MA1_SUB),("Ma2",MA2_SUB),("Ma3",MA3_SUB),("Ma4",MA4_SUB),
        ("Si1",SI1_SUB),("Si2",SI2_SUB),("Si3",SI3_SUB),
    ]:
        raw = score_scale(r, key)
        scores[f"{name}_raw"] = raw
        scores[f"{name}_T"]   = ct(raw, name)

    # Critical items
    critical_kb = {}
    for cat, items in CRITICAL_ITEMS_KB.items():
        flagged = []
        for item in items:
            if item in r:
                # Most critical items score True direction
                if r[item] is True:
                    flagged.append(item)
        if flagged:
            critical_kb[cat] = flagged
    scores["critical_kb"] = critical_kb

    critical_lw = {}
    for cat, items in CRITICAL_ITEMS_LW.items():
        flagged = [i for i in items if i in r and r[i] is True]
        if flagged:
            critical_lw[cat] = flagged
    scores["critical_lw"] = critical_lw

    # Profile elevation (mean of clinical scales > 44)
    clinical_ts = [scores[f"{s}_T"] for s in
                   ["Hs","D","Hy","Pd","Mf","Pa","Pt","Sc","Ma","Si"]]
    elevated = [t for t in clinical_ts if t > 44]
    scores["profile_elevation"] = round(sum(elevated)/len(elevated), 1) if elevated else 50.0

    # Welsh Code
    scale_order = [
        ("Hs",1),("D",2),("Hy",3),("Pd",4),("Mf",5),
        ("Pa",6),("Pt",7),("Sc",8),("Ma",9),("Si",0),
    ]
    sorted_scales = sorted(scale_order, key=lambda x: scores[f"{x[0]}_T"], reverse=True)
    codes = "".join(str(n) for _, n in sorted_scales)
    def elev_sym(t):
        if t>=120: return "!!"
        elif t>=110: return "!"
        elif t>=100: return "**"
        elif t>=90: return "*"
        elif t>=80: return '"'
        elif t>=70: return "'"
        elif t>=60: return "-"
        elif t>=50: return "/"
        elif t>=40: return ":"
        elif t>=30: return "#"
        else: return "#"
    prev_t = None
    welsh = ""
    for i,(s,n) in enumerate(sorted_scales):
        t = scores[f"{s}_T"]
        if prev_t is not None and prev_t != t:
            sym = elev_sym(prev_t)
            welsh += sym
        welsh += str(n)
        prev_t = t
    welsh += elev_sym(prev_t)
    scores["welsh_code"] = welsh

    # High-point pair
    top2 = sorted_scales[:2]
    scores["high_point_pair"] = f"{top2[0][1]}-{top2[1][1]}"

    return scores

# ══════════════════════════════════════════════════════════════
#  VALIDITY INTERPRETATION
# ══════════════════════════════════════════════════════════════

def check_validity(scores: dict) -> dict:
    flags = []
    valid = True

    if scores["cannot_say"] >= 30:
        flags.append("INVALID: Cannot Say ≥ 30 items omitted. Protocol should not be interpreted.")
        valid = False
    elif scores["cannot_say"] >= 10:
        flags.append(f"CAUTION: {scores['cannot_say']} items omitted. Interpret with caution.")

    vrin_t = scores["VRIN_T"]
    if vrin_t >= 80:
        flags.append(f"INVALID: VRIN T={vrin_t} — inconsistent random responding. Protocol invalid.")
        valid = False
    elif vrin_t >= 70:
        flags.append(f"CAUTION: VRIN T={vrin_t} — possible inconsistent responding.")

    trin_t = scores["TRIN_T"]
    if trin_t >= 80:
        flags.append(f"CAUTION: TRIN T={trin_t} — acquiescence or nay-saying response set detected.")

    f_t = scores["F_T"]
    if f_t >= 100:
        flags.append(f"CAUTION: F T={f_t} — possible random responding, faking bad, or severe psychopathology.")
    elif f_t >= 80:
        flags.append(f"NOTE: F T={f_t} — possible symptom exaggeration or genuine severe distress.")

    l_t = scores["L_T"]
    if l_t >= 65:
        flags.append(f"NOTE: L T={l_t} — overly virtuous presentation; possible defensiveness.")

    k_t = scores["K_T"]
    if k_t >= 65:
        flags.append(f"NOTE: K T={k_t} — defensive responding; possible underreporting of symptoms.")

    fk = scores["FK_index"]
    if fk > 9:
        flags.append(f"NOTE: F-K index = {fk} (>9) — possible symptom exaggeration.")
    elif fk < -9:
        flags.append(f"NOTE: F-K index = {fk} (<-9) — possible symptom minimization.")

    return {"valid": valid, "flags": flags}

# ══════════════════════════════════════════════════════════════
#  GROQ REPORT GENERATION
# ══════════════════════════════════════════════════════════════

def generate_report(client_name: str, age: str, gender: str, scores: dict, validity: dict) -> str:
    clinical = {
        "Hs (Scale 1)": scores["Hs_T"],
        "D (Scale 2)":  scores["D_T"],
        "Hy (Scale 3)": scores["Hy_T"],
        "Pd (Scale 4)": scores["Pd_T"],
        "Mf (Scale 5)": scores["Mf_T"],
        "Pa (Scale 6)": scores["Pa_T"],
        "Pt (Scale 7)": scores["Pt_T"],
        "Sc (Scale 8)": scores["Sc_T"],
        "Ma (Scale 9)": scores["Ma_T"],
        "Si (Scale 0)": scores["Si_T"],
    }
    content = {s: scores[f"{s}_T"] for s in
               ["ANX","FRS","OBS","DEP","HEA","BIZ","ANG","CYN","ASP","TPA","LSE","SOD","FAM","WRK","TRT"]}
    psy5 = {s: scores[f"{s}_T"] for s in ["AGGR","PSYC","DISC","NEGE","INTR"]}
    supp = {s: scores[f"{s}_T"] for s in ["A","R","MAC_R","Es","Do","Re","Mt","OH","APS","AAS","PK","Ho"]}

    elevated_clinical = {k:v for k,v in clinical.items() if v >= 65}
    elevated_content  = {k:v for k,v in content.items() if v >= 65}

    validity_summary = "\n".join(validity["flags"]) if validity["flags"] else "No significant validity concerns."

    prompt = f"""You are a licensed clinical psychologist writing a confidential MMPI-2 assessment report.

IMPORTANT DISCLAIMER: This is a research/training simulation. Scoring is approximate.
All findings should be treated as hypotheses only, not clinical conclusions.

CLIENT: {client_name}
AGE: {age}
GENDER: {gender}
ASSESSMENT: Minnesota Multiphasic Personality Inventory-2 (MMPI-2)
DATE: {datetime.datetime.now().strftime("%B %d, %Y")}

VALIDITY SCALE SUMMARY:
VRIN T={scores["VRIN_T"]} | TRIN T={scores["TRIN_T"]} | F T={scores["F_T"]} | Fb T={scores["Fb_T"]}
L T={scores["L_T"]} | K T={scores["K_T"]} | S T={scores["S_T"]}
F-K Index: {scores["FK_index"]}
{validity_summary}

CLINICAL SCALES (T-scores, clinically elevated ≥65):
{chr(10).join(f"  Scale {k}: T={v}" for k,v in clinical.items())}

HIGH-POINT PAIR: {scores["high_point_pair"]}
WELSH CODE: {scores["welsh_code"]}
PROFILE ELEVATION: {scores["profile_elevation"]}

ELEVATED CONTENT SCALES (T≥65):
{chr(10).join(f"  {k}: T={v}" for k,v in elevated_content.items()) if elevated_content else "  None elevated"}

PSY-5 SCALES:
{chr(10).join(f"  {k}: T={v}" for k,v in psy5.items())}

SUPPLEMENTARY SCALES:
{chr(10).join(f"  {k}: T={v}" for k,v in supp.items())}

HARRIS-LINGOES ELEVATED (T≥65):
{chr(10).join(f"  {s}: T={scores[s+'_T']}" for s in ["D1","D2","D3","D4","D5","Hy1","Hy2","Hy3","Hy4","Hy5","Pd1","Pd2","Pd3","Pd4","Pd5","Pa1","Pa2","Pa3","Sc1","Sc2","Sc3","Sc4","Sc5","Sc6","Ma1","Ma2","Ma3","Ma4","Si1","Si2","Si3"] if scores[s+"_T"] >= 65) or "  None elevated"}

Write a comprehensive professional MMPI-2 assessment report with these sections:

SECTION A — VALIDITY AND RESPONSE STYLE
Discuss the validity indicators. Is the protocol interpretable? Describe the client's approach to the assessment.

SECTION B — CLINICAL SCALE ANALYSIS
Discuss the clinical profile. Address the high-point pair and all elevated scales (T≥65). Describe clinical implications, behavioral correlates, and diagnostic considerations.

SECTION C — HARRIS-LINGOES SUBSCALE ANALYSIS
Interpret any elevated Harris-Lingoes subscales to clarify the elevated clinical scales.

SECTION D — CONTENT SCALE ANALYSIS
Discuss elevated content scales and their clinical significance.

SECTION E — PSY-5 AND SUPPLEMENTARY SCALES
Discuss PSY-5 personality dimensions and key supplementary scale findings.

SECTION F — INTEGRATED CLINICAL FORMULATION
Synthesize all findings into a coherent personality and psychopathology picture. Note diagnostic hypotheses.

SECTION G — TREATMENT IMPLICATIONS
Evidence-based treatment recommendations arising from the profile.

SECTION H — SUMMARY
One concise paragraph for clinical records.

Use formal clinical language. Reference specific T-scores. Note that scoring is approximate for research/training.
Do not reproduce the scoring guides verbatim. Label each section exactly as above."""

    api_key = st.secrets.get("GROQ_API_KEY", "")
    if not api_key:
        raise ValueError("GROQ_API_KEY is missing from Streamlit secrets.")

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={"model": "llama-3.3-70b-versatile",
              "messages": [{"role": "user", "content": prompt}],
              "max_tokens": 3500, "temperature": 0.4},
        timeout=120,
    )
    if not response.ok:
        try:    ed = response.json()
        except: ed = response.text
        raise Exception(f"Groq API error {response.status_code}: {ed}")
    return response.json()["choices"][0]["message"]["content"].strip()

# ══════════════════════════════════════════════════════════════
#  PDF CREATION
# ══════════════════════════════════════════════════════════════

def create_pdf(path, client_name, age, gender, scores, validity, report_text):
    DARK   = colors.HexColor("#1C1917")
    WARM   = colors.HexColor("#6B5B45")
    LIGHT  = colors.HexColor("#F7F3EE")
    BORDER = colors.HexColor("#DDD5C8")
    RED    = colors.HexColor("#B71C1C")
    BLUE   = colors.HexColor("#1A5CB8")
    GREEN  = colors.HexColor("#2E7D32")
    ORANGE = colors.HexColor("#E65100")

    def t_color(t):
        if t is None: return DARK
        if t >= 80: return RED
        elif t >= 65: return ORANGE
        elif t <= 40: return BLUE
        return DARK

    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=2*cm, rightMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)

    title_s  = ParagraphStyle("T", fontName="Times-Roman",      fontSize=18, textColor=DARK, alignment=TA_CENTER, spaceAfter=3)
    sub_s    = ParagraphStyle("S", fontName="Times-Italic",      fontSize=10, textColor=WARM, alignment=TA_CENTER, spaceAfter=2)
    meta_s   = ParagraphStyle("M", fontName="Helvetica",         fontSize=8,  textColor=WARM, alignment=TA_CENTER, spaceAfter=10)
    sec_s    = ParagraphStyle("Se",fontName="Helvetica-Bold",    fontSize=10, textColor=WARM, spaceBefore=12, spaceAfter=4)
    body_s   = ParagraphStyle("B", fontName="Helvetica",         fontSize=9.5,textColor=DARK, leading=15, spaceAfter=5)
    small_s  = ParagraphStyle("Sm",fontName="Helvetica",         fontSize=8,  textColor=WARM, leading=12)
    warn_s   = ParagraphStyle("W", fontName="Helvetica-Bold",    fontSize=9,  textColor=RED,  leading=14, spaceAfter=4)
    footer_s = ParagraphStyle("F", fontName="Helvetica-Oblique", fontSize=7,  textColor=WARM, leading=10, alignment=TA_CENTER)

    story = []
    date_str = datetime.datetime.now().strftime("%B %d, %Y  |  %H:%M")

    if os.path.exists(LOGO_FILE):
        try:
            logo = RLImage(LOGO_FILE, width=3.5*cm, height=1.8*cm)
            logo.hAlign = "CENTER"
            story.append(logo); story.append(Spacer(1, 0.2*cm))
        except: pass

    story += [
        Paragraph("Minnesota Multiphasic Personality Inventory-2", title_s),
        Paragraph("MMPI-2 — Extended Score Report (Research/Training Simulation)", sub_s),
        Paragraph(f"CONFIDENTIAL  ·  {date_str}", meta_s),
        HRFlowable(width="100%", thickness=1, color=BORDER), Spacer(1, 0.3*cm),
    ]

    # Disclaimer box
    story.append(Paragraph(
        "⚠  RESEARCH/TRAINING SIMULATION ONLY — Scoring is approximate based on published academic literature. "
        "Not validated for clinical use. Do not use for real diagnostic or treatment decisions.",
        ParagraphStyle("D", fontName="Helvetica-Bold", fontSize=8, textColor=RED,
                       backColor=colors.HexColor("#FFF3F3"), leading=12,
                       borderPad=6, spaceAfter=8)
    ))

    # Client info
    info_data = [
        [Paragraph("<b>Client</b>", small_s), Paragraph(client_name, body_s),
         Paragraph("<b>Age</b>", small_s), Paragraph(age, body_s),
         Paragraph("<b>Gender</b>", small_s), Paragraph(gender, body_s)],
        [Paragraph("<b>Assessment</b>", small_s), Paragraph("MMPI-2 (567 items)", body_s),
         Paragraph("<b>Date</b>", small_s), Paragraph(date_str, body_s),
         Paragraph("<b>Welsh Code</b>", small_s), Paragraph(scores["welsh_code"], body_s)],
    ]
    it = Table(info_data, colWidths=[2.5*cm, 4.5*cm, 1.5*cm, 2*cm, 2.5*cm, 4*cm])
    it.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),LIGHT),("BOX",(0,0),(-1,-1),0.5,BORDER),
        ("INNERGRID",(0,0),(-1,-1),0.3,BORDER),
        ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),
        ("LEFTPADDING",(0,0),(-1,-1),8),
    ]))
    story += [it, Spacer(1, 0.3*cm)]

    # Validity flags
    if validity["flags"]:
        story.append(Paragraph("VALIDITY FLAGS", sec_s))
        story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER))
        for flag in validity["flags"]:
            story.append(Paragraph(f"• {flag}", warn_s))
        story.append(Spacer(1, 0.2*cm))

    # Validity scales table
    story.append(Paragraph("VALIDITY SCALES", sec_s))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER))
    story.append(Spacer(1, 0.2*cm))

    def bar_str(t, width=20):
        if t is None: t = 50
        filled = max(0, min(width, int(((t-20)/100)*width)))
        hex_c = "#D9534F" if t>=80 else "#F0AD4E" if t>=65 else "#4A90D9" if t<=40 else "#4CAF50"
        return f'<font color="{hex_c}">{"█"*filled}</font><font color="#CCCCCC">{"░"*(width-filled)}</font>'

    val_rows = [[Paragraph("<b>Scale</b>",small_s), Paragraph("<b>Raw</b>",small_s),
                 Paragraph("<b>T</b>",small_s), Paragraph("<b>Profile</b>",small_s)]]
    for name, rk, tk in [
        ("VRIN","VRIN_raw","VRIN_T"),("TRIN","TRIN_raw","TRIN_T"),
        ("F","F_raw","F_T"),("Fb","Fb_raw","Fb_T"),("Fp","Fp_raw","Fp_T"),
        ("L","L_raw","L_T"),("K","K_raw","K_T"),("S","S_raw","S_T"),
    ]:
        t = scores.get(tk) or 50; raw = scores.get(rk) or 0
        val_rows.append([
            Paragraph(name, small_s),
            Paragraph(str(raw), ParagraphStyle("v",fontName="Helvetica",fontSize=8,alignment=TA_CENTER)),
            Paragraph(f"<b>{t}</b>", ParagraphStyle("vt",fontName="Helvetica-Bold",fontSize=9,textColor=t_color(t),alignment=TA_CENTER)),
            Paragraph(bar_str(t), ParagraphStyle("vb",fontName="Courier",fontSize=7)),
        ])
    vt = Table(val_rows, colWidths=[2.5*cm, 1.5*cm, 1.5*cm, 11.5*cm])
    vt.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#EDE9E3")),
        ("BOX",(0,0),(-1,-1),0.5,BORDER),("INNERGRID",(0,0),(-1,-1),0.3,BORDER),
        ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("LEFTPADDING",(0,0),(-1,-1),6),("ALIGN",(1,0),(2,-1),"CENTER"),
    ]))
    story += [vt, Spacer(1, 0.4*cm)]

    # Clinical scales
    story.append(Paragraph("CLINICAL SCALES", sec_s))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER))
    story.append(Spacer(1, 0.2*cm))

    clin_data = [
        ("1 — Hs  Hypochondriasis",     "Hs_T", "Hs_k"),
        ("2 — D   Depression",           "D_T",  "D_raw"),
        ("3 — Hy  Hysteria",             "Hy_T", "Hy_raw"),
        ("4 — Pd  Psychopathic Deviate", "Pd_T", "Pd_k"),
        ("5 — Mf  Masculinity-Femininity","Mf_T","Mf_raw"),
        ("6 — Pa  Paranoia",             "Pa_T", "Pa_raw"),
        ("7 — Pt  Psychasthenia",        "Pt_T", "Pt_k"),
        ("8 — Sc  Schizophrenia",        "Sc_T", "Sc_k"),
        ("9 — Ma  Hypomania",            "Ma_T", "Ma_k"),
        ("0 — Si  Social Introversion",  "Si_T", "Si_raw"),
    ]
    clin_rows = [[Paragraph("<b>Scale</b>",small_s), Paragraph("<b>Raw</b>",small_s),
                  Paragraph("<b>T</b>",small_s), Paragraph("<b>Profile (20–120)</b>",small_s)]]
    for label, tk, rk in clin_data:
        t = scores.get(tk) or 50; raw = scores.get(rk) or 0
        clin_rows.append([
            Paragraph(label, small_s),
            Paragraph(str(raw), ParagraphStyle("c",fontName="Helvetica",fontSize=8,alignment=TA_CENTER)),
            Paragraph(f"<b>{t}</b>", ParagraphStyle("ct",fontName="Helvetica-Bold",fontSize=9,textColor=t_color(t),alignment=TA_CENTER)),
            Paragraph(bar_str(t), ParagraphStyle("cb",fontName="Courier",fontSize=7)),
        ])
    ct_table = Table(clin_rows, colWidths=[5.5*cm, 1.5*cm, 1.5*cm, 8.5*cm])
    ct_table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#EDE9E3")),
        ("BOX",(0,0),(-1,-1),0.5,BORDER),("INNERGRID",(0,0),(-1,-1),0.3,BORDER),
        ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("LEFTPADDING",(0,0),(-1,-1),6),("ALIGN",(1,0),(2,-1),"CENTER"),
    ]))
    for i, (_, tk, _) in enumerate(clin_data, 1):
        if (scores.get(tk) or 0) >= 65:
            ct_table.setStyle(TableStyle([("BACKGROUND",(0,i),(-1,i),colors.HexColor("#FFF3F3"))]))
    story += [ct_table, Spacer(1, 0.3*cm)]
    story.append(Paragraph(
        f"Profile Elevation: {scores['profile_elevation']}  |  High-Point Pair: {scores['high_point_pair']}  |  Welsh Code: {scores['welsh_code']}  |  F-K Index: {scores['FK_index']}",
        ParagraphStyle("pe", fontName="Helvetica", fontSize=8, textColor=WARM, leading=11)
    ))
    story += [Spacer(1, 0.4*cm), PageBreak()]

    # Content scales
    story.append(Paragraph("CONTENT SCALES", sec_s))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER))
    story.append(Spacer(1, 0.2*cm))

    cont_scales = ["ANX","FRS","OBS","DEP","HEA","BIZ","ANG","CYN","ASP","TPA","LSE","SOD","FAM","WRK","TRT"]
    cont_labels = {
        "ANX":"Anxiety","FRS":"Fears","OBS":"Obsessiveness","DEP":"Depression",
        "HEA":"Health Concerns","BIZ":"Bizarre Mentation","ANG":"Anger",
        "CYN":"Cynicism","ASP":"Antisocial Practices","TPA":"Type A",
        "LSE":"Low Self-Esteem","SOD":"Social Discomfort","FAM":"Family Problems",
        "WRK":"Work Interference","TRT":"Negative Treatment Indicators",
    }
    cont_rows = [[Paragraph("<b>Scale</b>",small_s), Paragraph("<b>Raw</b>",small_s),
                  Paragraph("<b>T</b>",small_s), Paragraph("<b>Profile</b>",small_s)]]
    for s in cont_scales:
        t = scores.get(f"{s}_T") or 50; raw = scores.get(f"{s}_raw") or 0
        cont_rows.append([
            Paragraph(f"{s} — {cont_labels[s]}", small_s),
            Paragraph(str(raw), ParagraphStyle("d",fontName="Helvetica",fontSize=8,alignment=TA_CENTER)),
            Paragraph(f"<b>{t}</b>", ParagraphStyle("dt",fontName="Helvetica-Bold",fontSize=9,textColor=t_color(t),alignment=TA_CENTER)),
            Paragraph(bar_str(t), ParagraphStyle("db",fontName="Courier",fontSize=7)),
        ])
    cont_t = Table(cont_rows, colWidths=[5.5*cm, 1.5*cm, 1.5*cm, 8.5*cm])
    cont_t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#EDE9E3")),
        ("BOX",(0,0),(-1,-1),0.5,BORDER),("INNERGRID",(0,0),(-1,-1),0.3,BORDER),
        ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("LEFTPADDING",(0,0),(-1,-1),6),("ALIGN",(1,0),(2,-1),"CENTER"),
    ]))
    for i, s in enumerate(cont_scales, 1):
        if (scores.get(f"{s}_T") or 0) >= 65:
            cont_t.setStyle(TableStyle([("BACKGROUND",(0,i),(-1,i),colors.HexColor("#FFF3F3"))]))
    story += [cont_t, Spacer(1, 0.4*cm)]

    # Supplementary + PSY-5 side by side
    story.append(Paragraph("SUPPLEMENTARY & PSY-5 SCALES", sec_s))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER))
    story.append(Spacer(1, 0.2*cm))

    supp_list = [("A","Anxiety"),("R","Repression"),("MAC_R","MacAndrew Alcoholism-R"),
                 ("Es","Ego Strength"),("Do","Dominance"),("Re","Social Responsibility"),
                 ("Mt","College Maladjustment"),("OH","Overcontrolled Hostility"),
                 ("APS","Addiction Potential"),("AAS","Addiction Acknowledgment"),
                 ("MDS","Marital Distress"),("Ho","Cook-Medley Hostility"),("PK","PTSD-Keane"),
                 ("GM","Masculine Gender Role"),("GF","Feminine Gender Role")]
    psy5_list = [("AGGR","Aggressiveness"),("PSYC","Psychoticism"),("DISC","Disconstraint"),
                 ("NEGE","Neg Emotionality/Neuroticism"),("INTR","Introversion/Low Pos Emotion")]

    supp_rows = [[Paragraph("<b>Scale</b>",small_s),Paragraph("<b>Raw</b>",small_s),Paragraph("<b>T</b>",small_s)]]
    for s, lbl in supp_list:
        t = scores.get(f"{s}_T") or 50; raw = scores.get(f"{s}_raw") or 0
        supp_rows.append([
            Paragraph(f"{s} — {lbl}", small_s),
            Paragraph(str(raw), ParagraphStyle("sr",fontName="Helvetica",fontSize=8,alignment=TA_CENTER)),
            Paragraph(f"<b>{t}</b>", ParagraphStyle("st",fontName="Helvetica-Bold",fontSize=9,textColor=t_color(t),alignment=TA_CENTER)),
        ])
    psy5_rows = [[Paragraph("<b>PSY-5 Scale</b>",small_s),Paragraph("<b>Raw</b>",small_s),Paragraph("<b>T</b>",small_s)]]
    for s, lbl in psy5_list:
        t = scores.get(f"{s}_T") or 50; raw = scores.get(f"{s}_raw") or 0
        psy5_rows.append([
            Paragraph(f"{s} — {lbl}", small_s),
            Paragraph(str(raw), ParagraphStyle("pr",fontName="Helvetica",fontSize=8,alignment=TA_CENTER)),
            Paragraph(f"<b>{t}</b>", ParagraphStyle("pt",fontName="Helvetica-Bold",fontSize=9,textColor=t_color(t),alignment=TA_CENTER)),
        ])

    st_t = Table(supp_rows, colWidths=[5*cm, 1.2*cm, 1.2*cm])
    st_t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#EDE9E3")),
        ("BOX",(0,0),(-1,-1),0.5,BORDER),("INNERGRID",(0,0),(-1,-1),0.3,BORDER),
        ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
        ("LEFTPADDING",(0,0),(-1,-1),5),("ALIGN",(1,0),(2,-1),"CENTER"),
    ]))
    p5_t = Table(psy5_rows, colWidths=[5.5*cm, 1.2*cm, 1.2*cm])
    p5_t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#EDE9E3")),
        ("BOX",(0,0),(-1,-1),0.5,BORDER),("INNERGRID",(0,0),(-1,-1),0.3,BORDER),
        ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
        ("LEFTPADDING",(0,0),(-1,-1),5),("ALIGN",(1,0),(2,-1),"CENTER"),
    ]))
    combo = Table([[st_t, Spacer(0.3*cm,1), p5_t]], colWidths=[7.5*cm, 0.3*cm, 9.2*cm])
    story += [combo, Spacer(1, 0.4*cm), PageBreak()]

    # Harris-Lingoes
    story.append(Paragraph("HARRIS-LINGOES SUBSCALES", sec_s))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER))
    story.append(Spacer(1, 0.2*cm))

    hl_groups = {
        "Depression": [("D1","Subjective Depression"),("D2","Psychomotor Retardation"),
                       ("D3","Physical Malfunctioning"),("D4","Mental Dullness"),("D5","Brooding")],
        "Hysteria":   [("Hy1","Denial of Social Anxiety"),("Hy2","Need for Affection"),
                       ("Hy3","Lassitude-Malaise"),("Hy4","Somatic Complaints"),("Hy5","Inhibition of Aggression")],
        "Psychopathic Deviate": [("Pd1","Familial Discord"),("Pd2","Authority Problems"),
                                  ("Pd3","Social Imperturbability"),("Pd4","Social Alienation"),("Pd5","Self-Alienation")],
        "Paranoia":   [("Pa1","Persecutory Ideas"),("Pa2","Poignancy"),("Pa3","Naivete")],
        "Schizophrenia": [("Sc1","Social Alienation"),("Sc2","Emotional Alienation"),
                           ("Sc3","Lack of Ego Mastery-Cognitive"),("Sc4","Lack of Ego Mastery-Conative"),
                           ("Sc5","Lack of Ego Mastery-Defective Inhibition"),("Sc6","Bizarre Sensory Experiences")],
        "Hypomania":  [("Ma1","Amorality"),("Ma2","Psychomotor Acceleration"),
                       ("Ma3","Imperturbability"),("Ma4","Ego Inflation")],
        "Social Introversion": [("Si1","Shyness/Self-Consciousness"),("Si2","Social Avoidance"),
                                  ("Si3","Alienation-Self and Others")],
    }
    hl_rows = [[Paragraph("<b>Subscale</b>",small_s),Paragraph("<b>Raw</b>",small_s),Paragraph("<b>T</b>",small_s)]]
    for group, items in hl_groups.items():
        hl_rows.append([Paragraph(f"<b>{group}</b>", ParagraphStyle("gg",fontName="Helvetica-Bold",fontSize=8,textColor=WARM)), "", ""])
        for code, lbl in items:
            t = scores.get(f"{code}_T") or 50; raw = scores.get(f"{code}_raw") or 0
            hl_rows.append([
                Paragraph(f"  {code} — {lbl}", small_s),
                Paragraph(str(raw), ParagraphStyle("hr",fontName="Helvetica",fontSize=8,alignment=TA_CENTER)),
                Paragraph(f"<b>{t}</b>", ParagraphStyle("ht",fontName="Helvetica-Bold",fontSize=9,textColor=t_color(t),alignment=TA_CENTER)),
            ])
    hl_t = Table(hl_rows, colWidths=[10*cm, 1.5*cm, 1.5*cm])
    hl_style = [
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#EDE9E3")),
        ("BOX",(0,0),(-1,-1),0.5,BORDER),("INNERGRID",(0,0),(-1,-1),0.3,BORDER),
        ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
        ("LEFTPADDING",(0,0),(-1,-1),6),("ALIGN",(1,0),(2,-1),"CENTER"),
        ("SPAN",(0,1),(2,1)),
    ]
    hl_t.setStyle(TableStyle(hl_style))
    story += [hl_t, Spacer(1, 0.4*cm), PageBreak()]

    # Critical Items
    if scores["critical_kb"] or scores["critical_lw"]:
        story.append(Paragraph("CRITICAL ITEMS", sec_s))
        story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER))
        story.append(Spacer(1, 0.2*cm))
        story.append(Paragraph(
            "Items below were endorsed in the clinically significant direction. "
            "Caution: single-item responses are unreliable. Use for hypothesis generation only.",
            ParagraphStyle("ci", fontName="Helvetica-Oblique", fontSize=8, textColor=WARM, leading=12, spaceAfter=6)
        ))
        for cat, items in scores["critical_kb"].items():
            story.append(Paragraph(f"<b>Koss-Butcher — {cat}:</b>  Items {', '.join(str(i) for i in items)}", body_s))
        for cat, items in scores["critical_lw"].items():
            story.append(Paragraph(f"<b>Lachar-Wrobel — {cat}:</b>  Items {', '.join(str(i) for i in items)}", body_s))
        story += [Spacer(1, 0.3*cm), PageBreak()]

    # AI Clinical Report
    story.append(Paragraph("CLINICAL REPORT", sec_s))
    story.append(HRFlowable(width="100%", thickness=1, color=BORDER))
    story.append(Spacer(1, 0.2*cm))

    for line in report_text.split("\n"):
        line = line.strip()
        if not line: story.append(Spacer(1, 0.15*cm))
        elif line.startswith("SECTION") or (line.isupper() and len(line) < 60):
            story.append(Paragraph(line, sec_s))
            story.append(HRFlowable(width="100%", thickness=0.4, color=BORDER))
        else:
            story.append(Paragraph(line, body_s))

    story += [
        Spacer(1, 0.5*cm),
        HRFlowable(width="100%", thickness=0.5, color=BORDER),
        Spacer(1, 0.2*cm),
        Paragraph(
            "RESEARCH/TRAINING SIMULATION — Scoring reconstructed from published academic sources. "
            "Approximate only. Not validated for clinical use. "
            "This report is confidential and for the treating clinician only.",
            footer_s
        ),
    ]
    doc.build(story)

# ══════════════════════════════════════════════════════════════
#  EMAIL
# ══════════════════════════════════════════════════════════════

def send_email(pdf_path, client_name, scores, filename):
    date_str = datetime.datetime.now().strftime("%B %d, %Y at %H:%M")
    elevated = [(s, scores[f"{s}_T"]) for s in
                ["Hs","D","Hy","Pd","Mf","Pa","Pt","Sc","Ma","Si"]
                if scores[f"{s}_T"] >= 65]
    elev_html = "".join(
        f"<tr><td style='padding:4px 0;color:#6B5B45;'>Scale {s}</td><td><strong style='color:#D9534F;'>T={t}</strong></td></tr>"
        for s, t in elevated
    ) or "<tr><td colspan='2' style='color:#4CAF50;'>No clinical scales elevated ≥ 65</td></tr>"

    msg = MIMEMultipart("mixed")
    msg["From"] = GMAIL_ADDRESS; msg["To"] = THERAPIST_EMAIL
    msg["Subject"] = f"[MMPI-2 Report] {client_name} — {date_str}"
    body_html = f"""<html><body style="font-family:Georgia,serif;color:#1C1917;background:#F7F3EE;padding:24px;">
      <div style="max-width:580px;margin:0 auto;background:white;border:1px solid #DDD5C8;border-radius:4px;padding:32px;">
        <h2 style="font-weight:300;font-size:20px;margin-bottom:2px;">MMPI-2 Assessment Report</h2>
        <p style="color:#B71C1C;font-size:11px;margin-top:0;font-style:italic;">Research/Training Simulation — Not for clinical use</p>
        <hr style="border:none;border-top:1px solid #DDD5C8;margin:16px 0;">
        <table style="width:100%;font-size:13px;border-collapse:collapse;">
          <tr><td style="padding:5px 0;color:#6B5B45;width:40%;">Client</td><td><strong>{client_name}</strong></td></tr>
          <tr><td style="padding:5px 0;color:#6B5B45;">Date</td><td>{date_str}</td></tr>
          <tr><td style="padding:5px 0;color:#6B5B45;">High-Point Pair</td><td><strong>{scores["high_point_pair"]}</strong></td></tr>
          <tr><td style="padding:5px 0;color:#6B5B45;">Profile Elevation</td><td>{scores["profile_elevation"]}</td></tr>
          <tr><td style="padding:5px 0;color:#6B5B45;">Welsh Code</td><td><code>{scores["welsh_code"]}</code></td></tr>
        </table>
        <hr style="border:none;border-top:1px solid #DDD5C8;margin:16px 0;">
        <p style="font-size:12px;color:#6B5B45;font-weight:bold;">Elevated Clinical Scales (T≥65)</p>
        <table style="width:100%;font-size:12px;border-collapse:collapse;">{elev_html}</table>
        <hr style="border:none;border-top:1px solid #DDD5C8;margin:16px 0;">
        <p style="font-size:12px;line-height:1.6;">Full report attached as PDF.</p>
        <p style="font-size:10px;color:#6B5B45;font-style:italic;">Confidential — treating clinician only.</p>
      </div></body></html>"""
    msg.attach(MIMEText(body_html, "html"))
    with open(pdf_path, "rb") as f:
        part = MIMEBase("application","octet-stream"); part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f'attachment; filename="{filename}"')
    msg.attach(part)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as srv:
        srv.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
        srv.sendmail(GMAIL_ADDRESS, THERAPIST_EMAIL, msg.as_string())

# ══════════════════════════════════════════════════════════════
#  STREAMLIT UI
# ══════════════════════════════════════════════════════════════

st.set_page_config(page_title="MMPI-2 Assessment", page_icon="🧠",
                   layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500&family=Jost:wght@300;400;500&display=swap');
:root{--cream:#F7F3EE;--deep:#1C1917;--warm:#8B7355;--accent:#C4956A;--border:#DDD5C8;--selected:#2D2926;}
#MainMenu{visibility:hidden!important;display:none!important;}
header[data-testid="stHeader"]{visibility:hidden!important;display:none!important;}
footer{visibility:hidden!important;display:none!important;}
[data-testid="stToolbar"],[data-testid="stDecoration"],[data-testid="stStatusWidget"],[data-testid="stActionButton"]{display:none!important;}
a[href*="streamlit.io"]{display:none!important;}
[class*="viewerBadge"],[class*="ProfileBadge"]{display:none!important;}
html,body,[data-theme="dark"],[data-theme="light"]{color-scheme:light only!important;}
[data-testid="stAppViewContainer"],.stApp{background-color:#F7F3EE!important;color:#1C1917!important;}
html,body,[class*="css"]{font-family:'Jost',sans-serif;background-color:var(--cream);color:var(--deep);}
.stApp{background-color:var(--cream);}
.page-header{text-align:center;padding:2.5rem 0 1.5rem 0;border-bottom:1px solid var(--border);margin-bottom:1.5rem;}
.page-header h1{font-family:'Cormorant Garamond',serif;font-size:2.2rem;font-weight:300;margin-bottom:0.3rem;}
.page-header p{color:var(--warm);font-size:0.82rem;letter-spacing:0.08em;}
.q-card{background:white;border:1px solid var(--border);border-radius:4px;padding:1.2rem 1.5rem 0.5rem;margin-bottom:0.8rem;}
.q-num{font-size:0.68rem;font-weight:500;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);margin-bottom:0.3rem;}
.q-text{font-family:'Cormorant Garamond',serif;font-size:1.05rem;color:var(--deep);line-height:1.5;margin-bottom:0.8rem;}
div[data-testid="stRadio"]>label{display:none;}
div[data-testid="stRadio"]>div{gap:0.4rem!important;flex-direction:row!important;flex-wrap:wrap!important;}
div[data-testid="stRadio"]>div>label{background:var(--cream)!important;border:1px solid var(--border)!important;border-radius:20px!important;padding:0.4rem 1.2rem!important;cursor:pointer!important;font-size:0.85rem!important;color:var(--deep)!important;font-family:'Jost',sans-serif!important;transition:all 0.15s ease!important;white-space:nowrap!important;}
div[data-testid="stRadio"]>div>label:hover{border-color:var(--accent)!important;background:#FDF9F4!important;}
.progress-wrap{background:var(--border);border-radius:2px;height:3px;margin:1rem 0 0.5rem;}
.progress-fill{height:3px;border-radius:2px;background:linear-gradient(90deg,var(--warm),var(--accent));}
.stButton>button{background:var(--selected)!important;color:var(--cream)!important;border:none!important;padding:0.75rem 2.5rem!important;font-family:'Jost',sans-serif!important;font-size:0.82rem!important;font-weight:500!important;letter-spacing:0.1em!important;text-transform:uppercase!important;border-radius:2px!important;transition:background 0.2s!important;}
.stButton>button:hover{background:var(--warm)!important;}
.thank-you{text-align:center;padding:5rem 2rem;}
.thank-you h2{font-family:'Cormorant Garamond',serif;font-size:2.2rem;font-weight:300;margin-bottom:1rem;}
.thank-you p{color:var(--warm);font-size:0.95rem;max-width:420px;margin:0 auto;line-height:1.8;}
div[data-testid="stTextInput"] input,div[data-testid="stSelectbox"] div{background:white!important;border:1px solid var(--border)!important;border-radius:3px!important;font-family:'Jost',sans-serif!important;}
</style>""", unsafe_allow_html=True)

page = st.query_params.get("page", "client")

# ── ADMIN ──────────────────────────────────────────────────────
if page == "admin":
    st.markdown('<div class="page-header"><p>Therapist Portal</p><h1>MMPI-2 Reports</h1></div>', unsafe_allow_html=True)
    if "admin_auth" not in st.session_state: st.session_state.admin_auth = False
    if not st.session_state.admin_auth:
        pwd = st.text_input("Admin password", type="password", placeholder="Password")
        if st.button("Access Portal"):
            if pwd == st.secrets.get("ADMIN_PASSWORD",""):
                st.session_state.admin_auth = True; st.rerun()
            else: st.error("Incorrect password.")
    else:
        reports_dir = "reports"
        os.makedirs(reports_dir, exist_ok=True)
        files = sorted([f for f in os.listdir(reports_dir) if f.endswith(".pdf")], reverse=True)
        if not files: st.info("No reports yet.")
        else:
            st.markdown(f"**{len(files)} report(s)**")
            for fname in files:
                c1,c2 = st.columns([3,1])
                with c1: st.markdown(f"📄 `{fname}`")
                with c2:
                    with open(os.path.join(reports_dir,fname),"rb") as f:
                        st.download_button("Download",data=f,file_name=fname,mime="application/pdf",key=fname)
        if st.button("Log out"): st.session_state.admin_auth=False; st.rerun()

# ── CLIENT ──────────────────────────────────────────────────────
else:
    if "submitted" not in st.session_state: st.session_state.submitted = False
    if "current_page" not in st.session_state: st.session_state.current_page = 0
    if "responses" not in st.session_state: st.session_state.responses = {}

    total_pages = math.ceil(567 / ITEMS_PER_PAGE)

    if st.session_state.submitted:
        st.markdown("""<div class="thank-you">
            <h2>Thank You</h2>
            <p>Your responses have been submitted successfully.<br>
            Your clinician will be in touch with you shortly.</p>
        </div>""", unsafe_allow_html=True)
        if st.session_state.get("email_error"):
            st.warning(f"Report saved but email failed: {st.session_state.email_error}")
    else:
        if os.path.exists(LOGO_FILE):
            c1,c2,c3 = st.columns([1,2,1])
            with c2: st.image(LOGO_FILE, use_container_width=True)

        st.markdown("""<div class="page-header">
            <p>Confidential Psychological Assessment</p>
            <h1>MMPI-2</h1>
            <p>Minnesota Multiphasic Personality Inventory-2</p>
        </div>""", unsafe_allow_html=True)

        # Client info — only on first page
        if st.session_state.current_page == 0:
            st.markdown("""<p style="font-size:0.88rem;color:#8B7355;text-align:center;
                margin-bottom:1.5rem;line-height:1.8;">
                This questionnaire contains 567 statements. For each one, indicate whether it is
                <strong>True</strong> or <strong>False</strong> as applied to you.<br>
                Answer every statement. If unsure, choose what is <em>most</em> true for you.
            </p>""", unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)
            with col1:
                client_name = st.text_input("Your name (optional)", placeholder="First name or initials",
                                            key="client_name_input")
                if any('\u0600' <= c <= '\u06ff' for c in (client_name or "")):
                    st.markdown('<div style="color:#D9534F;font-size:0.82rem;">⚠ Please enter your name in English only.</div>', unsafe_allow_html=True)
            with col2:
                age = st.text_input("Age", placeholder="e.g., 35", key="age_input")
            with col3:
                gender = st.selectbox("Gender", ["— Select —", "Male", "Female"], key="gender_input")

        # Questions for current page
        cp = st.session_state.current_page
        start_idx = cp * ITEMS_PER_PAGE
        end_idx   = min(start_idx + ITEMS_PER_PAGE, 567)
        page_questions = list(enumerate(MMPI2_QUESTIONS[start_idx:end_idx], start=start_idx + 1))

        st.markdown(f"<br>", unsafe_allow_html=True)

        page_all_answered = True
        for item_num, q_text in page_questions:
            st.markdown(f"""<div class="q-card">
                <div class="q-num">Item {item_num} of 567</div>
                <div class="q-text">{q_text}</div>
            </div>""", unsafe_allow_html=True)

            prev = st.session_state.responses.get(item_num)
            prev_idx = None
            if prev is True: prev_idx = 0
            elif prev is False: prev_idx = 1

            choice = st.radio("", ["True", "False"], index=prev_idx,
                              key=f"item_{item_num}", horizontal=True,
                              label_visibility="collapsed")
            if choice is None:
                page_all_answered = False
            else:
                st.session_state.responses[item_num] = (choice == "True")

        # Progress
        answered = len(st.session_state.responses)
        pct = int((answered / 567) * 100)
        st.markdown(f"""<div style="text-align:center;font-size:0.78rem;color:#8B7355;
                        letter-spacing:0.06em;margin-top:1rem;">
            {answered} of 567 answered  ·  Page {cp+1} of {total_pages}
        </div>
        <div class="progress-wrap">
            <div class="progress-fill" style="width:{pct}%"></div>
        </div>""", unsafe_allow_html=True)

        # Navigation
        col_prev, col_mid, col_next = st.columns([1, 2, 1])
        with col_prev:
            if cp > 0:
                if st.button("← Previous"):
                    st.session_state.current_page -= 1; st.rerun()
        with col_next:
            if cp < total_pages - 1:
                if st.button("Next →"):
                    st.session_state.current_page += 1; st.rerun()

        # Final submit on last page
        if cp == total_pages - 1:
            all_answered_total = len(st.session_state.responses) == 567
            client_name = st.session_state.get("client_name_input","") or ""
            has_arabic  = any('\u0600' <= c <= '\u06ff' for c in client_name)
            gender_val  = st.session_state.get("gender_input","— Select —")

            if not all_answered_total:
                st.markdown(f"""<div style="background:#FFF8F0;border-left:3px solid #E07B39;
                    padding:1rem 1.2rem;border-radius:0 4px 4px 0;font-size:0.88rem;
                    color:#7A3D1A;margin:1rem 0;">
                    ⚠ Please answer all 567 items before submitting.
                    ({567 - len(st.session_state.responses)} remaining)
                </div>""", unsafe_allow_html=True)

            st.markdown('<div style="text-align:center;padding:2rem 0;">', unsafe_allow_html=True)
            submit = st.button("Submit Assessment", disabled=not all_answered_total)
            st.markdown('</div>', unsafe_allow_html=True)

            if submit and has_arabic:
                st.markdown("""<div style="background:#FFF0F0;border-left:3px solid #D9534F;
                    padding:1rem 1.2rem;border-radius:0 4px 4px 0;font-size:0.9rem;
                    color:#7A1A1A;margin:0.5rem 0;font-weight:500;">
                    ⚠ Please enter your name in English only.
                </div>""", unsafe_allow_html=True)

            if submit and all_answered_total and not has_arabic:
                with st.spinner("Processing your responses..."):
                    g = gender_val if gender_val != "— Select —" else "Male"
                    scores = compute_all_scores(st.session_state.responses, g)
                    validity = check_validity(scores)
                    report = generate_report(
                        client_name or "Anonymous",
                        st.session_state.get("age_input","") or "Not provided",
                        g, scores, validity
                    )
                    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    sn = (client_name or "anonymous").replace(" ","_").lower()
                    fname = f"MMPI2_{sn}_{ts}.pdf"
                    os.makedirs("reports", exist_ok=True)
                    pdf_path = os.path.join("reports", fname)
                    try:
                        create_pdf(pdf_path, client_name or "Anonymous",
                                   st.session_state.get("age_input","") or "N/A",
                                   g, scores, validity, report)
                    except Exception as e:
                        st.error(f"PDF error: {e}"); st.stop()

                    email_error = None
                    try:
                        send_email(pdf_path, client_name or "Anonymous", scores, fname)
                    except Exception as e:
                        email_error = str(e)

                    st.session_state.submitted   = True
                    st.session_state.email_error = email_error
                    st.rerun()
