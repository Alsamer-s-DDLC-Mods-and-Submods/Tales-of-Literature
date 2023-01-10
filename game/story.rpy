label story:
    show bg corridor
    play music t5
    player "Another Day in school is another day wasted"
    player "As I was walking down the hallway, I saw someone in the Distance"
    show monika 1a at t11
    m "Ah [player] I have something to ask you."
    "This is Monika, she is my Neighbor."
    player "Sorry Monika, I have to do something important fist."
    show monika 2c at t11
    m "What do you have to do [player]?"
    player "Sayori asked me for help."
    show monika 3b at t11
    m "Sayori? I saw her in your Classroom."
    player "Ok, thank you Monika, ask me later."
    m "I'll wait for you in the Libary."
    player "Got that, see you soon"
    hide monika

    stop music fadeout 2.0
    show bg class_day
    with wipeleft_scene
    play music t2 fadeout 1
    show sayori 1h at t11
    s "Hello [player]."
    "This is Sayori, my ex-childhood Friend and nowdays my Step-Sister."
    "My Family adopted her after her Parents died, 9 years ago."
    player "Sayori, whats up? You seem down."
    show sayori 1k at t11
    s "No [player], nothing is wrong. I just had a bad day."
    player "Are you hungry?"
    show sayori 5b at t11
    s "No..."
    player "Then im going to eat something alone."
    show sayori 4p at t11
    s "Wait!"
    s "Maybe i am a bit Hungry"
    show sayori 5a at s11
    s "But, I don't have any Money on me."
    player "Don't worry Sayori, food is on me today."
    show sayori 4r at h11
    s "Yay!"
    hide sayori

    show bg corridor
    with wipeleft_scene
    play music t5 fadeout 1
    show sayori 1a at t11
    "As we were walking down the Corridor, we heard a scream."
    show sayori 4m at h11
    n "WHAT THE FUCK!!!"
    s "What was that?"
    player "I don't know, but i think she need help"
    "We rushed where we thought the Scream came from."
    hide sayori

    show bg club_day
    with wipeleft_scene
    play music t6
    "We opened the Door and saw a little Girl with Pink Hair, staring at Manga on the Floor."
    show natsuki 5f at t22
    show sayori 2m at l21
    n "WHO THREW ALL MY MANGA ON THE FLOOR!"
    s "What Happened?"
    show natsuki 5g at t22
    show sayori 3c at t21
    n "Who are you two?"
    s "Im Sayori and thats [player]"
    player "Hello"
    player "And you are?"
    show natsuki 1c at t22
    show sayori 1a at t21
    n "Im Natsuki, second year."
    "I totally thought she is first year."
    player "Nice to meet you Natsuki."
    player "What happened again?"
    show natsuki 4e at t22
    n "Someone, threw all my Manga on the Floor!"
    show sayori 1b at t21
    s "I don't see it as a big problem, it's just books"
    show natsuki 5f at t22
    show sayori 1u at h21
    n "NO! IT'S NOT JUST A BOOKS!"
    show sayori 2u at s21
    s "Why are you yelling at me?"
    show natsuki 5g at t22
    n "These books mean a lot to me. Sorry for yelling at you, comes out sometimes."
    s "Im really sorry Natsuki, I din't know that this Manga means so much to you."
    player "May we assist you picking them up?"
    player "See it as a apologie"
    show natsuki 5e at t22
    n "No I don't need help of you two, I'll do it myself."
    show sayori 1f at t21
    player "Are you sure Natsuki?"
    show natsuki 4e at t22
    n "Yes I am Sure"
    player "Ok then, have great day!"
    show natsuki 1c at t22
    "Natsuki's Eyes light up as I said that"
    "But she doesn't say anything"
    hide sayori
    hide natsuki

    show bg lockers
    with wipeleft_scene
    show sayori 1f at t11
    player "Come on Sayori don't be sad just because someone yelled at you. It wasn't on purpose either."
    show sayori 1h at t11
    s "I know [player], but it just can't get it out of my Head."
    player "I know exactly what would brighten up your mood!"
    show sayori 3m at t11
    s "Oh Oh, What is it?, What is it?"
    player "I won't tell you, it's a surprise"
    show sayori 5c at t11
    s "Come on [player], please?"
    s "Pretty Please?"
    player "No, that would ruin the surprise."
    show sayori 1p at t11
    s "Meanie"
    "I ignore that. Let's get going now."
    hide sayori
    
    show bg house
    with wipeleft_scene
    show monika 3h at t22
    show sayori 1a at t21
    "As Sayori and I were walking back home, I saw Monika already waiting for me."
    show monika 3h at t22
    show sayori 1a at t21
    m "Where were you [player], I waited for you!"
    player "OMG Monika, I am so sorry. We had an accident on the way, that's when I must've forgotten about you."
    show monika 1r at t22
    m "It's alright [player], i gotta question for you."
    player "Please you can ask me inside my House, I just wanted to cook something for Sayori."
    player "You know, her cooking skills are bad. Like last time..."
    show monika 1c at t22
    show sayori 4p at t21
    s  "You know that it was an accident!"
    player "4 Times?"
    show sayori 1l at t21
    s "Eheh~"
    hide sayori
    hide monika

    show bg kitchen
    with wipeleft_scene
    "We entered mine and Sayori's House and made our way to the kitchen."
    show sayori 1a at t21
    show monika 1a at t22
    player "Sayori, why don't you relax a little."
    player "In the meantime, I will cook something for you, then Monika can ask her question."
    show sayori 3q at t21
    s "Ok [player]."
    show monika 4j at t11
    m "Now [player], I want to ask you, if you want to start a Club in school?"
    player "A Club huh?"
    player "Yeah I would be interested."
    player "Do you have any Idea about what kind of club?"
    show monika 3l at t11
    m "Not really."
    show monika 1k at t11
    m "But im sure we could figure it out."

    show bg black
    show monika 1a at t11
    m "This is the End of the Alpha."
    show monika 2b at t11
    m "So this is the goodbye for now."
    show monika 1e at t11
    m "See you around next time."
    "Wait before we roll the credits, I want to thank Milo and Dreamscached for supporting and helping me."
    show monika 4b at t11
    m "Now, roll the credits."
    jump credits
