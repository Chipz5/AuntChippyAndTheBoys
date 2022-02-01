# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character('Chippy', color="#c8ffc8")
define a = Character('Akiki', color="#c8c8ff")
define t = Character('Tommy', color="#c8c8ff")
define r = Character('Raphy', color="#c8c8ff")
define m = Character('Meekah', color="#c8c8ff")
define h = Character('Hot Guy', color="#c8ffc8")

image bg out = im.Scale("outside.png", 1920,1080)
image bg house_out = im.Scale("home.png", 1920,1080)
image bg house_living = im.Scale("inside.png", 1920,1080)
image tom = "tom.png"
image meech_hurt = "Meekah/Meekah end.png"

# The game starts here.
layeredimage chippy:

    always:
        "chippy/chippy base.png"

    group brows:

        attribute brows_1 default:
            "chippy/chippy brows.png"

    group eyes:

        attribute eyes_1 default:
            "chippy/chippy eyes open.png"

        attribute eyes_2:
            "chippy/chippy eyes closed happy.png"

        attribute eyes_3:
            "chippy/chippy eyes open up.png"

    group mouth:

        attribute mouth_1 default:
            "chippy/chippy mouth open happy.png"

        attribute mouth_2:
            "chippy/chippy mouth closed happy.png"

        attribute mouth_3:
            "chippy/chippy mouth curious.png"

    group hands:

        attribute hand_1 default:
            "blank.png"

        attribute hand_2:
            "chippy/chippy hand curious.png"




layeredimage chippy_chibi:
    always:
        "chippy chibi/chippy chibi base.png"

    group hair:

        attribute hair_1 default:
            "chippy chibi/hair.png"

    group face:

        attribute face_1 default:
            "chippy chibi/chippy chibi confused face.png"

        attribute face_2:
            "chippy chibi/chippy chibi weird.png"

        attribute face_3:
            "chippy chibi/chippy chibi shock.png"

        attribute face_4:
            "chippy chibi/chippy chibi daydreaming.png"

        attribute face_5:
            "chippy chibi/chippy chibi gloating.png"

        attribute face_6:
            "chippy chibi/chippy chibi happy.png"

        attribute face_7:
            "chippy chibi/chippy chibi pissed.png"

        attribute face_8:
            "chippy chibi/chippy chibi silly.png"

        attribute face_9:
            "chippy chibi/chippy chibi cry.png"

        attribute face_10:
            "chippy chibi/chippy chibi weird1.png"

        attribute face_11:
            "chippy chibi/chippy chibi meh.png"

        attribute face_12:
            "chippy chibi/chippy chibi happy1.png"

        attribute face_13:
            "chippy chibi/chippy chibi cry1.png"

        attribute face_14:
            "chippy chibi/chippy chibi drool.png"

    group expressions:

        attribute expression_1:
            "chippy chibi/question marks.png"

        attribute expression_2:
            "chippy chibi/sweat drop.png"

layeredimage akiki:
    always:
        "aki base.png"

    group face:
        attribute face_1 default:
            "aki smile open.png"

        attribute face_2:
            "aki smile close.png"

    group hands:

        attribute hand_1 default:
            "blank.png"

        attribute hand_2:
            "aki hands.png"

layeredimage meekah:
    group accessories:
        attribute accessory_1:
            "Meekah/lighter.png"
    always:
        "Meekah/Meekah.png"


layeredimage raphy:
    always:
        "Raphy/Raphy.png"

    group base:

        attribute base_1 default:
            "chippy/chippy holding raphy.png"

    group expressions:

        attribute expression_1 default:
            "Raphy/Raphy sleep.png"

        attribute expression_2:
            "Raphy/Raphy irritated.png"

        attribute expression_3:
            "Raphy/Raphy cry.png"

        attribute expression_4:
            "Raphy/Raphy happy.png"

        attribute expression_5:
            "Raphy/Raphy meh.png"


layeredimage hotguy:
    always:
        "Guy/base.png"

    group expressions:

        attribute expression_1 default:
            "Guy/normal.png"

        attribute expression_2:
            "Guy/smile.png"

        attribute expression_3:
            "Guy/eyes closed smile.png"


label start:

    $ meech_feed = 0;
    $ raph_feed = 0;
    $ meech_bath = 0;
    $ raph_bath = 0;
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.



    scene bg out

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show chippy brows_1

    # These display lines of dialogue.

    "{i}Ah, it’s such a warm and beautiful day today. A perfect day for a picnic.{/i}"

    show chippy hand_2 mouth_3 eyes_3 brows_1

    "{i}Or maybe I should go visit my precious little nephews.{/i}"

    show chippy hand_1 eyes_1 mouth_1 brows_1

    "{i}Um… it’s been a while so I guess I’ll spend some time with Meekah and Raphy.{/i}"

    scene bg house_out

    "Chippy proceeds to see her nephews. She reaches their home and knocks the front door"

    show akiki hand_2

    a "OMG CHIPPY! We were just talking about you."

    show akiki hand_1

    a "Come in, here, hold Raphy"

    a "Babe! Chippy’s here"

    hide akiki
    show tom

    t "Oh, speak of the devil! Well, I guess that settles that babe"
    hide tom

    show chippy mouth_3 brows_1
    c "Um- ? settles what?"

    hide chippy
    show tom
    t "Our babysitter cancelled on us so you’ll be babysitting Meekah and Raphy for a week"

    hide tom
    show chippy mouth_3 brows_1
    c "But-"

    hide chippy
    show akiki at right

    a "Make sure to feed Raphy 5-6 times and Meekah thrice a day. I've already fed them a few times today. The expressed breast milk is in the freezer, be diligent with it! Call us if you have any problems!"

    show tom at left
    t "Bye! Have fun!"
    hide tom
    hide akiki
    hide chippy
    show chippy_chibi expression_1
    "Chippy looks confused as she watches Akiki and Tommy scurry off"

    c "eh-? What just happened?"
    jump Day1
