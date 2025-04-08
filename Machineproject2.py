x0 = ' Zombie Protection System'
bubble = '*' * len(x0)
print('{0}{0}{0}\n{0}{1}{0}\n{0}{0}{0}'.format(bubble,x0))
print(' Peter Anthony.\n ****************\n Fatima Hameed.\n ****************\n Aisha Muhammad.\n ****************\n Beauty Wasem.\n ***************\n Junior Godwin Udu.\n ****************\n Olasunkanmi Bolutife.\n ****************\n This group teamed up to generate a program to save the world\n *************************************************************************************************=========================') 
x1 ='We will calculate your foraging missions '
bubble2 = '=' * len(x1)
print('{1}{0}'.format(bubble2,x1))

weight = float(input("Enter survivor's weight: "))
intensity = float(input("Enter the intensity of activity: "))
time = float(input("Enter the minutes of activity: "))
calories = float(input("Enter the number of calories available in food: "))

def basel(weight):
    return (weight/2.2) * 24.2
    
def calrequired(intensity,weight,time):
    return 0.0385 * intensity * weight * time

x =calrequired(intensity,weight,time)

totalenergy = (basel(weight)+x)/0.9
serve = totalenergy/calories

print('For the activity, the survivor will need %.0f Calories' %(totalenergy))

print('To maintain their weight, they will need to consume %.0f serving of food' %(serve))

print("---------------------------------")
print("---------------------------------")
print("---------------------------------")
print('Thank you for using our zombie protection system')
print("------------------------------------------------")
x3 = 'STAY SAFE, DONT GET EATEN BY VAMPIRE ZOMBIES'
bubble3 = '*' * len(x3)
print('{0}{0}{0}\n{0}{1}{0}\n{0}{0}{0}'.format(bubble3,x3))
