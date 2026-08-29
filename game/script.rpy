# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define car = Character("uni-rover")
define b =Character("boba 2")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    show road
    scene road

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory. 

    show uni-rover at right


    # These display lines of dialogue.

    car "You drive to a beach in Australia"

    hide uni-rover
    show boba

    # These display lines of dialogue.    
    b "You arrive on the uni-rover and it fades into you on the beach with refreshing iced matcha latte in hand." 