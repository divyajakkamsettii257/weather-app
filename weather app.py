import random
import string

a=input("enter your name:").lower()
print(a)
b=int(input("entr your age:"))
if b>=10 and b<=200:
  print(b)
elif b<=5:
  print("sorry!..","your is",b,"so you dont have acess to use this app")
  print("THANK YOU FOR VISITING THE WEATHER APP")
  c=input("enter your Gender:").lower()
if c=="male" or c=="female" or c=="other":
  print(c)
else:
  print("sorry your gender is not recognizable")
d=input("enter your emai_id:")
if "@" in d and d.endswith("gmail.com"):#to change the condition to check for @ and gmail.com and to compare two strings at a time
  print("valid email_id:", d)
else:
  print("invalid emai_ld",d)
e=input("enter your mobile number:")
if e.isdigit() and len(e) == 10:
  print(f"Valid mobile number: {e}")
  otp = "".join(random.choice(string.digits) for i in range(4))
  print(f"Your OTP is: {otp}")
  e1=input("enter your 4 digits otp for verfication purpose:")
  if len(e1) == 4 and e1 == otp:
    print("thank you for choosing WEATHER APP",e1)
  else:
    print("invalid otp please enter valid input")

else:
  print("invalid mobile number")
  print("THANKYOU FOR VISITING  THE WEATHER APP")

while True:
   try:
    temperature_in_fahrenheit=int(input("enter your current temperature in fahrenheits:"))
    temperature_in_celsius=int(input("enter your current temperature in celsius"))
   except ValueError:
    print("Please enter a valid numeric temperature value.")
    continue
   if temperature_in_fahrenheit>=1 and temperature_in_fahrenheit<=30  or temperature_in_celsius>=-1 and temperature_in_celsius<=-100:
    print(a,"your current weather report is")
    print("Commom Weather Discription:Snow o frost,cloudy or clear")
    print("What it feels like:Very cloud, possibly freezing")
    print("THANK YOU FOR VISITING THE WEATHER APP")
    break
   elif temperature_in_fahrenheit>=31 and temperature_in_fahrenheit>=40 or temperature_in_celsius>=1 and temperature_in_celsius<=4:
    print(a,"your current weather report is")
    print("Common Weather Discription:Cool day,cloudly or breezy")
    print("What it feels like:Cool, need a jacket")
    print("THANK YOU FOR VISITING THE WEATHER APP")
    break
   elif temperature_in_fahrenheit>=41 and temperature_in_fahrenheit<=50 or temperature_in_celsius>=5 and temperature_in_celsius<=10:
    print(a,"your current weather report is")
    print("Common Weather Discription:Mild,partly sunny")
    print("What it feels like: Cool, light sweater weather")
    print("THANK YOU FOR VISITING THE WEATHER APP")
    break
   elif temperature_in_fahrenheit>=51 and temperature_in_fahrenheit<=60 or temperature_in_celsius>=11 and temperature_in_celsius<=16:
    print(a,"your current weather report is")
    print("Common Weather Discription:Often sunny or cloudly")
    print("What it feels like:Mild, comfortable")
    print("THANK YOU FOR VISITING THE WEATHER APP")
    break
   elif temperature_in_fahrenheit>=61 and temperature_in_fahrenheit<=70 or temperature_in_celsius>=17 and temperature_in_celsius<=21:
    print(a,"your current weather report is")
    print("Common Weather Discription:Sunny, great outdoor weather")
    print("What it feels like:Warm and pleasant")
    print("THANK YOU FOR VISITING THE WEATHER APP")
    break
   elif temperature_in_fahrenheit>=71 and temperature_in_fahrenheit<=80 or temperature_in_celsius>=22 and temperature_in_celsius<=27:
    print(a,"your current weather report is")
    print("Common Weather Discription:Sunny, summer-like")
    print("What it feels like:Hot, may start to sweat")
    print("THANK YOU FOR VISITING THE WEATHER APP")
    break
   elif temperature_in_fahrenheit>=81 and temperature_in_fahrenheit<=90 or temperature_in_celsius>=28 and temperature_in_celsius<=32:
    print(a,"your current weather report is")
    print("Common Weather Discription:Heat, sun, drink water!")
    print("What it feels like:Very hot")
    print("THANK YOU FOR VISITING THE WEATHER APP")
    break
   elif temperature_in_fahrenheit>91 and temperature_in_fahrenheit<=100 or temperature_in_celsius>=33 and temperature_in_celsius<=38:
    print(a,"your current weather report is")
    print("Common Weather Discription:Heatwave, stay cool indoors")
    print("What it feels like:Extremly hot, can be dangerous")
    print("THANK YOU FOR VISITING THE WEATHER APP")
    break
   else:
    print("you entered in valid temperature plaese enter valid temperature:")


