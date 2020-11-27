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
default CecilDC = False
default IvyDC = False

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
        jump interogationWilburIntro

    "Wayne Howard":
        jump interogationWayne

    "Ivy Galloway":
        jump interogationIvy

    "That's all for now":
        return

menu interogationMichael:
    "What would you like to ask?"

    "Relationship to Scott Alston":
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

    "Push how Scott ran the company" if MichaelDC == True:
        show michael neutral
        d "In your honest opinion, do you think that your father ran the company well?"
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

    "Push on condition of company" if MichaelDC == True:
        show michael neutral
        d "Do you think the company is still in good condidtion?"
        show michael happy
        mi "I do detective. With the right direction, our company could flourish again."
        d "And you were next in line to inherit the company should your father pass.{w=0.3} Correct?"
        mi "Indeed I am."
        show michael anger
        mi "Wait.{w=0.3} I wouldn't actually kill my father just to inherit his company though!"
        d "We'll see, Mr. Alston."
        hide michael
        jump interogationMichael

    "That's all for now":
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
        s "Bitter is just rich. At times  I could barely stand him and his self-centered, arrogant world views."
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

    "That's all for now":
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

    "Relationship to Scott Alston":
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
        ma "Yes, the problems only started after he spending more time with her and that night only proved my suspicions."
        d "How did he and Ms. Galloway know each other?"
        ma "He was introduced to her through his work associates and...they quickly became close"
        d "You must have been quite angry with your husband after finding out that he was cheating on you."
        show marcella disdain
        ma "Believe me detective, I was. That filthy pig could not not even stay loyal to his wife."
        hide marcella
        jump interogationMarcella

    "That's all for now":
        jump interogationChoice

menu interogationCecil:
    "What would you like to ask?"

    "Relationship to Scott Alston":
        show cecil neutral
        d "Can you explain how you knew Mr. Alston."
        c "I tutored his son in college{w=0.3}, we shared a physics class and were quite close."
        show cecil surprise
        c "Am I a suspect?"
        d "I'm the one asking the questions here Mr. Sharpe."
        show cecil thinking
        c "Of course, sorry."
        show cecil neutral
        c "Anyways{w=0.3}, after I graduated I began teaching and began conducting my own studies and experiments."
        c "Mr. Alston took a personal interest in my findings and made a deal to to fund my ventures as long as he could use my research to help him build more weapons."
        hide cecil
        $CecilDC = True
        jump interogationCecil

    "Whereabouts that night":
        show cecil neutral
        d "Can you tell me about what happened that night?"
        c "Well, I had dinner with the Alston family and their friends and after that I spent the night here."
        d "Did anything noteworthy happen that night?"
        show cecil thinking
        c "Yes{w=0.3}, there was an argument that broke out between Michael and Mr. Alston."
        d "An argument between your boss and your friend.{w=0.3} It must be difficult to choose a side in that scenario."
        show cecil neutral
        c "Oh, I would never get involved their familial issues."
        d "Of course."
        hide cecil
        jump interogationCecil

    "Push relationship with Scott Alston" if CecilDC == True:
        show cecil neutral
        d "You said that Scott was paying you to research new alternatives for weapons?."
        c "Among other things. Yes, he was."
        d "How long have you been working for Mr. Alston?"
        show cecil thinking
        c "Uhh, maybe 3 or 4 years now?"
        d "Not very long then."
        d "What breakthroughs have you made so far?"
        show cecil panic
        c "Haha, uh.{w=0.3} Well."
        c "I-uh, had this idea of{w=0.3} increasing efficiency through{w=0.3} streamlining innovation."
        d "I'm assuming not a lot of progress then."
        show cecil surprise
        c "I've been distracted from my work lately. A lot of things happening."
        d "I'm assuming Mr. Alston wasn't too happy with those results."
        show cecil thinking
        c "No, he wasn't. He's been increasingly disappointed and annoyed. Lately he even threatened to cut my fundings for my projects."
        d "That must have put a lot of pressure on you."
        show cecil surprise
        c "Of course! I need the funds to pay for my home and necessities!"
        hide cecil
        jump interogationCecil
        
    "Push relationship with Michael Alston" if CecilDC == True:
        show cecil neutral
        d "You said that you were friends with Michael Alston in college?"
        c "Yes, we were dormmates our first year and stayed friends for the rest of our education."
        d "Are you still close?"
        c "I would say so, yes."
        d "You must be happy then to hear that he's inheriting the family empire."
        show cecil thinking
        c "Very. He's always been telling me about all the things he'd do if he were in charge."
        c "The changes he'd make. The ideas he had."
        d "Would you still be collaborating with the company with Michael in charge?"
        show cecil neutral
        c "Of course, he had told me that if he were in charge he would grant me more resources and a higher pay."
        d "So, to put it  into perspective. You'd benefit greatly from Mr. Scott Alston's death?"
        show cecil surprise
        c "I-I don't like your insinuation here detective."
        hide cecil
        jump interogationCecil

    "That's all for now":
        jump interogationChoice

