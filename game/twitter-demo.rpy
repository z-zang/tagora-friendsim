####################################################################################
######################## TEMPORARY TEASER FOR TWITTER ##############################
########################### label twitter_teaser ###################################
####################################################################################

label twitter_teaser:

    op "Well, isn't this exciting."

    op "I've bet you've never seen this text in a friendsim before."

    op "Perhaps you're wondering which Friendsim volume this will be."

    op "After all, you are always thirsty for..."

    op "{size=80}{=friend}FRIENDSHIP.{/=friend}{/size}"

    op "Hang on a moment... who's this?"

    scene bg tagora_int with dissolve

    $ quick_menu = True

    play music "music/tagora_theme.mp3" loop

    show robegor neutral with moveinbottom

    $ bill = 0

    $ tdone = "\n\n*__________"

    show screen billcount

    tspk "..."

    show robegor disgust

    show robegor disgust at shake

    tspk "Why am I in another friendsim." (amt = 5000, stmt="Unsolicited visitation")

    show robegor disgust at bounce

    tspk "This wasn't in my contract. [tdone]" (amt = 20)

    tspk "They better be paying me for this." (amt = 20)

    show robegor disgust twitch

    tspk "..." (amt = 20)

    show robegor shrug at shudder

    tspk "Well, I guess if I'm here, I might as well make the most of it." (amt = 20)

    tspk "It would be uncharacteristic of me to pass up the opportunity to profit after all. [tdone]" (amt = 200, stmt="Canon characterisation")

    show robegor neutral

    tspk "..." (amt = 20)

    show robegor neutral at nod

    tspk "As you may have gathered, this is an excerpt of a fan friendsim." (amt = 20)

    tspk "One that Banavalope (@banavalope) is writing and drawing for, whilst Zich (@sburbd) is programming." (amt = 150, stmt="Namedrop fees")

    show robegor neutral at twitch

    tspk "I can't give you any more details for now, but you should keep your eyes peeled for the release." (amt = 20)

    tspk "Whilst I know very little about their respective skills, the friendsim looks promising." (amt = 20)

    tspk "Mainly because I will be appearing in it." (amt = 500, stmt="Lawerly ego stroking")

    show robegor shrug at twitch

    tspk "That is, if they manage to get it done sometime soon. [tdone]" (amt = 20)

    hide robegor shrug with dissolve

    $ quick_menu = False

    $ renpy.pause()

    play music "music/victory_jingle.mp3" fadeout 1.0 noloop

    scene black with Dissolve(1.5)

    return

return
