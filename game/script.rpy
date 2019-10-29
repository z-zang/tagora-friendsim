# search zich to get to currently being modified parts of the code

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init -1 python:

    def tspk(what, amt=0, stmt=None, **kwargs):

        t(what, **kwargs)

        global amount
        amount = amt

        global bill

        portion = int(amt/5)

        if amt != 0:

            renpy.hide_screen("moneyadd", layer=None)
            renpy.show_screen("moneyadd", moneyadded=amt)

        if stmt != None:

            renpy.hide_screen("moneystmt", layer=None)
            renpy.show_screen("moneystmt", statement=stmt)

        i = 5

        while i > 0:

            renpy.pause(0.02)

            bill += portion
            amt -= portion

            i -= 1

###########################################################################
############# styles ######################################################


style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


style outlined:
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    color "FFFF00"
    bold True

style friend:
    outlines [ (absolute(2), "#FF00FF", absolute(1), absolute(1)) ]
    color "FFFF00"
    font "courbd.ttf"
    size 72

style choice_button_text:
    color "0000FF"
    font "courbd.ttf"

################CHARACTERS########################

# default MC textbox
define narrator = Character(window_background="gui/textbox_narration.png", what_font='courbd.ttf', what_size=22,  color='#000000', what_color='#000000')
# no background box, used for black screens
define op = Character(window_background="gui/textbox_blank.png", what_font='courbd.ttf', what_size=28,  color='#FFFFFF', what_color='#FFFFFF', what_xalign=0.5, what_text_align=0.5)
# TAGORA
define t = Character("TAGORA", color='#FFFFFF', image="tagora", window_background="gui/textbox_teal.png", who_outlines=[ (4, "#008282") ],)


############IMAGES AND SHIT#################
#i'd advise you keep ypos the same for the important characters!
#also, i've left an ardata sprite in there just to help you to keep everything in proportion
image robegor neutral = Image("images/goredit/robetagora_neutral.png", ypos=730)
image robegor disgust = Image("images/goredit/robetagora_disgust.png", ypos=730)
image robegor shrug = Image("images/goredit/robetagora_shrug.png", ypos=730)
image robegor think = Image("images/goredit/robetagora_think.png", ypos=730)
image robegor smug = Image("images/goredit/robetagora_smug.png", ypos=730)
image robegor sexy = Image("images/goredit/robetagora_whydoeshelooksexytho.png", ypos=730)

image bg mc_hideout = "images/bgs/mc_hideout.png"
image bg outglut = "images/bgs/outglut.png"
image bg tagora_bath = "images/bgs/tagorabath.png"
image bg tagora_int = "images/bgs/tagorainterior.png"
image bg tagora_ext = "images/bgs/tagoraexterior.png"

image ending = "images/bgs/a_happy_end.png"

image money = "images/money/cashmoney.png"

## COMMON TRANSFORMS ##
#these are all transforms to make your sprite bounce around a little! it's super useful for making your game more dynamic
# bounce
# nod
# twitch
# shudder
# lowered
# bouncing
# shaking
# shuddering
# speaking
# stopspeaking
# shoveright
# shoveleft
# shoveoffleft
#
# moveinright
# moveinleft
# moveinbottom
# moveintop
# quickbouncetwice
# flipped

transform wiggle:

    rotate 0
    ypos -250

    on hover:
        linear .1 rotate -2
        linear .1 rotate 0
        linear .1 rotate 2
        linear .1 rotate 0

transform bounce:
    ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730

transform nod:
    ypos 730
    easeout 0.12 ypos 742
    linear 0.12 ypos 730

transform twitch:
    ypos 730 xpos 640
    easein 0.06 ypos 736 xpos 644
    linear 0.06 ypos 730 xpos 640

transform shudder:

    xpos 640
    linear 0.04 xpos 637
    linear 0.04 xpos 640
    linear 0.04 xpos 643
    linear 0.04 xpos 640
    repeat 4

transform lowered:
    ypos 730
    linear 0.75 ypos 765

transform bouncing:
    ypos 730
    linear 0.1 ypos 720
    linear 0.1 ypos 730
    repeat

transform shake:
    ypos 730
    linear 0.07 ypos 732
    linear 0.07 ypos 730

transform shaking:
    ypos 730
    linear 0.07 ypos 732
    linear 0.07 ypos 730
    repeat