label interogationWilburIntro:
    d "Mr. Wyatt, welcome."
    wi "Can I call my lawyer?"
    d "You won't be needing them, we just want to ask you a few questions."
    wi "I don't think that would be wise.{w=0.3} I've always been told to contact my attorney should I ever end up in a conversation with the authorities."
    d "I just need a bit of information. Otherwise I'd have to keep you here until your lawyer arrived."
    d "And that would take some time."
    wi "That's{w=0.3}...true. Perhaps I could answer some questions."
    wi "Fine."

menu interogationWilbur:
    "What would you like to ask?"

    "Relationship to Scott Alston.":
        d "Could you please explain what your relationship was to Scott Alston."
        wi "Ah yes, Scott and I were college friends you see."
        wi "We got to know each other during our economics classes and we kept in contact after we graduated."
        d "From what I understand, you and Mr. Alston were rivals."
        wi "Professionally, but not privately."
        wi "At least, that's how it used to be"
        d "Oh? How so?"
        wi "I hate to admit it{w=0.3}, but lately he had been treating our friendly rivalry more seriously."
        wi "Before, we were weren't inclined towards running each other out of buisiness, but now?"
        wi "He's put my company under more pressure and to be quite frank, it's been taxing trying to keep up."
        wi "I've lost quite a few customers due to his backhandedness."
        d "Did you ever confront him about it?"
        wi "And let him know he was getting under my skin? Of course not!"
        wi "Besides, it was quite obvious that he knew what he was doing. He's been extremely smug."
        wi "He knew he was forcing me out of buisiness."
        d "You must have felt betrayed."
        wi "I did, detective.{w=0.3} It was always us two running the scene, u til he decided to stab me in the back."
        wi "He started lowering prices and actively started encroaching on my own usual buyers."
        d "That must have felt unfair."
        wi "Of course it did.{w=0.3} I must be honest with you detective, the economic situation might be even worse than how I'm making it out to be."
        wi "I'm almost facing bankruptcy, I can barely even spare the expenses of the suit I'm wearing."
        d "And this was all because of Scott."
        wi "Indeed. God, I hated his guts."
        jump interogationWilbur

    "Whereabouts that night.":
        d "What were you doing the night of Scott Alston's death?"
        wi "Not much. The most notable thing that happened that night was probably the argument during dinner."
        d "Nothing happened after that?"
        wi "Hmm{w=0.3}, an argument broke out while I played cards with Scott and Wayne."
        d "Over what?"
        wi "Well, Wayne accused me and Scott of cheating. He's an extremely sore loser with quite a temper."
        d "Were you cheating?"
        wi "Of course not, he just a terrible poker face."
        jump interogationWilbur

    "That's all for now":
        jump interogationChoice

