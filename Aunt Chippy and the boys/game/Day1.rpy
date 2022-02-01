# This script contains happenings of Day1 with the boys

label Day1:

    scene bg house_living

    show chippy mouth_2

    c "Well, Meech and Raph.. I guess it's just us for a few days"

    c "wait... where is Meekah?"

    hide chippy
    show chippy_chibi face_3

    "Turns around and sees Meekah playing with a lighter"

    hide chippy_chibi
    show meekah accessory_1
menu:

    "Do nothing":

        jump day1_choice1_bad

    "Grab the lighter and replace it with a toy":

        jump day1_choice1_good



label day1_choice1_bad:
    hide meekah
    show chippy_chibi face_5
    c "meh, it's only a lighter. I'm sure it's fine"

    hide chippy_chibi
    # enter pic of burnt meech

    jump fail

label fail:

    "You burnt your nephew. You're a bad aunt!"

    # pic of akki and tommy yelling in the bg

    return

label day1_choice1_good:
    hide meekah
    show chippy_chibi face_3
    c "OMG MEECH! Give me that!"

    c "Here, Play with this instead"
    hide chippy_chibi

    jump day1_choice1_continue

label day1_choice1_continue:

    show raphy

    "While Meekah continues playing happily, Chippy and Raphy sit beside him and watches him play"

    show raphy expression_2

    "After a while, Raphy gets restless and starts squirming to get out of Chippy's hold"


    r "{i} coos {/i}"

    menu:

        "Do nothing":

            jump day1_choice2_ignore

        "Squish him because he's so cute!":

            jump day1_choice2_squish

        "Get up and walk while cradling him":

            jump day1_choice2_walk


label day1_choice2_ignore:

    show raphy expression_3

    "Raphy starts screaming at the top of his lungs"

    hide raphy

    show chippy_chibi face_2

    menu:


        "{i} Oh no! What do I doooo?? {/i}"

        "Make funny faces":

            jump day1_choice2_funnyface

        "Feed":

            jump day1_choice2_walk


label day1_choice2_funnyface:

    show chippy_chibi face_8

    "Chippy ends up making scary faces and frightens Raphy"

    hide chippy_chibi

    show raphy expression_3

    "Raphy is inconsolable and Meekah starts crying too because of all the noise"

    hide raphy

    show chippy_chibi face_13

    menu:

        "{i} Ahhhh! How do I make them stop?? {/i}"



        "Run away and ditch the kids, because duh, they are not yours!":
            show chippy_chibi face_6
            jump day1_choice3_runaway

        "Switch on the TV and distract the kids":
            show chippy_chibi face_6
            jump day1_choice3_distract


label day1_choice3_runaway:

    show chippy_chibi face_13

    "You abandoned your nephews! You're a bad aunt!"

    return

label day1_choice3_distract:

    hide chippy_chibi

    show raphy expression_3

    "You were able to calm Meekah down but Raphy is still crying"

    menu:

        "Feed":

            jump day1_choice2_walk


label day1_choice2_squish:

    jump day1_choice2_ignore

label day1_choice2_walk:

    show raphy

    "Raphy stops crying and falls asleep"

    jump day1_choice2_continue


label day1_choice2_continue:

    hide raphy
    show chippy

    c "Finally some peace and quiet. I'm beat!"

    show chippy hand_2 mouth_3 eyes_3 brows_1

    menu:

        c "Maybe I should get some shut eyes too"



        "Fall asleep":
            hide chippy
            jump day1_choice4_fallasleep

        "Prepare food for Meekah":
            hide chippy
            jump day1_choice4_preparefood

label day1_choice4_fallasleep:

    show chippy_chibi face_11

    "You wake up to Meekah tugging your hair and crying"

    menu:

        "Check diaper":

            jump day1_choice5_diaper

        "Prepare food for Meekah":

            jump day1_choice4_preparefood


label  day1_choice5_diaper:

    show chippy_chibi face_2

    "You find a big poop in the diaper"

    menu:

        "Ewwww poop! Run away":

            jump day1_choice3_runaway

        "Change the diaper":

            c "There you go! All clean, come let's get you some food"

            jump day1_choice4_preparefood


