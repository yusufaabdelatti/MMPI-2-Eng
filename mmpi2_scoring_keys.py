# ══════════════════════════════════════════════════════════════
# MMPI-2 SCORING KEYS
# Reconstructed from published academic literature:
# Graham (2000), Butcher et al. (1989,1990), Harkness et al. (1995)
# Tellegen et al. (2003), and peer-reviewed sources.
# FOR RESEARCH/TRAINING USE ONLY — NOT FOR CLINICAL DECISIONS
# ══════════════════════════════════════════════════════════════

# Format: {item_number: True}  = item scores when answered TRUE
#         {item_number: False} = item scores when answered FALSE

# ── VALIDITY SCALES ────────────────────────────────────────────

L_SCALE = {
    15:False,45:False,75:False,105:False,135:False,
    165:False,195:False,225:False,255:False,285:False,
    315:False,345:False,375:False,405:False,435:False,
}

F_SCALE = {
    18:True,24:True,30:True,36:True,42:True,48:True,54:True,
    60:True,66:True,72:True,84:True,96:True,102:True,108:False,
    114:True,138:True,144:True,150:True,156:True,162:True,
    168:True,180:True,186:True,192:True,198:True,204:True,
    210:True,216:True,222:True,228:True,234:True,240:True,
    246:True,252:True,258:True,264:True,270:True,276:False,
    282:True,288:True,294:True,300:True,306:True,312:True,
    318:False,324:True,330:False,336:True,342:False,348:True,
    354:False,360:False,366:True,372:False,378:True,384:False,
    390:True,
}

FB_SCALE = {
    281:True,291:True,303:True,311:True,317:True,319:True,
    322:True,323:True,329:True,332:True,333:True,334:True,
    336:True,355:True,361:True,374:True,383:False,399:True,
    400:True,407:True,408:True,411:True,416:False,419:True,
    420:True,423:True,424:True,428:True,430:True,431:True,
    432:True,433:True,438:True,439:True,441:True,444:True,
    447:True,448:True,450:True,454:True,
}

FP_SCALE = {
    66:True,114:True,162:True,192:True,216:True,228:True,
    252:True,270:True,282:True,291:True,294:True,322:True,
    323:True,336:True,355:True,361:True,374:True,408:True,
    419:True,422:False,432:True,433:True,439:True,447:True,
    448:True,469:True,506:True,
}

K_SCALE = {
    83:True,105:False,109:True,111:False,117:True,124:False,
    135:False,140:True,148:True,160:False,183:False,217:True,
    218:False,229:False,233:False,243:False,262:True,265:False,
    267:False,272:True,275:False,276:True,278:True,280:True,
    284:False,290:False,338:False,339:False,341:False,346:False,
}

S_SCALE = {
    89:False,107:True,116:True,119:True,120:False,139:False,
    148:True,160:False,169:False,174:True,181:True,183:False,
    186:True,187:True,203:False,206:True,212:False,213:False,
    217:True,220:True,224:True,227:False,230:True,237:True,
    260:False,262:True,267:False,272:True,275:False,280:True,
    284:False,290:False,302:False,303:False,309:True,317:False,
    318:True,320:False,330:False,333:False,338:False,339:False,
    341:False,345:True,352:False,354:False,358:False,370:True,
    379:False,394:False,
}

K_CORRECTIONS = {"Hs":0.5,"Pd":0.4,"Pt":1.0,"Sc":1.0,"Ma":0.2}

# ── CLINICAL SCALES ─────────────────────────────────────────────

HS_SCALE = {
    23:False,29:True,43:False,45:False,47:False,57:False,
    91:False,97:True,101:True,111:True,133:False,141:False,
    142:False,143:False,144:False,151:False,152:False,153:False,
    164:False,173:False,175:True,176:False,179:False,181:False,
    194:False,204:False,208:False,224:False,247:True,249:False,
    255:False,295:False,
}

D_SCALE = {
    2:True,3:False,5:True,9:False,10:False,20:False,22:True,
    26:True,29:True,30:True,31:True,32:False,37:True,38:True,
    39:True,40:True,41:True,46:True,48:True,49:True,52:True,
    57:True,58:True,59:True,60:False,61:False,65:True,67:False,
    70:True,71:True,73:True,75:False,76:False,79:False,82:True,
    84:True,86:False,87:True,89:True,92:True,93:False,94:True,
    95:False,98:False,107:False,111:True,130:True,145:False,
    152:True,167:True,168:True,182:False,189:False,193:True,
    215:True,233:True,273:True,
}

HY_SCALE = {
    10:False,12:False,23:False,29:True,43:False,44:True,45:False,
    47:False,56:False,57:False,58:True,59:False,63:False,67:False,
    72:False,79:False,91:False,97:True,101:True,103:False,
    107:False,108:False,109:False,111:True,112:True,115:False,
    119:False,120:True,125:False,129:False,136:False,141:False,
    142:False,143:False,148:False,149:True,151:False,152:False,
    153:False,157:False,158:False,159:False,160:False,161:True,
    167:False,172:True,173:False,174:False,175:True,176:False,
    179:False,185:False,193:True,195:False,201:False,208:False,
    213:False,224:False,230:True,243:False,
}

