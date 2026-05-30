'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Type of work: School project 
Game Creation: 31/10/24
Game Completion: 05/03/25 (non-music version)
Developer Name: Huby
Name of game: PhantasmicRNG
Objective: traverse through the cruel world finding the cure of the permenant curse of luck
Game Type: interactive text-based, turn-based combat, adventure game 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Personal Notes: This project may be the biggest one I have made so far and will prove to be a big learning experience. As of writing this I predict
my project will go beyond 700 lines of code and can only hope for the best when making it. Also this program will be run on the fullscreen terminal 
this will hide the games code enchancing the experience and not expecting what will come next in each encounter. 
Another note id like to add all the assests such as sound music or any sort of media that I took will be given credit below. Anyways God speed and hope future me will revisit it.

Aftermath Notes (30/05/26): Future Huby here, this is the most yandere dev level of spaghetti code I have ever looked at in my life. I am so thankful that the combat and weapon generatio functions
can be all boiled down to a template with the exception of bosses and the player themseleves but having to navigate through 1k+ lines of pure repeated functions was hell on earth. 
OOP is king when it comes to tackling those kinds of problems and I dont need to say more as the code below shows themselves there are still a lot of improvements to be made in this 
entire process and future me may revisit it once more to implement futher changes but this is the biggest solution so far that eleminated a load of headaches. Last little note here
this game in its OOP form and its non OOP form can show future upcoming programmers the importance of using OOP concepts such as inheritence and when to use them if the size of a 
project is appropriate or not. 

INSTRUCTIONS: in order to play the game correctly with no errors you need to install 2 python modules this includes installing pygame and colorama 
pygame is used to play the audio required by the game and colorama is a module used to display colour to text and ascii art. 

NOTICE: when playing the game on a undesired screen size or not full-screening the terminal the ascii art being displayed could be messy and scrambled its also recommended to run this game under
Visual Studio Code however, feel free to use a text editor that best suits you and that supports the ascii art correctly. 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

CREDITS: 
https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20 [Website used to generate ASCII art for game title below]

https://kirilllive.github.io/ASCII_Art_Paint/ascii_paint.html [Website used to make ASCII art for icons, enemies etc]

https://emojicombos.com/south-park [Website used for grabbing Erik Cartman ascii art and Jesus from family guy ascii art]

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

# custom module i made to pull all the art from another python program to keep this script small 
import Ascii_Art as Ascii 

Player_Name = ""

POSTAL_DUDE_NAME = "Postal Dude"
SAKUYA_NAME = "Sakuya"
ZENITH_NAME = "Zenith"
ERIC_NAME = "Eric"
RNGESUS_NAME = "RNGesus"

RASPUTIN_NAME = "Rasputin"
IKU_BLACKROCK_NAME = "Iku Blackrock"
SERVANT_KNIGHT_NAME = "Slave Knight"
BLOODDRINKER_REI = "BloodDrinker Rei"
HUBY_DEVELOPER_NAME = "Huby"

# journey 1 Enemies HP
Postal_dude_HP = 115
Sakuya_HP = 165
Zenith_HP = 200
Eric_HP = 245
RNGesus_HP = 300

# journey 2 Enemies HP 

Rasputin_HP = 100
Iku_Blackrock_HP = 150
Servant_Knight_HP = 225
BloodDrinker_Rei_HP = 260
Huby_Developer_HP = 1000000

End_Combat = False
Input_Validation = False

HP_player = random.randint(185, 275)
Emergancy_Heal = random.randint(85, 170)

Death_Dialog = open("/home/hubyark/Downloads/RevampRNG/Death Dialog.txt")
PLAYER_DEATH_DIALOG_LIST = Death_Dialog.readlines()

# NOTE: split all of the character dialog into seperate arrays for their deaths and progression 
# also because eric has 3 lines of dialog combine 2 of them into one singular string with a new line escape sequence to make it only have 2 indexes 
# however the bosses of two journeys need to be a seperate functon as they have 5 attacks which breaks the typical character template that they could have used 

# last little thing too im too lazy to find a method of putting it all into a text file while also keeping the formatted strings functional so arrays will have to do for now lmfao 

POSTAL_DUDE_DEATH_DIALOG = [f"Postal Dude: but what did I do to deserve this...?", f"The fight concludes with {Player_Name} defeating the postal dude and continues to venture through the woods..."]
SAKUYA_DEATH_DIALOG = [f"Sakuya: Perhaps master shall take care of this...", f"The fight concludes with {Player_Name} defeating Sakuya and continues to venture through the woods..."]
ZENITH_DEATH_DIALOG = [f"Zenith: ah my legacy fades... the shackles attached to  my arms dissolved traveler, your strength befits a throne make great use of it...", f"The fight concludes with {Player_Name} defeating Zenith and wanders through the cave further..."]
ERIC_DEATH_DIALOG = [f"Eric: I know in my very mind and soul that you {Player_Name}, are not fit to what it takes to befit a crown... \n As Eric's lifeless body bleeds on the ground the player found a potion of healing perhaps this is enough to defeat a god..?", f"The fight concludes with {Player_Name} walking up the deepslated steps for an eternity"]

