# id 940200100 (Hidden Street : Elven Training Grounds), field 940200100
from net.swordie.ms.world.field.fieldeffect import GreyFieldType
sm.lockInGameUI(True, False)
sm.hideUser(True)
sm.removeAdditionalEffect()
sm.blind(True, 255, 0, 0, 0, 0)
sm.zoomCamera(0, 1000, 0, 20, -90)
sm.spawnNpc(3003274, 50, -20)
sm.showNpcSpecialActionByTemplateId(3003274, "summon", 0)
sm.spawnNpc(3003270, 115, -20)
sm.showNpcSpecialActionByTemplateId(3003270, "summon", 0)
sm.spawnNpc(3003275, -110, -20)
sm.showNpcSpecialActionByTemplateId(3003275, "summon", 0)
sm.sendDelay(1000)
sm.blind(False, 0, 0, 0, 0, 1500)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3003275) # Danika
sm.sendNext("Excellent work! It's clear the two of you are improving every day. Her Majesty will be pleased to see such young Elves giving their all for their kingdom.")
sm.setInnerOverrideSpeakerTemplateID(3003274) # Athena Pierce
sm.sendSay("#face1#Hehe, I couldn't help but do well after all my practicing. Um... Hey Danika, by the way...")
sm.sendSay("#face1#I was hoping for the opportunity to show Her Majesty the results of my training! I heard that she'll be returning to Elluel soon...")
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(300)
sm.removeOverlapScreen(1000)
sm.zoomCamera(0, 2000, 0, -90, 10)
sm.sendDelay(500)
sm.zoomCamera(3000, 2000, 3000, 5, 10)
sm.resetNpcSpecialActionByTemplateId(3003275)
sm.showNpcSpecialActionByTemplateId(3003275, "smile", 0)
sm.setInnerOverrideSpeakerTemplateID(3003275) # Danika
sm.sendNext("Well, she did mention wanting to stop by the training grounds for a visit. She's sorry she hasn't been able to devote as much attention to the two of you as she'd like.")
sm.setInnerOverrideSpeakerTemplateID(3003274) # Athena Pierce
sm.sendSay("#face1#Yahoo! Really? I-I'm going to train even harder! I've got to kick my training regimen up a notch. But I'm already practicing every day. Hmm.. Archery, running, what else is there?")
sm.setInnerOverrideSpeakerTemplateID(3003275) # Danika
sm.sendSay("Calm down Athena. I'm glad you're motivated to impress your queen, but don't overdo it.")
sm.setInnerOverrideSpeakerTemplateID(3003274) # Athena Pierce
sm.sendSay("#face1#Don't worry Danika. I've got oodles of stamina! Then I'll see you tomorrow! Let's go Lucid!")
sm.setInnerOverrideSpeakerTemplateID(3003275) # Danika
sm.sendSay("See you tomorrow.")
sm.setInnerOverrideSpeakerTemplateID(3003270) # Lucid
sm.sendSay("#face0#Goodbye.")
sm.moveNpcByTemplateId(3003274, False, 350, 160)
sm.moveNpcByTemplateId(3003270, False, 350, 160)
sm.sendDelay(500)
sm.zoomCamera(3000, 2000, 3000, 560, 10)
sm.setInnerOverrideSpeakerTemplateID(3003274) # Athena Pierce
sm.sendNext("#face1#Aren't you stoked? It's time to show off all our hard work to her majesty!")
sm.moveNpcByTemplateId(3003274, False, 160, 160)
sm.sendDelay(3000)
sm.moveNpcByTemplateId(3003274, True, 1, 160)
sm.sendNext("#face1#I'm putting my training into overdrive tomorrow! You'll join me, right?")
sm.setInnerOverrideSpeakerTemplateID(3003270) # Lucid
sm.sendSay("#face0#Yeah... tomorrow...")
sm.setInnerOverrideSpeakerTemplateID(3003274) # Athena Pierce
sm.sendSay("#face0#Well then, I'd better get a full night's sleep, hehe! Bye Lucid!")
sm.setInnerOverrideSpeakerTemplateID(3003270) # Lucid
sm.sendSay("#face0#Y-yeah... Bye Athena.")
sm.moveNpcByTemplateId(3003274, False, 600, 200)
sm.sendDelay(2000)
sm.moveNpcByTemplateId(3003270, False, 20, 160)
sm.sendDelay(500)
sm.setFieldGrey(GreyFieldType.Field, True)
sm.blind(True, 50, 0, 0, 0, 1300)
sm.sendDelay(1600)
sm.sendNext("#face0#...")
sm.sendDelay(1500)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.hideUser(False)
sm.lockInGameUI(False, True)
sm.warp(940200101)
