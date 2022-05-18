##PLEASE RUN IN TERMINAL, THIS WILL NOT WORK PROPERLY IN SHELL (CTRL + T IN THONNY)##
import os
import time 
import sys


##/////LOOP VARIABLES\\\\\##
def Loop_On() :pass
Loop_On = (1)
def Menu_Select() :pass
Menu_Select = (1)
def MOTHER_OF_ALL_LOOPS():pass
MOTHER_OF_ALL_LOOPS = (1)
#Huge Loop to allow Program to countinually Loop, all loops sued countinually
def Var():pass
var = (0)
#//////HOLIDAY VARIABLES\\\\\#
def days():pass
days = (0)
def Kids():pass
Kids = (0)
def Adults():pass
Adults = (0)
def Exit():pass
Exit = (0)
#///Cost Variables\\#
def CstAdlt():pass
CstAdlt = (0)
def CstKids():pass
CstKids = (0)
def DayCst():pass
DayCst = (0)
def TotalCst():pass
TotalCst = (0)
print ('''   _____       _ _              _____                _     _        _______                  _ 
  / ____|     | | |            / ____|              (_)   | |      |__   __|                | |
 | (___   __ _| | |_   _ ___  | (___   ___  __ _ ___ _  __| | ___     | |_ __ __ ___   _____| |
  \___ \ / _` | | | | | / __|  \___ \ / _ \/ _` / __| |/ _` |/ _ \    | | '__/ _` \ \ / / _ \ |
  ____) | (_| | | | |_| \__ \  ____) |  __/ (_| \__ \ | (_| |  __/    | | | | (_| |\ V /  __/ |
 |_____/ \__,_|_|_|\__, |___/ |_____/ \___|\__,_|___/_|\__,_|\___|    |_|_|  \__,_| \_/ \___|_|
                    __/ |                                                                      
                   |___/       
              ,.  _~-.,               .
           ~'`_ \/,_. \_
          / ,"_>@`,__`~.)             |           .
          | |  @@@@'  ",! .           .          '
          |/   ^^@     .!  \          |         /
          `' .^^^     ,'    '         |        .             .
           .^^^   .          \                /          .
          .^^^       '  .     \       |      /       . '
.,.,.     ^^^             ` .   .,+~'`^`'~+,.     , '
&&&&&&,  ,^^^^.  . ._ ..__ _  .'             '. '_ __ ____ __ _ .. .  .
%%%%%%%%%^^^^^^%%&&;_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,
&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=
%%%%%&&&&&&&&&&&%%%%&&&_,.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,
%%%%%%%%%&&&&&&&&&-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~'
##mjy#####*"'
_,.-=~'`^`'~=-Start your Holiday Today!!!`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'
              Press Any key to start seeing Offers
~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^
''')
var = input('>')
os.system('cls' if os.name == 'nt' else 'clear') #Clears Terminal, gets rid of start screen
while MOTHER_OF_ALL_LOOPS == 1:
    while Loop_On == 1: #This Loop is exclusivley for the Hotel Selection part of the program
        while Menu_Select == 1:
            print ('Select your Hotel!')
            print ('[X] Basils Backpackers')
            print ('[ ] Ocean Breeze Units ')
            print ('[ ] Silver Sands Hotel')
            print ('[ ] Capricorn Club')
            print ('[ ] Sunset Ridge Resort ')
            print ('Use W/S to go Up/Down, Press Enter to choose direction')
            Menu_Select = Menu_Select + 0.2 #Adding 0.2 means that Menu_Select is no longer a whole intiger, breaking the loop, repeated with every other menu
        while Menu_Select == 2:
            print ('Select your Hotel!')
            print ('[ ] Basils Backpackers')
            print ('[X] Ocean Breeze Units ')
            print ('[ ] Silver Sands Hotel')
            print ('[ ] Capricorn Club')
            print ('[ ] Sunset Ridge Resort ')
            print ('Use W/S to go Up/Down')
            Menu_Select = Menu_Select + 0.2
        while Menu_Select == 3: #Pretty self explanatory this part
            print ('Select your Hotel!')
            print ('[ ] Basils Backpackers')
            print ('[ ] Ocean Breeze Units ')
            print ('[X] Silver Sands Hotel')
            print ('[ ] Capricorn Club')
            print ('[ ] Sunset Ridge Resort ')
            print ('Use W/S to go Up/Down')
            Menu_Select = Menu_Select + 0.2
        while Menu_Select == 4:
            print ('Select your Hotel!')
            print ('[ ] Basils Backpackers')
            print ('[ ] Ocean Breeze Units ')
            print ('[ ] Silver Sands Hotel')
            print ('[X] Capricorn Club')
            print ('[ ] Sunset Ridge Resort ')
            print ('Use W/S to go Up/Down')
            Menu_Select = Menu_Select + 0.2
        while Menu_Select == 5:
            print ('Select your Hotel!')
            print ('[ ] Basils Backpackers')
            print ('[ ] Ocean Breeze Units ')
            print ('[ ] Silver Sands Hotel')
            print ('[ ] Capricorn Club')
            print ('[X] Sunset Ridge Resort ')
            print ('Use W/S to go Up/Down')
            Menu_Select = Menu_Select + 0.2
        Selection = input('') #Accept user input at this point for menu selection
        if Selection == ('w') or Selection == ('W'): #W is up
            Menu_Select = Menu_Select - 1
            if Menu_Select < 1.2: #If the menu is less than 1.2, then it loops back round so when u go up, it simply ends up @ the bottom
                Menu_Select = 5
            elif Menu_Select > 5.2: #Same as above except reverse
                Menu_Select = 1
            else:
                Menu_Select = Menu_Select - 0.2 #-0.2 ends the if statments, and allows a previous intiger while loop to begin
        if Selection == ('s') or Selection == ('S'): # S is down
            Menu_Select = Menu_Select + 1
            if Menu_Select < 1.2:
                Menu_Select = 5
            if Menu_Select > 5.2:
               Menu_Select = 1  
            else:
                Menu_Select = Menu_Select - 0.2  
        if Selection == (' ') or Selection == (''): #If the user hits enter it shows that he has made the selection within the program
            Loop_On = 2 #Disables Menu loop, enters another one for inputing numeric values
            Menu_Select = Menu_Select - 0.2 # Could try to optimise this but it would throw trace table into chaos
            Menu_Select = Menu_Select + 0.1
        elif int(Selection) == (0): #Turns off program,  breaks all loops since it is 0
            MOTHER_OF_ALL_LOOPS = (0)
            break
        os.system('cls' if os.name == 'nt' else 'clear') #Clears previus selection
    while Loop_On == 2:
        days = input('How many days do you want to stay for?') # Input days
        days = float(days) #Forces it to be flaot so no errors can occur
        if days == (0.0):
            MOTHER_OF_ALL_LOOPS = (0)#Exits program compeltley
            break
        kids = input('How many kids will be there?') #Input amount of kids
        kids = float(kids) #As above, so below
        Adults = input('How many Adults will be coming?') #Input Adult amount
        Adults = float(Adults) #Forces it to be flaot so no errors can occur
        os.system('cls' if os.name == 'nt' else 'clear')
        if Menu_Select == 1.1: #For if Basils Backpackers Selected, prices calculated in a single day stay
            CstKids = kids*12.50
            CstAdlt = Adults*25.00
        elif Menu_Select == 2.1: #For if Ocean breeze units Selected, prices calculated in a single day stay
            CstKids = kids*20.00
            CstAdlt = Adults*35.00 #E.t.c., E.t.c.
        elif Menu_Select == 3.1:
            CstKids = kids*30.00
            CstAdlt = Adults*50.00
        elif Menu_Select == 4.1:
            CstKids = kids*45.00
            CstAdlt = Adults*75.00
        elif Menu_Select == 5.1:
            CstKids = kids*65.00
            CstAdlt = Adults*120.00
        else:
            print ('Error, countinue program') #If weird error happens again, will assume 1 is selected
            Menu_Select = (1) #(0.2*10^13)+1 error only occurs when 1 is selected ¯\_(ツ)_/¯
            break #Break is god command since it restarts program
        DayCst = CstKids + CstAdlt #Adds 2 together to find cost over a day, 
        TotalCst = DayCst*days #Times the days cost over the total amount of days to show total
        print ('The Total cost for the '+ str(kids) + ' kid(s) per day is $' + str(CstKids)) #Shows all the prices for transparency or whatever, 
        print ('The Total cost for the '+ str(Adults) + ' adult(s) per day is $' + str(CstAdlt)) #str command used to frce string in case of intiger error or something
        print ('The Total cost per day is $' + str(DayCst) )
        print ('Therefore the total cost over the ' + str(int(days)) + ' days totals too:')
        print ('$' + str(TotalCst) ) #total cost obviosuly
        print(Exit)
        Exit == int(input('''Type 0 if you wish to exit the Program, type anything else if 
        you wish to countinue'''))
        if Exit != (0): #Exlcusive means that there is less room for user error
            Loop_On = (1)
            Menu_Select = (1)
            MOTHER_OF_ALL_LOOPS = (1)
            print (Exit)
            time.sleep(10)
            os.system('cls' if os.name == 'nt' else 'clear') #Clear previous screens
            continue
        else: #aka if Exit == 0
            Loop_On = (0)
            Menu_Select = (0)
            MOTHER_OF_ALL_LOOPS = (0)
            break

print ('Exiting Program...')