PD_SCALE = {
    17:True,21:True,22:True,31:True,32:False,33:False,35:True,
    37:True,38:True,39:True,41:True,42:True,52:True,54:True,
    56:True,71:True,77:False,79:False,81:True,82:True,84:True,
    85:True,87:True,92:True,94:True,96:True,98:False,99:True,
    103:True,104:True,105:True,110:True,123:True,127:True,
    129:True,134:True,145:True,155:False,160:False,166:False,
    167:True,185:True,196:True,202:True,213:True,214:True,
    215:True,216:True,224:False,239:False,
}

MF_MALE = {
    4:False,25:True,44:True,64:True,67:True,69:False,74:True,
    77:True,79:True,80:True,87:True,88:True,92:False,103:False,
    106:False,107:True,112:True,114:False,115:True,116:False,
    117:False,118:False,119:True,120:False,121:False,122:True,
    127:True,128:True,129:False,131:True,137:True,140:False,
    149:True,156:True,160:True,163:True,166:True,167:False,
    172:True,178:False,179:False,187:True,188:False,189:True,
    193:True,194:False,197:False,199:False,200:True,201:False,
    207:True,209:True,210:True,211:True,213:False,214:False,
}

MF_FEMALE = {
    4:False,25:False,44:False,64:False,67:False,69:True,74:False,
    77:False,79:False,80:False,87:False,88:False,92:True,103:True,
    106:True,107:False,112:False,114:True,115:False,116:True,
    117:True,118:True,119:False,120:True,121:True,122:False,
    127:False,128:False,129:True,131:False,137:False,140:True,
    149:False,156:False,160:False,163:False,166:False,167:True,
    172:False,178:True,179:True,187:False,188:True,189:False,
    193:False,194:True,197:True,199:True,200:False,201:True,
    207:False,209:False,210:False,211:False,213:True,214:True,
}

PA_SCALE = {
    17:True,22:True,23:False,24:True,42:True,99:True,100:False,
    104:True,106:False,110:True,113:True,124:True,127:True,
    129:True,136:True,138:True,141:False,144:True,145:True,
    146:True,162:True,163:False,215:True,216:True,228:True,
    241:True,246:True,254:True,259:True,271:True,277:True,
    285:False,286:False,314:False,315:False,333:True,336:True,
    355:True,361:True,466:True,
}

PT_SCALE = {
    11:True,15:True,17:True,22:True,25:True,28:True,29:True,
    30:True,31:True,33:True,38:True,40:True,44:True,52:True,
    56:True,65:True,82:True,85:True,87:True,89:True,94:True,
    100:True,106:False,125:True,138:True,140:True,148:False,
    165:False,196:True,218:True,221:False,233:True,234:True,
    243:True,251:True,261:False,263:False,273:True,299:True,
    301:True,304:True,305:True,317:True,320:True,325:True,
    326:True,327:True,328:True,
}

SC_SCALE = {
    16:True,17:True,21:True,22:True,23:False,31:True,32:True,
    35:True,38:True,40:True,41:True,47:True,52:True,65:True,
    92:True,96:True,100:True,119:False,121:False,122:True,
    123:True,124:True,127:True,128:False,133:False,135:False,
    139:False,141:False,146:True,151:True,157:True,159:False,
    160:False,162:True,163:True,168:True,170:True,177:False,
    179:False,182:True,190:True,221:True,229:True,233:True,
    234:True,238:True,241:True,244:False,254:True,258:True,
    276:False,277:True,279:False,282:True,291:True,292:True,
    296:True,298:True,299:True,301:True,303:True,305:True,
    307:True,311:True,315:False,316:True,319:True,320:True,
    322:True,323:True,324:True,325:True,326:True,327:True,
    328:True,336:True,355:True,
}

MA_SCALE = {
    11:False,13:True,15:False,21:True,22:True,23:False,50:True,
    55:True,61:True,73:False,85:True,87:True,98:True,100:True,
    103:True,105:False,109:False,110:True,122:True,134:True,
    136:True,141:False,146:True,147:False,148:False,150:True,
    156:True,157:True,159:True,164:False,168:True,169:True,
    171:False,172:True,177:False,178:True,188:True,189:True,
    190:True,200:False,205:True,206:True,211:True,212:True,
    218:True,226:True,
}

