import random

def generate():
 first = first_name.lower()
 middle = middle_name.lower()
 last = last_name.lower()

 username1 = first+middle+last
 username2 = first+"."+middle+"@"+last
 username3 = first+"!"+middle+"!"+last
 username3 = first+"$"+middle+last
 username4 = first+middle+"#"+last
 username5 = first[0:3]+middle[0:3]+last[0:3]
 username6 = first[0:2]+"."+middle[-1]+"~"+last[-1:-3]
 num = random.randint(0,99)
 username7 = first+str(num)+middle[0:3]+"£"+last
 username8 = first + last + middle
 username9 = last + first + middle
 username10 = first + middle + last + str(num) +str(num) + str(num)
 usernames = [username1,username2,username3,username4,username5,username6,username7,username8,username9,username10]
 return random.choice(usernames)
while True:
    first_name = input("What is your first name? (type 'exit' to leave)")
    if first_name == "exit":
       break
    middle_name = input("What is your middle name? ")
    last_name = input("What is your last name? ")
    name = generate()
    print("Your randomly generated user name is:",name)
