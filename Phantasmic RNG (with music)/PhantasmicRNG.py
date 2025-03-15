'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Type of work: School project 
Game Creation: 31/10/24
Game Completion: 05/03/25 (non-music version) 15/03/25 (music version)
Developer Name: Huby
Name of game: PhantasmicRNG
Objective: traverse through the cruel world finding the cure of the permenant curse of luck
Game Type: interactive text-based, turn-based combat, adventure game 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Personal Notes: This project may be the biggest one I have made so far and will prove to be a big learning experience. As of writing this I predict
my project will go beyond 700 lines of code and can only hope for the best when making it. Also this program will be run on the fullscreen terminal 
this will hide the games code enchancing the experience and not expecting what will come next in each encounter. 
Another note id like to add all the assests such as sound music or any sort of media that I took will be given credit below. Anyways God speed and hope future me will revisit it.

INSTRUCTIONS: in order to play the game correctly with no errors you need to install 2 python modules this includes installing pygame and colorama 
pygame is used to play the audio required by the game and colorama is a module used to display colour to text and ascii art. 

NOTICE: when playing the game on a undesired screen size or not full-screening the terminal the ascii art being displayed could be messy and scrambled its also recommended to run this game under
Visual Studio Code however, feel free to use a text editor that best suits you and that supports the ascii art correctly. 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

CREDITS: 
https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20 [Website used to generate ASCII art for game title below]

https://kirilllive.github.io/ASCII_Art_Paint/ascii_paint.html [Website used to make ASCII art for icons, enemies etc]

https://emojicombos.com/south-park [Website used for grabbing Erik Cartman ascii art and Jesus from family guy ascii art]

https://www.youtube.com/watch?v=boIZ91wPWzM&list=PLA10BBDE6A30B2674 Touhou 7 - Mystic Dream ~ Snow or Cherry Petal (Menu) [Zun's menu music for Touhou 7 Perfect Cherry Blossom used as introduction music for my game]

https://www.youtube.com/watch?v=5g3Os5T7q8g Postal 1 (1997) Soundtrack - The Ghetto [Christian Salyer's soundtrack for level 12 in Postal 1 used as bad ending music when the player completes journey 2 for my game]

https://www.youtube.com/watch?v=bIDu9Cixtqs Postal 2 OST - Title Screen [Christian Salyer's soundtrack for Postal 2's title screen used as background music when the player completes journey 1 for my game]