RASPUTIN_DEATH_DIALOG = [f"Rasputin: none shall claim the soviet legacy!!!", f"The fight concludes with {Player_Name} defeating Rasputin and wanders around the neighbourhood..."]
IKU_BLACKROCK_DEATH_DIALOG = [f"Iku Blackrock: you are nothing but a fool dont say I didnt warn you...", f"The fight concludes with {Player_Name} defeating Iku Blackrock and wanders around the alleyway..."]
SERVANT_KNIGHT_DEATH_DIALOG = [f"Slave Knight: nghhhh brave traveler, you are making a big mistake, death inevitable...", f"The fight concludes with {Player_Name} defeating the Slave Knight and continues to the swamp ahead"]
BLOODDRINKER_REI_DEATH_DIALOG = [f"BloodDrinker Rei: what are you trying to prove? how many have you killed to get here? did you even listen to them? I may fade but I sincerely wish you torturous death served on a silver platter.", f"The fight concludes with {Player_Name} defeating BloodDrinker Rei"]

# the universal OOP template made for every enemy character in the game for PhantasmicRNG
class Character_Template: 

  def __init__(self, WEAPON_MIN_1, WEAPON_MIN_2, WEAPON_MIN_3, WEAPON_MAX_1, WEAPON_MAX_2, WEAPON_MAX_3, WEAPON_TEXT_1, WEAPON_TEXT_2, WEAPON_TEXT_3, Character_Name, Enemy_HP, PLAYER_DEATH_DIALOG, ENEMY_DEATH_DIALOG):
    
    self.WEAPON_MIN_1 = WEAPON_MIN_1
    self.WEAPON_MIN_2 = WEAPON_MIN_2
    self.WEAPON_MIN_3 = WEAPON_MIN_3
    
    self.WEAPON_MAX_1 = WEAPON_MAX_1
    self.WEAPON_MAX_2 = WEAPON_MAX_2
    self.WEAPON_MAX_3 = WEAPON_MAX_3

    self.WEAPON_TEXT_1 = WEAPON_TEXT_1
    self.WEAPON_TEXT_2 = WEAPON_TEXT_2
    self.WEAPON_TEXT_3 = WEAPON_TEXT_3

    self.Enemy_HP = Enemy_HP
    self.ENEMY_DEATH_DIALOG = ENEMY_DEATH_DIALOG

    self.Character_Name = Character_Name
    self.PLAYER_DEATH_DIALOG = PLAYER_DEATH_DIALOG

    self.Weapon_1 = random.randint(WEAPON_MIN_1, WEAPON_MAX_1)
    self.Weapon_2 = random.randint(WEAPON_MIN_2, WEAPON_MAX_2)
    self.Weapon_3 = random.randint(WEAPON_MIN_3, WEAPON_MAX_3)

    self.Character_Random_Choices = random.randint(0, 2)

    self.Weapon_List = [self.Weapon_1, self.Weapon_2, self.Weapon_3]
    self.Weapon_Descriptions = [WEAPON_TEXT_1, WEAPON_TEXT_2, WEAPON_TEXT_3]

    self.Weapon_Selection = self.Weapon_List[self.Character_Random_Choices]
    self.Description_Selection = self.Weapon_Descriptions[self.Character_Random_Choices]

  # purely there so that once the next attack starts all of the randomized chocies and damage values changes once more repeating till a battle has been won or lost 
  def Reroll_Choice(self):
    self.__init__(self.WEAPON_MIN_1, self.WEAPON_MIN_2, self.WEAPON_MIN_3, self.WEAPON_MAX_1, self.WEAPON_MAX_2, self.WEAPON_MAX_3, self.WEAPON_TEXT_1, self.WEAPON_TEXT_2, self.WEAPON_TEXT_3, self.Character_Name, self.Enemy_HP, self.PLAYER_DEATH_DIALOG, self.ENEMY_DEATH_DIALOG)

