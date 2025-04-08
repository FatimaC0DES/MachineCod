
import math






print("**********************************************")
print("Daylight-Sensitive Zombie Protection System")
print("*********************************")
print("This program will calculate sunrise and sunset time for any date and location")
print("===================================================================================")
print('This zombie protection system was created by; \n Datalla Muhammad.\n Fatima Hamaeed.\n Tisan Lucas.\n Charlotte Mgbe.\n Fadlullah Yunusa.\n Bilaal Mustapha')





latitude=float (input('input your latitude remember +=north and -=south: '))

longtitude=float (input('input your longtitude remember +east and -=west:'))

timezone=float (input('input your time zone:'))

dayofyear=float (input('input the day of the year:'))

n=3.1415926

y=((2*n/365)*(dayofyear-1))

eqtime=(229.18*(0.000075+0.001868*math.cos(y)-0.032077*math.sin(y)-0.014615*math.cos(2*y)-0.040849*math.sin(2*y)))

decl=0.006918-0.399912*math.cos(y)+0.070257*math.sin(y)-0.006758*math.cos(2*y)+0.000907*math.sin(2*y)-0.002697*math.cos(3*y)+0.00148*math.sin(3*y)

ha=math.acos((((math.cos(1.5853))/(math.cos(latitude*(n/180))*math.cos(decl))-math.tan(latitude*n/180)*math.tan(decl))))*180 /n

sunrise=720+4*(longtitude-ha)-eqtime-(60*timezone)

sunset=720+4*(longtitude+ha)-eqtime-(60*timezone)

sunrisehour=int((sunrise/60))

sunriseminute=int(sunrise-(sunrisehour*60))

sunsethour=int((sunset/60))

sunsetminute=int(sunset-(sunsethour*60))

print("---------------------------------")
print("---------------------------------")

print('sunrise',sunrisehour,':',sunriseminute)

print('sunset',sunsethour,':',sunsetminute)

print("---------------------------------")
print("---------------------------------")

print('Thank you for using our zombie protection system')

print("---------------------------------")