SI_SCALE = {
    46:True,49:False,55:False,57:True,70:True,82:True,86:False,
    87:True,88:False,119:False,125:False,136:True,147:True,
    158:True,160:True,161:True,162:False,163:False,167:True,
    171:False,172:True,174:False,178:True,184:False,185:True,
    189:False,196:True,200:False,201:False,207:False,210:False,
    212:False,220:False,223:False,227:True,231:False,243:True,
    251:True,253:False,261:False,262:False,265:True,267:False,
    270:True,271:True,272:False,275:True,276:False,277:True,
    280:False,281:True,289:True,292:True,296:False,297:False,
    303:True,309:False,310:True,321:False,323:True,328:True,
    335:False,337:True,338:True,347:True,348:True,349:True,
    353:False,357:True,
}

# ── CONTENT SCALES ──────────────────────────────────────────────

ANX_SCALE = {
    2:True,3:True,5:True,10:False,15:True,17:True,28:True,
    31:True,36:True,39:True,40:True,44:True,56:True,65:True,
    87:True,135:True,196:True,218:True,223:True,232:False,
    261:False,273:True,290:True,299:True,301:True,317:True,
    320:True,330:False,396:True,415:True,420:True,421:True,
    428:True,469:True,471:True,496:False,
}

FRS_SCALE = {
    154:True,155:False,163:True,232:True,280:False,301:True,
    317:True,320:True,329:True,334:True,392:True,393:False,
    395:True,397:True,401:False,435:True,438:True,441:True,
    447:True,453:True,462:False,468:True,
}

OBS_SCALE = {
    3:True,31:True,38:True,56:True,87:True,93:True,136:True,
    196:True,217:False,221:True,234:True,243:True,251:True,
    263:False,309:False,313:True,325:True,327:True,328:True,
    394:True,402:True,408:True,421:True,424:True,425:True,
    428:True,442:True,446:True,456:False,460:False,469:True,
    472:True,491:True,497:True,509:True,547:True,
}

DEP_SCALE = {
    2:True,3:True,5:True,9:False,10:False,26:True,29:True,
    30:True,38:True,40:True,46:True,56:True,65:True,71:True,
    73:True,75:False,79:False,82:True,92:True,130:True,146:True,
    167:True,215:True,233:True,273:True,277:True,303:True,
    306:True,331:True,377:True,388:False,394:True,395:True,
    399:True,400:True,403:True,408:True,409:True,410:True,
    411:True,414:True,415:True,430:True,444:True,454:True,
    485:True,491:True,500:True,506:True,516:True,520:True,
    524:True,539:True,554:True,556:True,561:False,566:True,
}

HEA_SCALE = {
    11:True,18:True,20:False,28:True,29:True,36:True,40:True,
    44:True,47:False,53:True,57:True,59:True,91:False,97:True,
    101:True,111:True,142:False,144:True,148:False,149:True,
    152:True,164:False,172:True,174:False,175:True,176:False,
    179:False,182:True,194:False,204:False,224:False,247:True,
    249:False,255:False,295:False,
}

BIZ_SCALE = {
    24:True,32:True,60:True,72:True,96:True,106:False,138:True,
    144:True,162:True,180:True,198:True,228:True,229:True,
    241:True,247:True,252:True,256:False,270:True,291:True,
    292:True,296:True,298:True,307:True,311:True,316:True,
    319:True,333:True,336:True,355:True,361:True,466:True,
    490:True,508:True,543:True,551:True,
}

ANG_SCALE = {
    13:True,27:True,37:True,50:True,56:True,85:True,116:False,
    134:True,136:True,150:True,167:True,169:True,178:True,
    189:False,213:True,218:True,242:True,302:True,325:True,
    346:False,352:False,357:False,389:True,394:True,410:True,
    414:True,430:True,461:True,481:True,486:True,507:True,
    513:True,535:True,542:True,548:True,
}

CYN_SCALE = {
    50:True,58:True,76:True,81:True,82:True,89:False,104:True,
    110:True,124:True,125:False,254:True,283:True,284:True,
    286:True,315:False,338:True,352:True,358:True,374:True,
    399:True,403:True,445:True,470:True,483:True,484:True,
}

ASP_SCALE = {
    26:True,35:True,40:True,50:True,61:True,81:True,84:True,
    89:False,104:True,105:True,110:True,123:True,125:False,
    227:True,232:False,240:True,248:True,250:True,254:True,
    269:True,284:True,374:True,382:True,406:True,412:True,
    418:True,431:True,433:True,437:False,440:False,452:False,
    456:False,481:True,485:False,
}

TPA_SCALE = {
    18:True,27:True,29:True,50:True,55:True,84:True,136:True,
    151:False,212:True,249:False,251:True,290:True,302:True,
    358:True,414:True,419:True,420:True,423:True,430:True,
    437:True,461:True,507:True,510:False,513:True,523:True,
    531:True,535:True,541:True,545:True,
}

LSE_SCALE = {
    73:True,74:False,130:True,233:True,239:False,271:True,
    289:True,322:True,325:True,326:True,327:True,358:True,
    362:False,369:True,376:True,377:True,380:True,383:False,
    385:False,394:True,396:True,411:True,450:True,451:True,
    457:True,461:True,462:False,472:True,479:True,480:True,
    483:True,485:True,491:True,501:False,503:True,504:True,
    519:True,526:True,562:True,
}