# inherit all the properties and behaviors of class Character_Template to the class Combat_Mechanics 
class Combat_Mechanics(Character_Template):
    
  # this is so weird to implement but self is a variable represented by the currently used enemy object when the 
  # Combat_Mechanics class is called as an object of another variable this should hopefully make more sense later 
  def Enemy_Battle(self, HP_player):

    Death = 0
    Heal_player = random.randint(75, 125)

    End_Combat = False

    while self.Enemy_HP > Death or HP_player > Death and End_Combat == False:

      # import the variables returned from previous functions to this current function 
      HP_player, Dodge_Attack, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Players_turn(HP_player)
      # this is mainly there so that when a new attack begins it will be properly randomized instead of using the same attack over and over again
      self.Reroll_Choice()

      self.Character_Random_Choices = random.randint(0, 2)
      self.Description_Selection = self.Weapon_Descriptions[self.Character_Random_Choices]


      print(f"\n\n------------------------------------------------")
      print(f"              {self.Character_Name} HP: {self.Enemy_HP}")
      print(f"------------------------------------------------")

      Weapon_Choice = int(input("\nEnter the weapon choice you want to use! [choose by entering 1 - 4]: "))

      if Weapon_Choice == 1 and Dodge_Attack != 1:

        #Melee_Attack_Icon()

        self.Enemy_HP -= Death_Hunt_Sickle
        print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")

        HP_player -= self.Weapon_Selection
        print(f"\n{self.Character_Name} has {self.Description_Selection} and dealt {self.Weapon_Selection} damage!")

        time.sleep(3)
        clear_terminal()

      elif Weapon_Choice == 1 and Dodge_Attack == 1:

        #Melee_Attack_Icon()

        self.Enemy_HP -= Death_Hunt_Sickle
        print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")

        print(f"\n{self.Character_Name} has {self.Description_Selection} however, it missed! ")

        time.sleep(3)
        clear_terminal()

      elif Weapon_Choice == 2 and Dodge_Attack != 1:
            
        #Incantation_Icon_Art()

        self.Enemy_HP -= Glinted_Zweihander
        print(f"\n{Player_Name} casted the Glinted Zweihander sorcery and dealt {Glinted_Zweihander} damage! ")

        HP_player -= self.Weapon_Selection
        print(f"\n{self.Character_Name} has {self.Description_Selection} and dealt {self.Weapon_Selection} damage!")

        time.sleep(3)
        clear_terminal()

      elif Weapon_Choice == 2 and Dodge_Attack == 1:

        #Incantation_Icon_Art()

        self.Enemy_HP -= Glinted_Zweihander
        print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Glinted_Zweihander} damage! ")

        print(f"\n{self.Character_Name} has {self.Description_Selection} however, it missed! ")

        time.sleep(3)
        clear_terminal()

      elif Weapon_Choice == 3 and Dodge_Attack != 1: 
            
        #Incantation_Icon_Art()

        self.Enemy_HP -= Lightning_Strike
        print(f"\n{Player_Name} struck their lightning bolt incanation and dealt {Lightning_Strike} damage! ")

        HP_player -= self.Weapon_Selection
        print(f"\n{self.Character_Name} has {self.Description_Selection} and dealt {self.Weapon_Selection} damage!")

        time.sleep(3)
        clear_terminal()

      elif Weapon_Choice == 3 and Dodge_Attack == 1:

        #Incantation_Icon_Art()

        self.Enemy_HP -= Lightning_Strike
        print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Lightning_Strike} damage! ")

        print(f"\n{self.Character_Name} has {self.Description_Selection} however, it missed! ")

        time.sleep(3)
        clear_terminal()

      elif Weapon_Choice == 4:

        #Shield_Icon_Art()

        print(f"\n{self.Character_Name} has {self.Description_Selection} and dealt {self.Weapon_Selection} damage!")

        New_Damage = self.Weapon_Selection - (self.Weapon_Selection * Block)
        New_Damage_Rounded = round(New_Damage, 0)
        HP_player -= New_Damage_Rounded

        print(f"\n{Player_Name} used Block and has negated {Block_Percentage_Rounded}% of Postal Dude's damage! (damage now dealt: {New_Damage_Rounded}).")

        time.sleep(3)
        clear_terminal()

      else: 
        print("\nPlease enter a valid input!")
          
      if self.Enemy_HP <= Death: 
        End_Combat = True
        HP_player += Heal_player

        self.ENEMY_DEATH_DIALOG = self.ENEMY_DEATH_DIALOG

        time.sleep(3)
        print(f"\n{self.ENEMY_DEATH_DIALOG[0]}")
        time.sleep(5)
        print(f"\n{self.ENEMY_DEATH_DIALOG[1]} (HP awarded: {Heal_player} new HP: {HP_player}).")
        time.sleep(4)
        clear_terminal()


      elif HP_player <= Death: 
        End_Combat = True

        time.sleep(3)
        print(f"\n{Player_Name}: ah, my curse... permenant... i've met my match... ")
        time.sleep(5)
        print(f"\n{self.PLAYER_DEATH_DIALOG}")
        exit()

    return HP_player

def clear_colour():
  print(Style.RESET_ALL)

def clear_terminal():
  print("\033[2J")

def Player_Weapons(): 

  Potion_Display = False
  # normal damage: death = 7 - 25 glinted = 12 - 20 lightning = 13 - 16 debug: 99+ on all weapons

  # players may choose this weapon for inconsistent but high damage
  Death_Hunt_Sickle = random.randint(7, 25)
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
  
  return HP_player, Dodge_Attack, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded, 

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

