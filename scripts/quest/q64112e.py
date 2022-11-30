# id 64112 ([MONAD: The First Omen] Another Witness), field 867202300
sm.lockInGameUI(True, False)
sm.forcedFlip(True)
sm.setSpeakerType(3)
sm.setParam(57)
sm.setColor(1)
sm.sendNext("#bSanaan! ")
sm.flipNpcByTemplateId(9400586, False)
sm.flipNpcByTemplateId(9400601, False)
sm.sendSay("#bI was on my way to meet you! What are you doing here? ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400586) # Sanaan
sm.sendSay("Oh, #h0#... The child that lives here gives me such grief. He's held the doors shut on me for days... ")
sm.setParam(57)
sm.sendSay("#bIn this house? ")
sm.flipNpcByTemplateId(9400586, True)
sm.setParam(37)
sm.sendSay("Yes! Such a nuisance... nothing but skin and bones! I wonder what's made him shut us out this time? ")
sm.flipNpcByTemplateId(9400601, True)
sm.setInnerOverrideSpeakerTemplateID(9400601) # Elva
sm.sendSay("Shh, Sanaan. Einar might hear you. ")
sm.setInnerOverrideSpeakerTemplateID(9400586) # Sanaan
sm.sendSay("I hope he does! ")
sm.flipNpcByTemplateId(9400586, False)
sm.flipNpcByTemplateId(9400601, False)
sm.sendSay("Now then, what did you need me for? ")
sm.setParam(57)
sm.sendSay("#bI wanted to ask you a question. Did you see any outsiders while you were living in the forest? Or anyone suspicious? ")
sm.setParam(37)
sm.sendSay("I've seen several outsiders. Anything more specific? ")
sm.setParam(57)
sm.sendSay("#bHmm... Did you see any around 6 months ago? ")
sm.setParam(37)
sm.sendSay("...No. I didn't see who took the townsfolk. ")
sm.setParam(57)
sm.sendSay("#bAh, yeah. Sorry if that's a painful memory for you. ")
sm.setParam(37)
sm.sendSay("No, I'm fine. It's all in the past. Ask me anything that you think might help us find my Blanche. ")
sm.blind(True, 255, 0, 0, 0, 250)
sm.sendDelay(250)
sm.spawnNpc(9400586, 710, 0)
sm.showNpcSpecialActionByTemplateId(9400586, "summon", 0)
sm.spawnNpc(9400601, 770, 0)
sm.showNpcSpecialActionByTemplateId(9400601, "summon", 0)
sm.forcedFlip(True)
sm.moveNpcByTemplateId(9400601, False, 150, 70)
sm.moveNpcByTemplateId(9400586, False, 150, 70)
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(100)
sm.blind(False, 0, 0, 0, 0, 250)
sm.sendDelay(300)
sm.sendDelay(1500)
sm.forcedMove(False, 100)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 34418552, 0, 0)
sm.sendNext("That reminds me. I wanted to tell you something. ")
sm.sendDelay(900)
sm.setParam(57)
sm.sendNext("#bWhat would that be? ")
sm.flipNpcByTemplateId(9400586, True)
sm.flipNpcByTemplateId(9400601, True)
sm.setParam(37)
sm.sendSay("I'm sure you saw them when you were in the forest. Those sticky pink things? ")
sm.sendSay("They're everywhere, even around my cabin! ")
sm.setParam(57)
sm.sendSay("#bYes, we've seen them. Alika and I call them Jellyrashes. ")
sm.setParam(37)
sm.sendSay("Ha! Quite a fitting name. ")
sm.sendSay("Living out there on my own, I had plenty of time to observe those bizarre things. ")
sm.sendSay("It would seem the giant creature controls all the monsters of the forest through the Jellyrashes. ")
sm.setParam(57)
sm.sendSay("#bI knew it! We were on the right track... ")
sm.flipNpcByTemplateId(9400586, False)
sm.flipNpcByTemplateId(9400601, False)
sm.sendDelay(300)
sm.moveNpcByTemplateId(9400601, False, 150, 70)
sm.moveNpcByTemplateId(9400586, False, 150, 70)
sm.sendDelay(900)
sm.setParam(37)
sm.sendNext("Then I assume you know where the Jellyrashes come from? ")
sm.forcedMove(False, 100)
sm.sendDelay(900)
sm.setParam(57)
sm.sendNext("#bWhere they come from?")
sm.sendDelay(900)
sm.setParam(37)
sm.sendNext("The same giant creature is creating them. ")
sm.setParam(57)
sm.sendSay("#bWe did suspect there might be a connection... ")
sm.flipNpcByTemplateId(9400586, True)
sm.flipNpcByTemplateId(9400601, True)
sm.setParam(37)
sm.sendSay("When the giant appears, it fills the sky with its strange snow. It doesn't make snow, but its huge feet kick up great clouds of it. ")
sm.sendSay("What the beast makes is a strange red powder that mixes with the snow, which is what makes the storm look red. ")
sm.sendSay("I only saw the creature itself once, and it was strange... it seemed to be tearing parts of its own body off. ")
sm.sendSay("If that's how it creates Jellyrashes, that would mean it can only create so many at once. ")
sm.setParam(57)
sm.sendSay("#bAre you sure?")
sm.setParam(37)
sm.sendSay("I am. ")
sm.sendSay("If the beast is really using those Jellyrashes to control the monsters... ")
sm.setParam(57)
sm.sendSay("#bThat means if we take them out faster than it can make them, at some point it won't be able to keep up. ")
sm.setParam(37)
sm.sendSay("Exactly! ")
sm.setParam(57)
sm.sendSay("#bThat alone won't solve our problem, though. When we destroyed some of the Jellyrashes the monsters calmed down, but they fell back under its control when the creature came near. ")
sm.setParam(37)
sm.sendSay("So the beast can control the monsters directly as well. ")
sm.setParam(57)
sm.sendSay("#bRight. But I'm sure clearing its Jellyrashes would make it easier to combat. ")
sm.setParam(37)
sm.sendSay("Good, good. I'm glad I did something useful with my time out there in my cabin. ")
sm.sendSay("Is there anything else you need? ")
sm.sendSay("Considering you've been surviving the harsh realities of Abrup for some time now, I would think there isn't much you don't know already. ")
sm.sendSay("I'll let you know if anything else comes to mind. ")
sm.setParam(57)
sm.sendSay("#bGreat. Thank you, Sanaan.")
sm.completeQuestNoCheck(parentID)
sm.lockInGameUI(False, True)
