# id 2 (CaravanP1_chk2), field 867200500
sm.createQuestWithQRValue(64006, "WC=0;speed=20;man=200;prog=0;Pt=CaravanP1_chk1;Ec=2;weather=1;max=16;food=450")
sm.createQuestWithQRValue(64006, "WC=1;speed=20;man=200;prog=0;Pt=CaravanP1_chk1;Ec=2;weather=1;max=16;food=450")
sm.createQuestWithQRValue(64006, "WC=1;speed=20;man=200;prog=0;Pt=Caravan_chk2;Ec=2;weather=1;max=16;food=450")
sm.createQuestWithQRValue(64006, "WC=1;speed=20;man=200;prog=0;Pt=CaravanP1_chk2;Ec=2;weather=1;max=16;food=450")
sm.createQuestWithQRValue(49000, "count=0;Quest=0;day=152843;QET=20190622191818;state=2")
sm.createQuestWithQRValue(49000, "count=0;Quest=0;day=152843;QET=20190622191818;state=1")
sm.createQuestWithQRValue(49000, "count=0;Quest=0;day=152843;QET=20190622201819;state=1")
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendNext("#face0#Asking for help is an important way to deal with a situation if you're not fully informed. ")
sm.sendSay("#face0#Janyt is an Afinas Devata with healing abilities. Call her for help. ")
sm.setInnerOverrideSpeakerTemplateID(9400584) # Janyt
sm.sendSay("#face0#Have no fear. The protection of Afinas is upon you. ")
sm.setParam(57)
sm.sendSay("#bThank you, Janyt. ")
sm.setParam(37)
sm.sendSay("#face0#I am but a humble servant who shares the the blessings I've received from Afinas. ")
sm.setParam(57)
sm.sendSay("#bBut to have such powers at such a young age. It's impressive. ")
sm.setParam(37)
sm.sendSay("#face0#All thanks to Afinas. ")
sm.createQuestWithQRValue(64006, "WC=1;speed=20;man=200;prog=0;Pt=CaravanP1_chk2;Ec=3;weather=1;max=16;food=450")
sm.createQuestWithQRValue(64007, "happy0=65;happy1=50;happy2=60;happy3=55;man0=56;man1=33;man2=38;man3=73")
