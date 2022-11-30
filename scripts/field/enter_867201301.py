# id 867201301 (Abrup Basin : Glistening Sunlight Trail), field 867201301
sm.lockInGameUI(True, False)
sm.spawnNpc(9400580, 50, 445)
sm.showNpcSpecialActionByTemplateId(9400580, "summon", 0)
sm.spawnNpc(9400595, 180, 445)
sm.showNpcSpecialActionByTemplateId(9400595, "summon", 0)
sm.showNpcSpecialActionByTemplateId(9400580, "fear", -1)
sm.sendDelay(500)
sm.forcedMove(False, 130)
sm.sendDelay(1000)
sm.setSpeakerType(3)
sm.setParam(57)
sm.setColor(1)
sm.sendNext("#bAlika! Why are you here? ")
sm.sendDelay(1000)
sm.resetNpcSpecialActionByTemplateId(9400580)
sm.sendDelay(1000)
sm.moveNpcByTemplateId(9400580, True, 40, 70)
sm.sendDelay(500)
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendNext("#face5#I was so worried about you, #h0#. I just couldn't let you go by yourself. ")
sm.sendSay("#face5#The forest is so dangerous, especially with everything going on! I know you're very confident in your abilities, but I prepared for anything that might happen... ")
sm.showEffect("Effect/OnUserEff.img/questEffect/PL_MONAD1/8", 3000, 0, 0, 0, 33629382, 0, 0)
sm.sendSay("#face5#Medicine, compass, blanket, emergency rations... ")
sm.setParam(57)
sm.sendSay("#bWait, is that why you rushed out earlier? ")
sm.sendSay("#bAlika, as you said, the forest is too dangerous. You should go back. ")
sm.setParam(37)
sm.sendSay("#face1#Hang on, #h0#. You might have forgotten, but I am the youngest scholar of Afinas because of my talents. I'll be able to help you! ")
sm.startQuest(64162)
sm.sendSay("#face3#And I came too far for you to send me back on my own... right? ")
sm.setParam(57)
sm.sendSay("#bAlika, this is serious! ")
sm.setParam(37)
sm.sendSay("#face3#... ")
sm.setParam(57)
sm.sendSay("#b...Hah. ")
sm.sendSay("#bOkay, you win. But you stay right behind me. ")
sm.setParam(37)
sm.sendSay("#face2#Fine by me! Okay #h0#, lead the way!")
sm.lockInGameUI(False, True)
sm.completeQuestNoCheck(64072)
sm.startQuest(64073)
sm.startQuest(64058)
sm.warp(867201320)