#Test class
class Test:
    def __init__(self, name):
        self.name=name
        self.grade=0
        self.firstQ=None
        self.secondQ=None
        self.thirdQ=None
        self.fourthQ=None
    def checkFirst(self, answer):
        if answer==1911:
            self.firstQ=True
        else:
            self.firstQ=False
    def checkSecond(self, answer2):
        newanswer2=answer2.upper()
        if newanswer2=="ARVIND":
           self.secondQ=True
        else:
           self.secondQ=False
    def checkThird(self, answer3):
        newanswer3=answer3.upper()
        if newanswer3=="FLINT":
            self.thirdQ=True
        else:
            self.thirdQ=False
    def checkFourth(self, answer4):
        newanswer4=answer4.upper()
        if newanswer4=="ARMONK":
            self.fourthQ=True
        else:
            self.fourthQ=False
    def gradeTest(self):
        right=0
        wrong=0
        passorFail=None
        resultsArray=[self.firstQ, self.secondQ, self.thirdQ, self.fourthQ]
        for i in resultsArray:
            print(i)
            if(i==True):
                right=right+1
            else:
                wrong=wrong+1
        if right>2:
            passorFail="Congratulations You Passed!!"
        else:
            passorFail="Sorry you Failed Try again!"
        print(f"{passorFail} You got {right} question right and {wrong} wrong!!")


    


#Welcome user
print("Welcome to the four question IBM test?")


#Name Question
userName=input(str("What is your first name?: "))
##Set class object
testTaker=Test(userName)
print(f"Good Luck!! {testTaker.name}")



#First Question
try:
     answer1=int(input("What year was Ibm Founded(Integer Data Type): "))
except ValueError:
     print("Must be a Number!!")
     answer1=int(input("What year was Ibm Founded(Integer Data Type): "))
testTaker.checkFirst(answer1)


#Second Question
#Arvind
answer2=str(input("What is the first name of IBM's current CEO?: "))
testTaker.checkSecond(answer2)


#Third Question
answer3=str(input("What is the last name of the Founder of IBM?: "))
testTaker.checkThird(answer3)


#Fourth Question
answer4=str(input("What city is IBM headquarters located?: "))
testTaker.checkFourth(answer4)



testTaker.gradeTest()



 