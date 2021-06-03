#Dice Game Prototype 2 Pre GPIO

#Import Required Libs

import random #generates random seed
import time #implements sleep
import sys #used for CTL+C quit
import msvcrt #lockkeyboard fluff may not make it.
import winsound

winsound.PlaySound("DepatureforSpace.mp3", winsound.SND_ASYNC | winsound.SND_ALIAS )

def main():
#Set inital varible keep_rolling to yes counters for rolls and game counts.

    double_count = 0
    seven_count = 0
    eleven_count = 0
    times_played = 0
    keep_rolling = "yes"

#Initiate game holder for inital button left press:
#forwards to while loop left button plays right quits and displays exit message.

    print("Time to roll dice, 7's 11's and doubles for the win!")
    keep_rolling = input("\nROLL THE DICE? (Y/N)") 
    

#while keep rolling is true continue loop

    while keep_rolling == "yes" or keep_rolling == "y" or keep_rolling == "Y" or keep_rolling == "Yes": #extra or statements for prototype redundency while will be wait for next button press.
        try:
            print("\nRoll'em!")
            print("\n\nThe crimson dice fly through the air with grace and vigor!") #placeholder for lights flashing?
            time.sleep(1)   #Calls time libary 1 second delay

#lock input from keyboard and GPIO for redundency? to much fluff?

            '''class keyboardDisable():

                def start(self):
                    self.on = True

                def stop(self):
                    self.on = False

                def __call__(self): 
                    while self.on:
                        msvcrt.getwch()


                def __init__(self):
                    self.on = False
                    import msvcrt

            disable = keyboardDisable()
            disable.start()
            time.sleep(1)
            disable.stop()
            '''            

            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)    #calls random, random int function.

            results = dice1 + dice2         #results for if statements
    
            print("\n\nThe dice land on the table and the results are!!!!!")       
            print(f"\nDice 1: {dice1} \nDice 2: {dice2}")

            if dice1 == dice2:
                print("\nDOUBLES UP")       #Buzzer/audio sound plus counter up for doubles
                print(f"\nYou rolled a {results} :D")
                double_count += 1
            
            elif results == 7:
                print("\n7 UP!")            #Buzzer/audio sound plus counter up for 7s
                print(f"\nYou rolled a {results} :D")
                seven_count += 1
            
            elif results == 11:
                print("\nElevensies!")      #Buzzer/audio sound plus counter up for 7s
                print(f"\nYou rolled a {results} :D")
                eleven_count += 1
    
            else:
                print(f"You rolled a {results} :D")

                times_played += 1           #increases games played by 1

            if times_played == 10:
                print("\nBLAZING LIKE THE SUN!")
            elif times_played == 20:
                print("\nGETTING BORED YET?")
            
            keep_rolling = input("\nPlay again? (Y/N)") #left to roll again, right button to end game
        except KeyboardInterrupt: #on CTRL+C
            print("[CTRL+C detected Qutting Game]")
            print(f"\n\nIn a rush to leave? Thanks for playing!\n\nDoubles Rolled: {double_count} Sevens Rolled {seven_count} Elevens Rolled: {eleven_count} \nYou played: {times_played} games. ")
            sys.exit() #Uses sys libary to quit while in loop. 

    if keep_rolling == "N" or keep_rolling == "n" or keep_rolling == "NO" or keep_rolling == "No": #placeholder for right button press
        print(f"\n\nThanks for playing!\n\nDoubles Rolled: {double_count} Sevens Rolled {seven_count} Elevens Rolled: {eleven_count} \nYou played: {times_played} games. ")

if __name__ == '__main__':
    main()

