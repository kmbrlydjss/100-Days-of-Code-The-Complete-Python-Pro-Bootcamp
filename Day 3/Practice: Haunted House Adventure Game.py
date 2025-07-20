print(''' 
      !__!          O   _    __         /LL\         __    _    O
   /\__('')__/\     /L\  \'._(oo)  _    /LLLL\    _  (OO)_.'/   /L\
  / _        _ \   /LLL\  `.   (_.'/   /LLLLLL\   \'._)   .'   /LLL\
  \/ \/\  /\/ \/  /LLLLL_.' _.'-..'     |.--.|     '..-'._ `'._LLLLL\
        mm         |.-.'__.'____________||__||____________'. __'.-.|
     \_  '\/` \_   ||_||\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\||_||
,__/  /`  ,\_ /'  [_____]\_\_\/\_\_\_\_\_\/\_\_\_\_\_\/\_\_\_\[_____]
   \\/---./  \\   /LLLLL\\_\_//\\\_\_\_\_//\\\_\_\_\_//\\_\_\_/LLLLL\
  .'\\, // '. \\ /LLLLLLL\==//__\\======//oo\\======//__\\===/LLLLLLL\
 /   \\//    \ \/LLLLLLLLL\__|__|________|__|________|__|__ /LLLLLLLLL\
:     \#\   _ :[___________]_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_[___________]
'   _//\ (_// '\|    _   |_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|   _    |
 \  \ ( \ \/ / )|  .'|'.[__].=============================.[__].'|'.  |
  '. \ \) ).' / |  |-OO| || |          _________          | || |-+-|  |
    `-\/#(`  / /|  |_|_| || |    _    [_________]    _    | || |_|_|  |
     __\ ,\ / / |        || |  .'_'.   |__    _|   .'_'.  | ||        |
    (OO.-----.% |    _   || |  | | |_  (oo)_.'/|   | | |  | ||   _    |
     %%|R.I.P|%%|  .'|'. || |  |-+-|\'._)   .' |   |-+-|  | || .'|'.  |
    %%%|_____|%%|  |-+-| || |  |_|_| '..-'._ `'._  |_|_|  | || |OO-|  |
~^"^~[_________]|  |_|_| || | [_____]  |    '.__.'[_____] | || |_|_|  |
    ''"^"^"~~^"`|        || |          |       |          | ||        |
                | /\     || lc_________|_______|__________| ||        | _
                |_) )_   ||/                               \||      _ | ))
  .-~^"^-__    .' """ '._||_________________________________||______)\.'""'.
              / /\   /\ \__]XXXXXXXXXX[_________]XXXXXXXXXX[__]~"^.'""'.__.'
             |    /_\    |~"^~"^~"^~[_____________]~^"~_________  '.__.'~^"^
             |  _______  |                            /Keep Out/   -"~"-
              \ \W W W/ /                  _-        /________/
               '.\M M/.'               __--             / /
              '~"^"~"^~'.                              / /
   _-"^~"^"-                    __--              _-^~"^"~^-_      
      ''')

print("Welcome to the Haunted House Adventure!")
gate = input('You stand at the gate of a creepy haunted house. Do you "Enter" or "Run" ').lower()

# stand at the gate
if gate == "enter":
    inside = input('You step inside and hear a noise upstairs. Do you go "Upstairs" or check the "Basement"? ').lower()

    # inside and hear a noise upstairs 

    if inside == "upstairs":
        door = input('You find a locked door with two buttons: "Red" and "Green". Which one do you press? ').lower()

        # locked door   
        if door == "green":
            print("The door opens to a secret room filled with treasure. You win!")
   
        else:
            print("A trapdoor opens beneath you and you fall into a pit. Game over!")

    else:
        flashlight = input('You find a flashlight and a mysterious box. Do you "Open" the box or "Leave" it alone. ').lower()

        # flashlight and mysterious box
        if flashlight == "open":
            print("The box contains a friendly ghost who thanks you for freeing it. You win!")
        else:
            print("You quietly leave the box alone and head back upstairs. Suddenly, the house begins to shake! You rush out just in time. You escaped safely!")

else:
    print("You run away safely, but miss out on the adventure. Game over.")
