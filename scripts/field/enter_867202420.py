# id 867202420 (Abrup Basin : Training Grounds), field 867202420
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.spawnNpc(9400589, -638, -70)
sm.showNpcSpecialActionByTemplateId(9400589, "summon", 0)
sm.spawnNpc(9400592, -10, -70)
sm.showNpcSpecialActionByTemplateId(9400592, "summon", 0)
sm.setSpeakerType(3)
sm.setParam(57)
sm.setColor(1)
sm.sendNext("#bAruhi! Hit harder! ")
sm.showNpcSpecialActionByTemplateId(9400592, "attack1", 0)
sm.sendDelay(3000)
sm.sendNext("#bNow, Peytour! Throw your axe! ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendSay("#face0#Here goes!")
sm.showNpcSpecialActionByTemplateId(9400589, "attack2", 0)
sm.sendDelay(3000)
sm.setInnerOverrideSpeakerTemplateID(9400592) # Aruhi
sm.sendNext("#face0#Whoa! Amazing throw!")
sm.sendDelay(2000)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(500)
sm.lockInGameUI(False, True)
sm.createQuestWithQRValue(64110, "dir1=1;chk=0;chk1=1")
sm.warp(867202402)
