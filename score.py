def score():

    while  True: 
      try:
        n= int(input("please enter your score in high school (1-20):"))
        if 0 <= n <= 20:
         break
        else:
             print(" Wrong,Wrong,  You have to put a number from 0 to 20🧨") 
      except ValueError:
              print("again")
              
    if n == 20:
        print("Wow i just  can tell you, you are the best student i've ever witness in my life")
    elif n >= 19:
        return " You were so close to twenty you are so awesome😉"
    elif n >= 18:
        return " Oh that wonderful score you have been improved🙌"
    elif n >= 17:
        return "You did your best bro, you can get 20 if you improve your feature❤"
    elif n >= 16:
        return "Don't worry this is fantastic score👌 "
    elif n >= 15:
        return "It was good however you have to enhance your skills💕"
    elif n >= 14:
        return "Thats not bad you can get better score👍"
    elif n >= 11:
        return "This is not good you should change this situation🤦"
    elif n >= 10:
        return "Atleast you got a ten and now you can pass exam perfect😁"
    elif n >= 9:
        return "You are awful you can't get your dream😒"
    elif n >= 5:
        return "I dont know why you coming school🙄"
    elif n >= 0:
        return "WTf bro how did you even do that🤯"
result = score()
print(result)