----------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                 _____  _                 _                      _        _____  _   _  _____ 
                                                |  __ \| |               | |                    (_)      |  __ \| \ | |/ ____|
                                                | |__) | |__   __ _ _ __ | |_ __ _ ___ _ __ ___  _  ___  | |__) |  \| | |  __ 
                                                |  ___/| '_ \ / _` | '_ \| __/ _` / __| '_ ` _ \| |/ __| |  _  /| . ` | | |_ |
                                                | |    | | | | (_| | | | | || (_| \__ \ | | | | | | (__  | | \ \| |\  | |__| |
                                                |_|    |_| |_|\__,_|_| |_|\__\__,_|___/_| |_| |_|_|\___| |_|  \_\_| \_|\_____|

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''

# as the name implies this module helps make randomly generated numbered mechanics exist 
import random
# pygame in this use case is used for inserting music into this game  
import pygame
from pygame import mixer
pygame.mixer.init()
# the module time helps add cooldown to each procedure which is useful for giving the user time to read the current information before upcoming deletion 
import time 
# the module colorma is used to add colour to text in the terminal giving the game a more "lively" look to it 
# to find its usage of the coloured text simply look for the following: "Fore.CYAN" or "print(Style.RESET_ALL)" to clear the coloured text for the next procedures unless told otherwise
from colorama import Fore, Back, Style

# Declared & initialized global variables
# normal hp: 185 to 275 Debug hp: 999 999
HP_player = random.randint(185, 275)
# heals player when they defeat an enemy 
Heal_player = random.randint(75, 125)

Player_Name = ""
Path_chosen = ""

# player or enemy if their health value reaches this value or below is dead (thanks captain obvious!)
Death = 0
Emergancy_Heal = 0

End_Combat = False
Input_Validation = False
Potion_Display = False

# journey 1 Enemies HP
Postal_dude_HP = 115
Sakuya_HP = 165
Zenith_HP = 200
Eric_HP = 245
RNGesus_HP = 300

# journey 2 Enemies HP 

Rasputin_HP = 100
Iku_Blackrock_HP = 150
Slave_Knight_HP = 225
BloodDrinker_Rei_HP = 260
Huby_Developer_HP = 1000000

#   <><><><><><><><><><><><><><><><><><><><><><><><><><>
#                   DECLARED FUNCTIONS  
#   <><><><><><><><><><><><><><><><><><><><><><><><><><>

def clear_terminal():
  print("\033[2J")

def clear_colour():
  print(Style.RESET_ALL)

#   <><><><><><><><><><><><><><><><><><><><><><><><><><>
#            Music for both journey 1 and journey 2
#   <><><><><><><><><><><><><><><><><><><><><><><><><><>

def Introduction_Music(): 
  mixer.music.load("Touhou Intro Music.mp3")
  mixer.music.play(-1)

def Background_Music(): 
  mixer.music.load("Background Music.wav")
  mixer.music.play(-1)

def Enemy_Journey_1_Music(): 
  mixer.music.load("Enemy_Journey_1_Music.wav")
  mixer.music.play(-1)

def Enemy_Journey_2_Music(): 
  # this music has church bells sounds to indicate imanent death awaiting  
  mixer.music.load("Enemy_Journey_2_Music.wav")
  mixer.music.play(-1)

def Outro_Music(): 
  mixer.music.load("Outro Ending (Postal 2 title screen).wav")
  mixer.music.play(-1)

def Bad_Ending_Outro_Music(): 
  mixer.music.load("Bad ending (The Ghetto Postal 1).mp3")
  mixer.music.play(-1)

#-----------------------------------------------------------------------------------------------------
# Ascii Art Icon Drawings 
#-----------------------------------------------------------------------------------------------------

def Melee_Attack_Icon():
  print("""
        
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                
                                                                                                           ¢¢¢¢¢                            
                                                                                                          ¢ §§§ ¢                           
                                                                                                            §§§                             
                                                                                                            §§§                             
                                                                                                            §§§                             
                                                                                                            §§§                             
                                                                                                            §§§                             
                                                                                                            §§§                             
                                                                                                      ≡     §§§      ≡                      
                                                                                                    ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡                     
                                                                                                      ≡     §▒§      ≡                      
                                                                                                            §▒§                             
                                                                                                            §▒§                             
                                                                                                            §▒§                             
                                                                                                            §▒§                             
                                                                                                            §▒§                             
                                                                                                            §▒§                             
                                                                                                            §▒§                             
                                                                                                            §▒§                             
                                                                                                            §▒§                             
                                                                                                            §▒§                             
                                                                                                             ▼       

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                       

        """)

def Shield_Icon_Art():
  print("""
        
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                   ────────────────────────────────────────────────────────                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜═════════════════════┃═════════┃══════════════════════⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜═════════════════════┃═════════┃══════════════════════⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   ⎜                     ┃         ┃                      ⎜                                                     
                                                   \                     ┃         ┃                     /                                                      
                                                    \                    ┃         ┃                    /                                                       
                                                     \                   ┃         ┃                   /                                                        
                                                      \                  ┃         ┃                  /                                                         
                                                       \                 ┃         ┃                 /                                                          
                                                        \                ┃         ┃                /                                                           
                                                         \               ┃         ┃               /                                                            
                                                          \              ┃         ┃              /                                                             
                                                           \             ┃         ┃             /                                                              
                                                            \            ┃         ┃            /                                                               
                                                             \           ┃         ┃           /                                                                
                                                              \          ┃         ┃          /                                                                 
                                                               \         ┃         ┃         /                                                                  
                                                                \        ┃         ┃        /                                                                   
                                                                 \       ┃         ┃       /                                                                    
                                                                  \      ┃         ┃      /                                                                     
                                                                   \     ┃         ┃     /                                                                      
                                                                    \    ┃         ┃    /                                                                       
                                                                     \   ┃         ┃   /                                                                        
                                                                      \  ┃         ┃  /                                                                         
                                                                       \ ┃         ┃ /                                                                          
                                                                        \┃         ┃/                                                                           
                                                                         \         /                                                                            
                                                                          \       /                                                                             
                                                                           \     /                                                                              
                                                                            \   /                                                                               
                                                                             \─/                                                                        
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                         
""")

def Potion_Health_Art():
  print("""
                                                                                                                                                                                                                                                                                                                   
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                                                                                                                                                                                  
                                                                                                             ßßßßß                                                                                           
                                                                                                            ß■■■■■ß                                                                                          
                                                                                                            ß■■■■■ß                                                                                          
                                                                                                            ß■■■■■ß                                                                                          
                                                                                                           ─ΘΘΘΘΘΘΘ─                                                                                         
                                                                                                            ß     ß                                                                                          
                                                                                                            ß     ß                                                                                          
                                                                                                            ß     ß                                                                                          
                                                                                                            ß     ß                                                                                          
                                                                                                            ß     ß                                                                                          
                                                                                                            ß     ßßßßß                                                                                      
                                                                                                        ßßß          ßßßß                                                                                   
                                                                                                      ßßß               ß                                                                                   
                                                                                                    ßß──────────────────ß                                                                                   
                                                                                                    ßß■■■■■■■■■■■■■■■■■■ß                                                                                   
                                                                                                      ß■■■■■■■■■■■■■■■■■■ß                                                                                   
                                                                                                      ß■■■■■■■■■■■■■■■■ßß                                                                                   
                                                                                                      ßß■■■■■■■■■■■■■ßßß                                                                                    
                                                                                                        ßßß■■■■■■■ßßßßß                                                                                      
                                                                                                          ßßßßßßßßß                                                                                          
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                         
                                                                                                                                         
        """)

def Incantation_Icon_Art():
  print("""        
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                                    
                                                                                                        ΩΩΩΩΩΩΩΩΩΩΩΩΩΩ                                                                          
                                                                                                      ΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩ                                                                          
                                                                                                      ΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩ                                                                           
                                                                                                    ΩΩΩΩΩ ΩΩ      ΩΩΩ                                                                           
                                                                                                    ΩΩΩ                                                                                         
                                                                                                    ΩΩΩ      ■■■                                                                                
                                                                                                    ΩΩΩ     ■■■■■                                                                               
                                                                                                    ΩΩΩ     ■■■■■                                                                               
                                                                                                    ΩΩΩΩ     ■■■                                                                                
                                                                                                      ΩΩΩΩ                                                                                       
                                                                                                      ΩΩΩΩ                                                                                      
                                                                                                        ΩΩΩΩΩ  Ω                                                                                 
                                                                                                        ΩΩΩΩΩΩΩΩΩΩΩ                                                                               
                                                                                                            ΩΩΩΩΩΩΩΩ
                                                                                                              ΦΦΦΦ
                                                                                                              ΦΦΦΦ
                                                                                                              ΦΦΦΦ
                                                                                                              ΦΦΦΦ
                                                                                                             ┃ΦΦΦΦ┃
                                                                                                             ┃ΦΦΦΦ┃
                                                                                                             ┃ΦΦΦΦ┃
                                                                                                             ┃ΦΦΦΦ┃
                                                                                                              ΦΦΦΦ
                                                                                                              ΦΦΦΦ
                                                                                                              ΦΦΦΦ
                                                                                                              ΦΦΦΦ
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        """)

#-----------------------------------------------------------------------------------------------------
# Ascii Art Background Drawings (Journey 1)
#-----------------------------------------------------------------------------------------------------

def intro_background_Art():
  print(Fore.CYAN + """
                                                       
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                     
                                                                                                                                                       
                                  ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                  │                                                                                                                              │
                                  │                                                                                                                              │
                                  │                                                                  °°°°°°°°                                  °°°               │
                                  │                                     °°°°°°°°                  °°°       °°°                            °°°°   °              │
                                  │           °°°°°                   °°°     °°                 °°            °                         °°        °             │
                                  │         °°°   °                  °°      °°°°°°°°°         °°°            °°                        °         °              │
                                  │     °° °°     °°°°°°°°       °° °                °     °°° °            °°° °°°°°°°               °          °°° °°   °°°    │
                                  │    °°  °     °°      °°    °° °°°                °    °° °°                       °°          °°°                        °°  │
                                  │    °                 °°    °                     °    °°                           °°         °°                           ° │
                                  │    °°              °°°     °                     °     °                           °°         °                            ° │
                                  │     °°            °°°°     °°                   °°      °                         °°          °                   °°°° °°°°° │
                                  │     °                °     °                °°°°°       °°                       °°           °°     °              °°       │
                                  │     °                °     °                 °°        °°                    °°°°              °°°°°°°    °°°°      °°       │
                                  │     °°°°°     °°°°°°°      °°°°°°°    °°     °°        °                 °°°°                        °°°° °   °°°°°°         │
                                  │         °   °°°                  °   °°°°   °°         °°°°°°°°°°         °                                                  │
                                  │         °°°°°                    °°°°°   °°°°                   °°     °°°                                                   │
                                  │                                                                  °°°°°°                                                      │
                                  │                                                                                                                              │
                                  │                                                                                                                              │
                                  │                                                                                                                              │
                                  │                                                                                                                              │
                                  │                                      ■■■■■■                       ■■■■■■■■                                                   │
                                  │      ■■■■■■■■■■■■■■■              ■■■■    ■■■■■■               ■■■        ■■■          ■■■■■■         ■■■■■■■      ■■■■■■■■  │
                                  │   ■■■■              ■■         ■■■■             ■■■■         ■■■            ■■      ■■■■    ■■■     ■■      ■■   ■■■      ■■ │
                                  │■■■■                  ■■■     ■■■                   ■■■     ■■■               ■■■ ■■■■         ■■■ ■■         ■■■■■         ■■│
                                  │■                       ■■■■■■■                        ■■■■■■                   ■■■              ■■            ■■            ■│
                                  ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────                                                                                                                                                                                                                         

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                 
        """)
  return

def Trees_Path_Art():

  print(Fore.GREEN + """ 
                                                                                                                                                                
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                                               
                                                                                                                                                                                                                                                                                                                      
                                  ────────────•──────────────────────────────────────────────────────────────────────────────────────────────────•────────────────────────────────────────────────
                                            ••                                              •                                        •          ••                                         •     
                                            ••                                               •                                        •••         ••                                        •     
                                          •••                                             •••                 ••••••••                  ••         ••                                       ••    
                                        •••                                             •••                 •••      •                   ••         •              •••••                     ••   
                                      ••                   •••••••                    ••                  ••        • ••••••••           •         •           ••••   ••                     ••  
                                      ••                  •••     • •••••••          ••              •••••••         •••      •           •        ••         •••       ••••••••••             •• 
                                      •             ••••••••      ••      ••         •              ••     •                  •           •       ••      •••••         •        •              • 
                                      •            ••     ••      •        •         •             ••                    ••••••           •      ••     ••    ••              •••••             • 
                                      •           •       ••               •         •            ••                     •••             ••     ••     ••                          •           •• 
                                      ••          •                    ••••          •            ••••                      •           ••     ••      •                           •           •  
                                      ••         •                    ••••           •               ••••••                •           •      •       ••                     ••••••          •   
                                        •         •••                     ••          ••                   •         ••••••••          •       •        ••                    ••             ••   
                                        •            ••                   ••           ••                  •         •                ••       ••        ••••••••              •             •    
                                        •              •             •••••              •                 ••       •••                •         ••              •••            •             •    
                                        •              •               ••               •                 •        •                  •          •                •           ••             •    
                                      ••             ••               ••              ••                ••       ••                  •          •               ••           •              •    
                                      ••             ••             ••••               •                 •        •                    •         •              ••            •              •    
                                    ••             ••              •                  •               ••         •                    ••       ••             ••             •              •    
                                    ••             ••              ••                 ••             •••          •                     ••      •            •••              •              ••   
                                    •            •••               •                •••            •••            •                      ••    ••       •••••                  •••••          ••  
                                    •      •••••••                  •••••••••••              ••••••               •••                     ••   •  •••••••                          ••••••••    •• 
   
                                  ──────────────────────────────────────────────────────────────────────────────────•••••••••─────────────────────────────────────────────────────────────────────

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
""")

def Mansion_Art():

  print(Fore.RED + """
        
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
                                                                                                                                                                                                  
                                                                                                                              ß                                                                      
                                                                                     ΘΘ                                      ßßß                                                                     
                                                                                   ΘΘΘ ΘΘ                                   ß■■ßß
                                                                                 ΘΘΘ    Θ                                  ßß■■■ßß                                                                     
                                                 ß                             ΘΘΘ  ΘΘΘ  ΘΘ                               ßß■■■■■ßß                                                                    
                                                ßßßß                          ΘΘ   Θ │ Θ   ΘΘ                            ßßßß■■■■■ßß                                                                   
                                              ßßß  ßß                        ΘΘ    Θ └─Θ    Θ                          ßßß  ßß■■■■■ßß                                                                  
                                            ßß  ΘΘ ßß                       Θ       ΘΘΘ      ΘΘ                       ßß ΘΘ ßß■■■■■ßß                                                                 
                                            ß  Θ  Θ  ß                     ΘΘΘ────────────────ΘΘ                      ß Θ  Θ  ß■■■■■ßß                                                                
                                          ßß    ΘΘ    ßß                   ΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘ                     ßß  ΘΘ   ßß■■■ß■                                                                 
                                        ßßßß          ßß                   Θ                   Θ                  ßßßß          ßß■ß■■Θ                                                                
                                        ßß──────────────ßß                 Θ         φ         Θ                 ßß──────────────ßß■■ΘΘ                                                                
                                        αααααααααααααααααα                 Θ        φ φ        Θ                 αααααααααααααααααα■Θ■Θ                                                                
                                        Φ                Φ                 Θ        φ φ        Θ                 Φ                ΦΘ■■Θ                                                                
                                        Φ                ΦΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘ        φ φ        ΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΦ                Φ■■■Θ                                                                
                                        Φ  φ    φ    φ   Φ                 Θ         φ         Θ                 Φ   φ    φ    φ  Φ■■■Θ                                                                
                                        Φ φ φ  φ φ  φ φ  Φ  ΘΘ   ΘΘ   ΘΘ   Θ───────────────────Θ  ΘΘ   ΘΘ   ΘΘ   Φ  φ φ  φ φ  φ φ Φ■■■Θ                                                                
                                        Φ φ φ  φ φ  φ φ  Φ Θ  Θ Θ  Θ Θ  Θ  Θ                   Θ Θ  Θ Θ  Θ Θ  Θ  Φ  φ φ  φ φ  φ φ Φ■■■Θ                                                                
                                        Φ φ φ  φ φ  φ φ  Φ Θ  Θ Θ  Θ Θ  Θ  Θ                   Θ Θ  Θ Θ  Θ Θ  Θ  Φ  φ φ  φ φ  φ φ Φ■■■Θ                                                                
                                        Φ  φ    φ    φ   Φ Θ  Θ Θ  Θ Θ  Θ  Θ        φφφ        Θ Θ  Θ Θ  Θ Θ  Θ  Φ   φ    φ    φ  Φ■■■Θ                                                                
                                        Φ════════════════Φ═════════════════Θ       φ   φ       Θ═════════════════Φ════════════════Φ■■■Θ                                                                
                                        Φ                Φ       ║║║       Θ       φ   φ       Θ       ║║║       Φ                Φ■■■Θ                                                                
                                        Φ  ΘΘΘΘΘΘΘΘΘΘΘΘ  Φ       ║║║       Θ       φ   φ       Θ       ║║║       Φ  ΘΘΘΘΘΘΘΘΘΘΘΘ  Φ■■■Θ                                                                
                                        Φ Θ            Θ Φ       ║║║       Θ       φδ  φ       Θ       ║║║       Φ Θ            Θ Φ■■■Θ                                                                
                                        Φ  ΘΘΘΘΘΘΘΘΘΘΘΘ  Φ       ║║║       Θ       φ   φ       Θ       ║║║       Φ  ΘΘΘΘΘΘΘΘΘΘΘΘ  Φ■■Θ                                                                 
                                        Φ                Φ       ║║║       Θ       φ   φ       Θ       ║║║       Φ                Φ■Θ                                                                  
                                        ΦΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΦΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΦΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΦΘ   
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

        """)

def Door_To_Cave_Art():

  print(Fore.BLUE + """
      
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                              ────────────────────────────                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                    ┌─────│                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │                          │                                                                       
                                                                              │──────────────────────────│        
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         
        """)

def Stairs_To_Throne_Art():


  print("""
        
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
                                                                                         ΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩ                                           
                                                                        ΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩ πππππππππππππππππππππππππππππππ    ΩΩΩΩ                                        
                                                                 ΩΩΩΩΩΩΩ     δ        δδ π                               π       ΩΩΩΩ                                    
                                                             ΩΩΩΩ            δ       δδ  π                               π          ΩΩ                                   
                                                         ΩΩΩΩ                δ           πππππππππππππππππππππππππππππππππ           ΩΩΩ                                 
                                                       ΩΩ                    δδ     δδ  π                                 π            ΩΩΩ                               
                                                      ΩΩ                      δ    δ    π                                 π             δδΩ                              
                                                    ΩΩΩ                       δ   δδ    πππππππππππππππππππππππππππππππππππ             δ Ω                              
                                                   ΩΩ                 δδ      δ  δ     π                                   π           δ   Ω                             
                                                 ΩΩ                  δδδ      δ δδ     π                                   π          δ    ΩΩ                            
                                                 Ω                 δδ δ       δδδ      πππππππππππππππππππππππππππππππππππππ          δ     Ω                            
                                                Ω                δδ  δ        δδ      π                                     π        δ       ΩΩ                          
                                                Ω               δ    δ                π                                     π       δδ       δδΩ                         
                                                ΩΩ            δδ     δ                πππππππππππππππππππππππππππππππππππππππ      δδ      δδ  ΩΩ                        
                                                 Ω           δδ     δ                π                                       π     δ   δδδδ     Ω                        
                                                 ΩΩΩ        δδ      δ                π                                       π     δδδ          Ω                        
                                                   ΩΩ      δδ      δδ                πππππππππππππππππππππππππππππππππππππππππ                  Ω                        
                                                    ΩΩ    δδ       δ                π                                         π                 Ω                        
                                                      ΩΩ δ        δδ                π                                         π                 Ω                        
                                                       ΩΩ        δδ                 πππππππππππππππππππππππππππππππππππππππππππ                 Ω                        
                                                        ΩΩ       δ                 π                                           π               ΩΩ                        
                                                         ΩΩ     δ                  π                                           π               Ω                         
                                                           ΩΩ  δδ                  πππππππππππππππππππππππππππππππππππππππππππππ δ             Ω                         
                                                            ΩΩΩΩ                                                                 δδ           ΩΩ                         
                                                               ΩΩΩ                                       ΦΦΦ                    δδ δ         Ω                           
                                                                 ΩΩΩ                                    Φ   Φ                   δ   δ        Ω                           
                                                                   ΩΩΩ                                  Φ   Φ                   δ    δ     ΩΩ                            
                                                                     ΩΩΩ          │ φ                    ΦΦΦ                    δ    δδ   ΩΩ                             
                                                                       ΩΩΩΩ     Φ───                      │                    δδ     δ  Ω                               
                                                                           ΩΩΩ    │ φ                   ──│──                  δ      δδΩΩ                               
                                                                              ΩΩΩΩΩ                       │                    δ      Ωδ                                 
                                                                                   ΩΩΩΩΩΩΩΩΩ             σ σ                  δ     ΩΩΩ                                  
                                                                                            ΩΩΩΩΩΩΩ                           δ   ΩΩ                                     
                                                                                                  ΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩ         ΩΩΩΩΩ                                       
                                                                                                                    ΩΩΩΩΩΩΩΩΩ        
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        """)

def Throne_Art():

  print("""
        
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
                                                                            ßßßßßßßßßßßßßßßßß                                                                      ßßßßßßßßßßßßßßßßß                                  
                                                                           ß                 ß                                                                    ß                 ß                                 
                                                                            ßßßßßßßßßßßßßßßßß                                                                      ßßßßßßßßßßßßßßßßß                                  
                                                                             ß  α  ααα  α  ß                                                                        ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                                                                        ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                                                                        ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                                                                        ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                                                                        ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                                                                        ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                                                                        ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                                                                        ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                                                                        ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                            ΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘ                             ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                           ΘΘ      ║      ΘΘ                            ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                          ΘΘ       ║       ΘΘ                           ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                          Θ════════║════════Θ                           ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                          Θ        ║        Θ                           ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                          Θ        ║        Θ                           ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                         ΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘ                          ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                        Θ          ║          Θ                         ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                        Θ          ║          Θ                         ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                        Θ          ║          Θ                         ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                        Θ          ║          Θ                         ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                        Θ══════════║══════════Θ                         ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                      ΘΘΘΘ         ║         ΘΘΘΘ                       ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                     Θ    Θ        ║        Θ    Θ                      ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                     Θ    Θ        ║        Θ    Θ                      ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                     Θ    ΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘ    Θ                      ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                     Θ────Θ        ║        Θ────Θ                      ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                     Θ    Θ        ║        Θ    Θ                      ß  α  ααα  α  ß                                   
                                                                             ß  α  ααα  α  ß                     Θ    Θ        ║        Θ    Θ                      ß  α  ααα  α  ß                                   
                                                                            ßßßßßßßßßßßßßßßßß                    Θ    Θ        ║        Θ    Θ                     ßßßßßßßßßßßßßßßßß                                  
                                                                           ß                 ß                   ΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘ                    ß                 ß                                 
                                                                            ßßßßßßßßßßßßßßßßß                                                                      ßßßßßßßßßßßßßßßßß
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                    
        

        """)

#-----------------------------------------------------------------------------------------------------
# Ascii Art Background Drawings (Journey 2)
#-----------------------------------------------------------------------------------------------------

def Neighbourhood_Path_Art():
  print(Fore.WHITE + """ 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                      
                                          /\                           /\                                                                         /\                        /\                         
                                         /  \                         /  \                                                                       /  \                      /  \                        
                                        /────\                       /────\                                                                     /────\                    /────\                       
                                       /      \                     /      \                                                                   /      \                  /      \                      
                                      /────────\                   /────────\                                                                 /────────\                /────────\                     
                                     /          \                 /          \                 ΘΘΘΘ                                          /          \              /          \                    
                                    /────────────\               /────────────\              ΘΘΘ◙◙ΘΘ                            ΘΘΘΘ        /────────────\            /────────────\                   
                                   /              \             /              \            Θ◙◙◙◙◙◙Θ                          ΘΘΘ◙◙ΘΘ      /              \          /              \                  
                                  /────────────────\           /────────────────\          ΘΘ◙◙◙◙◙◙Θ                         Θ◙◙◙◙◙◙Θ     /────────────────\        /────────────────\                 
                                  ──────────────────           ──────────────────           ΘΘ◙◙◙◙ΘΘ                        ΘΘ◙◙◙◙◙◙Θ     ──────────────────        ──────────────────                 
                                  │                │           │                │            ΘΘ◙◙ΘΘ                          ΘΘ◙◙◙◙ΘΘ     │                │        │                │                 
                                  │  ───      ───  │           │  ───      ───  │              │ΘΘ                            ΘΘ◙◙ΘΘ      │  ───      ───  │        │  ───      ───  │                 
                                  │  │ │      │ │  │           │  │ │      │ │  │              │                                │ΘΘ       │  │ │      │ │  │        │  │ │      │ │  │                 
                                  │  │─│      │─│  │           │  │─│      │─│  │              │                                │         │  │─│      │─│  │        │  │─│      │─│  │                 
                                  │                │           │                │              │                                │         │                │        │                │                 
                                  │                │           │                │              │                                │         │                │        │                │                 
                                  │                │           │                │              │                                │         │                │        │                │                 
                                  │                │           │                │              │               ╱|、             │         │                │        │                │                 
                                  │      │──│      │           │      │──│      │              │              (˚ˎ。7             │         │      │──│      │        │      │──│      │                 
                                  │      │  │      │           │      │  │      │              │               |、˜〵             │         │      │  │      │        │      │  │      │                 
                                  │      │──│      │           │      │──│      │              │               じしˍ,)/           │         │      │──│      │        │      │──│      │                 
                              ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                                                                                                                                                                      
                                                                                                                                                                                                      
                                ───────────           ─────────           ────────────           ─────────      ──────────      ────────        ────────     ────────   ────────    ──────     ─────   
                                                                                                                                                                                                                                                                                                                                                      
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""")

def Alleyway_Art():

  print(Fore.LIGHTWHITE_EX + """
        
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                  
                                              │                                               Φ                            Φ               Φ               │                                           
                                              │                                              Φ                            Φ               Φ                │                                           
                                              │                                             Φ                            Φ               Φ                 │                                           
                                              │                                            Φ                            Φ               Φ                  │                                           
                                              │                                           Φ                            Φ               Φ                   │                                           
                                              │                                          │                            │               Φ                    │                                           
                                              │                                          │                 Φ          │              Φ                     │                                           
                                              │                                          │                ΦΦΦ         │             Φ                      │                                           
                                              │                                          │────────        ΦΦΦ         │            Φ                       │                                           
                                              │                                          │       │         │          │           Φ                        │                                           
                                              │                                          │      δδδ       ─│─         │          Φ                         │                                           
                                              │                                          │      δδδ        │          │         Φ                          │                                           
                                              │                                          │      δδδ       α α         │        Φ                           │                                           
                                              │                                          │                            │       Φ                            │                                           
                                              │                                          │                            │      Φ                             │                                           
                                              │                                          │                            │     Φ                              │                                           
                                              │                                          │                     σσσσσσσ│    Φ                               │                                           
                                              │                                          │                     σσσσσσσ│   Φ                                │                                           
                                              │                                          │                     σσσσσσσ│  Φ                                 │                                           
                                              │                                          │                     σσσσσσσ│ Φ                                  │                                           
                                              │                                          │                     σσσσσσσ│Φ                                   │                                           
                                              ───────────────────────────────────────────│                     σσσσσσσ│─────────────────────────────────────                                           
                                                                                                                                                                                                      
                                                                                          ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙                                                                                  
                                                                                                                                                                                                      
                                                                                          ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙                                                                                  
                                                                                                                                                                                                      
                                                                                          ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙                                                                                  
                                                                                                                                                                                                      
                                                                                          ∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙                                      
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        """)
  
# this is the final art for journey 2 (with our fellow Erik Cartman)
def Swamp_Art():
  print(Fore.GREEN + """
        
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                    ⠀⠀⠀⠀    ⢀⢀⣤⠴⠚⠛⠚⠶⣤⡀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                  ⠀⠀⠀⠀⠀⠀⠀⣠⠶⡛⠩⠜⣚⠹⣙⡒⡛⠥⢊⠍⡱⢢⡀⠀⠀⠀⠀⠀⠀
                                                                                  ⠀⠀⠀⠀⠀⢠⡾⢡⠣⠜⡡⣉⢆⣑⣢⣡⣙⣌⡃⢎⡑⢆⡙⢦⠀⠀⠀⠀⠀woah swamp
                                                                                  ⠀⠀⠀⠀⢠⣟⣠⣷⣺⠾⢋⠍⠛⠚⢇⠛⠛⠒⠫⡙⠻⢶⣼⣌⣧⠀⠀⠀⠀
                                                                                  ⠀⠀⠀⠀⢻⡟⠉⠀⠀⢠⠃⠀⠀⢀⣸⠀⠀⠀⢀⣴⠀⠀⠀⠈⣿⠀⠀⠀⠀
                                                                                  ⠀⠀⠀⠀⢱⡇⠀⠀⠀⠘⡀⠀⠀⢀⠌⠡⢀⠀⢀⡸⠀⠀⠀⠀⣾⠁⠀⠀⠀
                                                                                  ⠀⠀⠀⢀⣼⣷⡀⢀⠀⠀⠀⠁⠈⠁⠀⠀⠀⠉⠁⠀⠀⢀⠰⣸⣿⡄⠀⠀⠀
                                                                                  ⠀⣠⣴⣿⣿⣿⣿⣬⡐⢄⠀⠀⠀⠀⣀⣀⡀⠀⠀⢀⠔⣡⣾⣿⠿⣿⣧⡀⠀
                                                                                  ⢼⡃⢆⠩⡙⣿⣿⣿⣿⣶⣭⣖⣒⣠⠷⣖⣮⣒⣭⣴⣾⣿⣿⠏⢲⡐⠆⢿⠀                                                                                                 
                                                                                  ⢸⣗⡈⢆⡑⢬⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣕⠬⣙⣾⠃
                                                                                  ⠀⠈⢻⣿⣿⣿⣿⣿⣽⣿⣷⣿⣿⣽⣿⣿⣿⣿⣽⣿⣾⣿⣽⣿⣿⣿⣿⠁⠀
                                                                                  ⠀⠀⠈⠻⣿⣿⣷⣿⣿⣽⣾⣿⣯⣿⣿⣿⣿⣾⣿⣽⣯⣿⣿⣽⣿⡟⠁⠀⠀
                                                                                  ⠀⠀⠀⠀⠽⠿⠿⠿⠿⠿⠿⠾⠿⠿⠿⠿⠿⠿⠿⢿⠿⠿⠿⢿⣏⠀⠀⠀⠀


                                                                                  ∩∩ ∩ ∩∩∩ ∩ ∩∩∩∩∩∩ ∩ ∩∩∩∩∩ ∩ ∩ ∩ ∩∩∩ ∩                                                                            
                                                                          ∩∩∩∩∩∩∩                 ßßßßßßßß            ∩∩∩ ∩∩∩∩                                                                    
                                                                ∩∩∩∩∩∩∩∩∩                  ßß ßß ßß      ßßßß                 ∩∩∩∩                                                                
                                                          ∩∩∩∩∩∩∩                                            ßß                   ∩∩∩                                                              
                                                      ∩∩∩∩                                     ßßß ßßßßßßß                          ∩∩∩                                                           
                                                    ∩∩∩∩           φφ                        ßßßß          ßßß                          ∩∩                                                         
                                                  ∩∩           φφφ φ                       ßß               ß                            ∩∩∩                                                      
                                                  ∩∩        φφφφ   φφφφφ                        ßßßßßßßßßßß                                 ∩∩                                                     
                                                ∩∩       φφ          φφ                     ßßßß          ß                                 ∩∩∩                                                   
                                                ∩∩        φ         φφφ                    ßß                                          φφ      ∩                                                   
                                              ∩∩          φφφφ     φ                             ßßßßßß                            φφφ φ      ∩∩                                                  
                                              ∩∩            φφ    φφ                          ßßßß    ßßßß                     φφφφ   φφφφφ    ∩                                                  
                                                ∩          φφφ     φ                        ßßß            ß                  φφ          φφ    ∩∩                                                 
                                                ∩        φφφ       φ               ß  ß          ΘΘΘ                          φ         φφφ      ∩                                                 
                                                ∩∩   φφφφφ         φφφ            ß     ßß    ΘΘΘ    ΘΘΘ   ß   ßß              φφφφ     φ        ∩                                                 
                                                ∩∩∩                φφφφ         ß    ß      ΘΘ        ΘΘ    ß   ß               φφ    φφ        ∩                                                 
                                                  ∩∩                            ß   ß      ΘΘ          Θ     ßß  ß            φφφ     φ         ∩                                                 
                                                    ∩∩                               ß      Θ           Θ     ßß    ß        φφφ       φ        ∩∩                                                 
                                                      ∩∩∩                                   ΘΘ        ΘΘ    ßß      ß    φφφφφ         φφφ      ∩                                                  
                                                        ∩∩∩∩∩                               ΘΘΘΘΘΘΘΘΘΘ             ß                          ∩∩                                                  
                                                              ∩∩∩∩∩∩∩ ∩                                                                       ∩∩                                                   
                                                                      ∩∩∩∩∩∩∩∩∩∩∩∩                                                         ∩∩∩∩                                                    
                                                                                ∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩                   ∩∩∩∩∩∩∩∩∩∩                                                        
                                                                                                              ∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩∩                                                                 
                                                                                                                                                                                                  
                                                                                                                                                                                                  
                                                                                                                                                                                                  
                                                                                                                                                                                                  
                                                              │────────────────────────────────────────────────────────────────────────│                                                           
                                                              │                                    ΘΘΘ                                 │                                                           
                                                              │                                   Θ   Θ                                │                                                           
                                                              │                                    ΘΘΘ                                 │                                                           
                                                              │                                     │                                  │                                                           
                                                              │                                    ─│─                                 │                                                           
                                                              │                                     │                                  │                                                           
                                                              │                                    Θ Θ                                 │                                                           
                                                              ──────────────────────────────────────────────────────────────────────────       
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        """)

#-----------------------------------------------------------------------------------------------------
# Ascii Art People Drawings 
#-----------------------------------------------------------------------------------------------------

# art description: a skinny postal man wearing a baseball cap and sunglasses 
def Postal_Dude_Art():

  print("""
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                   
                                                                                                          ααααααααααα                                                                             
                                                                                                        ααα▀▀▀▀▀▀▀▀▀αααα                                                                          
                                                                                                      αα▀▀▀▀▀▀▀▀▀▀▀▀▀▀αα                                                                         
                                                                                                      αα▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀α                                                                         
                                                                                            αααααααααα▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀α                                                                         
                                                                                            α▀▀▀▀▀▀▀▀▀▀▀ΘΘΘΘΘΘΘΘΘ▀▀▀▀▀▀α                                                                         
                                                                                            αα▀▀▀▀▀▀▀ΘΘΘΘ       ΘΘΘ▀▀▀αα                                                                         
                                                                                              αααααααΘΘ    ────    Θαααα                                                                          
                                                                                                    ΘΘ   ────────   ΘΘ                                                                            
                                                                                                    Θ  ────────────  Θ                                                                            
                                                                                                    Θ ■■■■      ■■■■ Θ                                                                            
                                                                                                    Θ ■■■■■■■■■■■■■■ Θ                                                                            
                                                                                                    Θ ■■■■      ■■■■ Θ                                                                            
                                                                                                    Θ       ΘΘ       Θ                                                                            
                                                                                                    ΘΘ               Θ                                                                            
                                                                                                    Θ    ══════   ΘΘ                                                                             
                                                                                                      ΘΘ          ΘΘ                                                                              
                                                                                                      ΘΘΘΘ       Θ                                                                               
                                                                                                          Θ       Θ                                                                               
                                                                                                        ΘΘ       Θ                                                                               
                                                                                                        ΘΘ        ΘΘ                                                                              
                                                                                                      ΘΘ          Θ                                                                              
                                                                                                ΘΘΘΘΘΘΘ           ΘΘ                                                                             
                                                                                            ΘΘΘΘΘ                  ΘΘΘΘΘΘΘΘΘΘΘ
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""")

# art description: cleaning maid servant of master "Zenith"
def Sakuya_Art():
  print(Fore.RED + """
        
                                                                                                                                                                               
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                                                         
                                                                                                  ΦΦΦΦΦΦΦΦΦΦΦ                                                                          
                                                                                            ΦΦΦΦΦΦΦ▀▀┃▀▀┃▀▀┃ΦΦΦΦΦΦ                                                                     
                                                                                        ΦΦΦΦ▀▀┃▀▀┃▀▀┃▀▀┃▀▀┃▀▀▀┃▀ΦΦΦ                                                                   
                                                                                        ΦΦ ┃▀▀▀┃▀▀┃▀▀┃▀▀┃▀▀┃▀▀▀┃▀ ┃ΦΦΦ                                                                 
                                                                                        Φ▀▀┃▀▀▀┃▀▀┃▀▀┃▀▀┃▀▀┃▀▀▀┃▀▀┃▀▀ΦΦ                                                                
                                                                                      Φ┃▀▀┃▀▀▀┃▀▀┃▀▀┃▀▀┃▀▀┃▀▀▀┃▀▀┃▀▀┃Φ                                                                
                                                                                      Φ▀┃▀▀┃▀▀αααααααααααααα▀▀▀┃▀▀┃▀▀┃Φ                                                                
                                                                                    ΦΦ▀┃▀ααααα  °°°°°°°°°° ααααα▀┃▀▀┃Φ                                                                
                                                                                    ααααααα°°°°°         °°°°  αααα ΦΦ                                                                
                                                                                      αα αα°°                °°°   ααΦ                                                                 
                                                                                      αα ααα       ΩΩΩΩΩΩΩ      °° ααααα                                                               
                                                                                      αα αααΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩ°αα  αα                                                              
                                                                                    ααα° ααα                     αα°   αα                                                             
                                                                                    αααα° ααα                     αα°  αααα                                                            
                                                                                  αααα ° αα                      αα° ααα                                                              
                                                                                  ααα  ° ααα ΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩ αα°αα                                                               
                                                                                  α α  ° αα        ΩΩΩΩΩΩΩ         αα°αα                                                               
                                                                                  ααα °° α                         αα°αα                                                               
                                                                                  αα ° αα                         αα°αα                                                               
                                                                                    αα° αα          º  º           αα αα                                                               
                                                                                    αα° ααα                       ααα αα                                                               
                                                                                  ααα °°ααα                      ααα  α                                                                
                                                                                  αα   °  αα                       °                                                                   
                                                                                      °           ════════        °°                                                                   
                                                                                      °°         º        º      °°                                                                    
                                                                                        °°                      °°                                                                     
                                                                                        °°                    °°                                                                      
                                                                                          °°°                 °°                                                                       
                                                                                        °°°°                   °°                                                                      
                                                                                    °°°°                       °°°°                                                                   
                                                                                °°°°°                             °°°°                                                                
                                                                            °°°°                                     °°°                                                              
                                                              °°°°°°°°°°°°°°°                                           °°°°°°°°°°°°°°°°°                                             
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        """)

# art description: middle aged asian man with rice hat 
def Zenith_Art():

  print(Fore.BLUE + """
      
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
                                                                                                     σσσ                                                                              
                                                                                                  σσσΘΘσσσ                                                                            
                                                                                                σσσΘΘΘΘΘΘΘΘσσσσ                                                                        
                                                                                              σΘΘΘΘΘΘΘΘΘΘΘΘΘΘσσσ                                                                      
                                                                                            σσσΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘσσσ                                                                   
                                                                                          σσσΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘσσ                                                                  
                                                                                        σσσΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘσσ                                                                
                                                                                      σσσΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘσ                                                              
                                                                                    σσσΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘσ                                                             
                                                                                  σσΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘσσσ                                                          
                                                                                σσσΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘΘσσ                                                         
                                                                                σσσσσσσσσσσσσσσσσσσσσσσσσσσσσσσσσσσσσσσσσσσσσ                                                         
                                                                                    α α  °°                       °  α   αα                                                            
                                                                                    ααα °                           ° α  α                                                             
                                                                                    αα  °     ────        ────    °   αα α                                                             
                                                                                  ααα  °                           °  α α                                                             
                                                                                  α α °                             ° α αα                                                            
                                                                                  α α °                             ° α  α                                                            
                                                                                  α α°°                             ° α   α                                                           
                                                                                  α α°             ───             °  α   α                                                           
                                                                                  αα α°                             °  α  α                                                           
                                                                                αα αα°                              °  α  αα                                                          
                                                                                αα  α °°          ²²²²²           °°  αα  α                                                          
                                                                                      °      ²²²²²     ²²²²²      °    αα  αα                                                         
                                                                                      °      ²             ²     °°    α                                                              
                                                                                      °°                        °°                                                                    
                                                                                        °°                      °°                                                                     
                                                                                        °°                    °°                                                                      
                                                                                          °°°                 °°                                                                       
                                                                                        °°°°                   °°                                                                      
                                                                                    °°°°                       °°°°                                                                   
                                                                                °°°°°                             °°°°                                                                
                                                                            °°°°                                     °°°                                                              
                                                              °°°°°°°°°°°°°°°                                           °°°°°°°°°°°°°°°°°  
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                        
        
        """)

# art description: a knight with a helmet 
def Eric_Art():

  print(Fore.YELLOW + """

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                               °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°                                                                
                                                                                              °               π°π                °                                                               
                                                                                              °               πππ                °                                                               
                                                                                              °               π°π                °                                                               
                                                                                              °               πππ                °                                                               
                                                                                              °               π°π                °                                                               
                                                                                              °               πππ                °                                                               
                                                                                              °ππππππππππππππππππππππππππππππππππ°                                                               
                                                                                              °ππ        πππππππππππππ        πππ°                                                               
                                                                                              °ππππππππππππππππππππππππππππππππππ°                                                               
                                                                                              °               π°π                °                                                               
                                                                                              °               πππ                °                                                               
                                                                                              °   °  °  °     π°π           ≡    °                                                               
                                                                                              °               πππ           ≡    °                                                               
                                                                                              °   °  °  °     π°π        ≡≡≡≡≡≡≡ °                                                               
                                                                                              °               πππ           ≡    °                                                               
                                                                                              °   °  °  °     πππ           ≡    °                                                               
                                                                                              °               π°π                °                                                               
                                                                                                °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°                                                                
                                                                                                   °°                      °°                                                                     
                                                                                                    °°                    °°                                                                      
                                                                                                    °°°                 °°                                                                       
                                                                                                  °°°°                   °°                                                                      
                                                                                                °°°°                       °°°°                                                                   
                                                                                            °°°°°                             °°°°                                                                
                                                                                        °°°°                                     °°°                                                              
                                                                          °°°°°°°°°°°°°°°                                           °°°°°°°°°°°°°°°°°
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        """)


# art description: jesus from family guy
def RNGesus_Art():

  print(Fore.CYAN + """
        
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                      ⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣶⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀
                                                                              ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣷⣄⠀⠀⠀⠀
                                                                              ⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠀⠈⠻⣿⣿⣿⣷⡄⠀⠀
                                                                              ⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠈⠻⣿⣿⣷⠀⠀
                                                                              ⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⠋⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡆⠀
                                                                              ⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⠇⡼⠓⠒⠢⠭⠽⡅⠀⡾⠿⠯⣉⣻⣿⡇⠀
                                                                              ⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⡿⠀⢇⣀⣈⣁⠀⢀⠇⢸⠀⠀⠘⠀⠀⣿⡇⠀
                                                                              ⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⠳⠤⠤⠜⠋⠀⠀⢿⣍⣉⡱⠞⣿⠀⠀
                                                                              ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⢸⠀⠀
                                                                              ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⣀⣦⡀⠀⠀⡇⠀⠀⠀⢸⡆⠀
                                                                              ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡆⠀⠀⣸⠀⠀
                                                                              ⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠸⠿⠿⣿⣛⣉⢹⠻⠿⢿⠀⢰⡇⠀⠀
                                                                              ⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣜⣻⣿⣏⠉⠀⠀⠀⣰⣿⠀⠀⠀
                                                                              ⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⣭⣥⣬⠃⠀⣠⣾⣿⡟⠀⠀⠀
                                                                              ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⠃⠀⠀⠀
                                                                              ⠀⠀⢠⣿⣿⣿⣿⣿⣿⡿⢿⠇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡿⠀⠀⠀⠀
                                                                              ⣠⣤⠾⠟⠻⠿⠟⠛⠏⠀⢼⡀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
                                                                              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⡿⣿⣅⠀⠀⠀⠀
                                                                              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠻⡿⢿⣿⠋⠛⠟⠀⠈⠻⣦⠀⠀⠀
                                                                              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⢀⡇⠀⠸⡄⠀⠀⠀⠀⠀⠘⢧⠀⠀
                                                                              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣸⠁⠀⠀⢳⡀⠀⠀⠀⠀⠀⠈⢦⠀
                                                                              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠈⢇
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        """)

# art description: patriotic russian citizen wearing a ushanka 
def Rasputin_Art():

  print("""
  
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                       
                                                                                  ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ                                                                     
                                                                              ΦΦΦΦ                         ΦΦΦΦΦ                                                                 
                                                                              Φ                                ΦΦΦ                                                               
                                                                            Φ                │                  Φ                                                               
                                                                            Φ       │       ─│─       │          ΦΦ                                                             
                                                                            Φ      ─│─       │       ─│─     │    Φ                                                             
                                                                            Φ       │                 │     ─│─   ΦΦ                                                            
                                                                            ΦΦ           ΦΦΦ ΦΦΦ             │     ΦΦ                                                           
                                                                              Φ        ΦΦΦ       ΦΦΦΦΦ               Φ                                                           
                                                                              Φ   │   ΦΦ              ΦΦ             Φ                                                           
                                                                              Φ  ─│─ ΦΦ ΘΘΘΘ      ΘΘΘΘ  Φ       │    Φ                                                           
                                                                            ΦΦ    │  Φ   ΘΘ        ΘΘ   ΦΦ     ─│─   Φ                                                           
                                                                            ΦΦ       Φ  Θ  Θ      Θ  Θ   Φ      │    Φ                                                           
                                                                            Φ────────Φ   ΘΘ        ΘΘ    Φ───────────Φ                                                           
                                                                            Φ▄▄▄▄▄▄▄▄Φ                   Φ▄▄▄▄▄▄▄▄▄▄▄Φ                                                           
                                                                            Φ▄▄▄▄▄▄▄▄Φ                   Φ▄▄▄▄▄▄▄▄▄▄▄Φ                                                           
                                                                            Φ▄▄▄▄▄▄▄▄Φ                   Φ▄▄▄▄▄▄▄▄▄▄▄Φ                                                           
                                                                            Φ▄▄▄▄▄▄Φ                    Φ▄▄▄▄▄▄▄▄▄▄▄Φ                                                           
                                                                            Φ▄▄▄▄▄▄Φ                    Φ▄▄▄▄▄▄▄▄▄▄ΦΦ                                                           
                                                                            Φ▄▄▄▄▄ΦΦ                    ΦΦ▄▄▄▄▄▄▄▄▄Φ                                                            
                                                                              ΦΦΦΦΦΦ                      Φ▄▄▄▄▄▄▄▄ΦΦ                                                            
                                                                                °         ΦΦΦΦΦΦΦΦ        ΦΦΦΦΦΦΦΦ                                                              
                                                                                °         Φ      Φ         °°                                                                   
                                                                                °°        Φ      Φ        °°                                                                    
                                                                                  °°      ΦΦΦΦΦΦΦΦ       °°                                                                     
                                                                                  °°                    °°                                                                      
                                                                                    °°°                 °°                                                                       
                                                                                  °°°°                   °°                                                                      
                                                                              °°°°                       °°°°                                                                   
                                                                          °°°°°                             °°°°                                                                
                                                                      °°°°                                     °°°                                                              
                                                        °°°°°°°°°°°°°°°                                           °°°°°°°°°°°°°°°°°   
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
  """)

# art description: trench coat magic dealer 
def Iku_Blackrock_Art():

  print(Fore.CYAN + """
  
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
                                                                                        φφφφφφφ                                                                           
                                                                                     φφφ  ║   φφφ                                                                        
                                                                                  φφφ     ║     φφφ                                                                      
                                                                                 φφ       ║       φφ                                                                     
                                                                                φφ        ║        φ                                                                     
                                                                                φ         ║        φφ                                                                    
                                                                               φφ         ║         φφ                                                                   
                                                                               φ          ║          φ                                                                   
                                                                            φφφφφφφφφφφφφφφφφφφφφφφφφφφφφφ                                                               
                                                                    φφφφφφφφ                              φφφ                                                            
                                                                    φ                                        φφ                                                          
                                                                    φ══════════════════════════════════════════φφφφφ                                                     
                                                                    φ═════════════════════════════════════════════φφ                                                     
                                                                    φφφ                                           φφ                                                     
                                                                     δ φφφφφφ                                  φφφφδ                                                     
                                                                     δ  δδδδφφφφφφφφφφ                    φφφφφφ δ δ                                                     
                                                                    δ  δδδδ δ°       φφφφΘΘφφφφφφφφφφφφφφφ δ δ δ δ  δ                                                    
                                                                    δ  δ δ δδ°           Θ      ßßßßßß   ° δδδδδδδδ δ                                                    
                                                                    δ  δ δδδ °          Θ     ßßß     ßß °  δ δ δ δ  δ                                                   
                                                                   δ  δδδδδ °           Θ    ßß ΩΩΩΩ   ß  ° δ δ δ δδ δ                                                   
                                                                   δ  δ δδ  °           Θ      Ω    Ω     ° δ δ δδ δ δ                                                   
                                                                   δ  δ δδ °°          Θ       Ω    Ω     ° δ δ  δ δ δδ                                                  
                                                                   δ  δ δδ °          ΘΘ        ΩΩΩΩ      ° δ δ  δ δ  δ                                                  
                                                                   δ  δ δδ °        ΘΘ                    ° δδδδ δ δ  δ                                                  
                                                                   δ  δδδδ °ΘΘ    ΘΘΘ                     °  δ δ δ δ δδ                                                  
                                                                   δ   δδδ °° ΘΘ Θ                       °°  δ δ δ δ δ                                                   
                                                                   δδ  δδδ  °                           °   δδ δδδ δδδ                                                   
                                                                       δδδ  °        ═══════════       °°   δ  δδ δδδ                                                    
                                                                            °°                        °°    δ δ δ δ                                                      
                                                                             °°                      °°                                                                  
                                                                              °°                    °°                                                                   
                                                                               °°°                 °°                                                                    
                                                                             °°°°                   °°                                                                   
                                                                          °°°°                       °°°°                                                                
                                                                      °°°°°                             °°°°                                                             
                                                                  °°°°                                     °°°                                                           
                                                    °°°°°°°°°°°°°°°                                           °°°°°°°°°°°°°°°°°
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
  
  
  
  """)

# art description: old man with long beard (the beard kinda looks like a bandit mask not gonna lie lol)
def Slave_Knight_Art():
  print(Fore.RED + """

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                            
                                                                                                    ΩΩ Ω                                                                         
                                                                                                  ΩΩ                                                                             
                                                                                                  Ω                                                                              
                                                                                        ΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩ                                                                       
                                                                                      ΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩ                                                                     
                                                                                    ΩΩΩΩΩ °°°°°°°°°° ΩΩΩΩΩΩΩ                                                                    
                                                                                  ΩΩΩ°Ω°°°         °°°° ΩΩΩΩΩ                                                                   
                                                                                  ΩΩΩ°°                °°° ΩΩΩ                                                                   
                                                                                ΩΩΩ°°                    °°ΩΩΩΩ                                                                 
                                                                                ΩΩΩ°°  φφφφφ            φφ  °ΩΩΩΩ                                                                
                                                                                ΩΩ°  φφφ   φφφφ       φφφφφφφ °ΩΩΩ                                                               
                                                                              ΩΩΩ° φφ  ••    φ      φ      φφ° ΩΩ                                                               
                                                                            ΩΩΩ  °    •  •             ••    °  Ω                                                               
                                                                              Ω  °     ••             •  •    °  Ω                                                              
                                                                              Ω  °                     ••     °  Ω                                                              
                                                                            Ω  °°               ║              °  Ω                                                              
                                                                                °               ║              °  Ω                                                              
                                                                                °              ═║═             °                                                                 
                                                                                °φφφ                           °                                                                 
                                                                                °φ■ φφφφφφ                φφφφφ°                                                                 
                                                                                φφ■■■■■■■φφφφφφ      φφφφφ■■■φ                                                                  
                                                                                °φ■■■■■■■■■■■■■φφφφφφ■■■■■■■φ                                                                   
                                                                                °φφ■■■■■■■■■■■■■■■■■■■■■■■■■φ                                                                   
                                                                                  °φφ■■■■■■■■■■■■■■■■■■■■■■■φ                                                                    
                                                                                  °φφ■■■■■■■■■■■■■■■■■■■■■φφ                                                                    
                                                                                    °φφ■■■■■■■■■■■■■■■■■■■φφ                                                                     
                                                                                  °°°°φ■■■■■■■■■■■■■■■■■■■φ                                                                      
                                                                              °°°°    φ■■■■■■■■■■■■■■■■■φφ°°°                                                                   
                                                                          °°°°°        φ■■■■■■■■■■■■■■■φφ   °°°°                                                                
                                                                      °°°°              φφ■■■■■■■■■■■■■φ       °°°                                                              
                                                        °°°°°°°°°°°°°°°                  φφφ■■■■■■■■■■φφ          °°°°°°°°°°°°°°°°°                                             
                                                                                            φφφφ■■■■■■φφ                                                                         
                                                                                              φφ■■φφφ                                                                           
                                                                                                φφφ                              
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  """)

# art description: hooded assassin I guess forgot how bad at drawing I am 
def BloodDrinker_Rei_Art():
  print(Fore.LIGHTRED_EX + """

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
                                                                          ΘΘΘΘΘΘΘΘ ΘΘΘΘ ΘΘΘΘΘΘΘΘΘΘ                                                                       
                                                                      ΘΘΘΘ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ΘΘΘΘΘΘ                                                                 
                                                                   ΘΘΘ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ΘΘΘ                                                              
                                                                  ΘΘ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ΘΘΘ                                                           
                                                                 ΘΘ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀Θ                                                          
                                                                Θ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀Θ                                                         
                                                               Θ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀Θ                                                        
                                                              ΘΘ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀°°°°°°°°°°▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀Θ                                                       
                                                              Θ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀°°°°°         °°°°▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀Θ                                                      
                                                              Θ▀▀▀▀▀▀▀▀▀▀▀▀▀▀°°                °°°▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ΘΘ                                                     
                                                              Θ▀▀▀▀▀▀▀▀▀▀▀▀▀°°                    °°▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀Θ                                                     
                                                              Θ▀▀▀▀▀▀▀▀▀▀▀▀°°                       °▀▀▀▀▀▀▀▀▀▀▀▀▀▀Θ                                                     
                                                              Θ▀▀▀▀▀▀▀▀▀▀▀°───────────────────────────°▀▀▀▀▀▀▀▀▀▀▀▀Θ                                                     
                                                              Θ▀▀▀▀▀▀▀▀▀▀▀°                           °▀▀▀▀▀▀▀▀▀▀▀▀Θ                                                     
                                                              Θ▀▀▀▀▀▀▀▀▀▀▀°   ΘΘ                 ΘΘ   °▀▀▀▀▀▀▀▀▀▀▀▀Θ                                                     
                                                              Θ▀▀▀▀▀▀▀▀▀▀°   ΘΦΦΘ               ΘΦΦΘ   °▀▀▀▀▀▀▀▀▀▀▀Θ                                                     
                                                              Θ▀▀▀▀▀▀▀▀▀▀°    ΘΘ                 ΘΘ    °▀▀▀▀▀▀▀▀▀▀Θ                                                      
                                                              ΘΘ▀▀▀▀▀▀▀▀°°─────────────────────────────°▀▀▀▀▀▀▀▀▀▀Θ                                                      
                                                               ΘΘ▀▀▀▀▀▀▀°                              °▀▀▀▀▀▀▀▀▀▀Θ                                                      
                                                                Θ▀▀▀▀▀▀▀°                              °▀▀▀▀▀▀▀▀▀ΘΘ                                                      
                                                                ΘΘ▀▀▀▀▀▀°                              °▀▀▀▀▀▀▀▀▀Θ                                                       
                                                                 ΘΘ▀▀▀▀▀°°                            °°▀▀▀▀▀▀▀▀ΘΘ                                                       
                                                                  Θ▀▀▀▀▀▀°                           °▀▀▀▀▀▀▀▀▀▀Θ                                                        
                                                                   Θ▀▀▀▀▀°                          °°▀▀▀▀▀▀▀▀ΘΘ                                                         
                                                                    ΘΘ▀▀▀°°                        °°▀▀▀▀▀▀▀▀ΘΘ                                                          
                                                                      ΘΘΘ▀°°                      °°▀▀▀▀▀▀▀ΘΘΘ                                                           
                                                                         ΘΘ°°                    °°▀▀▀▀▀▀ΘΘΘ                                                             
                                                                           Θ°°°                 °°▀▀▀▀▀ΘΘΘ                                                               
                                                                          °°°°                   °°▀▀ΘΘΘ                                                                 
                                                                       °°°°                       °°°°                                                                   
                                                                   °°°°°                             °°°°                                                                
                                                               °°°°                                     °°°                                                              
                                                 °°°°°°°°°°°°°°°                                           °°°°°°°°°°°°°°°°°           
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
  
  """)
# art description: just a faceless man
def Huby_Developer_Art():

  print(Fore.WHITE + """
  
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
                                                                                                °°°°°°°°°°                                                                            
                                                                                            °°°°°°°°°°°°°°°°°°                                                                         
                                                                                          °°°°°°°°°°°°°°°°°°°°°                                                                       
                                                                                          °°°°°°°°°°°°°°°°°°°°°°°°                                                                     
                                                                                        °°°°°°°°°°°°°°°°°°°°°°°°°°°                                                                   
                                                                                        °°°°°°°°°°°°°°°°°°°°°°°°°°°°°                                                                  
                                                                                        °°°°°°°°°°°°°°°°°°°°°°°°°°°°°                                                                  
                                                                                        °°°°°°°°°°°°°°°°°°°°°°°°°°°°°                                                                  
                                                                                      °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°                                                                 
                                                                                      °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°                                                                 
                                                                                      °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°                                                                 
                                                                                      °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°                                                                 
                                                                                      °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°                                                                 
                                                                                      °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°                                                                 
                                                                                      °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°                                                                 
                                                                                      °°°°°°°°°°°°°°°°°°°°°°°°°°°°°                                                                   
                                                                                      °°°°°°°°°°°°°°°°°°°°°°°°°°°°°                                                                   
                                                                                      °°°°°°°°°°°°°°°°°°°°°°°°°°°°                                                                    
                                                                                        °°°°°°°°°°°°°°°°°°°°°°°°°°                                                                     
                                                                                        °°°°°°°°°°°°°°°°°°°°°°°°                                                                      
                                                                                          °°°°°°°°°°°°°°°°°°°°°°                                                                       
                                                                                        °°°°                   °°°                                                                     
                                                                                    °°°°                       °°°°                                                                   
                                                                                °°°°°                             °°°°                                                                
                                                                            °°°°                                     °°°                                                              
                                                              °°°°°°°°°°°°°°°                                           °°°°°°°°°°°°°°°°°
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                
  
""")

#-----------------------------------------------------------------------------------------------------
# START OF JOURNEY 1 WEAPON CHOICES 
#-----------------------------------------------------------------------------------------------------

# <><><><><><><><><><><><><><><><><><><><><><><><><><>
#                 PLAYER WEAPON CHOICES
# <><><><><><><><><><><><><><><><><><><><><><><><><><>

def Player_Weapons(): 

  # normal damage: death = 6 - 27 glinted = 12 - 20 lightning = 13 - 16 debug: 99+ on one weapon

  # players may choose this weapon for inconsistent but high damage
  Death_Hunt_Sickle = random.randint(999, 999)
  # players may choose this weapon for average consistent good damage
  Glinted_Zweihander = random.randint(12, 20)
  # players may choose this weapon for more consistent but lower damage
  Lightning_Strike = random.randint(13, 16)

  # the block mechanic will reduce damage inflicted by the enemy based on the random percentage value assigned e.x 0.39 = 39% damage reduction 
  Block = random.uniform(0.15, 0.40)
  Block_Percentage = Block * 100
  Block_Percentage_Rounded = round(Block_Percentage, 0)
  
  Weapon_List = ["Death_Hunt_Sickle", "Glinted_Zweihander", "Lightning_Strike", "Block"] 

  if Potion_Display == True:
    Weapon_List.append("Health Potion (can only be consumed once)")

  return Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded

def Postal_Dudes_Turn():
  Fist = random.randint(2, 7)
  Hatchet = random.randint(5, 13)
  Ak_47 = random.randint(7, 20)
  Postal_Dude_Random_Choices = random.randint(0, 2)

  Postal_Dude_Weapons = [Fist, Hatchet, Ak_47]
  Postal_Dude_Weapon_Description = ["hurled his fist", "swung his hatchet", "rained bullets with an Ak_47"]

  Weapon_Selection = Postal_Dude_Weapons[Postal_Dude_Random_Choices]
  Description_Selection = Postal_Dude_Weapon_Description[Postal_Dude_Random_Choices]

  return Weapon_Selection, Description_Selection

def Sakuyas_Turn():
  Killing_Doll = random.randint(7, 12)
  The_World = random.randint(8, 15)
  Anti_Clockwise = random.randint(10, 22)
  Sakuya_Random_Choices = random.randint(0, 2)

  Sakuya_Weapons = [Killing_Doll, The_World, Anti_Clockwise]
  Sakuya_Weapon_Description = ["scattered her kunai knives", "splashed the room with knives", "used stopwatch disorienting the player"]

  Weapon_Selection = Sakuya_Weapons[Sakuya_Random_Choices]
  Description_Selection = Sakuya_Weapon_Description[Sakuya_Random_Choices]

  return Weapon_Selection, Description_Selection

def Zeniths_Turn():
  All_Thats_Blue = random.randint(9, 15)
  Pyromantic = random.randint(11, 19)
  volans_lutum = random.randint(13, 26)
  Zenith_Random_Choices = random.randint(0, 2)

  Zenith_Weapons = [All_Thats_Blue, Pyromantic, volans_lutum]
  Zenith_Weapon_Description = ["threw a giant cluster of crystals cutting the player", "showered the player with fire", "shifted the ground making the player fall"]

  Weapon_Selection = Zenith_Weapons[Zenith_Random_Choices]
  Description_Selection = Zenith_Weapon_Description[Zenith_Random_Choices]

  return Weapon_Selection, Description_Selection


def Erics_Turn():
  MoonLight_Arrow_Fall = random.randint(5, 9)
  Collapsing_Star = random.randint(9, 12)
  Absolute_Kelvin = random.randint(14, 30)
  Eric_Random_Choices = random.randint(0, 2)

  Erics_Weapons = [MoonLight_Arrow_Fall, Collapsing_Star, Absolute_Kelvin]
  Eric_Weapon_Description = ["multishotted his bow impaling the player", "whispered to the player's ear persuading to join the lunar moon", "froze all particles nearby to a complete stop"]

  Weapon_Selection = Erics_Weapons[Eric_Random_Choices]
  Description_Selection = Eric_Weapon_Description[Eric_Random_Choices]


  return Weapon_Selection, Description_Selection

# my creativity levels is slowly being drained here 
def RNGesus_Turn():
  Divinus_hasta = random.randint(10, 17)
  Cleansed_Dice = random.randint(3, 10)
  True_Or_False = random.randint(9, 22)
  Mystic_Justice = random.randint(12, 15)
  Hollowed = random.randint(15, 25)
  RNGesus_Random_Choices = random.randint(0, 4)

  RNGesus_Weapons = [Divinus_hasta, Cleansed_Dice, True_Or_False, Mystic_Justice, Hollowed]
  RNGesus_Weapon_Description = ["spawned a holy spear and impaled the player", "summoned a dice nausnauseating the player of luck", "proposed a true and false question confusing the player", "slashed the player with a wetstone blade", "casted a spell making the player go mad"]

  Weapon_Selection = RNGesus_Weapons[RNGesus_Random_Choices]
  Description_Selection = RNGesus_Weapon_Description[RNGesus_Random_Choices]

  return Weapon_Selection, Description_Selection

#-----------------------------------------------------------------------------------------------------
# END OF JOURNEY 1 WEAPON CHOICES
# START OF JOURNEY 2 WEAPON CHOICES
#-----------------------------------------------------------------------------------------------------

def Rasputins_Turn():
  Sickle = random.randint(2, 7)
  Hammer = random.randint(5, 13)
  Broken_Stoli = random.randint(7, 20)
  Rasputin_Random_Choices = random.randint(0, 2)

  Rasputin_Weapons = [Sickle, Hammer, Broken_Stoli]
  Rasputin_Weapon_Description = ["shanked player with a sickle", "bashed the player with his hammer", "threw his broken stoli"]

  Weapon_Selection = Rasputin_Weapons[Rasputin_Random_Choices]
  Description_Selection = Rasputin_Weapon_Description[Rasputin_Random_Choices]

  return Weapon_Selection, Description_Selection

def Iku_Blackrocks_Turn():
  Stained_Scythe = random.randint(9, 14)
  Mercury_Poisoning = random.randint(10, 19)
  Rapport = random.randint(3, 20)
  Iku_Blackrocks_Random_Choices = random.randint(0, 2)


  Iku_Blackrock_Weapons = [Stained_Scythe, Mercury_Poisoning, Rapport]
  Iku_Blackrock_Description = ["stabbed the player with a stained scythe poisioning the player", "sprayed mercury on the players open wounds", "slightly charmed the player"]

  Weapon_Selection = Iku_Blackrock_Weapons[Iku_Blackrocks_Random_Choices]
  Description_Selection = Iku_Blackrock_Description[Iku_Blackrocks_Random_Choices]

  return Weapon_Selection, Description_Selection

def Servant_Knight_Turn():
  White_Corona = random.randint(5, 10)
  Lightning_Strike = random.randint(10, 20)
  Executioners_Greatsword = random.randint(7, 30)
  Servant_Knight_Random_Choices = random.randint(0, 2)

  Servant_Knight_Weapons = [White_Corona, Lightning_Strike, Executioners_Greatsword]
  Servant_Knight_Description = ["casted a magic saw blade", "electrocuted the player by striking lightning", "bashed the player with a greatsword"]

  Weapon_Selection = Servant_Knight_Weapons[Servant_Knight_Random_Choices]
  Description_Selection = Servant_Knight_Description[Servant_Knight_Random_Choices]


  return Weapon_Selection, Description_Selection

def BloodDrinker_Reis_Turn():
  Hand_Of_Blood = random.randint(2, 7)
  Sacrifical_Lamb = random.randint(12, 20)
  Tres_duos_unus = random.randint(18, 31) # just watch the elden ring mohg fight and you will understand why I named this spell card 
  BloodDrinker_Reis_Random_Choices = random.randint(0, 2)

  BloodDrinker_Reis_Weapons = [Hand_Of_Blood, Sacrifical_Lamb, Tres_duos_unus]
  BloodDrinker_Reis_Description = ["shedded the players skin causing blood loss", "sacrificed a lamb making the player distressed", "casted a bloodloss spell making the player lightheaded"]


  Weapon_Selection = BloodDrinker_Reis_Weapons[BloodDrinker_Reis_Random_Choices]
  Description_Selection = BloodDrinker_Reis_Description[BloodDrinker_Reis_Random_Choices]

  return Weapon_Selection, Description_Selection  

# note: user will die as the bad ending of the game aka its a scripted death 
def Huby_developers_Turn():
  Night_Of_Nights = 10000
  Allruing_Skull = 10000
  Memory_Address_Removal = 10000
  Huby_Developer_Random_Choices = random.randint(0, 2)

  Huby_developer_Weapons = [Night_Of_Nights, Allruing_Skull, Memory_Address_Removal]
  Huby_Developer_Description = ["has fast forwarded time by ten folds killing the player in confusion", "chucked a tempting skull making the player jump off a cliff", "erased the memory location of the player"]

  Weapon_Selection = Huby_developer_Weapons[Huby_Developer_Random_Choices]
  Description_Selection = Huby_Developer_Description[Huby_Developer_Random_Choices]

  return Weapon_Selection, Description_Selection

#-----------------------------------------------------------------------------------------------------
# END OF JOURNEY 2 WEAPON CHOICES
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# DISPLAY WEAPON CHOICES FOR PLAYER    
#-----------------------------------------------------------------------------------------------------

def Players_turn(HP_player):
  
  Numerical_Order = 0
  Dodge_Attack = random.randint(1, 12)

  # 7 tab indents is the golden number of centering left-aligned text at least for these boxes specifically 
  print(f"\n\n------------------------------------------------")
  print(f"                  {Player_Name} HP: {HP_player}")
  print(f"------------------------------------------------")
    
  time.sleep(0.5)
  print("\n------------------------------------------------")

  time.sleep(0.5)
  print(f"                  WEAPON LIST: ")

  time.sleep(0.5)
  print("------------------------------------------------")

  # import the previous varaible values into the current function 
  Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Player_Weapons()

  for i in range(0, len(Weapon_List)):
     
    Numerical_Order += 1
    Weapon_Names = Weapon_List[i]

    print(f"\n{Weapon_Names} [{Numerical_Order}]")

  print("\n------------------------------------------------")
  
  return HP_player, Numerical_Order, Dodge_Attack, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded

#-----------------------------------------------------------------------------------------------------
# JOURNEYS  
#-----------------------------------------------------------------------------------------------------

def Start_Journey_1(Input_Validation):

  clear_colour()
  Trees_Path_Art()

  time.sleep(3)
  print("\nYou continue to wander through the trees, birds chirp, leaves blow, a Postal dude has arrived... ")

  time.sleep(2)
  Postal_Dude_Art()
  print(f"\nPostal dude (HP: {Postal_dude_HP}): This place ain't for foreigners like you {Player_Name}, Get outta here or you're gonna have an unpleasant time.")
  
  while Input_Validation == None:
    time.sleep(2)
    flee_detector = input("\nFight or Flight? [Fight - Flight]: ")

    # if the player is a coward exit the program 
    if flee_detector.lower() == "flight":

      Input_Validation = False
      print("\nYou ran away, you coward! We can't continue in a scenario like this! grow up.")
      exit()
    
    elif flee_detector.lower() == "fight":
      
      Input_Validation = False
      time.sleep(3)
      print("\nYou have angered the Postal dude, you also seem to be bamboozled, but nothing is getting in the way of curing your curse! will you come out of this alive?")
    
    else: 
      print("\nPlease enter a valid input!")

  return

def Start_Journey_2(Input_Validation, Rasputin_Art):

  clear_colour()
  Neighbourhood_Path_Art()
  
  print("\nYou arrived at the neighbourhood. It seems awfully quiet for a busy morning at 13:15. Oh..? At least one person is walking on the curb.")
  
  time.sleep(2)
  print(f"\nRasputin (HP: {Rasputin_HP}): Hey man! watch where you're going you freaking pinko!")
  
  while Input_Validation == None:
    time.sleep(2)
    flee_detector = input("\nFight or Flight? [Fight - Flight]: ")
 
    if flee_detector.lower() == "flight":

      Input_Validation = False
      print("\nYou made a good choice my friend, you both saved yourself and other people from a potential mass murder...")
      exit()
    
    elif flee_detector.lower() == "fight":
      
      Input_Validation = False
      time.sleep(3)

      Rasputin_Art()
      print(f"\nRasputin (HP: {Rasputin_HP}): I will kill you with the blood of my sickle just as the founding fathers intended...")
    
    else: 
      print("\nPlease enter a valid input!")
      
  return Input_Validation

#-----------------------------------------------------------------------------------------------------
# COMBAT SYSTEMS JOURNEY 1  
#-----------------------------------------------------------------------------------------------------

def Postal_Dude_Fight(HP_player, Postal_dude_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded):

  while Postal_dude_HP > Death or HP_player > Death and End_Combat == False:
    
    # import the variables returned from previous functions to this current function 
    HP_player, Weapon_List, Dodge_Attack, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Players_turn(HP_player)
    Weapon_Selection, Description_Selection = Postal_Dudes_Turn() 
    
    print(f"\n\n------------------------------------------------")
    print(f"              Postal Dude HP: {Postal_dude_HP}")
    print(f"------------------------------------------------")

    Weapon_Choice = int(input("\nEnter the weapon choice you want to use! [choose by entering 1 - 4]: "))

    if Weapon_Choice == 1 and Dodge_Attack != 1:
      
      Melee_Attack_Icon()

      Postal_dude_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nPostal dude has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 1 and Dodge_Attack == 1:
    
      Melee_Attack_Icon()

      Postal_dude_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")

      print(f"\nPostal dude has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 2 and Dodge_Attack != 1:
            
      Incantation_Icon_Art()

      Postal_dude_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} casted the Glinted Zweihander sorcery and dealt {Glinted_Zweihander} damage! ")

      HP_player -= Weapon_Selection
      print(f"\nPostal dude has {Description_Selection} and dealt {Weapon_Selection} damage!")
      
      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 2 and Dodge_Attack == 1:
      
      Incantation_Icon_Art()

      Postal_dude_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Glinted_Zweihander} damage! ")

      print(f"\nPostal dude has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 3 and Dodge_Attack != 1: 
            
      Incantation_Icon_Art()

      Postal_dude_HP -= Lightning_Strike
      print(f"\n{Player_Name} struck their lightning bolt incanation and dealt {Lightning_Strike} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nPostal dude has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 3 and Dodge_Attack == 1:
      
      Incantation_Icon_Art()

      Postal_dude_HP -= Lightning_Strike
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Lightning_Strike} damage! ")

      print(f"\nPostal dude has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()
  
    elif Weapon_Choice == 4:
      
      Shield_Icon_Art()

      print(f"\nPostal dude has {Description_Selection} and dealt {Weapon_Selection} damage!")

      New_Damage = Weapon_Selection - (Weapon_Selection * Block)
      New_Damage_Rounded = round(New_Damage, 0)
      HP_player -= New_Damage_Rounded

      print(f"\n{Player_Name} used Block and has negated {Block_Percentage_Rounded}% of Postal Dude's damage! (damage now dealt: {New_Damage_Rounded}).")

      time.sleep(3)
      clear_terminal()

    else: 
      print("\nPlease enter a valid input!")
          
    if Postal_dude_HP <= Death: 
      End_Combat = True
      HP_player += Heal_player

      time.sleep(3)
      print(f"\nPostal Dude (HP: {Postal_dude_HP}): but what did I do to deserve this...?")
      time.sleep(5)
      print(f"\nThe fight concludes with {Player_Name} defeating the postal dude and continues to venture through the woods... (HP awarded: {Heal_player} new HP: {HP_player}).")
      time.sleep(4)
      clear_terminal()


    elif HP_player <= Death: 
      End_Combat = True

      time.sleep(3)
      print(f"\n{Player_Name} (HP: {HP_player}) ah, my curse... permenant... i've met my match... ")
      time.sleep(5)
      print(f"\nThe fight concludes with {Player_Name}'s lifeless body bleeding on the ground endlessly. (how the hell did you die to a postal dude????).")
      exit()
     
  return HP_player

def Sakuya_Fight(HP_player, Sakuya_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded):

  while Sakuya_HP > Death or HP_player > Death and End_Combat == False:
    
    # import the variables returned from previous functions to this current function 
    HP_player, Weapon_List, Dodge_Attack, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Players_turn(HP_player)
    Weapon_Selection, Description_Selection = Sakuyas_Turn() 
    
    print(f"\n\n------------------------------------------------")
    print(f"                Sakuya HP: {Sakuya_HP}")
    print(f"------------------------------------------------")

    Weapon_Choice = int(input("\nEnter the weapon choice you want to use! [choose by entering 1 - 4]: "))

    if Weapon_Choice == 1 and Dodge_Attack != 1:
            
      Melee_Attack_Icon()

      Sakuya_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nSakuya has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 1 and Dodge_Attack == 1:
      
      Melee_Attack_Icon()

      Sakuya_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")

      print(f"\nSakuya has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 2 and Dodge_Attack != 1:
            
      Incantation_Icon_Art()

      Sakuya_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} casted the Glinted Zweihander sorcery and dealt {Glinted_Zweihander} damage! ")

      HP_player -= Weapon_Selection
      print(f"\nSakuya has {Description_Selection} and dealt {Weapon_Selection} damage!")
      
      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 2 and Dodge_Attack == 1:
      
      Incantation_Icon_Art()

      Sakuya_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Glinted_Zweihander} damage! ")

      print(f"\nSakuya has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 3 and Dodge_Attack != 1: 
            
      Incantation_Icon_Art()

      Sakuya_HP -= Lightning_Strike
      print(f"\n{Player_Name} struck their lightning bolt incanation and dealt {Lightning_Strike} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nSakuya has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 3 and Dodge_Attack == 1:
      
      Incantation_Icon_Art()

      Sakuya_HP -= Lightning_Strike
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Lightning_Strike} damage! ")

      print(f"\nSakuya has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()
  
    elif Weapon_Choice == 4:
      
      Shield_Icon_Art()

      print(f"\nSakuya has {Description_Selection} and dealt {Weapon_Selection} damage!")

      New_Damage = Weapon_Selection - (Weapon_Selection * Block)
      New_Damage_Rounded = round(New_Damage, 0)
      HP_player -= New_Damage_Rounded

      print(f"\n{Player_Name} used Block and has negated {Block_Percentage_Rounded}% of Sakuya's damage! (damage now dealt: {New_Damage_Rounded}).")

      time.sleep(3)
      clear_terminal()

    else: 
      print("\nPlease enter a valid input!")
      
    if Sakuya_HP <= Death: 
      End_Combat = True
      HP_player += Heal_player

      time.sleep(3)
      print(f"\nSakuya (HP: {Sakuya_HP}): Perhaps master shall take care of this.. ")
      time.sleep(5)
      print(f"\nThe fight concludes with {Player_Name} defeating Sakuya and continues to venture through the woods... (HP awarded: {Heal_player} new HP: {HP_player}).")
    
    elif HP_player <= Death: 
      End_Combat = True

      time.sleep(3)
      print(f"\n{Player_Name} (HP: {HP_player}) ah, my curse... permenant... i've met my match... ")
      time.sleep(5)
      print(f"\nThe fight concludes with {Player_Name}'s lifeless body bleeding on the clean marble ground endlessly.")
      exit()
     
  return HP_player

def Zenith_Fight(HP_player, Zenith_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded):

  while Zenith_HP > Death or HP_player > Death and End_Combat == False:
    
    # import the variables returned from previous functions to this current function 
    HP_player, Weapon_List, Dodge_Attack, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Players_turn(HP_player)
    Weapon_Selection, Description_Selection = Zeniths_Turn() 
    
    print(f"\n\n------------------------------------------------")
    print(f"                Zenith HP: {Zenith_HP}")
    print(f"------------------------------------------------")

    Weapon_Choice = int(input("\nEnter the weapon choice you want to use! [choose by entering 1 - 4]: "))

    if Weapon_Choice == 1 and Dodge_Attack != 1:
            
      Melee_Attack_Icon()

      Zenith_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nZenith has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 1 and Dodge_Attack == 1:
      
      Melee_Attack_Icon()

      Zenith_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")

      print(f"\nZenith has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 2 and Dodge_Attack != 1:
            
      Incantation_Icon_Art()

      Zenith_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} casted the Glinted Zweihander sorcery and dealt {Glinted_Zweihander} damage! ")

      HP_player -= Weapon_Selection
      print(f"\nZenith has {Description_Selection} and dealt {Weapon_Selection} damage!")
      
      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 2 and Dodge_Attack == 1:
      
      Incantation_Icon_Art()

      Zenith_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Glinted_Zweihander} damage! ")

      print(f"\nZenith has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 3 and Dodge_Attack != 1: 
            
      Incantation_Icon_Art()

      Zenith_HP -= Lightning_Strike
      print(f"\n{Player_Name} struck their lightning bolt incanation and dealt {Lightning_Strike} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nZenith has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 3 and Dodge_Attack == 1:
      
      Incantation_Icon_Art()

      Zenith_HP -= Lightning_Strike
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Lightning_Strike} damage! ")

      print(f"\nZenith has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()
  
    elif Weapon_Choice == 4:
      
      Shield_Icon_Art()

      print(f"\nZenith has {Description_Selection} and dealt {Weapon_Selection} damage!")

      New_Damage = Weapon_Selection - (Weapon_Selection * Block)
      New_Damage_Rounded = round(New_Damage, 0)
      HP_player -= New_Damage_Rounded

      print(f"\n{Player_Name} used Block and has negated {Block_Percentage_Rounded}% of Zenith's damage! (damage now dealt: {New_Damage_Rounded}).")

      time.sleep(3)
      clear_terminal()

    else: 
      print("\nPlease enter a valid input!")
      
    if Zenith_HP <= Death: 
      End_Combat = True
      HP_player += Heal_player

      time.sleep(3)
      print(f"\nZenith (HP: {Zenith_HP}): ah my legacy fades... the shackles attached to  my arms dissolved traveler, your strength befits a throne make great use of it...")
      time.sleep(5)
      print(f"\nThe fight concludes with {Player_Name} defeating Zenith and wanders through the cave further... (HP awarded: {Heal_player} new HP: {HP_player}).")
    
    elif HP_player <= Death: 
      End_Combat = True

      time.sleep(3)
      print(f"\n{Player_Name} (HP: {HP_player}) ah, my curse... permenant... i've met my match... ")
      time.sleep(5)
      print(f"\nThe fight concludes with {Player_Name}'s lifeless body bleeding on the harsh spiky ground endlessly.")
      exit()
     
  return HP_player
  
def Eric_Fight(HP_player, Eric_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded):

  while Eric_HP > Death or HP_player > Death and End_Combat == False:
      
      # import the variables returned from previous functions to this current function 
      HP_player, Weapon_List, Dodge_Attack, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Players_turn(HP_player)
      Weapon_Selection, Description_Selection = Erics_Turn()
      
      print(f"\n\n------------------------------------------------")
      print(f"                Eric HP: {Eric_HP}")
      print(f"------------------------------------------------")

      Weapon_Choice = int(input("\nenter the weapon choice you want to use! [choose by entering 1 - 4]: "))

      if Weapon_Choice == 1 and Dodge_Attack != 1:
                
        Melee_Attack_Icon()

        Eric_HP -= Death_Hunt_Sickle
        print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")
        
        HP_player -= Weapon_Selection
        print(f"\nEric has {Description_Selection} and dealt {Weapon_Selection} damage!")

        time.sleep(3)
        clear_terminal()

      elif Weapon_Choice == 1 and Dodge_Attack == 1:
        
        Melee_Attack_Icon()

        Eric_HP -= Death_Hunt_Sickle
        print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")

        print(f"\nEric has {Description_Selection} however, it missed! ")
        
        time.sleep(3)
        clear_terminal()

      elif Weapon_Choice == 2 and Dodge_Attack != 1:
                
        Incantation_Icon_Art()

        Eric_HP -= Glinted_Zweihander
        print(f"\n{Player_Name} casted the Glinted Zweihander sorcery and dealt {Glinted_Zweihander} damage! ")

        HP_player -= Weapon_Selection
        print(f"\nEric has {Description_Selection} and dealt {Weapon_Selection} damage!")
        
        time.sleep(3)
        clear_terminal()
      
      elif Weapon_Choice == 2 and Dodge_Attack == 1:
        
        Incantation_Icon_Art()

        Eric_HP -= Glinted_Zweihander
        print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Glinted_Zweihander} damage! ")

        print(f"\nEric has {Description_Selection} however, it missed! ")
        
        time.sleep(3)
        clear_terminal()

      elif Weapon_Choice == 3 and Dodge_Attack != 1: 
                        
        Incantation_Icon_Art()

        Eric_HP -= Lightning_Strike
        print(f"\n{Player_Name} struck their lightning bolt incanation and dealt {Lightning_Strike} damage! ")
        
        HP_player -= Weapon_Selection
        print(f"\nEric has {Description_Selection} and dealt {Weapon_Selection} damage!")

        time.sleep(3)
        clear_terminal()
      
      elif Weapon_Choice == 3 and Dodge_Attack == 1:
        
        Incantation_Icon_Art()

        Eric_HP -= Lightning_Strike
        print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Lightning_Strike} damage! ")

        print(f"\nEric has {Description_Selection} however, it missed! ")
        
        time.sleep(3)
        clear_terminal()
    
      elif Weapon_Choice == 4:
        
        Shield_Icon_Art()

        print(f"\nEric has {Description_Selection} and dealt {Weapon_Selection} damage!")

        New_Damage = Weapon_Selection - (Weapon_Selection * Block)
        New_Damage_Rounded = round(New_Damage, 0)
        HP_player -= New_Damage_Rounded

        print(f"\n{Player_Name} used Block and has negated {Block_Percentage_Rounded}% of Eric's damage! (damage now dealt: {New_Damage_Rounded})")

        time.sleep(3)
        clear_terminal()

      else: 
        print("\nPlease enter a valid input!")
        
      if Eric_HP <= Death: 
        End_Combat = True
        HP_player += Heal_player

        time.sleep(3)
        print(f"\nEric (HP: {Eric_HP}): I know in my very mind and soul that you {Player_Name}, are not fit to what it takes to befit a crown...")
        time.sleep(5)
        print("\nAs Eric's lifeless body bleeds on the ground the player found a potion of healing perhaps this is enough to defeat a god..?")
        time.sleep(5)
        print(f"\nThe fight concludes with {Player_Name} walking up the deepslated steps for an eternity (HP awarded: {Heal_player} new HP: {HP_player})")
        
      elif HP_player <= Death: 
        End_Combat = True

        time.sleep(3)
        print(f"\n{Player_Name} (HP: {HP_player}) ah, my curse... permenant... i've met my match... ")
        time.sleep(5)
        print(f"\nThe fight concludes with {Player_Name}'s lifeless body being chucked to the endless abyss...")
        exit()

  return HP_player

def RNGesus_Fight(HP_player, RNGesus_HP, Emergancy_Heal, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded):

  Potion_Activation = True
  Weapon_List.append("Drink health potion")

  while RNGesus_HP > Death or HP_player > Death and End_Combat == False:
      
      # import the variables returned from previous functions to this current function 
      HP_player, Weapon_List, Dodge_Attack, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Players_turn(HP_player)
      Weapon_Selection, Description_Selection = RNGesus_Turn()

      print(f"\n\n------------------------------------------------")
      print(f"                RNGesus HP: {RNGesus_HP}")
      print(f"------------------------------------------------")

      Weapon_Choice = int(input(f"\nenter the weapon/consumable choice you want to use! [choose by entering 1 - 5]: "))

      if Weapon_Choice == 1 and Dodge_Attack != 1:
                
        Melee_Attack_Icon()

        RNGesus_HP -= Death_Hunt_Sickle
        print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")
        
        HP_player -= Weapon_Selection
        print(f"\nRNGesus has {Description_Selection} and dealt {Weapon_Selection} damage!")

        time.sleep(3)
        clear_terminal()

      elif Weapon_Choice == 1 and Dodge_Attack == 1:
        
        Melee_Attack_Icon()

        RNGesus_HP -= Death_Hunt_Sickle
        print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")

        print(f"\nRNGesus has {Description_Selection} however, it missed! ")
        
        time.sleep(3)
        clear_terminal()

      elif Weapon_Choice == 2 and Dodge_Attack != 1:
                
        Incantation_Icon_Art()

        RNGesus_HP -= Glinted_Zweihander
        print(f"\n{Player_Name} casted the Glinted Zweihander sorcery and dealt {Glinted_Zweihander} damage! ")

        HP_player -= Weapon_Selection
        print(f"\nRNGesus has {Description_Selection} and dealt {Weapon_Selection} damage!")
        
        time.sleep(3)
        clear_terminal()
      
      elif Weapon_Choice == 2 and Dodge_Attack == 1:
        
        Incantation_Icon_Art()

        RNGesus_HP -= Glinted_Zweihander
        print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Glinted_Zweihander} damage! ")

        print(f"\nRNGesus has {Description_Selection} however, it missed! ")
        
        time.sleep(3)
        clear_terminal()

      elif Weapon_Choice == 3 and Dodge_Attack != 1: 
                
        Incantation_Icon_Art()

        RNGesus_HP -= Lightning_Strike
        print(f"\n{Player_Name} struck their lightning bolt incanation and dealt {Lightning_Strike} damage! ")
        
        HP_player -= Weapon_Selection
        print(f"\nRNGesus has {Description_Selection} and dealt {Weapon_Selection} damage!")

        time.sleep(3)
        clear_terminal()
      
      elif Weapon_Choice == 3 and Dodge_Attack == 1:
        
        Incantation_Icon_Art()

        RNGesus_HP -= Lightning_Strike
        print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Lightning_Strike} damage! ")

        print(f"\nRNGesus has {Description_Selection} however, it missed! ")
        
        time.sleep(3)
        clear_terminal()
    
      elif Weapon_Choice == 4:
        
        Shield_Icon_Art()

        print(f"\nRNGesus has {Description_Selection} and dealt {Weapon_Selection} damage!")

        New_Damage = Weapon_Selection - (Weapon_Selection * Block)
        New_Damage_Rounded = round(New_Damage, 0)
        HP_player -= New_Damage_Rounded

        print(f"\n{Player_Name} used Block and has negated {Block_Percentage_Rounded}% of RNGesus's damage! (damage now dealt: {New_Damage_Rounded})")

        time.sleep(3)
        clear_terminal()
      
      elif Weapon_Choice == 5 and Potion_Activation == True:
                
        Potion_Activation = None

        Emergancy_Heal = random.randint(85, 170)
        Potion_Health_Art()
        
        HP_player += Emergancy_Heal
        print(f"\n{Player_Name} has drank the health potion losing its use and gained {Emergancy_Heal} Health!")

        time.sleep(3)
        clear_terminal()
      
      elif Weapon_Choice == 5 and Potion_Activation == None:
        
        Potion_Display = False
        print("\nsorry but you already used the potion!")
      
      else: 
        print("\nPlease enter a valid input!")
       
      if RNGesus_HP <= Death: 
        End_Combat = True
        HP_player += Heal_player

        time.sleep(3)
        print(f"\nRNGesus (HP: {RNGesus_HP}): but why..? do you truly believe this old system will suffice for the next decade down the line?")
        time.sleep(5)
        print("\nMy crown befits your head please reconsider your decisions the status quo must be broken... at least I will leave as a worthy successor...")
        time.sleep(5)
        print(f"\nThe fight concludes with {Player_Name} walking up the deepslated steps for an eternity (HP awarded: {Heal_player} new HP: {HP_player})")
      
      elif HP_player <= Death: 
        End_Combat = True

        time.sleep(3)
        print(f"\n{Player_Name} (HP: {HP_player}) ah, my curse... permenant... i've met my match... ")
        time.sleep(5)
        print(f"\nThe fight concludes with {Player_Name}'s lifeless body being chucked to the endless abyss...")
        exit()

  return HP_player


#-----------------------------------------------------------------------------------------------------
# COMBAT SYSTEMS JOURNEY 2 
#-----------------------------------------------------------------------------------------------------

def Rasputin_Fight(HP_player, Rasputin_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded):

  while Rasputin_HP > Death or HP_player > Death and End_Combat == False:
    
    # import the variables returned from previous functions to this current function 
    HP_player,  Numerical_Order, Dodge_Attack, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Players_turn(HP_player)
    Weapon_Selection, Description_Selection = Rasputins_Turn() 
    
    print(f"\n\n------------------------------------------------")
    print(f"              Rasputin HP: {Rasputin_HP}")
    print(f"------------------------------------------------")

    Weapon_Choice = int(input("\nenter the weapon choice you want to use! [choose by entering 1 - 4]: "))

    if Weapon_Choice == 1 and Dodge_Attack != 1:

      Melee_Attack_Icon()

      Rasputin_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nRasputin has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 1 and Dodge_Attack == 1:
      Melee_Attack_Icon()

      Rasputin_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")

      print(f"\nRasputin has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 2 and Dodge_Attack != 1:
      
      Incantation_Icon_Art()

      Rasputin_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} casted the Glinted Zweihander sorcery and dealt {Glinted_Zweihander} damage! ")

      HP_player -= Weapon_Selection
      print(f"\nRasputin has {Description_Selection} and dealt {Weapon_Selection} damage!")
      
      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 2 and Dodge_Attack == 1:
      Incantation_Icon_Art()

      Rasputin_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Glinted_Zweihander} damage! ")

      print(f"\nRasputin has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 3 and Dodge_Attack != 1: 
      
      Incantation_Icon_Art()

      Rasputin_HP -= Lightning_Strike
      print(f"\n{Player_Name} struck their lightning bolt incanation and dealt {Lightning_Strike} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nRasputin has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 3 and Dodge_Attack == 1:
      Incantation_Icon_Art()

      Rasputin_HP -= Lightning_Strike
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Lightning_Strike} damage! ")

      print(f"\nRasputin has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()
  
    elif Weapon_Choice == 4:
      Shield_Icon_Art()

      print(f"\nRasputin has {Description_Selection} and dealt {Weapon_Selection} damage!")

      New_Damage = Weapon_Selection - (Weapon_Selection * Block)
      New_Damage_Rounded = round(New_Damage, 0)
      HP_player -= New_Damage_Rounded

      print(f"\n{Player_Name} used Block and has negated {Block_Percentage_Rounded}% of Rasputin's damage! (damage now dealt: {New_Damage_Rounded})")

      time.sleep(3)
      clear_terminal()
    
    else: 
      print("please enter a valid input!")
  
    if Rasputin_HP <= Death: 
      End_Combat = True
      HP_player += Heal_player

      time.sleep(3)
      print(f"\nRasputin (HP: {Rasputin_HP}) none shall claim the soviet legacy!!! ")
      time.sleep(5)
      print(f"\nThe fight concludes with {Player_Name} defeating Rasputin and wanders around the neighbourhood... (HP awarded: {Heal_player} new HP: {HP_player})")
      time.sleep(4)

    elif HP_player <= Death: 
      End_Combat = True

      time.sleep(3)
      print(f"\n{Player_Name} (HP: {HP_player}) ah, my curse... permenant... i've met my match... ")
      time.sleep(5)
      print(f"\nThe fight concludes with {Player_Name}'s lifeless body bleeding on the ground endlessly. (how the hell did you die to Rasputin????)")
      exit()

  return HP_player

def Iku_Blackrock_Fight(HP_player, Iku_Blackrock_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded):

  while Iku_Blackrock_HP > Death or HP_player > Death and End_Combat == False:
    
    # import the variables returned from previous functions to this current function 
    HP_player, Numerical_Order, Dodge_Attack, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Players_turn(HP_player)
    Weapon_Selection, Description_Selection = Iku_Blackrocks_Turn() 
    
    print(f"\n\n------------------------------------------------")
    print(f"              Iku Blackrock HP: {Iku_Blackrock_HP}")
    print(f"------------------------------------------------")

    Weapon_Choice = int(input("\nenter the weapon choice you want to use! [choose by entering 1 - 4]: "))

    if Weapon_Choice == 1 and Dodge_Attack != 1:

      Melee_Attack_Icon()

      Iku_Blackrock_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nIku Blackrock has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 1 and Dodge_Attack == 1:
      Melee_Attack_Icon()

      Iku_Blackrock_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")

      print(f"\nIku Blackrock has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 2 and Dodge_Attack != 1:
      
      Incantation_Icon_Art()

      Iku_Blackrock_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} casted the Glinted Zweihander sorcery and dealt {Glinted_Zweihander} damage! ")

      HP_player -= Weapon_Selection
      print(f"\nIku Blackrock has {Description_Selection} and dealt {Weapon_Selection} damage!")
      
      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 2 and Dodge_Attack == 1:
      Incantation_Icon_Art()

      Iku_Blackrock_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Glinted_Zweihander} damage! ")

      print(f"\nIku Blackrock has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 3 and Dodge_Attack != 1: 
      
      Incantation_Icon_Art()

      Iku_Blackrock_HP -= Lightning_Strike
      print(f"\n{Player_Name} struck their lightning bolt incanation and dealt {Lightning_Strike} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nIku Blackrock has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 3 and Dodge_Attack == 1:
      Incantation_Icon_Art()

      Iku_Blackrock_HP -= Lightning_Strike
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Lightning_Strike} damage! ")

      print(f"\nIku Blackrock has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()
  
    elif Weapon_Choice == 4:
      Shield_Icon_Art()

      print(f"\nIku Blackrock has {Description_Selection} and dealt {Weapon_Selection} damage!")

      New_Damage = Weapon_Selection - (Weapon_Selection * Block)
      New_Damage_Rounded = round(New_Damage, 0)
      HP_player -= New_Damage_Rounded

      print(f"\n{Player_Name} used Block and has negated {Block_Percentage_Rounded}% of Iku Blackrock's damage! (damage now dealt: {New_Damage_Rounded})")

      time.sleep(3)
      clear_terminal()
    
    else: 
      print("please enter a valid input!")
  
    if Iku_Blackrock_HP <= Death: 
      End_Combat = True
      HP_player += Heal_player

      time.sleep(3)
      print(f"\nIku Blackrock (HP: {Iku_Blackrock_HP}) you are nothing but a fool dont say I didnt warn you... ")
      time.sleep(5)
      print(f"\nThe fight concludes with {Player_Name} defeating Iku Blackrock and wanders around the alleyway... (HP awarded: {Heal_player} new HP: {HP_player}).")
      time.sleep(4)

    elif HP_player <= Death: 
      End_Combat = True

      time.sleep(3)
      print(f"\n{Player_Name} (HP: {HP_player}) ah, my curse... permenant... i've met my match...")
      time.sleep(5)
      print(f"\nThe fight concludes with {Player_Name}'s lifeless body bleeding on the new york city ground with vermins nibbling at their corpse.")
      exit()

  return HP_player

def Slave_Knight_Fight(HP_player,  Slave_Knight_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded):

  while Slave_Knight_HP > Death or HP_player > Death and End_Combat == False:
    
    # import the variables returned from previous functions to this current function 
    HP_player, Numerical_Order, Dodge_Attack, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Players_turn(HP_player)
    Weapon_Selection, Description_Selection = Servant_Knight_Turn() 
    
    print(f"\n\n------------------------------------------------")
    print(f"              Servant Knight HP: {Slave_Knight_HP}")
    print(f"------------------------------------------------")

    Weapon_Choice = int(input("\nenter the weapon choice you want to use! [choose by entering 1 - 4]: "))

    if Weapon_Choice == 1 and Dodge_Attack != 1:

      Melee_Attack_Icon()

      Slave_Knight_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nServant Knight has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 1 and Dodge_Attack == 1:
      Melee_Attack_Icon()

      Slave_Knight_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")

      print(f"\nServant Knight has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 2 and Dodge_Attack != 1:
      
      Incantation_Icon_Art()

      Slave_Knight_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} casted the Glinted Zweihander sorcery and dealt {Glinted_Zweihander} damage! ")

      HP_player -= Weapon_Selection
      print(f"\nServant Knight has {Description_Selection} and dealt {Weapon_Selection} damage!")
      
      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 2 and Dodge_Attack == 1:
      Incantation_Icon_Art()

      Slave_Knight_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Glinted_Zweihander} damage! ")

      print(f"\nServant Knight has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 3 and Dodge_Attack != 1: 
      
      Incantation_Icon_Art()

      Slave_Knight_HP -= Lightning_Strike
      print(f"\n{Player_Name} struck their lightning bolt incanation and dealt {Lightning_Strike} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nServant Knight has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 3 and Dodge_Attack == 1:
      Incantation_Icon_Art()

      Slave_Knight_HP -= Lightning_Strike
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Lightning_Strike} damage! ")

      print(f"\nnServant Knight has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()
  
    elif Weapon_Choice == 4:
      Shield_Icon_Art()

      print(f"\nServant Knight has {Description_Selection} and dealt {Weapon_Selection} damage!")

      New_Damage = Weapon_Selection - (Weapon_Selection * Block)
      New_Damage_Rounded = round(New_Damage, 0)
      HP_player -= New_Damage_Rounded

      print(f"\n{Player_Name} used Block and has negated {Block_Percentage_Rounded}% of Slave Knight's damage! (damage now dealt: {New_Damage_Rounded})")

      time.sleep(3)
      clear_terminal()
    
    else: 
      print("please enter a valid input!")
  
    if Slave_Knight_HP <= Death: 
      End_Combat = True
      HP_player += Heal_player

      time.sleep(5)
      print(f"\nSlave Knight (HP: {Slave_Knight_HP}): nghhhh brave traveler, you are making a big mistake, death inevitable... ")
      time.sleep(3)
      print(f"\nThe fight concludes with {Player_Name} defeating the Slave Knight and continues to the swamp ahead (HP awarded: {Heal_player} new HP: {HP_player}).")
      time.sleep(4)

    elif HP_player <= Death: 
      End_Combat = True

      time.sleep(3)
      print(f"\n{Player_Name} (HP: {HP_player}) ah, my curse... permenant... i've met my match... ")
      time.sleep(5)
      print(f"\nThe fight concludes with {Player_Name}'s lifeless body bleeding in the stinky rancid swamp travelling to the water.")
      exit()

  return HP_player

def BloodDrinker_Rei_Fight(HP_player, BloodDrinker_Rei_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded):

  while BloodDrinker_Rei_HP > Death or HP_player > Death and End_Combat == False:
    
    # import the variables returned from previous functions to this current function 
    HP_player, Numerical_Order, Dodge_Attack, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Players_turn(HP_player)
    Weapon_Selection, Description_Selection = BloodDrinker_Reis_Turn() 
    
    print(f"\n\n------------------------------------------------")
    print(f"         BloodDrinker Rei's HP: {BloodDrinker_Rei_HP}")
    print(f"------------------------------------------------")

    Weapon_Choice = int(input("\nenter the weapon choice you want to use! [choose by entering 1 - 4]: "))

    if Weapon_Choice == 1 and Dodge_Attack != 1:

      Melee_Attack_Icon()

      BloodDrinker_Rei_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nBloodDrinker Rei has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 1 and Dodge_Attack == 1:
      Melee_Attack_Icon()

      BloodDrinker_Rei_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")

      print(f"\nBloodDrinker Rei has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 2 and Dodge_Attack != 1:
      
      Incantation_Icon_Art()

      BloodDrinker_Rei_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} casted the Glinted Zweihander sorcery and dealt {Glinted_Zweihander} damage! ")

      HP_player -= Weapon_Selection
      print(f"\nBloodDrinker Rei has {Description_Selection} and dealt {Weapon_Selection} damage!")
      
      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 2 and Dodge_Attack == 1:
      Incantation_Icon_Art()

      BloodDrinker_Rei_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Glinted_Zweihander} damage! ")

      print(f"\nBloodDrinker Rei has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 3 and Dodge_Attack != 1: 
      
      Incantation_Icon_Art()

      BloodDrinker_Rei_HP -= Lightning_Strike
      print(f"\n{Player_Name} struck their lightning bolt incanation and dealt {Lightning_Strike} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nBloodDrinker Rei has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 3 and Dodge_Attack == 1:
      Incantation_Icon_Art()

      BloodDrinker_Rei_HP -= Lightning_Strike
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Lightning_Strike} damage! ")

      print(f"\nBloodDrinker Rei has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()
  
    elif Weapon_Choice == 4:
      Shield_Icon_Art()

      print(f"\nBloodDrinker Rei has {Description_Selection} and dealt {Weapon_Selection} damage!")

      New_Damage = Weapon_Selection - (Weapon_Selection * Block)
      New_Damage_Rounded = round(New_Damage, 0)
      HP_player -= New_Damage_Rounded

      print(f"\n{Player_Name} used Block and has negated {Block_Percentage_Rounded}% of BloodDrinker Rei's damage! (damage now dealt: {New_Damage_Rounded}).")

      time.sleep(3)
      clear_terminal()
    
    else: 
      print("please enter a valid input!")
  
    if BloodDrinker_Rei_HP <= Death: 
      End_Combat = True
      HP_player += Heal_player

      time.sleep(3)
      print(f"\nBloodDrinker Rei (HP: {BloodDrinker_Rei_HP}) what are you trying to prove? how many have you killed to get here? did you even listen to them? I may fade but I sincerely wish you torturous death served on a silver platter. ")
      time.sleep(5)
      print(f"\nThe fight concludes with {Player_Name} defeating BloodDrinker Rei (HP awarded: {Heal_player} new HP: {HP_player}).")
      time.sleep(4)


    elif HP_player <= Death: 
      End_Combat = True

      time.sleep(3)
      print(f"\n{Player_Name} (HP: {HP_player}) ah, my curse... permenant... i've met my match... ")
      time.sleep(5)
      print(f"\nThe fight concludes with {Player_Name}'s lifeless body rolling to the swampy water discolouring the water endlessly.")
      exit()

  return HP_player

def Huby_Developer_Fight(HP_player, Huby_Developer_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded):

  while Huby_Developer_HP > Death or HP_player > Death and End_Combat == False:
    
    # import the variables returned from previous functions to this current function 
    HP_player,  Numerical_Order, Dodge_Attack, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Players_turn(HP_player)
    Weapon_Selection, Description_Selection = Huby_developers_Turn() 
    
    print(f"\n\n------------------------------------------------")
    print(f"              Huby Developer HP: ???????")
    print(f"\n           status: your bloody screwed!!")
    print(f"------------------------------------------------")

    Weapon_Choice = int(input("\nenter the weapon choice you want to use! [choose by entering 1 - 4]: "))

    if Weapon_Choice == 1 and Dodge_Attack != 1:

      Melee_Attack_Icon()

      Huby_Developer_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nHuby Developer has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 1 and Dodge_Attack == 1:
      Melee_Attack_Icon()

      Huby_Developer_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")

      print(f"\nHuby Developer has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 2 and Dodge_Attack != 1:
      
      Incantation_Icon_Art()

      Huby_Developer_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} casted the Glinted Zweihander sorcery and dealt {Glinted_Zweihander} damage! ")

      HP_player -= Weapon_Selection
      print(f"\nHuby Developer has {Description_Selection} and dealt {Weapon_Selection} damage!")
      
      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 2 and Dodge_Attack == 1:
      Incantation_Icon_Art()

      Huby_Developer_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Glinted_Zweihander} damage! ")

      print(f"\nHuby Developer has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 3 and Dodge_Attack != 1: 
      
      Incantation_Icon_Art()

      Huby_Developer_HP -= Lightning_Strike
      print(f"\n{Player_Name} struck their lightning bolt incanation and dealt {Lightning_Strike} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nHuby Developer has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 3 and Dodge_Attack == 1:
      Incantation_Icon_Art()

      Huby_Developer_HP -= Lightning_Strike
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Lightning_Strike} damage! ")

      print(f"\nHuby Developer has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()
  
    elif Weapon_Choice == 4:
      Shield_Icon_Art()

      print(f"\nHuby Developer has {Description_Selection} and dealt {Weapon_Selection} damage!")

      New_Damage = Weapon_Selection - (Weapon_Selection * Block)
      New_Damage_Rounded = round(New_Damage, 0)
      HP_player -= New_Damage_Rounded

      print(f"\n{Player_Name} used Block and has negated {Block_Percentage_Rounded}% of Huby Developer's damage! (damage now dealt: {New_Damage_Rounded})")

      time.sleep(3)
      clear_terminal()
    
    else: 
      print("please enter a valid input!")
  
    if Huby_Developer_HP <= Death: 
      End_Combat = True
      HP_player += Heal_player

      time.sleep(3)
      print(f"\nHuby Developer (HP: {Huby_Developer_HP}) you were clearly cheating you cheap player!")


    elif HP_player <= Death: 
      End_Combat = True

      time.sleep(3)
      print(f"\n{Player_Name} (HP: {HP_player}) ah, my curse... permenant... i've met my match... ")
      time.sleep(5)
      print("\nYou got demolished so hard your body didnt even have time to decompose it simply turned to dust in conclusion your extremely stubborn good job you recieved a garbage ending...")
      time.sleep(4)
      print("\nYou also killed innocent bystanders you got brutally murdered by the developer and you didnt even cure your curse...")
      exit()

  return HP_player  

#-----------------------------------------------------------------------------------------------------
# START GAME
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# Introduction
#-----------------------------------------------------------------------------------------------------

Introduction_Music()

intro_background_Art()

print("\nThe dice is rolling way too many ones, the weather is always rainy, you have been laid off from your job, but most importantly your luck reeks of misfortune... it's time to proclaim justice. Your journey begins now...")
time.sleep(5)

Player_Name = input("\nEnter your name: ")

print("\nYou proceed to seep your way to the trees encountering a neighbourhood on your arrival. Continue through the trees? or take a visit to the neighbourhood [Trees/Neighbourhood].")
time.sleep(2)

#-----------------------------------------------------------------------------------------------------
# End Introduction and start journey 
#-----------------------------------------------------------------------------------------------------

while Input_Validation == False: 

  Path_chosen = input("\nYour Path? [Trees/Neighbourhood]: ")
  
  # Player chooses trees path initiating journey 1
  if Path_chosen.lower() == "trees":

    Input_Validation = None

    time.sleep(2)
    clear_terminal()

    Start_Journey_1(Input_Validation)

    # load player weapons and start the first enemy fight 
    Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Player_Weapons()
    HP_player = Postal_Dude_Fight(HP_player, Postal_dude_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)

    Background_Music()

    # start sakuya fight  
    clear_colour()

    time.sleep(3.5)
    print(f"\nAfter wandering through the woods {Player_Name} suddenly stumbled upon a gothic mansion it seems unvacant.")

    # this art here is very likely to stretch out if you dont have a sizable monitor that fits it properly 
    Mansion_Art()
    time.sleep(6.5)
    
    time.sleep(3.5)
    print("\nOpening the heavy door, looking through the main hall sounds of walking can be heard atop the balcony. A mysterious figure appears...")
    
    time.sleep(3.5)
    Sakuya_Art()

    time.sleep(3.5)
    print(f"\nSakuya (HP: {Sakuya_HP}): I never knew master invited unwarranted visitors... ")
    time.sleep(3.5)
    print(f"\nSakuya (HP: {Sakuya_HP}): what do you say stranger, care for a sharp dance? ")

    Input_Validation == None

    while Input_Validation == None:

      User_Response = int(input("\nYour response? [1: gee I didnt know your 'master' hired body guards too] [2: out of my way I have stuff to do]: "))

      if User_Response == 1:
        
        Input_Validation = True
        print(f"\nSakuya (HP {Sakuya_HP}): ...")

        Enemy_Journey_1_Music()
        HP_player = Sakuya_Fight(HP_player, Sakuya_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)
      
      elif User_Response == 2:
        
        Input_Validation = True
        print(f"\nSakuya (HP {Sakuya_HP}): I simply wont allow that to happen.")

        Enemy_Journey_1_Music()
        HP_player = Sakuya_Fight(HP_player, Sakuya_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)
      
      else:
        print("Please enter a valid input!")


    time.sleep(3.5)
    clear_colour()
    time.sleep(3.5)
    clear_terminal()

    # Start the Zenith fight 

    Background_Music()

    time.sleep(5.5)
    print("\nAs the lifeless servant lays on the dirtless ground the player checks through the entire mansion however,")
    time.sleep(5.5)
    print("\nThe incarcerated souls faintly screaming nearby caught the player's attention and they investiageted further leading up to a door...")

    Door_To_Cave_Art()

    time.sleep(5.5)
    print("\nUpon opening the door a cave is revealed with no other enterance the player jumps down the smell of rotten flesh within previous travelers and there lies Zenith the reclaimer of succession...")

    time.sleep(7.5)
    clear_terminal()

    Zenith_Art()
    time.sleep(4.5)
    print(f"\nZenith (HP: {Zenith_HP}): ah, annother ignorant successor of wizardry bold of you to assume the invasion of my layer, what desire is being achived?")
    time.sleep(4.5)
    print(f"\nZenith (HP: {Zenith_HP}): vengence? diamonds? a broken home? whatever its you seek this may be your final destination none shall claim the title of control...")

    time.sleep(4.5)
    Enemy_Journey_1_Music()
    HP_player = Zenith_Fight(HP_player, Zenith_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)

    # start the Eric fight 
    Background_Music()

    time.sleep(4.5)
    print("\nThe incarcerated souls continue to scream but slowly tones down each iteration thankfully this cave has one enterance.")
    time.sleep(4.5)
    print("\nInvestigating the cave further the path leads to a stormy enviorment with a familiar face staring upon the deepslated stairs.")    
    time.sleep(4.5)
    print("\nHowever the player's footsteps broke the figures fixation and took notice...")

    time.sleep(3.5)
    clear_terminal()
    clear_colour()

    Eric_Art()
    time.sleep(4.5)
    print(f"\nEric (HP: {Eric_HP}): ah, {Player_Name}, I have not been informed of your existance for however long if your motivations align with mines im afraid I have to interfere with your ambitions.")
    time.sleep(4.5)
    print(f"\nEric (HP: {Eric_HP}): the title of control only belongs to one crown and you of all people should not possess it. Your level of reliability is a concern to behold leave now or face adversity.")


    while Input_Validation == True: 
      
      User_Response = int(input("\nYour response?: [1. what are you going to change that will benefit everyone?] [2. I dont think I can trust to make this decision]: "))
    
      if User_Response == 1: 
        
        Input_Validation = None
        
        print(f"\nEric (HP: {Eric_HP}): none of your business however I promise a millenium long policy that will affect everyone positively.")
        time.sleep(4.5)
        Enemy_Journey_1_Music()
        HP_player = Eric_Fight(HP_player, Eric_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)
      
      elif User_Response == 2:
        
        Input_Validation = None

        print(f"\nEric (HP: {Eric_HP}): neither can I yet we will fight in an empty hopeless world awaiting a miracle to shine through let it be I Eric the first Moon Knight.")
        time.sleep(4.5)
        Enemy_Journey_1_Music()
        HP_player = Eric_Fight(HP_player, Eric_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)
      
      else: 
        print("\nPlease enter a valid input!")
    
    # start final boss (RNGesus)
    Background_Music()

    Potion_Display = True

    time.sleep(5)
    clear_colour()
    clear_terminal()

    time.sleep(3)
    Stairs_To_Throne_Art()

    time.sleep(4.5)
    print("\nYou conclude this very area alone can lead to the root of your curse you mutter under your breath 'gosh why didnt they think to build some sort of elevator here?' ")
    time.sleep(6.5)
    print("\nAfter what felt centuries passing by ever so convinient enough to be an enemy awaiting a visitor of their throne resting upon a massive floating rock.")
    time.sleep(5.5)
    print("\nThe possibility of winning this battle tingles in your head but there is no turning back...")

    time.sleep(5.5)
    RNGesus_Art()

    print(f"\nRNGesus (HP: {RNGesus_HP}): you of all people is the last type I would anticipate the visitation either way none shall take the throne the harvest will prevail and I will be the luckiest of them all.")

    while Input_Validation == None:

      time.sleep(5)
      User_Response = int(input("\nYour response?: [1. my and others lives incredibly inconvinient either put an end to this or be granted death] [2. what even is your end goal when you harvest all luck?]: "))

      if User_Response == 1: 
        
        Input_Validation = False
        
        print(f"\nRNGesus (HP: {RNGesus_HP}): why would I help any of you? luck should be attained through perserverence and determination not by sheer randomness let my plans follow through and you get your share of the luck.")
        time.sleep(4.5)
        Enemy_Journey_1_Music()
        HP_player = RNGesus_Fight(HP_player, RNGesus_HP, Emergancy_Heal, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)
      
      elif User_Response == 2:
        
        Input_Validation = False

        print(f"\nRNGesus (HP: {RNGesus_HP}): I promise all a 10 century long proposal of luck being earned through perserverance and determination no person shall earn a bag of money for repeating a phrase let my plans follow through and luck as a system will be refined and will be ruled by action not words.")
        time.sleep(4.5)
        Enemy_Journey_1_Music()
        HP_player = RNGesus_Fight(HP_player, RNGesus_HP, Emergancy_Heal, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)
      
      else: 
        print("\nPlease enter a valid input!")
    
    # Player kills RNGesus concluding journey 1's ending depending on what option the player picked and exiting the game
    
    Outro_Music()

    clear_colour()
    Throne_Art()

    time.sleep(6)
    print("\nExploring the area leads to an obelisk with a wetstone blade nearby it seems that the obelisk is responsible for the policies implemented for the effects to take place...")
    time.sleep(4)
    print("\nYou grab the wetstone blade and read the last line while deciding what luck policy should be written.")
    
    while Input_Validation == False:

      time.sleep(4)
      User_Response = int(input("\nThese are your following options: [1. reinforce the old order and return the luck to everyone] [2. adapt the old order to include the aspect of enchanced luck for exerting effort] [3. completely abandon the old order to implement the previous successor's order]: "))

      if User_Response == 1: 
        
        Input_Validation = None
        
        time.sleep(4.5)
        print("\nAs the player finishes carving the policy onto the obelisk they drop the wetstone blade and returned home.")
        time.sleep(4.5)
        print("\nWith the incident resolved the world remains the same way it previously has however there was an opportunity to take some of the luck for your own gain...")

        print("\n-----------------------------------------------------------------------")
        print("\nEnding: Netural 1 (cmon man steal some luck for yourself will ya?)")
        print("\n-----------------------------------------------------------------------")

        exit()

      elif User_Response == 2:
        
        Input_Validation = None

        time.sleep(4.5)
        print("\nAs the player finishes carving the policy onto the oblisk they drop the wetstone blade and returned home with the incident resolved the world remains the same.")
        time.sleep(4.5)
        print("\nHowever your luck is echanced ten folds and now those who put the effort are recognized for it and are awarded proprotionally while any math with probability still function accordingly...")

        print("\n--------------------------------------------------------------------------")
        print("\nEnding: Good (not only are you considered king but everyone is happy!)")
        print("\n--------------------------------------------------------------------------")

        exit()
      
      elif User_Response == 3:

        
        Input_Validation = None

        time.sleep(4.5)
        print("\nAs the player finishes carving the policy onto the obelisk they drop the wetstone blade and returned home.")
        time.sleep(4.5)
        print("\nWith the incident being resolved however you have recieved unlimited luck and now only luck is granted to those with effort and math with probability cease to exist... ")

        print("\n------------------------------------------------------------------------------")
        print("\nEnding: Netural 2 (greedy are you now? now maths is a more confusing subject!)")
        print("\n------------------------------------------------------------------------------")

        exit()
      
      else: 
        print("\nPlease enter a valid input!")

  # Player chooses neighbourhood path initiating journey 2
  if Path_chosen.lower() == "neighbourhood":

    Input_Validation = None

    time.sleep(2)
    clear_terminal()
      
    Start_Journey_2(Input_Validation, Rasputin_Art)

    # load player weapons and start the first enemy fight 
    Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Player_Weapons()
    HP_player = Rasputin_Fight(HP_player, Rasputin_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)

    # start iku blackrock fight 
    Background_Music()

    clear_terminal()
    clear_colour()

    time.sleep(3.5)
    print("\nAfter the player defeats rasputin the player wanders the neighbourhood wearing the stolen ushanka from rasputins dead body when suddenly they discover an alleyway.")
    
    time.sleep(3.5)
    Alleyway_Art()

    time.sleep(3.5)
    print("\nPeaking the players interest they decided to wander through the suspiciously dangerous alleyway only to be confronted by a mysterious person with a trenchcoat.")
    
    time.sleep(3.5)
    clear_terminal()
    Iku_Blackrock_Art()

    time.sleep(3.5)
    print(f"\nIku Blackrock (HP: {Iku_Blackrock_HP}): hey, this aint a safe place for your kind turn back while you can otherwise this aint going to be pretty.")
    time.sleep(3.5)

    Input_Validation = False

    while Input_Validation == False: 

      User_Response = int(input("\nYour response?: [1. no I came to retrieve my luck not be cursed forever with bad luck] [2. yeah maybe this area isnt the root of my problem]: "))

      if User_Response == 1: 
        
        Input_Validation = None

        print(f"\nIku Blackrock (HP: {Iku_Blackrock_HP}): ah so stubborn you should put your foolish ambitions to rest it isnt too late...")
        Enemy_Journey_2_Music()
        HP_player = Iku_Blackrock_Fight(HP_player, Iku_Blackrock_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)

      elif User_Response == 2: 
        
        Input_Validation = None
  
        print(f"\nIku Blackrock (HP: {Iku_Blackrock_HP}): yeah thats more like it now scram before you get yourself killed.")
        time.sleep(3.5)
        print("\nThe player leaves the neighbourhood to try another potential path exiting the game as a result of this decision...")
        exit()

      else:
        print("\nPlease enter a valid input!")

    # start Slave Knight fight
    Background_Music()

    time.sleep(4)
    clear_terminal()
    clear_colour()

    time.sleep(3.5)
    print("\nAfter the player defeats Iku Blackrock they wandered further in the alleyway to find an odd glowing sign with unintelligible texts written allover it.")
    time.sleep(3.5)
    print("\nTouching it disoriented the player for a brief moment only to be taken to the swamps with an extra stroke of bad luck bubbling can be heard across one of the lakes merging a severely drenched Slave Knight.")
    
    time.sleep(3.5)
    Swamp_Art()
    clear_colour()
    time.sleep(7.5)

    clear_terminal()
    Slave_Knight_Art()

    time.sleep(3.5)
    print(f"\nSlave Knight (HP: {Slave_Knight_HP}): ah, you, there, dont know how you arrived no matter may you lend me your organs? for me myself and I.")

    while Input_Validation == None: 

      User_Response = int(input("\nYour response?: [1. how are you even still alive? you should be dead you know if I were you id count my days] [2. yeah no... im getting the hell out of here]: "))

      if User_Response == 1: 
        
        Input_Validation = False 
        
        print(f"\nSlave Knight (HP: {Slave_Knight_HP}): no question my body is as hollow as a teapot be so kind to let me harvest it all.")
        Enemy_Journey_2_Music()
        HP_player = Slave_Knight_Fight(HP_player, Slave_Knight_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)

      elif User_Response == 2:

        Input_Validation = False

        print("\nYou tried to run away but the slave knight teleported right infront of you leaving you with no other choice...")
        Enemy_Journey_2_Music()
        HP_player = Slave_Knight_Fight(HP_player, Slave_Knight_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)

      else: 
        print("\nPlease enter a valid input!")
    

    # start blooddrinker Rei fight
    Background_Music()

    time.sleep(4)
    clear_terminal()
    clear_colour()

    time.sleep(3.5)
    print(f"\n{Player_Name} (HP: {HP_player}): I want to go home badly I'm tired please let this be over with... ")
    time.sleep(3.5)
    print("\nThe blood flowing south east intensified only to be gathered in a pool of blood emerging a daunting terrifying humanoid wielding a heavily poisoned scythe...")

    BloodDrinker_Rei_Art()
    
    time.sleep(5)  
    print(f"\nBloodDrinker Rei (HP: {BloodDrinker_Rei_HP}): you called for death and death answered {Player_Name}, you killed my servant interrupting my plan its only fair to steal your existance.")
    time.sleep(5)
    print(f"\nBloodDrinker Rei (HP: {BloodDrinker_Rei_HP}): ever heard of the saying 'an eye for an eye a tooth for a tooth'? nevermind that your an atheist equally as ignorant as your kind a mere fool if you will now perish at once.")

    Enemy_Journey_2_Music()
    HP_player = BloodDrinker_Rei_Fight(HP_player, BloodDrinker_Rei_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)

    # start huby developer fight (scripted death)
    Bad_Ending_Outro_Music()

    time.sleep(4)
    clear_terminal()
    clear_colour()

    time.sleep(3.5)
    print("\nA summoning stone has appeared as a result of Rei's death the player gripped the stone getting ready to skim it across the lake nearby for fun to only be teleported to a foggy world.")
    time.sleep(5.5)
    print("\nThe player's throat clenches for its life bringing laboured breathing to the table this air is toxic they may have been telling the truth all along...")
    
    time.sleep(4.5)
    Huby_Developer_Art()

    time.sleep(5.5)
    print("\nHuby Developer (HP: ???): I would normally have a long drawn out monologue of calling you an dumb idiot stubborn moron but you wont even listen anyways, you are solely responsible for this.")

    time.sleep(5)
    HP_player = Huby_Developer_Fight(HP_player, Huby_Developer_HP, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)

  else:
    print("\nPlease enter a valid input!")