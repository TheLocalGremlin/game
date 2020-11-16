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
default StuartDC = False
default MarcellaDC = False

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
        jump interogationMarcellaIntro

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
        show stuart neutral
        d "What was your relationship with Mr. Alston?"
        show stuart proud
        s "Let's see...{w=0.3} I have been serving the family for several decades."
        s "I was here to watch his son grow up, and was even here to watch Mr. Alston grow up for a while."
        d "You must have been close to him then."
        show stuart neutral
        s "Hardly detective, I am merely a humble servant of the family."
        d "Surely after serving the family for many years must have made even a little close to them?"
        show stuart bitter
        s "I'm afraid that isn't within the parameters of my profession."
        d "So you never expected more?"
        show stuart neutral
        s "Hmm{w=0.3}, I suppose I did on some level."
        hide stuart
        $StuartDC = True
        jump interogationStuart

    "Whereabouts that night":
        show stuart neutral
        d "Can you recall what happened on the night of Mr. Alston's murder?"
        s "Ah, yes.{w=0.3} I was serving the guests and then cleaned while the party was winding down and then excused the rest of the house staff."
        d "That sounds like it must have been a lot of work."
        show stuart proud
        s "It usually is but I take in my hard work detective."
        hide stuart
        jump interogationStuart

    "Push about relationship with his employer" if StuartDC == True:
        show stuart neutral
        d "So even after all those years of service, you and Mr. Alston never became close?"
        show stuart proud
        s "I'm afraid that Mr. Alston was very traditional with his views on help."
        d "Could you elaborate on that?"
        s "He believed that help should be invisible, never to be acknowledged."
        d "Being the head of a weapons manufacturing empire, I'd imagine that he was very detail oriented."
        show stuart bitter
        s "Detail oriented is undercutting it by a large sum detective."
        s "The only time he would actually converse with me was to make complaints about my work."
        s "He would routinely berate and slander the hard work of both me and my staff."
        d "That must have been infuriating."
        show stuart anger
        s "Oh let me tell you detective, it was absolutely outrageous. All those years of service and not a single word of gratitude."
        d "Sounds like you were bitter towards Mr. Alston."
        s "Just biter is just rich. At times  I could barely stand him and his self-centered, arrogant world views."
        s "And the {i}nerve{/i} to TELL ME I'M A BAD BUTLER!"
        show stuart proud
        s "Oh."
        show stuart neutral
        s "It seems I lost my composure there detective."
        s "Very unprofessional of me{w=0.3}, please excuse my behavior."
        s "I did what I was told to do and served the Alston's to the best of my abilities."
        s "It's a shame that the old Mr. passed away so suddenly."
        hide stuart
        jump interogationStuart

    "That's it for now":
        jump interogationChoice

label interogationMarcellaIntro:
    "Trooper Grimes brings in a furious Marcella Alston."
    show marcella disdain
    ma "Why am I here?"
    d "We just have a few questions to ask about your husband."
    ma "I am a suspect aren't I?"
    show marcella anger
    ma "How could you do this to a newly widowed woman? how some respect."
    d "Ma'am, this is simply an investigation and if you refuse to collaborate it's going to turn into a bigger thing than it needs to."
    show marcella neutral
    ma "Fine."
    ma "What do you want from me?"
    hide marcella
    jump interogationMarcella

menu interogationMarcella:
    "What would you like to ask?"

     "Relationship with Scott Alston":
        show marcella neutral
        d "Can you tell me about your relationship with your husband?"
        ma "He wasnt't the same charming buisinessman I met in France.{w=0.3} The man who promised me the world and took me back to America with him."
        show marcella disdain
        ma "Those feelings died out long ago, but it's not like I have anything to return to and I am not going to live out there on the streets with the dirty rabble."
        ma "Just imagine the filth{w=0.3}, the illnesses they must have."
        d "So you were stuck here with him then?"
        show marcella neutral
        ma "Indeed, and I must admit I have hated every second of the past 20 years but there was never a chance to leave him."
        ma "Without his income I would I have to live in the lice filled shacks with all the other peasantry."
        hide marcella
        jump interogationMarcella

    "Whereabouts that night":
        show marcella neutral
        d "Can you tell what you did that night?"
        show marcella disdain
        ma "I was enjoying my night{w=0.3}, just like everyone else."
        d "I'm going to need some specifics Mrs. Alston."
        show marcella neutral
        ma "I went out for a walk detective, I didn't see anything of interest though."
        d "Why did you for a walk?"
        ma "The young Miss Galloway and I got into a{w=0.3}...disagreement."
        d "Over what?"
        show marcella disdain
        ma "Those are private details detective."
        d "It could help the investigation."
        ma "I said that it was private."
        d "Ma'am, I can arrest you for impeding an investigation and refusing to cooperate."
        show marcella anger
        ma "How DARE you!"
        ma "Do you know who you're talking to?{w=0.3} Threatening a poor widow like that. Do you have no shame?"
        d "I'll have to write it up then, we can settle this in court."
        show marcella disdain
        ma "..."
        show marcella neutral
        ma "I'll tell you. {w=0.3}You bastard."
        show marcella disdain
        ma "I had reason to believe that my husband was having an affair{w=0.3}, with Ms. Galloway."
        d "Why do you think that?"
        show marcella neutral
        ma "Miss Galloway had...been spending the night here in anticipation for the dinner."
        ma "Three days before his death my husband had been working late in his study and he never came to bed."
        show marcella disdain
        ma "Something he only started doing since Miss Galloway came to the house."
        ma "I had walked over to his office to check on him when I heard...noises coming from inside."
        ma "I knocked on the door at first before slamming it open and there I saw the pig desperately tring to button his shirt."
        ma "The room was empty but the window had been opened."
        d "You think the person he was having an affair with escaped through the window?"
        ma "Of course, I knew he was up to something and after sending the fool to bed I searched the room and sure as day I found a hairpin in the rug."
        d "And you believe it was Ms. Galloway?"
        show marcella neutral
        ma "Yes, the problems only started after he spending more tiem with her and that night only proved my suspicions."
        d "How did he and Ms. Galloway know each other?"
        ma "He was introduced to her through his work associates and...they quickly became close"
        d "You must have been quite angry with your husband after finding out that he was cheating on you."
        show marcella disdain
        ma "Believe me detective, I was. That filthy pig could not not even stay loyal to his wife."
        hide marcella
        jump interogationMarcella

    "That's it for now":
        jump interogationChoice

menu interogationCecil:
    "What would you like to ask?"

    "Relationship with Scott Alston":
        d "Can you explain how you knew Mr. Alston."
        c "I tutored his son in college{w=0.3}, we shared a physics class and were quite close."
        c "Am I a suspect?"
        d "I'm the one asking the questions here Mr. Sharpe."
        c "Of course, sorry.{w=0.3} Continue."
        c "Anyways{w=0.3}, after I graduated I began teaching and began conducting my own studies and experiments."
        c "Mr. Alston took a personal interest in my findings and made a deal to to fund my ventures as long as he could use my research to help him build more weapons."
        jump interogationCecil

    "Whereabouts that night":
        d "Can you tell me about what happened that night?"
        c "Well, I had dinner with the Alston family and their friends and after that I spent the night here."
        d "Did anything noteworthy happen that night?"
        c "Yes{w=0.3}, there was an argument that broke out between Michael and Mr. Alston."
        d ""
        
