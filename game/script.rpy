# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define y = Character("You", color="#F195E7")
define n = Character("Narrator", color="#50FFD6")

define tex_merman = Character("Texas Sea-Cowboy Merman", color="#00BFFF")
define pearl_mermaid = Character("Rose Pearl the Mermaid", color="#FFB6C1")
define merfin = Character("Merfin", color="#1E1AFF")

define krak = Character("Kraken the evil octopus", color="#800080")


# The game starts here.
label start:

    scene road

    show uni-rover

    n "You drive to a beach in Australia in your brand new uni-rover"

    hide uni-rover
    scene empty beach
    show boba 
    n "you arrive at the beach with a refreshing iced matcha latte in hand"
    
    n "You step onto the tropical white sand, and the beautiful crystal clear turquoise water ripples in front of you"
    
    n "You think 'This will be a peaceful idyllic day, but you’re not sure if it’ll end up ideal' as you sip your matcha latte" # would like to make quotations
    n "heheh vut i am sure of the delicious matcha i have, you then CHUG the matcha latte"
    hide boba
    jump scene_1

label scene_1:
    hide empty beach
    scene beach

    n "You set up your beach umbrella and it is so stylish!"

    n "It’s summer, and that means in Australia the temperatures are lower than the winter"

    n "And today means perfect weather! Not scorching hot, but not cold at all"

    n "Are you enjoying the weather?"
    menu:
        "Yes":
            jump yes_weather
        "No":
            jump no_weather

    jump scene_2 

# weathers
label yes_weather:
    n "You apply some sunscreen and sunbathe for a while, deciding how long you want to stay in the sun for"
    menu:
        "A 30 minutes":
            n "You don't see much tan"
        "B 1 hour":
            n "You have a perfect tan"
        "C 2 hours":
            n "You're slightly sun burnt but overall a nice tan"
        "D 10 hours":
            n "You're now a lobster 🦞"

    jump scene_2


label no_weather:
    n "You apply an exorbitant amount of sunscreen on your skin and hide behind your beach umbrella, reading a book, for a while "
    jump scene_2


label scene_2:
    n "Finally, you decide to take a dip in the ocean. You run to the waters and splash!! You're out for a swim!"
    show seagull
    n "Meanwhile, a sneaky seagull grabs a bite out of your fries"

    n "Seagull is yelling 'Krraaa! Krraaa!'"
    hide seagull
    hide beach
    show underwater

    n "First you swim in the left direction"
    jump swim_left

label swim_left:
    show mermen
    n "You see a merman with a cowboy hat!"

    tex_merman "Yeehaw! Howdy there! How are ya?"

    y "Huh?? Who are you?"

    tex_merman "I am a Texas merman, and a sea-cowboy by heart."

    y "I think I need to go now."

    tex_merman "Wait! I have a gift for you!"

    n "He gives you a magical lasso. And you say thank you and swim away."
    hide mermen

    n "Next you swim in the right direction"
    jump swim_right

label swim_right:
    n "There’s something shining so bright in the distance that you’re getting kinda blinded"
    show mermaid
    n "You see a mermaid! :D Her scales are pink and so is her outfit, she has a plethora of pink gems including pink pearls, pink sapphire, pink opals, pink coral and more! "

    y "Huh?? Who are you? How do you have an extravagant amount of gems?"

    pearl_mermaid "I am the pink mermaid. My name is Rose Pearl. That is whatever, the real question is who are you ? "

    y "I am a proud Aussie, that’s who I am!"

    pearl_mermaid "Hmmm okay Aussie. I need some help on the island."

    y "What kind of help do you need?"

    pearl_mermaid "I need you to help me find my lost pink pearl necklace. It is very important to me, and I can’t find it anywhere."

    y "Okay, I will help you find it."

    n "In an hour you come back with the pink pearl necklace for Rose Pearl the Mermaid. She is very happy and grateful for your help." 

    pearl_mermaid "Rose Pearl: Thank you so much for helping me find my pink pearl necklace! I would like to give you a gift in return."

    n "She gives you a magical brooch."
    hide mermaid

    n "Finally you swim under the undercurrent! :0 ToT"
    jump swim_undercurrent

label swim_undercurrent:
    n "Aaaah the undercurrent!!!"

    n "You are being pulled down by the undercurrent, and you are struggling to swim back up to the surface"

    n "You see a merfin, a mermaid/merman type creature but nonbinary, swimming towards you and pulls you into a bubble of air"
    show merfin
    y "I don't know who you are but thank you for saving me from that horrible undercurrent!"

    merfin "You're welcome, I am a merfin. and because i saved you i need you to help me too! ToT"

    y "What do you need help with?"
hide merfin
    merfin "You need to help me with deciphering codes from a book"
    show book
    n "try to decifer the code!"

    n "You help the merfin decipher the codes from the book"
    hide book
    jump scene_3

label scene_3:
    n "You swim back to the shore and dry off in the sun."
    scene beach
    y "Ah! Time for another swim."

    n "For some reason, you forgot to put your magical lasso and brooch away"
    scene underwater
    n "You jump back in but you see all the fishes, merfolk and sea creatures of all kind rushing to the shore"

    y "Hmmm why is everyone swimming to the shore?"

    n "Well, you're not exactly concerned about that and just keep swimming"

    n "Then you see it... A Sea Monster!"

    n "And just a sea monster... a Kraken!!"

    n "You have no where to run! or may I say swim"

    n "You do what all imbecilic heroes do... Fight!! :D"

    y "Hmmm maybe this lasso and brooch can be a weapon?"

    y "Aah I got this! The brooch might be a nuclear launch pad and the deciphered code is a nuclear code :D"

    n "KRAKEN BOSS FIGHT TIME!"
    jump kraken_fight

label kraken_fight:
    n "Choose your weapon"
        menu:
            "Magical Lasso"
            "Brooch broach attack!"




n "You swing the magical lasso around and it whips the Kraken. You do that a couple of times until the Kraken is weaker!"
