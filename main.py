import random
import sys
import osikytretykuikyefwtyiltres
GAME_OVER = False
GAME_TYPE=""
os.system('clear')
easy={'Toronto':{"MILES_TO_GO": 491, "PLAYER_MONEY": 500},
  'Chicago': {"MILES_TO_GO":789,"PLAYER_MONEY":500},
  'Birmingham': {"MILES_TO_GO":962,"PLAYER_MONEY":800}, 
  'Nashville': {"MILES_TO GO": 886, "PLAYER_MONEY":700},
  'St. Louis': {"MILES_TO_GO": 953,"PLAYER_MONEY":1000}, 
  'Baltimore': {"MILES_TO_GO":187,"PLAYER_MONEY":200},
  'Washington': {"MILES_TO_GO":226,"PLAYER_MONEY":200},
  'Boston':{"MILES_TO_GO":215,"PLAYERMONEY":200}
}
normal={ 
  'Miami': {"MILES_TO_GO":1285, "PLAYER_MONEY": 1000},
  'Denver': {"MILES_TO_GO":1778,"PLAYER_MONEY":1500},
}
hard={
  'Los Angeles': {"MILES_TO_GO": 2789, "PLAYER_MONEY": 2500},'Seattle': {"MILES_TO_GO": 2852,"PLAYER_MONEY":2500},
  'Pheonix': {"MILES_TO_GO":2409, "PLAYER_MONEY":2000},
  'Portland': {"MILES_TO_GO":2894,"PLAYER_MONEY":2500}, 
  'El Paso': {"MILES_TO_GO":2182, "PLAYER_MONEY":2000},
  'Oakland': {"MILES_TO_GO":2896,"PLAYER_MONEY":2500},
  'Mexico City': {"MILES_TO_GO": 2628, "PLAYER_MONEY":2000},
}
insane={
  'Anchorage': {"MILES_TO_GO": 4358, "PLAYER_MONEY":3300},
  
}

cities=0
while cities==0:
  GAME_TYPE = GAME_TYPE.lower()
  GAME_TYPE=input("Which difficulity would you like to play? \n Easy: 0-1000 miles \n Normal: 1001-2000 miles \n Hard: 2001-3000 \n Insane: 3001-4000 or above miles.\n")
  if GAME_TYPE=="easy":
    cities=easy
  elif GAME_TYPE=="normal":
    cities=normal
  elif GAME_TYPE=="hard":
    cities=hard
  elif GAME_TYPE=="insane":
    cities=insane
  else:
    print("I don't know what",GAME_TYPE,"means?")
print("")

CITY=random.choice(list(cities.keys()))
PLAYER_HEALTH = 5
PLAYER_MONEY = cities[CITY]["PLAYER_MONEY"]
MILES_TO_GO = cities[CITY]["MILES_TO_GO"]
START_DISTANCE = cities[CITY]["MILES_TO_GO"]


CURRENT_DAY = 0
PLAYER_CONSUME=100

print("\033[0;36;40m")
print("Your goal is to make it from NY to",CITY,"while managing your money, food, and sleep while still making progress toward your goal by driving. You can also earn medals depending on your performance \n Your options are,")

def rest():
 global PLAYER_HEALTH
 HOTEL_COST=random.randint(100,200)
 if PLAYER_HEALTH < 5:
   PLAYER_HEALTH = PLAYER_HEALTH + 1
 global PLAYER_MONEY
 PLAYER_MONEY= PLAYER_MONEY - HOTEL_COST
 global CURRENT_DAY
 CURRENT_DAY= CURRENT_DAY + 1
 print("You've spent",HOTEL_COST,"dollars.")

def eat():
  global PLAYER_MONEY
  global PLAYER_CONSUME
  food=input("Where do you want to eat? \n Diner:($100, +10 Sustinance) \n Restaurant:($350, +50 Sustinance) \n Buffet:($225, +30 Sustinance) \n")
  food=food.lower()
  if food =="buffet":
    x=30
    print("You go to an all you can eat buffet and spent $225")
    PLAYER_MONEY=PLAYER_MONEY - 225
    PLAYER_CONSUME=PLAYER_CONSUME + x
    if PLAYER_CONSUME >100:
      PLAYER_CONSUME=100
    print("You've gained", x, "sustinance")
  elif food == "restaurant":
    z=50
    print("You eat a nice beef wellington with a side of mashed potatos at a local restaurant. You spent $350 on your meal")
    PLAYER_MONEY=PLAYER_MONEY - 350
    PLAYER_CONSUME=PLAYER_CONSUME + z
    if PLAYER_CONSUME >100:
      PLAYER_CONSUME=100
    print("You've gained", z, "sustinance")
  elif food=="diner":
    y=10
    print("You go to a local diner and order Belguian Waffles. You spent $100 on your meal.")
    PLAYER_MONEY=PLAYER_MONEY - 100
    PLAYER_CONSUME=PLAYER_CONSUME + y
  if PLAYER_CONSUME >100:
    PLAYER_CONSUME=100
    print("You've gained", y, "sustinance")
  else:
    print("I don't understand what,", food, "means")


