# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define o = Character("evil octopus")
define n = Character("Narrator", color="#c8ffc8") # maybe change colors?? idk


# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show uni-rover

    # These display lines of dialogue.

    n "You drive to a beach in Australia"
    
    n "You arrive on the uni-rover and it fades into you on the beach with refreshing iced matcha latte in hand"
    
    n "You step onto the tropical white sand, and the beautiful crystal clear turquoise water ripples in front of you"
    
    n "This will be a peaceful perfect day, but you’re not sure if it’ll end up perfect"


    jump scene_1

label scene_1:

    scene bg room

    show uni-rover.png

    n "You set up your beach umbrella and it is so stylish!"

    n "It’s summer, and that means in Australia the temperatures are lower than the winter"

    n "And today means perfect weather! Not scorching hot, but not cold at all"

    jump scene_2 