transform shuddering:

    xpos 640
    linear 0.04 xpos 637
    linear 0.04 xpos 640
    linear 0.04 xpos 643
    linear 0.04 xpos 640
    repeat

transform speaking:
    easein 0.1 zoom 1.01

transform stopspeaking:
    easein 0.1 zoom 1

#Quickly push sprite to side of screen
transform shoveright:

    linear 0.1 xpos 960

transform shoveleft:

    xpos 640
    linear 0.1 xpos 320

transform shoveoffleft:

    linear 0.1 xpos -320

transform shoveoffright:

    linear 0.1 xpos 1320

transform shoveup:

    xpos 640 ypos 1440
    linear 0.1 ypos 730

## ADDED ANIMATIONS
# quickbouncetwice
# flipped

transform quickbouncetwice:
    ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730

transform flipped:
    xzoom -1.0

########################################################################
#####zich################ MONEY TRANSFORMS ###########################
########################################################################

transform moneybounce:

    parallel:

        alpha 0.0
        linear 0.1 alpha 1.0
        pause 1.8
        easeout 2.0 alpha 0.0
    parallel:

        xpos 910 ypos 80
        easein 1 ypos 65
        pause 1.8
        easeout 1 ypos 80

transform statementbounce:

    parallel:

        alpha 0.0
        linear 0.1 alpha 1.0
        pause 1.8
        easeout 2 alpha 0.0

    parallel:

        xpos 910 ypos 110
        easein 1 ypos 95
        pause 1.8
        easeout 1 ypos 110

########################################################################
#####zich################ CUSTOM TRANSFORMS ###########################
########################################################################

transform speaking2:
    easein 0.3 zoom 1.01

transform stopspeaking2:
    easein 0.3 zoom 1.0

########################################################################
#####zich################ ACTUAL GAME SCRIPT ###########################
########################################################################

label start:

    # This is used to easily add a formatted '>' to the start of choices in menus.
    $ pick = "{color=#000000}>{/color}"

    $ quick_menu = True

    $ volume1 = True

    jump start2

label start2:

    # Stop main menu music, or any other music playing, and transition to volume select.
    stop music fadeout 1.5

    show image "gui/main_menu.png"

    window hide

    scene black with Dissolve(1.5)

    $ main_menu = True

    call screen vol_select()

    stop music fadeout 1.5

####################################################################################
###zich#################### BANA'S ROUTE TEST ######################################
####################################################################################

