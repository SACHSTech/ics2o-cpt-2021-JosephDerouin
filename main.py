# Defining Score variables 
x = 0
score = x

# Disclaimer - in the code if you see 'print(" ")', that is so there is a puase in the output

# Introduction
print(" ")
print("Welcome to Joseph's python quiz, made in VSCode! There are 20 questions, but 2 parts to the quiz...")
print("The first 10 questions are computer related questions. Each question relates back to what we did in class, so hopefully you payed attention!")
print("The next 10 questions are math related questions. No calculators are allowed!!!")
print("At the end it will tell you your total grade, %, and wether you passed. Good luck!")
print(" ")

# Question One 
print("What is the type of software called in a computer that is dedicated to viewing/browsing the internet?")
answer_1 = input("a)Programming IDEs\nb)Web Browser\nc)MultiMedia\nd)Design\n:")
if answer_1.lower() == "b" or answer_1.lower() == "Web Browser":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, it is called a Web Browser")

print(" ")
print("Next Question")
print(" ")

# Question Two
print("What is the type of software called in a computer that provides the platform for all other software and hardware to operate on a computer?")
answer_2 = input("a)Utility\nb)Computer\nc)Operating System\nd)Graphics Card\n:")
if answer_2.lower() == "c" or answer_2.lower() == "Operating System":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, it is called an Operating System")

print(" ")
print("Next Question")
print(" ")

# Question Three
print("True or False... a virus is a type of malware?")
answer_3 = input(":")
if answer_3.lower() == "true" or answer_3.lower() == "t":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")
  
print(" ")
print("Next Question")
print(" ")

# Question Four
print("What does a graphics card do?")
answer_4 = input("a)Accelerates the creation and rendering of images, video, and animations.\nb)Potato\nc)Makes Computer Faster\nd)Makes the computer brighter\n:")
if answer_4.lower() == "a" or answer_4 == "Makes graphics look nicer":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, a graphics card accelerates the creation and rendering of images, video, and animations.")

print(" ")
print("Next Question")
print(" ")

# Question Five 
print("True or False... Any mother bord is compatable with any CPU?")
answer_5 = input(":")
if answer_5.lower() == "false" or answer_5.lower() == "f":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, only certain brands of motherboards are compatable with certain brands of CPU's")

print(" ")
print("Next Question")
print(" ")

# Question Six
print("What is the main difference of a computer and a laptop?")
answer_6 = input("a)One is bigger\nb)One is very mobile while one is stationary\nc)One is better\nd)One is always plugged in\n:")
if answer_6.lower() == "b" or answer_6.lower() == "One is very mobile while one is stationary":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, one is very mobile while one is stationary")

print(" ")
print("Next Question")
print(" ")

# Question Seven
print("If you were to build a whole new PC, how many parts are required in order for the computer to succesfuly run?")
answer_7 = input("a)3\nb)4\nc)5\nd)6\n:")
if answer_7.lower() == "c" or answer_7.lower() == "5":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, you need a storage, motherboard, memory, CPU, video card. (Which is 5 in total)")

print(" ")
print("Next Question")
print(" ")

# Question Eight
print("True or False... A laptop also requires all 5 of the main computer parts?")
answer_8 = input(":")
if answer_8.lower() == "true" or answer_8.lower() == "t":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")  

print(" ")
print("Next Question")
print(" ")

# Question Nine
print("Who invented the Apple-1?")
answer_9 = input("a)Steve Jobs and Steve Wozniak\nb)Bill Gates\nc)Wayne Gretzky\nd)Lebron James\n:")
if answer_9.lower() == "a" or answer_9 == "Steve Jobs and Steve Wozniak":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, it was Steve Jobs and Steve Wozniak. It was the very first computer they built.")

print(" ")
print("Next Question")
print(" ")

# Question Ten 
print("True or False... A CPU is an operating system?")
answer_10 = input(":")
if answer_10.lower() == "false" or answer_10.lower() == "f":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")

print(" ")
print(" ")
print("Next is Math Quiz")
print(" ")
print(" ")


# Question Eleven
print("What is 1 + 1?")
answer_11 = input("a)1\nb)2\nc)3\nd)4\n:")
if answer_11.lower() == "b" or answer_11.lower() == "2":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, it is 2")

print(" ")
print("Next Question")
print(" ")

# Question Twelve
print("What is 4 x 4?")
answer_12 = input("a)12\nb)18\nc)16\nd)10\n:")
if answer_12.lower() == "c" or answer_12.lower() == "16":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, it is 16")

print(" ")
print("Next Question")
print(" ")

# Question Thirteen
print("True or False... 16 - 40 is -24?")
answer_13 = input(":")
if answer_13.lower() == "true" or answer_13.lower() == "t":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")
  
print(" ")
print("Next Question")
print(" ")

# Question Fourteen
print("What is 90 - 3 x 4?")
answer_14 = input("a)78\nb)90\nc)85\nd)86\n:")
if answer_14.lower() == "a" or answer_14 == "78":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, it is 78")

print(" ")
print("Next Question")
print(" ")

# Question Fifteen
print("True or False... 100 x 5 - 6 / 2 is 456?")
answer_15 = input(":")
if answer_15.lower() == "false" or answer_15.lower() == "f":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, it is 497")

print(" ")
print("Next Question")
print(" ")

# Question Sixteen
print("what is 89 - (6 x 4)?")
answer_16 = input("a)60\nb)65\nc)70\nd)75\n:")
if answer_16.lower() == "b" or answer_16.lower() == "65":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, it is 65")

print(" ")
print("Next Question")
print(" ")

# Question Seventeen
print("X = 4, What is 4X?")
answer_17 = input("a)10\nb)6\nc)16\nd)26\n:")
if answer_17.lower() == "c" or answer_17.lower() == "16":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, you need a power supply, storage, motherboard, memory, CPU, video card. (Which is 6 in total)")

print(" ")
print("Next Question")
print(" ")

# Question Eighteen
print("True or False... X = 2, is 7X + (7 x 4 - 3) - 6 = 33?")
answer_18 = input(":")
if answer_18.lower() == "true" or answer_18.lower() == "t":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, it is true")  

print(" ")
print("Next Question")
print(" ")

# Question Nineteen
print("X = 9, What is 3X + ((5 + 6 - 3)2 - 6)?")
answer_19 = input("a)37\nb)40\nc)12\nd)43\n:")
if answer_9.lower() == "a" or answer_19 == "37":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, it is 37")

print(" ")
print("Next Question")
print(" ")

# Question Twenty
print("True or False... X = 4, is 6X + (9 x 7) = 86?")
answer_20 = input(":")
if answer_20.lower() == "false" or answer_20.lower() == "f":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, it is 87")


# Computer Quiz Score
grade = float(x / 20) * 100
print(x,"out of 20, that is",grade, "%")

print(" ")

# Turning variable 'grade' from float to integer
grade = int(grade)

# Tells you your grade and if you passed or not
if grade <= 49 :
    print("Sorry, you didnt pass... you got an F")
elif grade >= 50 and grade <= 59 :
    print("You passed, and got a D")
elif grade >= 60 and grade <= 69 :
    print("You passed, and got a C")
elif grade >= 70 and grade <= 79 :
    print("You passed, and got a B")
elif grade >= 80 and grade <= 89 :
    print("You passed, and got an A!")
elif grade >= 90 and grade <= 100 :
    print("You passed, and got a A+!")

print(" ")

## this is the answer rythem ##
# b
# c
# true
# a
# false