label day1_choice4_preparefood:

    hide chippy_chibi

    show chippy

    "Chippy feeds Meekah and then puts him to bed and he falls asleep"

    c "Phew! Finally both are asleep"

    show chippy hand_2 mouth_3 eyes_3 brows_1

    menu:

        c "Hmm... what should I do now?"

        "Go out to get your nails done":

            jump day1_choice6_nails

        "Get some shut eyes":

            jump day1_choice6_sleep


label day1_choice6_nails:

    hide chippy

    show chippy_chibi face_13

    "You left the kids alone at home! You're a bad aunt"

    return

label day1_choice6_sleep:

    hide chippy

    "You sleep a peaceful sleep and dream pleasant dreams"

    show chippy_chibi face_5

    "You wake up to small coos and see that Raphy is awake in his craddle"

    show chippy eyes_2

    c "Hi Raphy-Waphy! Did you have a good nap?"

    menu:

        "Play with him":

            "You play with him for a while and then gently rock him back to sleep"

        "Feed him":

            "Raphy falls asleep while you feed him"


    "With both kids asleep again, Chippy decides to read a book for a while"

    show chippy hand_2 mouth_3 eyes_3 brows_1

    c "Yawn.. better watch some youtube videos"

    "Opens Youtube and watches cute videos of weird animal friends"

    hide chippy

    show chippy_chibi face_8

    menu:

        c "Hm.. I'm pretty hungry, let's see what's there to eat"

        "Pop some popcorn":

            "The sound of the popcorn popping wakes Meech"

            jump day1_choice7_wakekids

        "Go out to eat":

            jump day1_choice6_nails

        "Reach for the cookies from the top shelf":

            "You clumsily reach up and push down the jar and break it."

            "The sound of the jar shattering wakes both the children up, but Raphy curls back to sleep"

            c "Ah, I should clean the shattered pieces so that noone gets hurt, but if I don't go to Meech now, he'll bring the whole house down"

            c "What do I do"

            menu:

                "Ignore the mess":

                    c "Um, I can clean up later. Let me go check on Meech first"

                    $ glass_on_floor = True;

                "Clean up first":

                    c "Meech can wait for a bit. I don't want anyone getting hurt on the glass shards"

                    "Chippy cleans the floor and then quickly goes and checks on Meekah"

            jump day1_choice7_wakekids


label day1_choice7_wakekids:

    show chippy_chibi face_9

    "{i} Darn, my few mins of peace are over. How do I engage them now. {/i}"

    hide chippy_chibi

    show chippy

    "{i} Maybe a short stroll in the park would help {/i}"

    "Chippy quickly got Meekah ready and put Raphy in the baby stroller. Raphy slightly opens his eyes but then closes it immediately and cuddles back in his stroller"

    scene bg out

    "At the park, Meekah runs around excited and looks intently at the big kids playing dodgeball"

    "You notice Meekah walking towards them"

    menu:

        "Let Meekah wander around":

            "Meekah walks too close to them and a ball hits his head"

            jump day1_choice8_bump

        "Pull Meekah back to the small kid area of the park":

            "Meekah fusses around for a bit but then gets distracted by the swings"

            jump day1_choice8_continue


label day1_choice8_bump:

    show meech_hurt

    "Meekah gets a bump on his head"

    "You let your nephew get hurt! You're a bad aunt!"

    # pic of meekah with bump

    return


label day1_choice8_continue:

    "Chippy sees a very hot guy reading on a bench in the park"

    show chippy_chibi face_6

    c "Oooo... maybe I should walk past him and get his attention"

    menu:

        "Walk past him":

            jump day1_choice9_walkpast

        "Ignore him":

            c "Meh, I can't chase hot guys while taking care of these two. *sigh* Maybe another day"

            jump day1_choice9_continue


