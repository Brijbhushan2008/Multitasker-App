import time
import math
import random
import datetime
import os
from colorama import Fore ,Style,init 
init(autoreset=True)

#--------------------------------DEFINATIONS---------------------------------------------------

def Rectangle_area():
  length=float(input("\n👉Enter the length of rectangle:"))
  breadth=float(input("👉Enter the breadth of the rectangle:"))
  #The formula 
  area=length*breadth
  #Printing the area 
  print(f"Rectangle specifications- length: {length} breadth: {breadth}")
  print(f"The area of rectangle is: {area}")


def hypotneuse_of_triangle():

  b=float(input("\n👉Enter the base of triangle:"))
  p=float(input("👉Enter the perpendicular of triangle:"))
  #The formula  
  h=math.sqrt(pow(b,2)+pow(p,2))
  #printing the h of triangle 
  print(f"The hypotneuse of triangle is: {round(h,2)}") 
  

def table():
  num=int(input("\n👉Enter the number:"))

  for i in range(1,11):
    print(f"{num} x {i} = {num*i}")


def area_or_perimeter():
  
  print("\nwhat do you want to do:")
  print("1. Calculate area ")
  print("2. calculate perimeter")
  choice=int(input("👉Enter your choice(1or2)"))
  radius=float(input("👉Enter radius of circle:"))
   #The formulas 
  area=3.14*pow(radius,2)
  perimeter=2*3.14*radius
   #Making condition
  if choice==1:
     print(f"Area of the circle with radius {radius} is: {area}")
  elif choice==2:
     print(f"perimeter of the circle with radius {radius} is: {perimeter}")
  else:
     print("Invalid choice")


def even_odd():
   #Getting inputs 
 num=int(input("\n👉Enter an integer:"))
  #condition making 
 if num%2==0:
     print(f"The number {num} you entered is even number")
 else:
     print(f"The number {num} you entered is odd number")


def simple_calculation():
   num1=float(input("\n👉Enter the first num:"))
   num2=float(input("👉Enter the second num: "))
   oprator=input("👉Enter the oprator (/,*,-,+):")
   if oprator=="/":
      print(f"Result:{num1/num2}")
   elif oprator=="*":
      print(f"Result:{num1*num2}")
   elif oprator=="-":
      print(f"Result:{num1-num2}") 
   elif oprator=="+":
      print(f"Result:{num1+num2}")
   else:
      print("Invalid oprator...")


def largest_num():
   x=float(input("\n👉Enter the first number:"))
   y=float(input("👉Enter the second number:"))
   z=float(input("👉Enter the third number:"))
   #making the condition 
   max=x 
   if y>max:
      max=y 
   if z>max:
      max=z
   print(f"The largest number is: {max}")
    

def uppeercase_lowercase():
   ch=input("\n👉Enter a single character: ")
  #Making condition 
   if ch>='A'and ch<='Z':
      print(f"The character {ch} you entered is an : UPPERCASE CHARACTER")
   elif ch>='a'and ch<='z':
      print(f"The character {ch} you entered is an : lowercase character")
   elif ch>='0'and ch<='9':
      print(f"The character {ch} you entered is an : digit")
   else:
      print(f"The character {ch} you entered is an : special character")


def speed():
   distance=float(input("\n👉Enter the distance covered (in meters):"))
   time=float(input("👉Enter the time taken(in seconds):"))
   speed=distance/time #formula for speed 
   if time==0:
      print("Time cannot be zero.")
   else:
      print(f"The speed of the object is: {speed} m/s")


def velocity():
   displacement=float(input("\n👉Enter the displacement covered (in meters):"))
   time=float(input("👉Enter the time taken(in seconds):"))
   direction=input("👉Enter the direction of motion(e.g., North,East etc):")
   velocity=displacement/time #formula for velocity 
   if time==0:
      print("Time cannot be zero.")
   else:
      print(f"The velocity of the object is: {velocity} m/s, towards {direction}")


def roll_the_dice():
   
   print("\nlets roll the dice to make the game going...")
   i=0
   while i<5:  
    input("press enter to roll the dice🎲:")
    print(f"you got:{random.randint(1,6)}") #using this we get random number between 1-6 
    i+=1


def clock():
   today= datetime.datetime.now().time()
   date= datetime.date.today()
   print(f"\nCurrent time: {today}")
   print(f"Date: {date}")


def BMI():
   
   weigth_in_kg=int(input("\n👉Enter the weigth(in kg):"))
   height_in_meters=int(input("👉Enter the heigth(in metres):"))
   bmi=weigth_in_kg/pow(height_in_meters,2)
   print(f"Your BMI is: {bmi}")


