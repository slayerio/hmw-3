#hmw 3 answers

#1.
print("for the job applications, we are going to ask for a few dry questions");
id = int(input("id"));
name =input("first name");
ln = input("last name");
height = int(input("height (in cm)"));
year = int(input("birth year"));


print(f"your stats are: #id {id}, first name {name}, last name {ln}, height {height}, birth year {year}")

#2.
x = int(input("whats your final grade?"));


if 96 <= x <= 100:
   print("excellent work!");
elif 81 <= x <= 95:
   print("nice job");
elif 61 <= x <= 80:
   print("not good not bad");
elif 41 <= x <= 60:
   print("did you do your homework?");
elif 0 <= x <= 40:
   print("how?");
else:
   print("invalid grade")





















#3.
vol = int(input("select volume level (1-10 whole num)"))


match vol:
   case 0:
       print("mute");
   case 1:
       print("very quite it is");
   case 2:
       print("very quite it is");
   case 3:
       print("quite it is");
   case 4:
       print("moderately quite");
   case 5:
       print("medium");
   case 6:
       print("medium");
   case 7:
       print("moderately loud");
   case 8:
       print("loud");
   case 9:
       print("very loud");
   case 10:
       print("extremely loud")
   case _:
       print("Invalid. please select a whole number 1-10");





#4.
x = int(input("selecta number"));
print(f"{'NOT' if not x % 7 ==0 else ''} seven boom")




#5.
x = int(input("select a number"));
if not x % 5:
   print("Fizz", end=' ');
if not x % 3:
   print("Buzz");





#bonus:

x = int(input("how many pizza slices left?"))
fr: int = 4;


if x % fr == 0:
   print(f"there are {x/fr} slice for a friend")
else:
   print(f"there are {x//fr} slice for a friend, {x % 4} remained")


x = int(input("how many pizza slices left?"))
fr = int(input("how many friends"))


if x % fr == 0:
   print(f"there are {x//fr} slice for a friend")
else:
   print(f"there are {x//fr} slice for a friend, {x % fr} remained")