label  day1_choice9_walkpast:

    show chippy_chibi face_2

    "He doesn't notice you."

    c "He didn't even look up! Maybe it's because I'm pushing a stroller and he thinks I'm a mom"

    show chippy_chibi face_5

    c "Well, Raph is still asleep so I could just leave him in the shade for a bit"

    "Chippy leaves the stroller under a tree and walks past him again keeping one eye on the stroller"

    show chippy_chibi face_11

    "Yet again, he doesn't notice you"

    menu:

        "Perseverance is key! You decide to try again":

            show chippy_chibi face_10 expression_2

            "You strut past him again but it's in vain"

            hide chippy_chibi

            show chippy_chibi face_6

            c "Well, time for plan B"

            # Chippys eyes glowing with determination

            show hotguy at right

            show chippy at left

            "Chippy sits on the other side of the bench and strikes up a conversation about the book he's reading"

            "Chippy's plan works and the two engage in a long conversation. After a while, they decide to take a short stroll in the park"

            hide chippy
            hide hotguy

            show hotguy expression_3

            h "I feel so much connection with you, would you like to grab a coffee sometime?"

            menu:

                "For sure, I'd love to see you again!":

                    hide hotguy
                    show chippy
                    "Chippy gives the hot guy her number"

                "Meh, he's not that attractive anymore":
                    hide hotguy
                    show chippy_chibi face_2
                    c "Eh, well, you see - , I'm in town only for today... "
                    hide chippy_chibi
                    show hotguy
                    h "Oh, that's a shame! I hope our paths cross again someday"

            hide hotguy
            "The two bid farewell and Chippy suddenly returns to the real world and realises she's forgotten about the kids!"

            show chippy_chibi face_3

            c "AAAAHH!!! OMG I totally forgot about Meech and Raph"

            "Chippy rushes to the tree under which she left Raphy and her heart sinks"

            "The stroller is not there anymore!"

            jump day1_choice10_RaphyMissing

        "Meh, he's not that hot":

            show chippy_chibi face_2

            c "He's so not worth it"

            "Chippy makes her way back to Raphy but still eyes the hot guy from under the tree"

            show chippy_chibi face_14

            "Chippy keeps eying the hot guy from a distance till he finally gets up and leaves"

            # chippy drooling

            c "Well Raphy, I guess we should be heading back home as well"

            "Chippy looks in the stroller and finds Raphy still sleeping peacefully"

            show chippy_chibi face_6

            c "Awwww... my precious lil baby... come let's go find your brother"

            "Chippy makes her way back to the kids park and finds a number of mothers huddled together around a crying child"

            c "Oh gosh, please let that not be Meech! I cannot bear the judgement from those mothers!"

            "Chippy slowly makes way towards the crowd"

            show chippy_chibi face_5

            c "Phew, it's not Meech! Thank goodness!"

            "Chippy looks around for Meech in the kids park but can't spot him"

            show chippy_chibi face_1

            c "It's getting late... MEECH! Where are you!"

            "Everyone starts leaving the park and it's half empty now. Chippy franctically runs around searching for Meekah"

            "You search high and low for almost an hour with the help of a few parents"

            jump day1_choice10_MeekahMissing


label day1_choice10_RaphyMissing:

    show chippy_chibi face_13

    "Raphy's been kidnapped! You're a bad Aunt!"

    return

label day1_choice10_MeekahMissing:

    show chippy_chibi face_13

    "Meekah's wandered off and nowhere to be found! You're a bad Aunt!"

    return


label day1_choice9_continue:

    "Raphy wakes up in between but just coos and looks up at the beautiful sky. Meekah has the time of his life and even makes new friends"

    "One of the mothers approaches Chippy and strikes up a conversation with her and asks whether Meekah would like to have a play date with her twins"

    "Chippy agrees and the two exchange numbers"

    "Chippy and the kids stay in the park till dusk and then they finally go back home."

    "Meekah is half asleep by the time you get back home"

    menu:

        "You tuck Meekah into bed":

            c "Goodnight sweetheart.. sweet dreams"

            jump day1_choice11_continue

        "Eww... Meech is super muddy and dirty, he has to have a bath!":

            c "Come on baby, let's get you cleaned up"

            jump day1_choice11_bath


label day1_choice11_continue:

    return

label day1_choice11_bath:

    return
