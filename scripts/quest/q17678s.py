# id 17678 ([Commerci Republic] Ship of Blood), field 865010001
sm.setSpeakerID(9390244) # Leon Daniella
sm.sendNext("W-what the...? He's gone. How'd he do that?")
sm.setParam(2)
sm.sendSay("Leon, look!")
sm.setParam(0)
sm.sendSay("He's already on his ship! Poop! We were so close!")
sm.setParam(2)
sm.sendSay("What now? That felt like our best shot, but he still got away. I don't think following him to his base is a good idea...")
sm.setParam(0)
sm.sendSay("But, but, we can't give up now! I can't go back empty-handed! I'll never get my allowance at this rate!")
res = sm.sendAskYesNo("Look, I know this is probably Captain Blood's trap, leading us into his base like this. You don't have to come, but I'm going. For me, for my dad, and for Commerci!")
sm.setParam(2)
sm.sendNext("Well, when you say it like that, I'm in!")
sm.setParam(0)
sm.sendSay("Really? I thought traps were bad things.")
sm.setParam(2)
sm.sendSay("It's okay. I'm pretty used to this kind of thing. ")
sm.setParam(4)
sm.setInnerOverrideSpeakerTemplateID(9390204) # Robed Lady
sm.sendSay("Shall I come too?")
sm.setParam(0)
sm.sendSay("No. You stay behind, guard the ship, and think about our date.")
sm.sendSay("All right, #h0#! Let's move out! I got the door! ")
sm.setParam(2)
sm.sendSay("Hold up. I'm going in there alone.")
sm.setParam(0)
sm.sendSay("What? No! I didn't come all this way to watch someone else beat the boss!")
sm.setParam(2)
sm.sendSay("Leon, think about it. You're the captain of this ship. What if something happens while the captain is away? You have to put your crew first.")
sm.setParam(0)
sm.sendSay("Yeah, but... I want glory!")
sm.setParam(2)
sm.sendSay("Shh, I know. But a captain's glory comes from doing his duty.")
sm.setParam(0)
sm.sendSay("...This sucks.")
sm.startQuest(parentID)