def stats():
 print("\n CURRENT STATS: \n")
 print("Health:",PLAYER_HEALTH,)
 print("Money:",PLAYER_MONEY,)
 print("Day:",CURRENT_DAY,)
 print("Miles Left:",MILES_TO_GO,)
 print("Sustanence:", PLAYER_CONSUME)


def drive():
 global MILES_TO_GO
 global PLAYER_CONSUME
 x=15
 x1=random.randint(1,300)
 MILES_TO_GO = MILES_TO_GO - x1
 if x1 <= 100:
  print("\033[0;31;40m")
  print("Your car broke down, you were only able to drive,",x1,"miles.")
  PLAYER_CONSUME= PLAYER_CONSUME - x
 elif x1 >= 100 and x1 <=200:
  print("\033[0;32;40m")
  print("There was no traffic, you drove,",x1,'miles.')
  PLAYER_CONSUME= PLAYER_CONSUME - x
 elif x1 >= 201 and x1 <=300:
  print("\033[0;34;40m")
  print("You found a secret shortcut only the FBI knows of you successfuly drove,",x1, "miles.")
  PLAYER_CONSUME= PLAYER_CONSUME - x
 global CURRENT_DAY
 CURRENT_DAY = CURRENT_DAY + 1
 global PLAYER_MONEY
 PLAYER_MONEY = PLAYER_MONEY - random.randint(1,60)
 global PLAYER_HEALTH
 PLAYER_HEALTH = PLAYER_HEALTH - 1

def chance_to_win():
  jobs=random.randint(1,4) 
  global PLAYER_CONSUME
  PLAYER_CONSUME=PLAYER_CONSUME - 15
  global PLAYER_MONEY
  global CURRENT_DAY
  CURRENT_DAY = CURRENT_DAY + 1
  global PLAYER_HEALTH
  print('You rolled for a job and have....')
  if jobs == 1:
    print("entered a local casino, where you test your luck.")
    MONEY_=random.randint(-150,800)
    PLAYER_MONEY += MONEY_
    print("You've gained", MONEY_, "dollars")
    PLAYER_HEALTH = PLAYER_HEALTH - 1
  elif jobs == 2:
    print("been selected to be in Jepoardy.")
    MONEY_=random.randint(100,550)
    PLAYER_MONEY += MONEY_
    print("You've gained", MONEY_, "dollars")
    PLAYER_HEALTH = PLAYER_HEALTH - 1
  elif jobs == 3:
    print("decided to beg for some money from some good samaratins.")
    MONEY_=random.randint(5,150)
    PLAYER_MONEY += MONEY_
    print("You've gained", MONEY_, "dollars")
    PLAYER_HEALTH = PLAYER_HEALTH - 1
  elif jobs == 4:
    print("Found money on the sidewalk instead.")
    MONEY_=random.randint(0,125)
    PLAYER_MONEY += MONEY_
    print("You've gained", MONEY_,"dollars")
    PLAYER_HEALTH = PLAYER_HEALTH - 1


while GAME_OVER == False:
  if PLAYER_HEALTH == 0:
    print("You fell asleep while driving and drove into a lagoon causing your death.")
    break
  elif MILES_TO_GO <= 0:
    print("You've made it to,",CITY)
    print("\033[0;33;40m")    
    print("""
                                   _________
                             .---'::'        `---.
                            (::::::'              )
                            |`-----._______.-----'|
                            |              :::::::|
                          .-|               ::::::|-.
                           \|               :::::/|/
                            |               ::::::|
                            | You have made it to:|
                            | Your destination::::|
                            |               ::::::|
                            |              .::::::|
                            |              :::::::|
                             \            :::::::/
                              `.        .:::::::'
                                `-._  .::::::-'
                                    |     |
                                    |  :::|
                                    |   ::|
                                   /     ::\                                        
                              __.-'      :::`-.__
                             (_           ::::::_)
                              '-----------------'
  """)
    break
  elif PLAYER_CONSUME <= 0:
    print("You starved to death.")
    break
  elif PLAYER_MONEY <= 0:
    print("You couldn't pay for anything, not even a bus fare.")
    break