SOD_SCALE = {
    46:True,86:False,158:True,167:True,170:False,185:True,
    207:False,265:True,270:True,275:True,281:True,289:True,
    296:False,303:True,309:False,310:True,317:True,337:True,
    338:True,349:True,353:False,357:True,359:False,360:False,
    362:False,363:False,367:True,391:True,409:True,420:True,
    421:True,427:False,446:True,449:False,450:True,451:True,
    461:True,465:False,473:False,479:True,480:True,481:True,
    483:True,515:True,531:False,547:True,
}

FAM_SCALE = {
    21:True,52:True,54:True,83:False,88:True,125:False,145:True,
    190:True,195:True,202:True,213:True,217:False,219:True,
    225:True,226:False,256:True,277:True,288:True,292:True,
    300:True,337:False,383:False,412:True,413:True,416:False,
    425:True,434:False,449:True,455:False,463:True,478:True,
    481:True,520:True,542:True,543:True,550:True,563:True,
    567:True,
}

WRK_SCALE = {
    2:True,3:True,5:True,10:False,29:True,31:True,43:False,
    47:False,51:True,52:True,54:True,57:True,67:False,89:True,
    95:False,107:False,108:False,109:False,129:True,135:True,
    152:True,161:True,164:True,167:True,178:True,213:True,
    214:True,221:True,223:True,233:True,243:True,251:True,
    262:False,263:False,269:True,271:True,289:True,290:True,
    302:True,311:True,316:True,319:True,325:True,328:True,
    339:True,341:True,365:False,394:True,396:True,399:True,
    400:True,401:False,408:True,409:True,410:True,414:True,
    415:True,418:True,424:True,430:True,444:True,445:True,
    450:True,464:True,485:True,491:True,497:True,506:True,
    517:True,531:False,539:True,545:True,554:True,559:True,
    566:True,
}

TRT_SCALE = {
    22:True,92:True,274:True,277:True,306:True,363:False,
    364:True,368:True,377:True,380:True,391:True,399:True,
    400:True,404:False,409:True,411:True,421:True,440:False,
    443:False,445:True,450:True,491:True,495:True,497:True,
    499:True,500:True,504:True,506:True,507:True,516:True,
    517:True,526:True,539:True,545:True,554:True,
}

# ── PSY-5 SCALES ───────────────────────────────────────────────

AGGR_SCALE = {
    27:True,50:True,85:True,134:True,136:True,148:False,
    167:True,213:True,239:False,294:False,324:True,346:True,
    350:True,358:True,414:True,423:True,452:False,457:False,
    463:False,477:False,521:True,537:True,
}

PSYC_SCALE = {
    24:True,32:True,60:True,72:True,96:True,138:True,144:True,
    162:True,180:True,198:True,228:True,229:True,247:True,
    252:True,270:True,279:False,291:True,292:True,296:True,
    298:True,307:True,311:True,316:True,319:True,336:True,
    355:True,361:True,427:False,466:True,490:True,508:True,
    543:True,551:True,
}

DISC_SCALE = {
    35:True,50:True,84:True,103:True,105:True,123:True,169:True,
    189:True,209:True,210:True,222:False,240:True,248:True,
    264:True,287:True,344:True,390:False,412:True,418:True,
    421:False,431:True,433:True,440:False,448:True,455:False,
    487:True,489:True,502:False,511:True,522:False,527:True,
    534:False,540:True,
}

NEGE_SCALE = {
    3:True,5:True,17:True,29:True,39:True,40:True,56:True,
    65:True,82:True,87:True,89:True,94:True,100:True,130:True,
    146:True,170:True,196:True,215:True,218:True,273:True,
    277:True,278:False,290:True,299:True,301:True,303:True,
    305:True,308:True,320:True,326:True,327:True,328:True,
    339:True,374:True,390:True,394:True,404:False,409:True,
    415:True,420:True,430:True,442:True,444:True,451:True,
    463:True,469:True,471:True,485:True,491:True,496:False,
    500:True,507:True,513:True,554:True,
}

INTR_SCALE = {
    9:False,46:True,49:False,56:True,70:True,86:False,88:False,
    95:False,116:False,126:False,147:True,158:True,167:True,
    178:True,181:False,185:True,200:False,201:False,207:False,
    226:False,231:False,244:False,261:False,267:False,275:True,
    289:True,296:False,309:False,311:True,337:True,349:True,
    352:False,363:False,367:True,370:False,388:False,390:True,
    391:True,399:True,400:True,409:True,411:True,415:True,
    444:True,450:True,457:True,473:False,480:True,481:True,
    497:True,515:True,516:True,554:True,
}

# ── SUPPLEMENTARY SCALES ────────────────────────────────────────

