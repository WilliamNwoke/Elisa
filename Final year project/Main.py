print("""
	IIIIIIII   II	   II   IIIIII      II
	II	   II	   II   II         IIII
	IIIIIIII   II	   II   IIIIII    II__II
	II	   II      II       II   II    II
	IIIIIIII   IIIIII  II   IIIIII  II      II
""")
import time
def CGPA():
    Courses = list()
    Course = input("Enter the number of courses you offer: ")
    print ("Input your courses code: ")
    for i in range(int(Course)):
        n = input("Course : ")
        Courses.append(int(n))
    print('Courses',Courses)

#print ("Please reply in lower case....")
#print ("I do not remember the function for lowercase only....")
print("WELCOME TO ELIZA")
print("For '0' errors, reply in lowercase")
time.sleep(0.2)
print(".....LOADING.......")
cgpa=input("Do you want to input your courses: \nyes or no\n ")


def behave():
        Q1 = input("Are you an extrovert: \nYes or no \n")
        if (Q1 == "yes"):
            Q2 = input("Are you the first to speak in a conversation,group or gathering?: \nyes or no \n")
            if Q1 ==    "yes":
                Q3 = input("Are you a good sales man type or marketer: \nyes or no \n")
                if(Q3=="yes"):
                    print("You are a Sanguine")
            if (Q2 == "no"):
                if(Q3=="no"):
                    Q4 = input("Are you a strong natural leader: \nyes or no \n")
                    #create an else statement for the Question
                if (Q4 == "yes"):
                    print("You are probably a choleric")
        elif (Q1 == "no"):
            Q5 = input("Are you a perfectionist, analytical and somewhat critical: \nyes or no \n")
            if (Q5 == "yes"):
                print("you are probably predominantly a melancholy")
            elif (Q5 == "no"):
                Q6 = input("Are you known by others as quiet? "
                           "Do you rarely get angry but experience many fears and worries? "
                           "yes or no \n")
                if (Q6 == "yes"):
                    print("You are probably a plegmatic")

def behave2():

        Q1 = input("Are you an extrovert or an introvert: \n ")
        if Q1 == "extrovert" or Q1 == "Extrovert":
            Q2=input("Are you a spontaneous quick-talker: \nyes or no\n")
            Q3=input("Do you have to apologize frequently: \nyes or no\n")
            Q4=input("Do you have high emotional response: \nyes or no\n")
            if Q2=="yes" and Q3=="yes" and Q4=="yes":
                print("You are probably a sanguine")

            elif Q2=="yes" or Q3=="yes" or Q4=="yes":
                print("You are probably a choleric")


        elif Q1=="Introvert" or Q1=="introvert":
            Q5=input("Are you quiet and slow of speech: \nyes or no\n")
            Q6=input("Are  you a good speller: \nyes or no\n")
            Q7=input("Do you do well at math and detail: \nyes or no\n")
            Q8=input("Do you get depressed easily: \nyes or no\n")

            if Q6=="yes" and Q7=="yes" and Q8=="yes":
                print("You are probably a melancholic")
            elif Q5=="yes" and Q8=="no":
                print("You are probably a phlegmatic")

print(".....LOADING.......")
#CGPA() if cgpa == "yes" else print("Temperament test")
print(".....LOADING.......")
time.sleep(1.5)
behave()
print("")
sure=input("Do you want to take a second test:\n yes or no\n")
print(".....LOADING.......")
time.sleep(1.5)

behave2() if sure =="yes" else print("\nOk thanks for the test")
print("Bye")
time.sleep(4)

