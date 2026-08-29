# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define o = Character("evil octopus, color=purple")
define n = Character("Narrator", color="#50FFD6") 


# The game starts here.
label start:

    scene bg beach_1

    show uni-rover

    n "You drive to a beach in Australia"

    hide uni-rover
    show matcha_latte 
    
    n "You arrive on the uni-rover and it fades into you on the beach with refreshing iced matcha latte in hand"
    
    n "You step onto the tropical white sand, and the beautiful crystal clear turquoise water ripples in front of you"
    
    n "You think 'This will be a peaceful idyllic day, but you’re not sure if it’ll end up ideal' as you sip your matcha latte" # would like to make quotations
    n "heheh i am sure a delicious matcha, thinks the matcha latte"

    jump scene_1

label scene_1:

    scene bg beach_1

    show boba 

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

    n "Meanwhile, a sneaky seagull grabs a bite out of your fries"

    n "Seagull is yelling 'Krraaa!'"

    n "Which direction you swim to?"
    menu:
        "Left":
            jump swim_left
        "Right":
            jump swim_right
        "the undercurrent!! :D ^_^":
            jump swim_undercurrent

label swim_left:
    n "You see a merman with a cowboy hat!"

    n "MM: Yeehaw! Howdy there! How are ya?"

    n "Y: Huh?? Who are you?"

    n "MM: I am a Texas merman, and a sea-cowboy by heart "