#Callings
  choice = input("\n Drive, \n Rest, \n Profit, \n Stats, \n Eat, \n Quit \n")
  choice = choice.lower()
  os.system('clear')
  if choice == "drive":
    drive()
    stats()
  elif choice=="eat":
    eat()
    stats()
    
  elif choice == "rest":
    print("\033[0;36;40m")
    print("You've decided to rest in a nearby hotel")
    rest()
    stats()
  elif choice == "profit":
    chance_to_win()
    stats()
  elif choice == "stats":
   print('\033[0;33;40m')
   stats()
  elif choice == "quit":
    os._exit(0)
  else:
    print("I'm sorry I don't know what "+ choice," means")
  print("") 
print('\n --------------------------------------------------------------- \n')
print("GAME OVER")
if MILES_TO_GO <=0:
  print("You reached you're destination",CURRENT_DAY,"days,", PLAYER_MONEY,"dolands, headed towards",CITY,)

#easy achievements
#Travel Time Achievements(Easy)
if GAME_TYPE=="easy":
  if CURRENT_DAY <=8:
    print("You have achieved gold in travel time, good job.")
  elif CURRENT_DAY >=9 and CURRENT_DAY <=16:
    print("You have achieved silver in travel time, you can be quicker then that.")
  elif CURRENT_DAY >=17 and CURRENT_DAY <=24:
    print("You have achieved bronze in travel time, where's your time management skills?.")
  else:
    print("You have to do better if you want an award.")
      
  #Money Achievements(easy)
    
  if PLAYER_MONEY >=1000:
    print("You have achieved platinum in money, I didn't even know that was possible.")
  elif PLAYER_MONEY <=500 and PLAYER_MONEY >=400:
    print("You have achieved gold in money, can't do better then gold, right?")
  elif PLAYER_MONEY <=399 and PLAYER_MONEY >=301:
    print("You have a achieved silver in money, always room for imporvement.")
  elif PLAYER_MONEY <=300 and PLAYER_MONEY >=199:
    print("You have achieved bronze in money, how about another try, hmmm?")
  else:
    print("Did you even try to manage your money?")

  #Health

  if PLAYER_HEALTH <=5 and PLAYER_HEALTH >=4:
    print("You kept yourself alive and earned a gold in health, impressive.")
  elif PLAYER_HEALTH <=3 and PLAYER_HEALTH >=2:
    print("You got to your destination but got the flu when you got there thus earning you a silver for health.")
  else:
    print("You all most died and recieved no medal for health.")

  #Consume 

  if PLAYER_CONSUME <=100 and PLAYER_CONSUME >=80:
    print("You got there well fed and nurished, and recieved a gold in sustanence.")
  elif PLAYER_CONSUME <=79 and PLAYER_CONSUME >=59:
    print("You got there peckish and was awarded a silver in sustanence.")
  elif PLAYER_CONSUME <=58 and PLAYER_CONSUME >=38:
    print("You got there with your stomach growling and for that was awarded a bronze medal in sustanence.")
  else:
    print("You passed out and your grandma had to drag you out of the car and recieved no medal for sustanence.")
  print("\n ----------------------------------------------------- \n")

#Normal Achievements
#Travel Time(Normal)

if GAME_TYPE=="normal":
  if CURRENT_DAY <=12:
    print("You have achieved gold in travel time, good job.")
  elif CURRENT_DAY > 13 and CURRENT_DAY <=20:
    print("You have achieved silver in travel time, you can be quicker then that.")
  elif CURRENT_DAY > 21 and CURRENT_DAY <=28:
    print("You have achieved bronze in travel time, where's your time management skills?.")
  else:
    print("You have to do better if you want an award.")

    #Money Achievements
    
  if PLAYER_MONEY >=1800:
    print("You have achieved platinum in money, i didn't even know that was possible.")
  elif PLAYER_MONEY <=1000 and PLAYER_MONEY >=800:
    print("You have achieved gold in money, can't do better then gold, right?")
  elif PLAYER_MONEY <=799 and PLAYER_MONEY >=701:
    print("You have a achieved silver in money, always room for imporvement.")
  elif PLAYER_MONEY <=700 and PLAYER_MONEY >=600:
    print("You have achieved bronze in money, how about another try, hmmm?")
  else:
    print("Did you even try to manage your money?")

  #Health

  if PLAYER_HEALTH <=5 and PLAYER_HEALTH >=4:
    print("You kept yourself alive and earned a gold in health, impressive.")
  elif PLAYER_HEALTH <=3 and PLAYER_HEALTH >=2:
    print("You got to your destination but got the flu when you got there thus earning you a silver for health.")
  else:
    print("You all most died and recieved no medal for health.")

  #Consume

  if PLAYER_CONSUME <=100 and PLAYER_CONSUME >=80:
    print("You got there well fed and nurished, and recieved a gold in sustanence.")
  elif PLAYER_CONSUME <=79 and PLAYER_CONSUME >=59:
    print("You got there peckish and was awarded a silver in sustanence.")
  elif PLAYER_CONSUME <=58 and PLAYER_CONSUME >=38:
    print("You got there with your stomach growling and for that was awarded a bronze medal in sustanence.")
  else:
    print("You passed out and your grandma had to drag you out of the car and recieved no medal for sustanence.")
  print("\n ----------------------------------------------------- \n")
