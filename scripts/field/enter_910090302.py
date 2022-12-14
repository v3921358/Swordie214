# id 910090302 (Partem : Partem Ruins Interior 2), field 910090302
if not sm.hasHadQuest(35902):
    sm.completeQuestNoCheck(35900)
    sm.startQuest(11620)
    sm.createQuestWithQRValue(15710, "lasttime=19/07/04/16/47")
    sm.createQuestWithQRValue(25980, "normal=#")
    sm.createQuestWithQRValue(25980, "normal=#;hard=#")
    sm.setSpeakerType(3)
    sm.setParam(548)
    sm.setColor(1)
    sm.setInnerOverrideSpeakerTemplateID(1013358) # Pathfinder
    sm.sendNext("#face3#Hmm... An arrow and a potion? They look old enough, sure, but they don't seem particularly significant.")
    sm.sendSay("#face6#Tch... It doesn't seem any different from those of modern times. In other words, it's just like any other junk. Did I come all the way here for nothing?")
    sm.sendSay("#face0#...Huh. There's something written on the outside of this box. Might as well take a look-see.")
    sm.setSpeakerType(4)
    sm.setSpeakerID(1013305) # Ancient Crate
    res = sm.sendAskAccept("#face0#It's written in an ancient script. Question is, is it worth trying to decipher it?")
    sm.setSpeakerType(3)
    sm.sendNext("#face2#It'll take some time, but... Haha, of course it's worth it. Mostly because it would drive me nuts if I didn't. Ah, curiosity, you're the itch I always have to scratch.")
    sm.startQuest(35901)
    sm.createQuestWithQRValue(63369, "chk=2")
    sm.createQuestWithQRValue(63369, "chk=2;day=0")
    sm.createQuestWithQRValue(63369, "chk=2;day=1")
    sm.completeQuestNoCheck(63360)
    sm.sendNext("#face0##g'A temperamental dancer / best viewed with distant gaze,'\r\n'In crimson does it pirouette / in black its footfall stays.'#k")
    sm.sendSay("#face1#Oooh, ancient poetry. Which is ALSO a riddle. Score! Now that we've got the basic rhyme scheme, the next verse would go like so...")
    sm.sendSay("#face0##b(You deciphered the ancient script on the box. It's written with a figurative lilt, as ancient verse is wont to do, but after mulling over it a while, you think you have a good idea what it's referring to.)#k")
    sm.completeQuestNoCheck(35901)
    sm.startQuest(11620)
    sm.setSpeakerType(4)
    if sm.sendAskAccept("#face6#So basically, it's telling me to get the offering from whatever is guarding these ruins. Then once I've done that, I place it in front of the pillar that correctly answers the riddle. Gotta love the way these ancient ruins are always so roundabout with their secrets, eh?"):
        sm.setSpeakerType(3)
        sm.sendNext("#face0#I know the answer now! Take that, ancient riddle makers. Now, let's find this #r#o2300200##k and get #b#i4036523# #t4036523##k x#b5#k. I think if I poke around here, I'm bound to run into the Ruins Guardian sooner or later.")
        sm.startQuest(35902)
        sm.completeQuestNoCheck(63363)
        sm.createQuestWithQRValue(63367, "dam=0")
        sm.createQuestWithQRValue(63367, "dam=170")
        sm.createQuestWithQRValue(63368, "day=0")
        sm.createQuestWithQRValue(63368, "day=1")
        sm.createQuestWithQRValue(63366, "minlv=-9999")
        sm.createQuestWithQRValue(63366, "minlv=-9999;maxlv=99999")
        sm.completeQuestNoCheck(63361)
        sm.completeQuestNoCheck(63362)
        sm.completeQuestNoCheck(63363)
        sm.completeQuestNoCheck(63370)