A_SCALE = {
    15:True,16:True,22:True,26:True,28:True,29:True,31:True,
    38:True,39:True,40:True,44:True,56:True,65:True,71:True,
    82:True,87:True,88:False,89:True,94:True,130:True,147:True,
    193:True,196:True,215:True,218:True,223:True,233:True,
    234:True,243:True,251:True,261:False,273:True,277:True,
    289:True,299:True,301:True,305:True,317:True,320:True,
}

R_SCALE = {
    1:True,7:False,10:True,14:True,37:False,45:True,69:True,
    96:False,100:False,103:False,107:True,108:True,109:True,
    115:True,116:True,117:True,120:False,121:True,128:True,
    140:True,148:True,160:True,165:True,166:True,167:False,
    174:True,188:True,189:False,197:True,199:True,209:False,
    210:True,211:True,213:False,217:True,252:False,265:True,
}

MACR_SCALE = {
    7:True,24:True,36:True,49:True,52:True,82:True,84:True,
    103:True,105:True,113:True,115:True,117:False,118:True,
    120:True,127:True,134:True,135:False,142:False,148:False,
    149:True,156:True,168:True,172:True,178:True,182:True,
    189:True,197:True,199:True,214:True,226:True,228:True,
    230:True,236:False,239:True,244:True,245:False,248:True,
    251:True,263:False,283:True,287:True,310:True,338:True,
    356:True,393:True,406:True,412:True,417:True,422:True,
}

ES_SCALE = {
    2:False,3:True,9:True,10:True,20:True,33:True,36:False,
    39:False,45:True,51:True,57:False,68:False,75:True,76:True,
    83:True,95:True,107:True,108:True,109:True,118:True,125:True,
    133:True,140:True,143:True,145:False,152:False,165:True,
    173:True,174:True,176:True,179:True,181:True,194:True,
    204:True,205:True,208:True,213:False,217:True,218:False,
    224:True,226:False,229:False,232:False,237:True,245:True,
    247:False,249:True,250:False,251:False,253:True,259:False,
    260:False,
}

DO_SCALE = {
    26:False,32:False,49:True,57:False,61:True,78:True,82:False,
    87:False,98:True,107:True,108:True,109:True,115:True,116:True,
    148:True,170:False,200:True,202:False,211:True,219:False,
    232:False,239:True,261:True,266:False,268:False,
}

RE_SCALE = {
    105:False,110:False,123:False,127:False,129:False,148:True,
    160:True,164:True,183:True,185:False,209:False,214:False,
    232:True,233:False,243:False,248:False,250:False,267:True,
    269:False,280:True,286:False,309:True,404:True,418:False,
    430:False,433:False,440:True,450:False,452:True,497:False,
}

MT_SCALE = {
    2:True,3:True,5:True,9:False,10:False,14:True,17:True,
    22:True,23:False,28:True,29:True,30:True,31:True,40:True,
    44:True,56:True,65:True,87:True,89:True,94:True,95:False,
    125:False,130:True,148:False,152:True,158:True,167:True,
    218:True,223:True,233:True,239:False,243:True,251:True,
    261:False,289:True,295:False,305:True,317:True,320:True,
    328:True,415:True,
}

OH_SCALE = {
    1:True,7:True,9:True,10:True,14:True,15:True,29:False,
    37:False,82:False,89:False,96:False,107:True,115:True,
    116:True,117:True,129:False,136:False,148:True,151:False,
    155:True,160:True,161:False,168:False,185:False,213:False,
    222:True,241:False,263:True,
}

APS_SCALE = {
    7:True,29:True,41:True,82:True,84:True,85:True,87:True,
    89:False,100:True,111:True,116:True,118:False,120:True,
    122:True,130:True,134:True,136:True,148:False,167:True,
    172:True,186:False,201:False,214:True,221:True,233:True,
    250:True,251:True,279:False,302:True,323:True,325:True,
    387:True,388:False,389:True,391:True,399:True,401:False,
    502:True,503:True,
}

AAS_SCALE = {
    168:True,172:True,264:True,362:False,387:True,388:False,
    489:True,501:False,502:True,511:True,527:True,540:True,
    544:True,
}

MDS_SCALE = {
    125:False,167:True,184:False,207:False,245:False,271:True,
    277:True,289:True,297:False,306:True,363:False,395:True,
    413:True,449:True,
}

HO_SCALE = {
    27:True,50:True,58:True,76:True,81:True,82:True,87:True,
    89:False,104:True,110:True,124:True,136:True,151:False,
    167:True,213:True,214:True,219:True,244:False,248:True,
    250:True,254:True,258:False,283:True,284:True,286:True,
    296:False,315:False,338:True,346:False,352:True,358:True,
    374:True,381:True,389:True,396:True,399:True,403:True,
    406:True,414:True,419:True,430:True,444:True,452:False,
    456:False,481:True,507:True,513:True,537:True,542:True,
    548:True,
}