#Hard Achievements

if GAME_TYPE=="hard":
  if CURRENT_DAY <=16:
    print("You have achieved gold in travel time, good job.")
  elif CURRENT_DAY > 17 and CURRENT_DAY <=24:
    print("You have achieved silver in travel time, you can be quicker then that.")
  elif CURRENT_DAY > 25 and CURRENT_DAY <=32:
    print("You have achieved bronze in travel time, where's your time management skills?.")
  else:
    print("You have to do better if you want an award.")

    #Money Achievements
    
  if PLAYER_MONEY >=2500:
    print("You have achieved platinum in money, i didn't even know that was possible.")
  elif PLAYER_MONEY <=2200 and PLAYER_MONEY >=2000:
    print("You have achieved gold in money, can't do better then gold, right?")
  elif PLAYER_MONEY <=1999 and PLAYER_MONEY >=1799:
    print("You have a achieved silver in money, always room for imporvement.")
  elif PLAYER_MONEY <=1798 and PLAYER_MONEY >=1598:
    print("You have achieved bronze in money, how about another try, hmmm?")
  else:
    print("Did you even try to manage your money?")

  #Health

  if PLAYER_HEALTH <=5 and PLAYER_HEALTH >=4:
    print("You kept yourself alive and earned a gold in health, impressive.")
  elif PLAYER_HEALTH <=3 and PLAYER_HEALTH >=2:
    print("You got to your destination but got the flu when you got there thus earning you a silver for health.")
  else:
    print("You all most died and recieved no medal for health.")

  #Consume

  if PLAYER_CONSUME <=100 and PLAYER_CONSUME >=80:
    print("You got there well fed and nurished, and recieved a gold in sustanence.")
  elif PLAYER_CONSUME <=79 and PLAYER_CONSUME >=59:
    print("You got there peckish and was awarded a silver in sustanence.")
  elif PLAYER_CONSUME <=58 and PLAYER_CONSUME >=38:
    print("You got there with your stomach growling and for that was awarded a bronze medal in sustanence.")
  else:
    print("You passed out and your grandma had to drag you out of the car and recieved no medal for sustanence.")
  print("\n ----------------------------------------------------- \n")

#Insane 

if GAME_TYPE=="insane ":
  if CURRENT_DAY <=20:
    print("You have achieved gold in travel time, good job.")
  elif CURRENT_DAY > 21 and CURRENT_DAY <=28:
    print("You have achieved silver in travel time, you can be quicker then that.")
  elif CURRENT_DAY > 29 and CURRENT_DAY <=36:
    print("You have achieved bronze in travel time, where's your time management skills?.")
  else:
    print("You have to do better if you want an award.")

    #Money Achievements
    
  if PLAYER_MONEY >=3000:
    print("You have achieved platinum in money, i didn't even know that was possible.")
  elif PLAYER_MONEY <=2600 and PLAYER_MONEY >=2400:
    print("You have achieved gold in money, can't do better then gold, right?")
  elif PLAYER_MONEY <=2399 and PLAYER_MONEY >=2199:
    print("You have a achieved silver in money, always room for imporvement.")
  elif PLAYER_MONEY <=2198 and PLAYER_MONEY >=1998:
    print("You have achieved bronze in money, how about another try, hmmm?")
  else:
    print("Did you even try to manage your money?")

  #Health

  if PLAYER_HEALTH <=5 and PLAYER_HEALTH >=4:
    print("You kept yourself alive and earned a gold in health, impressive.")
  elif PLAYER_HEALTH <=3 and PLAYER_HEALTH >=2:
    print("You got to your destination but got the flu when you got there thus earning you a silver for health.")
  else:
    print("You all most died and recieved no medal for health.")

  #Consume

  if PLAYER_CONSUME <=100 and PLAYER_CONSUME >=80:
    print("You got there well fed and nurished, and recieved a gold in sustanence.")
  elif PLAYER_CONSUME <=79 and PLAYER_CONSUME >=59:
    print("You got there peckish and was awarded a silver in sustanence.")
  elif PLAYER_CONSUME <=58 and PLAYER_CONSUME >=38:
    print("You got there with your stomach growling and for that was awarded a bronze medal in sustanence.")
  else:
    print("You passed out and your grandma had to drag you out of the car and recieved no medal for sustanence.")
  print("\n ----------------------------------------------------- \n")