# two of the boss fights that have more than three attacks that cannot be simply applied to the character class template unless if i had more bosses implementing them manually would be 
# a better use of my time and would not over complicate things here 
def RNGesus_Fight(HP_player, RNGesus_HP, Emergancy_Heal, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded):

  Death = 0
  Potion_Activation = True
  Weapon_List.append("Drink health potion")

  while RNGesus_HP > Death or HP_player > Death and End_Combat == False:
      
      # import the variables returned from previous functions to this current function 
      HP_player, Dodge_Attack, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Players_turn(HP_player)
      Weapon_Selection, Description_Selection = RNGesus_Turn()

      print(f"\n\n------------------------------------------------")
      print(f"                RNGesus HP: {RNGesus_HP}")
      print(f"------------------------------------------------")

      Weapon_Choice = int(input(f"\nenter the weapon/consumable choice you want to use! [choose by entering 1 - 5]: "))

      if Weapon_Choice == 1 and Dodge_Attack != 1:
                
        Ascii.Melee_Attack_Icon()

        RNGesus_HP -= Death_Hunt_Sickle
        print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")
        
        HP_player -= Weapon_Selection
        print(f"\nRNGesus has {Description_Selection} and dealt {Weapon_Selection} damage!")

        time.sleep(3)
        clear_terminal()

      elif Weapon_Choice == 1 and Dodge_Attack == 1:
        
        Ascii.Melee_Attack_Icon()

        RNGesus_HP -= Death_Hunt_Sickle
        print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")

        print(f"\nRNGesus has {Description_Selection} however, it missed! ")
        
        time.sleep(3)
        clear_terminal()

      elif Weapon_Choice == 2 and Dodge_Attack != 1:
                
        Ascii.Incantation_Icon_Art()

        RNGesus_HP -= Glinted_Zweihander
        print(f"\n{Player_Name} casted the Glinted Zweihander sorcery and dealt {Glinted_Zweihander} damage! ")

        HP_player -= Weapon_Selection
        print(f"\nRNGesus has {Description_Selection} and dealt {Weapon_Selection} damage!")
        
        time.sleep(3)
        clear_terminal()
      
      elif Weapon_Choice == 2 and Dodge_Attack == 1:
        
        Ascii.Incantation_Icon_Art()

        RNGesus_HP -= Glinted_Zweihander
        print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Glinted_Zweihander} damage! ")

        print(f"\nRNGesus has {Description_Selection} however, it missed! ")
        
        time.sleep(3)
        clear_terminal()

      elif Weapon_Choice == 3 and Dodge_Attack != 1: 
                
        Ascii.Incantation_Icon_Art()

        RNGesus_HP -= Lightning_Strike
        print(f"\n{Player_Name} struck their lightning bolt incanation and dealt {Lightning_Strike} damage! ")
        
        HP_player -= Weapon_Selection
        print(f"\nRNGesus has {Description_Selection} and dealt {Weapon_Selection} damage!")

        time.sleep(3)
        clear_terminal()
      
      elif Weapon_Choice == 3 and Dodge_Attack == 1:
        
        Ascii.Incantation_Icon_Art()

        RNGesus_HP -= Lightning_Strike
        print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Lightning_Strike} damage! ")

        print(f"\nRNGesus has {Description_Selection} however, it missed! ")
        
        time.sleep(3)
        clear_terminal()
    
      elif Weapon_Choice == 4:
        
        Ascii.Shield_Icon_Art()

        print(f"\nRNGesus has {Description_Selection} and dealt {Weapon_Selection} damage!")

        New_Damage = Weapon_Selection - (Weapon_Selection * Block)
        New_Damage_Rounded = round(New_Damage, 0)
        HP_player -= New_Damage_Rounded

        print(f"\n{Player_Name} used Block and has negated {Block_Percentage_Rounded}% of RNGesus's damage! (damage now dealt: {New_Damage_Rounded})")

        time.sleep(3)
        clear_terminal()
      
      elif Weapon_Choice == 5 and Potion_Activation == True:
                
        Potion_Activation = None
        Ascii.Potion_Health_Art()
        
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

        time.sleep(3)
        print(f"\nRNGesus: but why..? do you truly believe this old system will suffice for the next decade down the line?")
        time.sleep(5)
        print("\nMy crown befits your head please reconsider your decisions the status quo must be broken... at least I will leave as a worthy successor...")
        time.sleep(5)
        print(f"\nThe fight concludes with {Player_Name} walking up the deepslated steps for an eternity")
      
      elif HP_player <= Death: 
        End_Combat = True

        time.sleep(3)
        print(f"\n{Player_Name}: ah, my curse... permenant... i've met my match... ")
        time.sleep(5)
        print(f"\nThe fight concludes with {Player_Name}'s lifeless body being chucked to the endless abyss...")
        exit()

  return HP_player