PK_SCALE = {
    16:True,17:True,22:True,29:True,30:True,31:True,39:True,
    44:True,48:True,52:True,56:True,59:True,65:True,82:True,
    85:True,87:True,92:True,94:True,100:True,168:True,170:True,
    196:True,221:True,274:True,277:True,302:True,303:True,
    305:True,316:True,317:True,319:True,320:True,325:True,
    327:True,328:True,329:True,332:True,339:True,347:True,
    349:True,366:True,367:True,389:True,399:True,400:True,
    463:True,
}

GM_SCALE = {
    1:True,8:True,12:True,43:True,45:True,57:False,68:False,
    79:True,84:False,87:False,88:True,89:False,99:False,113:False,
    115:True,116:True,117:True,120:False,127:False,129:False,
    138:False,141:True,143:True,154:False,163:True,164:True,
    166:True,177:True,179:True,181:True,188:True,195:True,
    200:True,202:True,205:True,209:False,210:True,211:True,
    213:False,219:False,221:False,233:False,237:True,239:True,
    245:True,261:True,267:True,
}

GF_SCALE = {
    11:False,18:False,25:False,34:True,38:False,47:True,49:True,
    50:False,57:False,60:False,64:True,65:False,68:True,80:True,
    86:True,88:True,90:True,95:True,100:False,107:True,112:True,
    114:False,119:True,120:True,122:False,123:False,128:True,
    131:False,132:True,136:False,137:True,139:True,142:True,
    163:False,185:False,192:True,194:True,200:False,201:True,
    207:True,209:True,214:False,217:True,236:True,247:False,
    275:False,
}

# ── HARRIS-LINGOES SUBSCALES ─────────────────────────────────────

D1_SUB = {
    2:True,3:False,5:True,22:True,26:True,29:True,30:True,
    31:True,32:False,37:True,38:True,39:True,40:True,46:True,
    56:True,65:True,73:True,79:False,82:True,86:False,87:True,
    88:False,89:True,92:True,94:True,95:False,98:False,130:True,
    145:False,233:True,273:True,
}
D2_SUB = {
    9:False,29:True,38:True,48:True,49:False,52:True,57:True,
    79:False,86:False,92:True,93:False,95:False,167:True,233:True,
}
D3_SUB = {10:False,57:True,58:True,59:True,111:True,182:False,}
D4_SUB = {
    15:True,19:False,31:True,38:True,44:True,52:True,56:True,
    65:True,80:False,88:False,147:True,151:True,233:True,234:True,
    255:True,273:True,299:True,325:True,341:True,
}
D5_SUB = {
    38:True,40:True,41:True,67:False,71:True,82:True,91:False,
    130:True,215:True,
}

HY1_SUB = {129:False,161:False,167:False,185:False,243:False,265:False,275:False,}
HY2_SUB = {
    89:False,117:True,124:False,131:True,186:True,190:False,
    203:False,217:True,229:False,230:True,233:False,234:False,
    265:True,267:True,
}
HY3_SUB = {
    11:True,40:True,47:False,60:False,111:True,179:False,
    189:False,208:False,224:False,
}
HY4_SUB = {
    10:False,23:False,44:True,47:False,97:True,106:False,
    114:False,115:False,182:True,184:False,189:False,194:False,
}
HY5_SUB = {6:False,7:False,37:False,102:False,106:True,109:True,392:False,}

PD1_SUB = {21:True,54:True,84:True,105:True,137:True,141:False,145:True,202:True,}
PD2_SUB = {35:True,84:True,105:True,110:True,129:True,202:True,266:False,}
PD3_SUB = {129:False,158:False,167:False,185:False,243:False,265:False,}
PD4_SUB = {
    17:True,22:True,42:True,56:True,99:True,113:True,219:True,
    225:True,226:False,277:True,288:True,306:True,
}
PD5_SUB = {32:True,33:False,61:False,82:True,89:True,94:True,113:True,246:True,273:True,380:True,}

PA1_SUB = {
    17:True,22:True,42:True,99:True,113:True,138:True,145:True,
    162:True,215:True,216:True,228:True,241:True,251:True,
    259:True,277:True,285:False,286:False,314:False,333:True,
    336:True,355:True,361:True,
}
PA2_SUB = {22:True,44:True,56:True,116:False,127:True,172:True,196:True,271:True,}
PA3_SUB = {89:False,100:False,119:True,148:True,183:True,243:False,261:True,}

SC1_SUB = {
    16:True,21:True,22:True,46:True,138:True,145:True,190:True,
    221:True,254:True,277:True,288:True,292:True,304:True,309:False,
}
SC2_SUB = {65:True,92:True,127:True,146:True,215:True,273:True,303:True,323:True,383:False,}
SC3_SUB = {31:True,32:True,44:True,147:True,170:True,180:True,299:True,311:True,316:True,325:True,}
SC4_SUB = {38:True,48:True,65:True,92:True,233:True,234:True,273:True,303:True,323:True,339:True,}
SC5_SUB = {23:False,85:True,96:True,122:True,168:True,182:True,229:True,}
SC6_SUB = {22:True,32:True,44:True,53:True,55:False,145:True,162:True,247:True,296:True,298:True,}

