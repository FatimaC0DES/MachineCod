x0 = ' Zombie Protection System'
bubble = '*' * len(x0)
print('{0}{0}{0}\n{0}{1}{0}\n{0}{0}{0}'.format(bubble,x0))
print('\n ****************\n Fatima Hameed.\n ****************') 
x1 ='My Program would help you Identify your target '
bubble2 = '=' * len(x1)
print('{1}{0}'.format(bubble2,x1))


def main():
    yescount = []
    def questionaire():
        while True:
            try:
                answer = str(input("Enter y for yes and n for no; "))
                if answer[0].lower() not in ['y','n']:
                    raise Exception("Invalid input")
            except Exception as e:
                print(str(e))
            else:
                break
        if answer[0].lower() == 'y':
            yescount.append(answer[0])
            return True
        elif answer[0].lower() == "n":
            return False
    
    Questions = ["Does the subject have a glazed over look?","Is the subject moaning?","Is the subject missing any limbs?","Does the subject have pale or gray skin?","Does the subject have any exposed organs?","Is the subject on fire without showing pain?","Does the subject show little response to objects in its path?","Is the subject limping?","Is the subject wearing a jacket with shoulder pads?","Does subject crave brains and its not the first full week of October?"]
    for i in Questions:
        print(i)
        questionaire()
    print(yescount)
    print(len(yescount))

    Prob = (len(yescount)/10) * 100
    print("The probability is {}% ".format(Prob))

    if Prob>50:
        print("The target is likely a Zombie...RUN FOR YOUR LIFE")
    elif Prob<50:
        print("The target is an ally...You're safe")
        
main()

while True:
    restart= input("Do you wish to identify another target...y for Yes and n for No:  ")
    if restart[0].lower() == 'y':
        main()
    elif restart[0].lower() == 'n':
        print("Thank You for using my Zombie protection Program")
        break
    
    




