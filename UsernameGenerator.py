import random
def generate(full_name):
    name_parts = full_name.split()
    if len(name_parts) < 2:
        return "Please enter your FULL name with a space in between them"
    
    first_name = name_parts[0].lower()
    last_name = name_parts[-1].lower()

    username1 = first_name+last_name
    username2 = first_name+"/"+last_name
    username3 = first_name+"."+last_name
    username4 = first_name+"@"+last_name
    username5 = first_name+"~"+last_name
    username6 = first_name+"~"+last_name
    username7 = first_name[0:3]+last_name[0:3]
    num = random.randint(0,99)
    username8 = first_name+str(num)+last_name

    usernames = [username1,username2,username3,username4,username5,username6,username7,username8]
    return random.choice(usernames)

while True:
    full_name = input( "Please enter your FULL NAME and please have spaces in between them or type 'exit' to quit " )
    if full_name.lower() == "exit":
        break

    username = generate(full_name)
    print("Your Randomly generated username is:",username )