MA1_SUB = {81:True,110:True,157:True,212:True,227:True,248:True,}
MA2_SUB = {15:False,85:True,87:True,122:True,169:True,206:True,218:True,242:True,244:False,}
MA3_SUB = {93:False,136:True,158:False,167:False,243:False,263:True,}
MA4_SUB = {13:True,50:True,55:True,61:True,98:True,136:True,141:False,145:True,211:True,}

SI1_SUB = {46:True,86:False,161:True,167:True,185:True,243:True,251:True,265:True,275:True,289:True,}
SI2_SUB = {86:False,207:False,231:False,260:False,337:True,340:False,349:True,353:False,359:False,363:False,367:True,370:False,}
SI3_SUB = {
    22:True,44:True,56:True,82:True,89:True,94:True,125:False,
    232:False,234:True,251:True,261:False,289:True,290:True,
    293:False,305:True,317:True,320:True,338:True,469:True,471:True,
}

# ── NORMATIVE DATA ─────────────────────────────────────────────
# (mean_male, sd_male, mean_female, sd_female)
NORMATIVE_DATA = {
    "L":(3.5,2.5,3.5,2.6),"F":(4.7,4.0,4.6,3.9),"Fb":(4.5,4.2,4.6,4.3),
    "Fp":(1.4,1.6,1.3,1.5),"K":(15.3,4.8,15.0,4.6),"S":(29.7,7.5,28.1,7.6),
    "VRIN":(5.5,2.8,5.4,2.7),"TRIN":(9.0,2.2,8.9,2.1),
    "Hs":(6.1,4.5,8.2,5.0),"D":(21.7,5.7,23.5,5.4),"Hy":(22.2,5.6,24.1,5.4),
    "Pd":(16.5,4.5,16.8,4.5),"Mf_M":(26.0,5.1,0,1),"Mf_F":(0,1,35.9,4.3),
    "Pa":(10.1,3.2,11.0,3.4),"Pt":(11.5,6.4,13.8,6.6),"Sc":(12.5,7.9,13.8,8.0),
    "Ma":(18.9,4.4,19.2,4.0),"Si":(27.4,9.5,30.7,9.7),
    "ANX":(10.0,5.5,12.1,5.8),"FRS":(5.5,3.8,7.8,4.2),"OBS":(8.5,4.8,9.8,5.0),
    "DEP":(10.4,7.3,13.0,7.8),"HEA":(9.7,6.4,11.0,6.6),"BIZ":(3.0,2.9,3.1,2.9),
    "ANG":(8.5,4.5,8.0,4.4),"CYN":(11.2,5.6,9.9,5.3),"ASP":(9.5,5.0,8.0,4.5),
    "TPA":(12.5,5.0,11.5,4.8),"LSE":(5.8,5.3,7.3,5.6),"SOD":(14.6,8.1,16.7,8.3),
    "FAM":(7.5,4.8,7.8,4.9),"WRK":(11.5,8.2,13.2,8.4),"TRT":(8.0,5.8,8.8,6.0),
    "AGGR":(9.0,4.8,7.0,4.2),"PSYC":(5.5,4.0,5.0,3.8),"DISC":(15.0,5.5,12.5,5.0),
    "NEGE":(19.0,9.5,22.5,9.8),"INTR":(17.5,8.5,18.0,8.8),
    "A":(14.5,8.0,16.5,8.5),"R":(15.5,5.5,16.0,5.5),"MAC_R":(21.5,4.5,18.5,4.0),
    "Es":(35.0,7.5,33.5,7.0),"Do":(15.0,4.5,14.5,4.3),"Re":(20.5,4.0,22.0,4.2),
    "Mt":(13.5,7.5,15.5,7.8),"OH":(14.0,4.5,13.5,4.2),
    "APS":(17.0,5.5,15.0,5.0),"AAS":(2.5,2.0,2.0,1.8),
    "MDS":(4.0,3.0,4.5,3.2),"Ho":(19.5,9.0,18.0,8.5),
    "PK":(10.5,8.0,12.0,8.5),"GM":(33.0,6.0,25.0,5.8),"GF":(22.0,4.5,28.5,4.2),
    "D1":(13.0,6.5,15.0,6.8),"D2":(6.5,2.8,7.0,2.9),"D3":(2.8,1.8,3.2,1.9),
    "D4":(7.0,4.0,8.0,4.2),"D5":(3.5,2.5,4.0,2.6),
    "Hy1":(4.5,1.8,4.8,1.9),"Hy2":(8.5,2.5,9.0,2.6),"Hy3":(4.5,3.0,5.5,3.2),
    "Hy4":(5.0,3.0,5.5,3.2),"Hy5":(3.5,1.8,3.8,1.9),
    "Pd1":(3.0,2.0,3.2,2.0),"Pd2":(2.5,1.8,2.2,1.7),"Pd3":(4.0,1.8,4.0,1.8),
    "Pd4":(4.5,2.8,4.5,2.8),"Pd5":(3.5,2.5,3.8,2.6),
    "Pa1":(4.0,2.8,4.5,3.0),"Pa2":(3.5,2.0,4.0,2.0),"Pa3":(4.5,1.8,5.0,1.9),
    "Sc1":(4.0,3.0,4.5,3.2),"Sc2":(2.0,1.8,2.2,1.8),"Sc3":(3.5,2.5,3.8,2.5),
    "Sc4":(3.5,2.8,4.0,2.9),"Sc5":(2.5,1.8,2.5,1.8),"Sc6":(3.0,2.5,2.8,2.4),
    "Ma1":(2.0,1.5,1.8,1.5),"Ma2":(4.5,2.0,4.5,2.0),"Ma3":(3.0,1.8,3.2,1.8),
    "Ma4":(3.5,2.0,3.5,2.0),
    "Si1":(4.5,3.0,5.0,3.0),"Si2":(3.5,2.5,3.5,2.5),"Si3":(6.0,4.0,6.5,4.0),
}