def Huby_Developer_Fight(HP_player, Huby_Developer_HP, End_Combat, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded):

  Death = 0

  while Huby_Developer_HP > Death or HP_player > Death and End_Combat == False:
    
    # import the variables returned from previous functions to this current function 
    HP_player, Dodge_Attack, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Players_turn(HP_player)
    Weapon_Selection, Description_Selection = Huby_developers_Turn() 
    
    print(f"\n\n------------------------------------------------")
    print(f"              Huby Developer HP: ???????")
    print(f"\n           status: your bloody screwed!!")
    print(f"------------------------------------------------")

    Weapon_Choice = int(input("\nenter the weapon choice you want to use! [choose by entering 1 - 4]: "))

    if Weapon_Choice == 1 and Dodge_Attack != 1:

      Ascii.Melee_Attack_Icon()

      Huby_Developer_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nHuby Developer has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 1 and Dodge_Attack == 1:
      Ascii.Melee_Attack_Icon()

      Huby_Developer_HP -= Death_Hunt_Sickle
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Death_Hunt_Sickle} damage! ")

      print(f"\nHuby Developer has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 2 and Dodge_Attack != 1:
      
      Ascii.Incantation_Icon_Art()

      Huby_Developer_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} casted the Glinted Zweihander sorcery and dealt {Glinted_Zweihander} damage! ")

      HP_player -= Weapon_Selection
      print(f"\nHuby Developer has {Description_Selection} and dealt {Weapon_Selection} damage!")
      
      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 2 and Dodge_Attack == 1:
      Ascii.Incantation_Icon_Art()

      Huby_Developer_HP -= Glinted_Zweihander
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Glinted_Zweihander} damage! ")

      print(f"\nHuby Developer has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()

    elif Weapon_Choice == 3 and Dodge_Attack != 1: 
      
      Ascii.Incantation_Icon_Art()

      Huby_Developer_HP -= Lightning_Strike
      print(f"\n{Player_Name} struck their lightning bolt incanation and dealt {Lightning_Strike} damage! ")
      
      HP_player -= Weapon_Selection
      print(f"\nHuby Developer has {Description_Selection} and dealt {Weapon_Selection} damage!")

      time.sleep(3)
      clear_terminal()
    
    elif Weapon_Choice == 3 and Dodge_Attack == 1:
      Ascii.Incantation_Icon_Art()

      Huby_Developer_HP -= Lightning_Strike
      print(f"\n{Player_Name} has swinged their Death Hunt Sickle and dealt {Lightning_Strike} damage! ")

      print(f"\nHuby Developer has {Description_Selection} however, it missed! ")
      
      time.sleep(3)
      clear_terminal()
  
    elif Weapon_Choice == 4:
      Ascii.Shield_Icon_Art()

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

      time.sleep(3)
      print(f"\nHuby Developer: you were clearly cheating you cheap player!")

    elif HP_player <= Death: 
      End_Combat = True

      time.sleep(3)
      print(f"\n{Player_Name}: ah, my curse... permenant... i've met my match... ")
      time.sleep(5)
      print("\nYou got demolished so hard your body didnt even have time to decompose it simply turned to dust in conclusion your extremely stubborn good job you recieved a garbage ending...")
      time.sleep(4)
      print("\nYou also killed innocent bystanders you got brutally murdered by the developer and you didnt even cure your curse...")
      exit()

  return HP_player  

#-----------------------------------------------------------------------------------------------------
# Introduction
#-----------------------------------------------------------------------------------------------------

def Start_Journey_1(Input_Validation):

  clear_colour()
  Ascii.Trees_Path_Art()

  time.sleep(3)
  print("\nYou continue to wander through the trees, birds chirp, leaves blow, a Postal dude has arrived... ")

  time.sleep(2)
  Ascii.Postal_Dude_Art()
  print(f"\nPostal dude: This place ain't for foreigners like you {Player_Name}, Get outta here or you're gonna have an unpleasant time.")
  
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
  Ascii.Neighbourhood_Path_Art()
  
  print("\nYou arrived at the neighbourhood. It seems awfully quiet for a busy morning at 13:15. Oh..? At least one person is walking on the curb.")
  
  time.sleep(2)
  print(f"\nRasputin: Hey man! watch where you're going you freaking pinko!")
  
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
      print(f"\nRasputin: I will kill you with the blood of my sickle just as the founding fathers intended...")
    
    else: 
      print("\nPlease enter a valid input!")
      
  return Input_Validation

Ascii.intro_background_Art()

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
    Postal_Dude = Combat_Mechanics(2, 5, 7, 7, 13, 20, "hurled his fist", "swung his hatchet", "rained bullets with an Ak_47", POSTAL_DUDE_NAME, Postal_dude_HP, PLAYER_DEATH_DIALOG_LIST[0], POSTAL_DUDE_DEATH_DIALOG)
    HP_player = Postal_Dude.Enemy_Battle(HP_player)

    # start sakuya fight  
    clear_colour()

    time.sleep(3.5)
    print(f"\nAfter wandering through the woods {Player_Name} suddenly stumbled upon a gothic mansion it seems unvacant.")

    # this art here is very likely to stretch out if you dont have a sizable monitor that fits it properly 
    Ascii.Mansion_Art()
    time.sleep(6.5)
    
    time.sleep(3.5)
    print("\nOpening the heavy door, looking through the main hall sounds of walking can be heard atop the balcony. A mysterious figure appears...")
    
    time.sleep(3.5)
    Ascii.Sakuya_Art()

    time.sleep(3.5)
    print(f"\nSakuya: I never knew master invited unwarranted visitors... ")
    time.sleep(3.5)
    print(f"\nSakuya: what do you say stranger, care for a sharp dance? ")

    Input_Validation == None

    while Input_Validation == None:

      User_Response = int(input("\nYour response? [1: gee I didnt know your 'master' hired body guards too] [2: out of my way I have stuff to do]: "))

      if User_Response == 1:
        
        Input_Validation = True
        print(f"\nSakuya: ...")

        Sakuya = Combat_Mechanics(7, 8, 10, 12, 15, 22, "scattered her kunai knives", "splashed the room with knives", "used stopwatch disorienting the player", SAKUYA_NAME, Sakuya_HP, PLAYER_DEATH_DIALOG_LIST[1], SAKUYA_DEATH_DIALOG)
        HP_player = Sakuya.Enemy_Battle(HP_player)      

      elif User_Response == 2:
        
        Input_Validation = True
        print(f"\nSakuya (HP {Sakuya_HP}): I simply wont allow that to happen.")

        
        Sakuya = Combat_Mechanics(7, 8, 10, 12, 15, 22, "scattered her kunai knives", "splashed the room with knives", "used stopwatch disorienting the player", SAKUYA_NAME, Sakuya_HP, PLAYER_DEATH_DIALOG_LIST[1], SAKUYA_DEATH_DIALOG)
        HP_player = Sakuya.Enemy_Battle(HP_player)      

      else:
        print("Please enter a valid input!")

    time.sleep(3.5)
    clear_colour()
    time.sleep(3.5)
    clear_terminal()

    # Start the Zenith fight 

    time.sleep(5.5)
    print("\nAs the lifeless servant lays on the dirtless ground the player checks through the entire mansion however,")
    time.sleep(5.5)
    print("\nThe incarcerated souls faintly screaming nearby caught the player's attention and they investiageted further leading up to a door...")

    Ascii.Door_To_Cave_Art()

    time.sleep(5.5)
    print("\nUpon opening the door a cave is revealed with no other enterance the player jumps down the smell of rotten flesh within previous travelers and there lies Zenith the reclaimer of succession...")

    time.sleep(7.5)
    clear_terminal()

    Ascii.Zenith_Art()
    time.sleep(4.5)
    print(f"\nZenith: ah, annother ignorant successor of wizardry bold of you to assume the invasion of my layer, what desire is being achived?")
    time.sleep(4.5)
    print(f"\nZenith: vengence? diamonds? a broken home? whatever its you seek this may be your final destination none shall claim the title of control...")

    time.sleep(4.5)
    
    Zenith = Combat_Mechanics(9, 11, 13, 15, 19, 26, "threw a giant cluster of crystals cutting the player", "showered the player with fire", "shifted the ground making the player fall", ZENITH_NAME, Zenith_HP, PLAYER_DEATH_DIALOG_LIST[2], ZENITH_DEATH_DIALOG)
    HP_player = Zenith.Enemy_Battle(HP_player)

    # start the Eric fight 
    
    time.sleep(4.5)
    print("\nThe incarcerated souls continue to scream but slowly tones down each iteration thankfully this cave has one enterance.")
    time.sleep(4.5)
    print("\nInvestigating the cave further the path leads to a stormy enviorment with a familiar face staring upon the deepslated stairs.")    
    time.sleep(4.5)
    print("\nHowever the player's footsteps broke the figures fixation and took notice...")

    time.sleep(3.5)
    clear_terminal()
    clear_colour()

    Ascii.Eric_Art()
    time.sleep(4.5)
    print(f"\nEric: ah, {Player_Name}, I have not been informed of your existance for however long if your motivations align with mines im afraid I have to interfere with your ambitions.")
    time.sleep(4.5)
    print(f"\nEric: the title of control only belongs to one crown and you of all people should not possess it. Your level of reliability is a concern to behold leave now or face adversity.")

    while Input_Validation == True: 
      
      User_Response = int(input("\nYour response?: [1. what are you going to change that will benefit everyone?] [2. I dont think I can trust to make this decision]: "))
    
      if User_Response == 1: 
        
        Input_Validation = None
        
        print(f"\nEric: none of your business however I promise a millenium long policy that will affect everyone positively.")
        time.sleep(4.5)
        
        Eric = Combat_Mechanics(5, 9, 14, 9, 12, 30, "multishotted his bow impaling the player", "whispered to the player's ear persuading to join the lunar moon", "froze all particles nearby to a complete stop", ERIC_NAME, Eric_HP, PLAYER_DEATH_DIALOG_LIST[3], ERIC_DEATH_DIALOG)
        HP_player = Eric.Enemy_Battle(HP_player)
      
      elif User_Response == 2:
        
        Input_Validation = None

        print(f"\nEric: neither can I yet we will fight in an empty hopeless world awaiting a miracle to shine through let it be I Eric the first Moon Knight.")
        time.sleep(4.5)
        
        Eric = Combat_Mechanics(5, 9, 14, 9, 12, 30, "multishotted his bow impaling the player", "whispered to the player's ear persuading to join the lunar moon", "froze all particles nearby to a complete stop", ERIC_NAME, Eric_HP, PLAYER_DEATH_DIALOG_LIST[3], ERIC_DEATH_DIALOG)
        HP_player = Eric.Enemy_Battle(HP_player)
      
      else: 
        print("\nPlease enter a valid input!")
    
    # start final boss (RNGesus)
    
    Potion_Display = True

    time.sleep(5)
    clear_colour()
    clear_terminal()

    time.sleep(3)
    Ascii.Stairs_To_Throne_Art()

    time.sleep(4.5)
    print("\nYou conclude this very area alone can lead to the root of your curse you mutter under your breath 'gosh why didnt they think to build some sort of elevator here?' ")
    time.sleep(6.5)
    print("\nAfter what felt centuries passing by ever so convinient enough to be an enemy awaiting a visitor of their throne resting upon a massive floating rock.")
    time.sleep(5.5)
    print("\nThe possibility of winning this battle tingles in your head but there is no turning back...")

    time.sleep(5.5)
    Ascii.RNGesus_Art()

    print(f"\nRNGesus: you of all people is the last type I would anticipate the visitation either way none shall take the throne the harvest will prevail and I will be the luckiest of them all.")

    while Input_Validation == None:

      time.sleep(5)
      User_Response = int(input("\nYour response?: [1. my and others lives incredibly inconvinient either put an end to this or be granted death] [2. what even is your end goal when you harvest all luck?]: "))

      if User_Response == 1: 
        
        Input_Validation = False
        
        print(f"\nRNGesus: why would I help any of you? luck should be attained through perserverence and determination not by sheer randomness let my plans follow through and you get your share of the luck.")
        time.sleep(4.5)
        
        HP_player = RNGesus_Fight(HP_player, RNGesus_HP, Emergancy_Heal, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)
      
      elif User_Response == 2:
        
        Input_Validation = False

        print(f"\nRNGesus: I promise all a 10 century long proposal of luck being earned through perserverance and determination no person shall earn a bag of money for repeating a phrase let my plans follow through and luck as a system will be refined and will be ruled by action not words.")
        time.sleep(4.5)
        
        HP_player = RNGesus_Fight(HP_player, RNGesus_HP, Emergancy_Heal, End_Combat, Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)
      
      else: 
        print("\nPlease enter a valid input!")
    
    # Player kills RNGesus concluding journey 1's ending depending on what option the player picked and exiting the game
    
    clear_colour()
    Ascii.Throne_Art()

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
      
    Start_Journey_2(Input_Validation, Ascii.Rasputin_Art)

    # load player weapons and start the first enemy fight 
    Weapon_List, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded = Player_Weapons()
    Rasputin = Combat_Mechanics(2, 5, 7, 7, 13, 20, "shanked player with a sickle", "bashed the player with his hammer", "threw his broken stoli", RASPUTIN_NAME, Rasputin_HP, PLAYER_DEATH_DIALOG_LIST[4], RASPUTIN_DEATH_DIALOG)
    HP_player = Rasputin.Enemy_Battle(HP_player)

    # start iku blackrock fight 

    clear_terminal()
    clear_colour()

    time.sleep(3.5)
    print("\nAfter the player defeats rasputin the player wanders the neighbourhood wearing the stolen ushanka from rasputins dead body when suddenly they discover an alleyway.")
    
    time.sleep(3.5)
    Ascii.Alleyway_Art()

    time.sleep(3.5)
    print("\nPeaking the players interest they decided to wander through the suspiciously dangerous alleyway only to be confronted by a mysterious person with a trenchcoat.")
    
    time.sleep(3.5)
    clear_terminal()
    Ascii.Iku_Blackrock_Art()

    time.sleep(3.5)
    print(f"\nIku Blackrock: hey, this aint a safe place for your kind turn back while you can otherwise this aint going to be pretty.")
    time.sleep(3.5)

    Input_Validation = False

    while Input_Validation == False: 

      User_Response = int(input("\nYour response?: [1. no I came to retrieve my luck not be cursed forever with bad luck] [2. yeah maybe this area isnt the root of my problem]: "))

      if User_Response == 1: 
        
        Input_Validation = None

        print(f"\nIku Blackrock: ah so stubborn you should put your foolish ambitions to rest it isnt too late...")
        
        Iku_Blackrock = Combat_Mechanics(9, 10, 3, 14, 19, 20, "stabbed the player with a stained scythe poisioning the player", "sprayed mercury on the players open wounds", "slightly charmed the player", IKU_BLACKROCK_NAME, Iku_Blackrock_HP, PLAYER_DEATH_DIALOG_LIST[5], IKU_BLACKROCK_DEATH_DIALOG)
        HP_player = Iku_Blackrock.Enemy_Battle(HP_player)

      elif User_Response == 2: 
        
        Input_Validation = None
  
        print(f"\nIku Blackrock: yeah thats more like it now scram before you get yourself killed.")
        time.sleep(3.5)
        print("\nThe player leaves the neighbourhood to try another potential path exiting the game as a result of this decision...")
        exit()

      else:
        print("\nPlease enter a valid input!")

    # start Slave Knight fight

    time.sleep(4)
    clear_terminal()
    clear_colour()

    time.sleep(3.5)
    print("\nAfter the player defeats Iku Blackrock they wandered further in the alleyway to find an odd glowing sign with unintelligible texts written allover it.")
    time.sleep(3.5)
    print("\nTouching it disoriented the player for a brief moment only to be taken to the swamps with an extra stroke of bad luck bubbling can be heard across one of the lakes merging a severely drenched Slave Knight.")
    
    time.sleep(3.5)
    Ascii.Swamp_Art()
    clear_colour()
    time.sleep(7.5)

    clear_terminal()
    Ascii.Slave_Knight_Art()

    time.sleep(3.5)
    print(f"\nSlave Knight: ah, you, there, dont know how you arrived no matter may you lend me your organs? for me myself and I.")

    while Input_Validation == None: 

      User_Response = int(input("\nYour response?: [1. how are you even still alive? you should be dead you know if I were you id count my days] [2. yeah no... im getting the hell out of here]: "))

      if User_Response == 1: 
        
        Input_Validation = False 
        
        print(f"\nSlave Knight: no question my body is as hollow as a teapot be so kind to let me harvest it all.")
        
        Servant_Knight = Combat_Mechanics(5, 10, 7, 10, 20, 30, "casted a magic saw blade", "electrocuted the player by striking lightning", "bashed the player with a greatsword", SERVANT_KNIGHT_NAME, Servant_Knight_HP, PLAYER_DEATH_DIALOG_LIST[6], SERVANT_KNIGHT_DEATH_DIALOG)
        HP_player = Servant_Knight.Enemy_Battle(HP_player)

      elif User_Response == 2:

        Input_Validation = False

        print("\nYou tried to run away but the slave knight teleported right infront of you leaving you with no other choice...")
        
        Servant_Knight = Combat_Mechanics(5, 10, 7, 10, 20, 30, "casted a magic saw blade", "electrocuted the player by striking lightning", "bashed the player with a greatsword", SERVANT_KNIGHT_NAME, Servant_Knight_HP, PLAYER_DEATH_DIALOG_LIST[6], SERVANT_KNIGHT_DEATH_DIALOG)
        HP_player = Servant_Knight.Enemy_Battle(HP_player)

      else: 
        print("\nPlease enter a valid input!")
    
    # start blooddrinker Rei fight
    
    time.sleep(4)
    clear_terminal()
    clear_colour()

    time.sleep(3.5)
    print(f"\n{Player_Name}: I want to go home badly I'm tired please let this be over with... ")
    time.sleep(3.5)
    print("\nThe blood flowing south east intensified only to be gathered in a pool of blood emerging a daunting terrifying humanoid wielding a heavily poisoned scythe...")

    Ascii.BloodDrinker_Rei_Art()
    
    time.sleep(5)  
    print(f"\nBloodDrinker Rei: you called for death and death answered {Player_Name}, you killed my servant interrupting my plan its only fair to steal your existance.")
    time.sleep(5)
    print(f"\nBloodDrinker Rei: ever heard of the saying 'an eye for an eye a tooth for a tooth'? nevermind that your an atheist equally as ignorant as your kind a mere fool if you will now perish at once.")
    
    BloodDrinker_Reis = Combat_Mechanics(2, 12, 18, 7, 20, 31, "shedded the players skin causing blood loss", "sacrificed a lamb making the player distressed", "casted a bloodloss spell making the player lightheaded", BLOODDRINKER_REI, BloodDrinker_Rei_HP, PLAYER_DEATH_DIALOG_LIST[7], BLOODDRINKER_REI_DEATH_DIALOG)
    HP_player = BloodDrinker_Reis.Enemy_Battle(HP_player)

    # start huby developer fight (scripted death)
    time.sleep(4)
    clear_terminal()
    clear_colour()

    time.sleep(3.5)
    print("\nA summoning stone has appeared as a result of Rei's death the player gripped the stone getting ready to skim it across the lake nearby for fun to only be teleported to a foggy world.")
    time.sleep(5.5)
    print("\nThe player's throat clenches for its life bringing laboured breathing to the table this air is toxic they may have been telling the truth all along...")
    
    time.sleep(4.5)
    Ascii.Huby_Developer_Art()

    time.sleep(5.5)
    print("\nHuby Developer: I would normally have a long drawn out monologue of calling you an dumb idiot stubborn moron but you wont even listen anyways, you are solely responsible for this.")

    time.sleep(5)
    HP_player = Huby_Developer_Fight(HP_player, Huby_Developer_HP, End_Combat, Death_Hunt_Sickle, Glinted_Zweihander, Lightning_Strike, Block, Block_Percentage_Rounded)

  else:
    print("\nPlease enter a valid input!")
