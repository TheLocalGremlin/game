# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Detective")
define mi = Character("Michael Alston")
define s = Character("Stuart Baldwin")
define ma = Character("Marcella Alston")
define c = Character("Cecil Sharpe")
define wi = Character("Wilbur Wyatt")
define wa = Character("Wayne Howard")
define i = Character("Ivy Galloway")
define p = Character("Trooper Grimes")

default MichaelDC = False

label start:
    scene bg room
    p "Who should I bring in first detective?"

menu interogationChoice:
    "Who would you like to interogate?"

    "Michael Alston":
        jump interogationMichael

    "Stuart Baldwin":
        jump interogationStuart

    "Marcella Alston":
        jump interogationMarcella

    "Cecil Sharpe":
        jump interogationCecil

    "Wilbur Wyatt":
        jump interogationWilbur

    "Wayne Howard":
        jump interogationWayne

    "Ivy Galloway":
        jump interogationIvy

    "That's it for now":
        return

menu interogationMichael:
    "What would you like to ask?"

    "Relationship with Scott Alston":
        d "Mr. Alston, how would you describe your relationship with your father?"
        show michael neutral
        mi "He was a good man, if a bit...{w=0.3} let's say emotionally distant."
        show michael happy
        mi "Nevertheless, he helped me get to where I am today."
        d "Sounds like you have a lot to accredit to your father. I imagine he supported you well when you decided to venture into your own buisiness."
        show michael smug
        mi "Hah, my father preferred a hands off approach to his \"support\"."
        d "Oh?{w=0.3} Could you please elaborate on that?"
        show michael neutral
        mi "There's not much too it detective,{w=0.3} the old man refused to step down for anyone else. Even when it might have been more favorable."
        show michael anger
        mi "It almost drove the company into the ground."
        d "That must've been frustrating."
        show michael anger
        mi "Extremely so detective."
        hide michael
        $MichaelDC = True
        jump interogationMichael

    "Whereabouts on the night of Scott Alston's death":
        d "What do remember from the night your father died?"
        show michael neutral
        mi "Not much if I'm being honest detective."
        mi "I remember drinking a lot that night, and I remember getting into a spat with my father at the dinner table before that."
        d "And after that?"
        show michael neutral
        mi "I believe I went out for a walk, but that's about it. Can’t remember anything about the walk."
        d "And that's everything?" 
        mi "That's everything."
        hide michael
        jump interogationMichael

    "Push about his relationship with his father" if MichaelDC == True:
        d "Your father was a very successful businessman."
        show michael happy
        mi "Indeed he was."
        d "There must have been a lot of pressure to make him proud." 
        show michael happy
        mi "Of course. I had always wanted to build something of my own like my father."
        mi "I couldn’t rely on my father forever." 
        show michael neutral
        mi "It's such a shame he passed away before I could ever prove myself in his eyes."
        d "That hasn't really gone well for you, has it?"
        show michael anger
        mi "No."
        mi "No it hasn't."
        d "And now you will inherit your father's company, isn't that right?"
        show michael smug
        mi "Yes, yes I will. With the resources I will have access to, I can make the company grow faster than ever before."
        mi "If only my father could be there to see me succeed." 
        hide michael
        jump interogationMichael

    "Do you believe your father ran the company well?" if MichaelDC == True:
        show michael smug
        mi "Of course,{w=0.3} you can't grow one of the biggest weapons manufacturing company overnight."
        show michael happy
        mi "It's something that requires dicipline{w=0.2}, patience{w=0.2}, focus.{w=0.3} That's what my father always told me."
        show michael neutral
        mi "Although, I felt my father was slipping in that regard."
        d "Oh? Could you elaborate on that?"
        mi "In his prime, my father was a paragon of hardwork and dedication who grew the company immensely."
        mi "As he grew older though, his success stagnated."
        show michael anger
        mi "He grew old and stale and let his company fall apart while he reaped the benefits of his past successes."
        d "And you believed that the company could be saved with newer ideas? {w=0.3} Newer blood?"
        show michael happy
        mi "Exactly detective! Everything was falling apart, I-we could have lost everything!"
        hide michael
        jump interogationMichael

    "Do you believe that the company is still in good condition?" if MichaelDC == True:
        show michael happy
        mi "I do detective. With the right direction, our company could flourish again."
        d "And you were next in line to inherit the company should your father pass.{w=0.3} Correct?"
        mi "Indeed I am."
        show michael anger
        mi "Wait.{w=0.3} I wouldn't actually kill my father just to inherit his company though!"
        d "We'll see, Mr. Alston."
        jump interogationMichael

    "That's it for now":
        jump interogationChoice


menu interogationStuart:
    "What would you like to ask?"

    "Relationship to Scott Alston":
        d "What was your relationship with Mr. Alston?"
        s "Let's see...{w=0.3} I have been serving the family for several decades."
        s "I was here to watch his son grow up, and was even here to watch Mr. Alston grow up for a while."
        d "You must have been close to him then."
        s "Hardly detective, I am merely a humble servant of the family."
        d "Surely after serving the family for many years must have made even a little close to them?"
        s "I'm afraid that isn't within the parameters of my profession."
        d "So you never expected more?"
        s "Hmm{w=0.3}, I suppose I did on some level."
        d "So even after all those years of service, you and Mr. Alston never became close?"
        s "I'm afraid that Mr. Alston was very traditional with his views on help."
        d "Could you elaborate on that?"
        s "He believed that help should be invisible, never to be acknowledged."
        s "Except for when it came to complaints of course."
        

    "That's it for now":
        jump interogationChoice