# Critical Items (Koss-Butcher)
CRITICAL_ITEMS_KB = {
    "Acute Anxiety State": [2,3,5,28,39,140,218,223,301,444],
    "Depressed Suicidal Ideation": [9,38,65,71,75,92,95,130,146,215,233,273,303,411,454,485,518],
    "Threatened Assault": [213,285,314],
    "Situational Stress Due to Alcoholism": [125,264,487,518],
    "Mental Confusion": [31,168,299,325],
    "Persecutory Ideas": [17,42,99,124,138,144,162,216,228,241,259,314,333,336,355,361],
}

CRITICAL_ITEMS_LW = {
    "Antisocial Attitude": [35,84,105,412,418],
    "Family Conflict": [21,83,125,288,292],
    "Somatic Symptoms": [28,53,101,111,164,175,182,247,464],
    "Anxiety and Tension": [15,17,218,223,261,299,301,415,463,469,471],
    "Sleep Disturbance": [5,30,39,140,423,471],
    "Depression and Worry": [2,3,65,73,75,130,165,273,303,339,411,415,454],
    "Deviant Beliefs": [42,99,138,144,162,216,228,241,259,314,336,355,361,466],
    "Problematic Anger": [85,134,213,389],
}

# ── VRIN / TRIN INCONSISTENCY PAIRS ─────────────────────────────

# VRIN: pairs that SHOULD be answered consistently
# Format: (item1, item2, "TF") = score if item1=T and item2=F
# Format: (item1, item2, "FT") = score if item1=F and item2=T
VRIN_PAIRS = [
    (3,39,"TF"),(6,90,"TF"),(6,90,"FT"),(9,56,"TF"),(9,56,"FT"),
    (15,45,"TF"),(15,45,"FT"),(35,158,"TF"),(35,158,"FT"),
    (37,89,"TF"),(37,89,"FT"),(38,188,"TF"),(38,188,"FT"),
    (46,265,"TF"),(46,265,"FT"),(48,184,"TF"),(48,184,"FT"),
    (49,280,"TF"),(58,76,"TF"),(69,208,"TF"),(69,208,"FT"),
    (70,233,"TF"),(70,233,"FT"),(95,388,"TF"),(107,160,"TF"),
    (107,160,"FT"),(110,374,"TF"),(116,430,"TF"),(116,430,"FT"),
    (122,226,"TF"),(130,215,"TF"),(130,215,"FT"),(140,421,"TF"),
    (145,217,"TF"),(146,167,"TF"),(158,288,"TF"),(166,282,"TF"),
    (166,282,"FT"),(167,243,"TF"),(177,295,"TF"),(177,295,"FT"),
    (185,275,"TF"),(196,415,"TF"),(196,415,"FT"),(199,467,"TF"),
    (214,502,"TF"),(220,335,"TF"),(225,405,"TF"),(242,266,"TF"),
]

# TRIN: True-True pairs add 1; False-False pairs subtract 1
TRIN_TRUE_PAIRS = [
    (3,39),(12,166),(40,176),(48,184),(63,120),(70,233),(71,283),
    (110,374),(116,430),(130,215),(158,288),(163,453),(166,282),
    (167,243),(185,275),(196,415),(199,467),(220,335),(228,352),
    (346,470),(356,413),(364,477),(409,499),
]
TRIN_FALSE_PAIRS = [
    (46,265),(48,184),(49,280),(69,208),(95,388),(107,160),
    (122,226),(136,507),(146,167),(177,295),(214,502),(225,405),
    (242,266),(264,544),(409,499),
]