def guessing_game():
   # A simple number guessing game 

  

  number= random.randint(10,50) # this will generate a number randomly within the range 10-50
  ctr=0
  while ctr<5:
    guess=int(input("\nGuess a number in range (10...50):"))
    if guess==number:
        print("You win! 😊 ")
        break
    else:
        ctr += 1 
  if not ctr<5: #i.e, whethernthe loop terminated after 5 iteration
     print(f"You lose 😩 \n The number was: {number}")


def vote():
   age=int(input("\nEnter your age:"))
   
   if age>=18:
      print("Hooray!🎉Your are eligible to vote")
   elif age<=18:
      yer=18-age
      print(f"You are not eligible you will be eligible after {yer} year.")
   else:
      print("Invald input!")


def list_of_things():
   print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
   print("List of things what this multitasker can do:\n")
   print("1.Area of rectangle")
   print("2.Find hypotneuse of triangle")
   print("3.To print table of any number")
   print("4.Area or perimeter of circle")
   print("5.To check even or odd")
   print("6.To do simple calculations")
   print("7.To check largest number between three num")
   print("8.To check uppercase or lowercase")
   print("9.To calculate speed of object")
   print("10.To calculate the velocity of object")
   print("11.Roll the dice for your ludo game")
   print("12.To check the time")
   print("13.To check BMI")
   print("14 play a guessing game")
   print("15 To check if you are eligible to vote")
   print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")


#----------------------------------------MAIN PROGRAM------------------------------------------------------


os.system("cls")
time.sleep(1)

print(f"{Fore.YELLOW+Style.BRIGHT}\t\t>===========[MULTITASKER]===========<\n\n")

print(f"{Fore.LIGHTBLUE_EX+Style.DIM}\n[Welcome to multitasker]")
list_drop_down=input("Press enter to see the list of things this can do:")
time.sleep(1)
list_of_things()

def main():
   while True:
    Choice=input("\nEnter the option number which you want to do(1to15) or(q)to exit:")
 
    if Choice=="1":
     time.sleep(0.9)
     print("Initating...")
     time.sleep(1)
     print("Done")
     Rectangle_area()

    elif Choice=="2":
     time.sleep(0.9)
     print("Initating...")
     time.sleep(2)
     print("Done")
     hypotneuse_of_triangle()

    elif Choice=="3":
     time.sleep(0.9)
     print("Initating...")
     time.sleep(2)
     print("Done")
     table()

    elif Choice=="4":
     time.sleep(0.9)
     print("Initating...")
     time.sleep(2)
     print("Done")
     area_or_perimeter()

    elif Choice=="5":
     time.sleep(0.9)
     print("Initating...")
     time.sleep(2)
     print("Done")
     even_odd()

    elif Choice=="6":
     time.sleep(0.9)
     print("Initating...calculator")
     time.sleep(2)
     print("Done")
     simple_calculation()

    elif Choice=="7":
     time.sleep(0.9)
     print("Initating...")
     time.sleep(2)
     print("Done")
     largest_num()

    elif Choice=="8":
     time.sleep(0.9)
     print("Initating...")
     time.sleep(2)
     print("Done")
     uppeercase_lowercase()
     
    elif Choice=="9":
     time.sleep(0.9)
     print("Initating...")
     time.sleep(2)
     print("Done")
     speed()

    elif Choice=="10":
     time.sleep(0.9)
     print("Initating...")
     time.sleep(2)
     print("Done")
     velocity()

    elif Choice=="11":
     time.sleep(0.9)
     print("Initating...")
     time.sleep(2)
     print("Done")
     roll_the_dice() 

    elif Choice=="12":
     time.sleep(0.9)
     print("Initating...")
     time.sleep(2)
     print("Done")
     clock()

    elif Choice=="13":
     time.sleep(0.9)
     print("Initating...")
     time.sleep(2)
     print("Done")
     BMI() 

    elif Choice=="14":
     time.sleep(0.9)
     print("Initating...")
     time.sleep(2)
     print("Done")
     guessing_game()

    elif Choice=="15":
     time.sleep(0.9)
     print("Initating...")
     time.sleep(2)
     print("Done")
     vote()
    elif Choice=="q":
     ask=input("\nDO YOU WANT TO EXPLORE OUR ANOTHER APPS ALSO(Y/N):")
     if ask=="Y" or "y" :
        os.system("cls")
        import Task_management_app
        break
     else:
       print("THANKS FOR USEING THE APP.HAVE A NICE DAY.")
       break 
      
    else:
     print("Invalid choice?")

main()