menu interogationWayne:
    "What would you like to ask?"

    "Relationship to Scott Alston":
        show wayne neutral
        d "How did you know Scott Alston?"
        wa "Scott was one of our weapons contractors. We got in contact because of his contract with the military, I was one of the people on our end handling buisiness."
        d "You must've gotten close to be invited to his birthday dinner."
        wa "Yeah. We got to know each other pretty well, it's good to maintain good relations with your contractor."
        d "So there was a buisiness angle to your friendship?"
        show wayne anger
        wa "There's always a buisiness angle with these people."
        d "These people?"
        wa "Buisiness people! Contractors, designers, all of them. It's part of the deal."
        d "You don't seem to have the highest regard for them."
        show wayne fury
        wa "You got that right.{w=0.3} I would they weren't cowards."
        d "Cowards?"
        wa "Have you ever seen a buisiness man drafted? Or their families for that matter?"
        show wayne anger
        wa "Always a private doctor there to let them off the hook with some rare medical condition for the right amount of money."
        d "I see."
        hide wayne
        jump interogationWayne

    "Whereabouts that night":
        show wayne neutral
        d "So what happened that night?"
        show wayne anger
        wa "Scott's faliure of a son started an argument again so I told him to shut it."
        d "Was this during the dinner?"
        show wayne neutral
        wa "Yeah, it was."
        d "And what happened after that?"
        wa "We played some cards, had us a drink."
        d "Who's we?"
        wa "Me, and those cheating worms Scott and Wyatt."
        show wayne anger
        d "Cheating?"
        show wayne fury
        wa "Yes! They were obviously cheating, they won every round we played!"
        d "You must've been quiet annoyed."
        wa "Yeah, I was furious! A bunch of con-men, that's what they are!"
        hide wayne
        jump interogationWayne

    "That's all for now":
        jump interogationChoice
        
menu interogationIvy:
    "What would you like to ask?"

    "Relationship to Scott Alston":
        d "So{w=0.3}, how did you know Scott Alston?"
        i "We were introduced through a couple of Scott's work friends at a party one night and we had been{w=0.3}...friendly ever since."
        d "With all due respect Ms. Galloway, I'm afraid we have multiple witnesses."
        d "They can pin you two at the Hotel Nova, the Sanctum Spa and Resort, the Atlantis Summit Hotel, the Lavish Chateau and the Eclipse. Just to name a few."
        i "Then why through this song and dance of asking me when you've already made up your mind detective?"
        d "It's just procedure. So?"
        i "A lady doesn't kiss and tell."
        d "There's something to tell then?"
        i "Interpret that as you will detective."
        $IvyDC = True
        jump interogationIvy

    "Whereabouts that night":
        d "Can you tell me what happened that night?"
        i "Certainly detective."
        i "There was an argument between Scott and his son, Michael, during dinner."
        d "Did you take any sides?"
        i "Of course not, who wants to get in between a boy's squabble? I merely observed."
        d "And after that?"
        i "I'm afraid I got into a squabble myself, with Mrs. Alston herself."
        d "About what?"
        i "She accused me of having an affair with her husband."
        d "And?"
        i "I defended myself, of course."
        d "You denied the affair?"
        i "I said I defended myself."
        i "After that I went on a walk around the grounds to calm myself down."
        d "Did anyone see you?"
        i "I do not believe so."
        d "So we don't have anyone to verify that."
        d "Did anything else happen that night?"
        i "I saw Michael on the way in.{w=0.3} He looked awful so I helped him back to his room."
        d "Did anything happen with him?"
        i "He was rather drunk."
        i "The poor boy could barely handle himself anymore, let alone a woman."
        jump interogationIvy

    "Push relationship with Scott Alston" if IvyDC == True:
        d "So, you mentioned that you were introduced to Scott through his work associates?"
        i "Yes, I was."
        d "Could you tell me how you knew them?"
        i "I would but I feel like you already know."
        d "We have evidence of you being associated with several men with wealth or in power."
        d "All of them were drained financially during the periods in which you were with them."
        i "And you think I was doing the same to Scott?"
        d "We have his financial reccords from 2 months back, the same amount of time you've known Mr. Alston and they show they same decline."
        d "Although, recently the decline flattened out.{w=0.3} Let me give you a hypothetical."
        d "You and Scott Alston are having an affair and you've been draining him dry of all his money."
        d "He figures that out and there's an argument.{w=0.3} The argument turns into a fight and soon that fight turns physical and before you know it, you've killed him."
        i "That{w=0.3}, that's preposterous."
        jump interogationIvy

    "That's all for now":
        jump interogationChoice