label tagora_route_test:

  $ renpy.block_rollback()

  $ main_menu = False

  $ bill = 0

  $ tdone = "\n\n*__________"

  show image "gui/game_menu.png"

  window hide

  scene black with Dissolve(1.5)

  ############################################################
  ###################### START ROUTE #########################

  op "What's been with everything lately?"

  op "Has there even been a lately?"

  op "You're not trying to be dramatic here, after a series of recent unsettling events making you painfully aware of it..."

  op "...you’re honestly beginning to doubt the linearity and stability of time, along with the validity of your whole existence up to this point."

  op "{size=24}What if this whole time you’ve just been stuck in a loop, reliving the same handful of days over and over again with no sign of progress past this miserable experience of reliving your successes and failures all at once?"

  op "{size=24}It’s like some kind of fucked up purgatory, where your agency over your free will was stripped from you just to make you dance like a puppet for hungry, ruthless Gods desperate for something they can’t have."

  op "{size=80}{=friend}FRIENDSHIP.{/=friend}{/size}"

  op "And for what? What did you do to deserve this?"

  op "..."

  op "Maybe you ARE being dramatic."

  op "Being dramatic sure does wipe you out."

  op "{size=26}Your unquenchable thirst for budding new meaningful connections between yourself with strangers has really dried out from all this existential peril - you're run into the ground."

  op "You are operating at zero friendmiles per hour, the gumption tank is completely empty."

  scene bg mc_hideout with dissolve

  $ quick_menu = True

  "As you continue to spiral into an endless thought hole of depression you feel your palmhusk buzz with the custom notification ding you set for each of your pals-"

  play music "music/tagora_cash.mp3" noloop

  "-it's the sound of a cash register, so immediately you know it's Tagora. You quickly unlock it to read his messages."

  $ renpy.pause(1)

  play sound "music/sfx-phonebeep.wav"

  $ renpy.pause(1.5)

  play music "music/tagora_mobile.mp3" loop

  t "Is everything alright?"

  t "You called me five times last night,"

  t "I tried listening to your messages but it was mostly static."

  t "And honking."

  "You’re going to hyperventilate. You don’t even remember calling Tagora and already that’s a disconcerting implication of how your day might go."

  menu:

    "What will you do?" # This text is optional, I added it in as it looked strange to have the previous text in there

    "[pick] Have an existential crisis":

        "You can feel the panic setting in already over this - was it really you that sent those texts, or was it another you?"

        "Are you the real you, or are you another version of you that’s just going to become a memory to you? How real are any of you?"

        "The room is spinning and you feel like you want to throw up, before that ridiculous cash ca-ching centers you in reality again."

        t "Do I have to come get you?"

        t "Are you okay?"

        menu:

          "[pick] Respond":

            "You decide to respond, Tagora is what you as a human would consider to be your best friend."

    "[pick] Respond":

        "You decide to respond, Tagora is what you as a human would consider to be your best friend."

  "He’s slow to admit it himself, but the social constructs on Alternia are different than Earth and you’re suspicious about whether or not the concept of platonic friendship is the same here as it is back home."

  "Regardless, you think he’d agree!"

  "You mention in a series of texts back to him that you were at a concert last night and must have butt dialed him."

  t "On a touch screen?"

  "Listen, we all make lie-adjacent mistakes."

  t "Right."

  t "Well, I have a proposition for you, regardless."

  t "Why don’t you come over in the hour?"

  t "We can talk about it at my hive."

  t "See you."

  $ renpy.pause(0.5)

  stop music fadeout 0.3

  $ renpy.pause(0.5)

  play sound "music/sfx-phonebeep.wav"

  "You see Tagora pretty often as it is so you agree and gather yourself together."

  "Maybe you just need a day where you aren’t walking a fine, indistinguishable line between making the right choices on a new face and tearing the fabric of reality into shreds."

  "You need a day where you aren’t being prompted to smell clown stank."

  $ renpy.pause(1)

  show bg outglut with CropMove(2.0, "wipeleft")

  show bg tagora_ext with CropMove(2.0, "wipeleft")

  "It doesn’t take long to get to Tagora’s hive, you knock on his door and can hear scritching and skittering coming from the other side before Tagora opens the door."

  play music "music/tagora_theme.mp3" loop

  show robegor neutral at default with moveinbottom

  show screen billcount

  tspk "Wow, you look like shit. [tdone]" (amt = -50, stmt = "Swear Jar")

  "The slung insult at the expense of his own expenses slides off of you and leaves you completely unphased, it's just really nice to see a friend you already have an established rapport with."

  "Besides he’s absolutely right, you DO look like shit."

  "But uh, oh, is this like. A bad time?"

  t "Why would it be a bad time, this is when I told you to come over. [tdone]"

  "You've just never seen this casual look before, is all."

  t "That {b}is{/b} the point. [tdone]"

  show bg tagora_int with CropMove(1.2, "wipeleft")

  "He invites you in, attempting to put space between you when you pass under his nostrils."

  show robegor disgust at twitch

  tspk "You {i}smell{/i} like shit. [tdone]" (amt = -50, stmt = "Swear Jar 2, Electric Boogaloo")

  "{size=19}Yeah, you say, briefly explaining again about the concert while making an executive decision NOT to mention the parts where you pissed/shit yourself in front of an extremely sexy clown, and were so tired after the whole ordeal you just decided to say fuck it to your dignity and slept in your filth.{size=16}"

  "Some things are best left unsaid, as was once spoken by the great social climbers looking to keep their fragile constructed identities intact."

  "Tagora would be proud if this entire situation didn’t involve him."

  "You had a long night, that’s all there is to say on the matter."

  show robegor disgust at shudder

  t "I can’t believe you went to one of those awful things. You must not have known the typical protocol, I probably can’t blame you for being ignorant."

  "We all make poor judgment calls when we’re at our lowest."

  show robegor neutral

  t "It’s a good thing I asked you over, then. [tdone]"

  "You start to follow Tagora through to the main room and ask why DID he invite you over?"

  t "A self-care date."

  t "It doesn’t take a genius to notice you’ve been stressed lately, going to a jerkoff clown event makes it more obvious you’re in need of some downtime."

  "Sounds expensive."

  show robegor smug at twitch

  t "Please. I’m doing you a favor, free of charge."

  hide screen billcount

  t "That’s what friends are for. [tdone]"

  "Wow, that’s… really nice of him, and sort of unexpected. You’re starting to question how you feel about spontaneity lately."

  show bg tagora_bath with CropMove(1.2, "wipedown")

  "He leads you both into his bathroom where it looks like a bath was already drawn, it’s fizzing over and multicolored like the bath bombs you’ve seen Influencer douchebags take pictures of, trying to flex their faux luxe lifestyles."

  "The water looks thick from how opaque it is."

  "Is that for you? Like, are you going to get in that while Tagora’s in here, too?"

  "That’s cool if he’s curious or something. You’re kind of shy, but you’ve embarrassed yourself in worse ways, especially in the last 24 hours."

  "Really, at this point, you’re surprised you’ve managed to somehow hold onto even an inch of modesty."

  "Tagora gives you an indifferent look and shrugs."

  show robegor shrug at bounce

  t "You have nothing I’m interested in, don’t make this weird. [tdone]"

  "Fair enough."

  "You at the very least tug the shower curtain forward to TRY and cover yourself as you start to undress."

  show robegor think

  "Tagora goes over to his shelf of endless beauty supplies, occupied by scrutinizing over the options until you’re submerged and obscured by the technicolor bubbles."

  "He fills an arm full of tiny bottles and packets, turning back to you with them and setting them down carefully on the ground by you both."

  "He takes a seat on the ledge of what you’ve assumed is a smaller tub attached to the bigger one, but really you have no fucking idea."

  "This is nice."

  show robegor think at bounce

  t "So."

  t "Lowest? [tdone]"

  "It takes you a second to realize what he’s asking - he’s busy sorting through the bottles he’s picked out, giving you a pause to think."

  menu:

    "[pick] No you have to look cool in front of this joker.":

      "You laugh lightly and try to pass it off with a very noncommittal ‘Yeah.’ Hoping maybe you can encourage the conversation away from a potential mental breakdown."

      "Tagora stops fussing over the bottles and instead gives you a dull look that immediately conveys that he doesn’t appreciate your dodging of his question, repeating it back to you in a no-bullshit way."

      t "Yeah."

      t "So tell me about it. [tdone]"

      "Yeah, admittedly shit’s been rough."

      menu:

        "[pick] Have that existential crisis now, since you so selfishly put it off before.":

            "..."

    "[pick] Have that existential crisis now, since you so selfishly put it off before.":

        "Yeah, admittedly shit’s been rough."

  "{size=20}There’s the obvious fact you don’t even belong on this planet at all, and then the presumptuous effort of making friends with most every inhabitant you’ve encountered, taking it upon yourself to try and fit into a narrative you don’t belong in, it’s arduous to put it lightly."

  "You thought making friends here would fill you with purpose, make you feel special and like you would be bringing something meaningful from your species to theirs."

  "Maybe."

  "Maybe that’s what you thought you were doing at first, but who’s to say for sure your thoughts are YOUR thoughts? Lately you doubt you have free will at all."

  "Instead it feels like you’re just prolonging something dreadful."

  "Honestly you're having a hard time really putting into exact words the feelings your having, here."

  "A couple of times you let out an irritated sigh followed by awkward pauses as you try to catch your wording up to your thoughts before Tagora finally waves a hand at you."

  show robegor smug at nod

  t "It was a mistake to ask; nevermind. [tdone]"

  show robegor neutral

  t "You're frustrating yourself trying to explain this to me. It defeats the purpose of trying to relax if you keep tensing yourself up."

  t "I’d like to avoid that. [tdone]"

  "You guess that makes sense. A morose laugh huffs out of you, muttering; for a second there you thought you said the wrong thing. You still kind of expect the world to start crashing down around you any second now, though."

  t "Nothing {i}bad{/i} is going to happen to you here. [tdone]"

  show robegor think

  "Tagora sits looking at you as his hands fidget with a small black pot, screwing and unscrewing the lid. You can notice from his expression he’s carefully considering the risk of damaging his social facade over what he’s planning to say."

  t "But, when expectations get to be too much, I can understand how you can start to feel that way."

  t "It’s easy to convince yourself your entire world and existence hinges on making ‘right answers’"

  show robegor shrug at twitch

  t "“I can’t make the bold claim to know what you’re going through, specifically. I’m not, nor have I been, in your exact situation."

  show robegor think

  t "Though I’ve probably experienced something of an equivalent nature to being alien in a scenario. [tdone]"

  "God you wish this were a situation where you weren’t being literal, that this was all the result of a prolonged anxiety attack, then maybe Tagora’s heartfelt efforts to reassure you wouldn’t be wasted on someone so resigned."

  "Though, you do allow yourself to settle into that possible reality for the sake of the moment."

  t "Hmm."

  "He looks like he’s trying to decide between two different bottles of indiscernible product, you’re not sure what they’re for but you could offer to be a tie breaker for whatever internal argument he’s having."

  menu:

    "[pick] The small black pot?":

        "The small black pot? Wait, no, you meant the one with the fancy label! Why’d you say that? You bite the inside of your lip and look like you’re thinking too hard as the weight of incorrect choices makes your head start to spin again."

    "[pick]  The tube with the really intricate label?":

        "The small black pot? Wait, no, you meant the one with the fancy label! Why’d you say that? You bite the inside of your lip and look like you’re thinking too hard as the weight of incorrect choices makes your head start to spin again."

  "So much for being relaxed."

  "It must be apparent on your face because Tagora gives you a raised eyebrow, a look of concern for your mental well being."

  "You guess he’s never actually seen you this unsure before, you think. Again, he cuts your stammering off and opens the small pot, dipping his fingers into the thick, light pink contents inside."

  show robegor shrug at bounce

  t "Unless you’re allergic to red prickle leaf extract I really don’t need your input. [tdone]"

  show robegor think

  "You clamp your mouth shut as Tagora sets to smearing the floral smelling paste on your face. It stings for a moment from how cold it is but warms up to your skin quickly, filling you with a soothing sensation of relief."

  "Tagora crosses his legs and starts spreading a lotion from a completely different bottle on himself now that you’re well taken care of and in fucking cloud town."

  "{size=20}You feel safe from anything in this tranquil setting Tagora took time to carve out for the both of you. You shut your eyes and sigh as you sink deeper into the water, just enough for it to come to your chin and for bubbles to pop around your ears."

  "You haven’t had a chance to feel so free of responsibility in a while. He’s really good at this."

  show robegor shrug at twitch

  t "I know how to take care of myself. [tdone]"

  "You probably would too if you had access to a bathroom, or any kind of supplies, but you are kind of just visiting Alternia so there’s no real sense in you getting too settled in here."

  "{size=20}Something about that thought really stings, probably because you hadn’t entertained the naivety of it - part of you from the beginning {i}had{/i} thought this was going to be a permanent adventure, that you would be going through this friendship cycle forever and you guess just… live here?"

  "What were you expecting?"

  "This place fucking sucks."

  "What happens at the end?"

  "How do you go home?"

  "..."

  "You don’t have the answer to that."

  show robegor sexy

  t "That’s why I offered this in the first place."

  "Oh shit you weren’t listening—"

  show robegor think

  t "I have no idea what you’re calling your hive right now, and I doubt I would like it if I did, but I can’t imagine it’s comfortable whatsoever, considering you’re not from here."

  t "Having nowhere to really {i}go{/i} to escape how you’re feeling is probably rough. [tdone]"

  show robegor sexy

  t "So I thought"

  t "I would try"

  t "replicating that for you. [tdone]"

  "Oh. Damn."

  "Pretty bold of him to make the assumption he could make his company feel any more at home to you than anyone else. It gets a gentle laugh out of him, and you smile a little."

  t "Maybe."

  t "But it seems like it’s working out well. [tdone]"

  "Enough that you might even cry."

  show robegor disgust at shudder

  t "Please, don’t."

  t "That would be really awkward for both of us. [tdone]"

  hide robegor disgust with dissolve

  $ quick_menu = False

  $ renpy.pause(0.8)

  play music "music/victory_jingle.mp3" noloop

  scene ending with Dissolve(1.0)

  $ renpy.pause(1.5)

  scene black with Dissolve(1.5)

  return

return
