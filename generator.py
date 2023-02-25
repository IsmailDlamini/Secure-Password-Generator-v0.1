
import random

#pass1 = ""

#s1 = "off"
#s2 = "on"
#s3 = "on"

def generate_password_file(password, pass_len, u_let, u_num, u_spec):

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "123456789"
    characters = "!@#$%&"

    choices = [letters,numbers,characters]
    store = []

    let = list(letters)
    nums = list(numbers)
    chars = list(characters)

    
    if u_let == "on" and u_num == "on" and u_spec == "on":
        for i in range(pass_len):
            decider = random.randint(0,2)
            if decider == 0:
                store.append(let[random.randint(0, 51)])

            if decider == 1:
                store.append(nums[random.randint(0, 8)])

            if decider == 2:
                store.append(chars[random.randint(0, len(chars) - 1)])


        new_pass = ''.join(store)
        final_pass = password
        return(new_pass)

    elif  u_let == "on" and u_num == "on" and u_spec == "off":

        for i in range(pass_len):

            decider = random.randint(0,1)
            if decider == 0:
                store.append(let[random.randint(0, 51)])

            if decider == 1:
                store.append(nums[random.randint(0, 8)])

        new_pass = ''.join(store)
        final_pass = password
        return(new_pass)

    elif u_let == "on" and u_spec == "on" and u_num == "off":

        for i in range(pass_len):

            decider = random.randint(0,1)
            if decider == 0:
                store.append(let[random.randint(0, 51)])

            if decider == 1:
                store.append(chars[random.randint(0, len(chars) - 1)])

        new_pass = ''.join(store)
        final_pass = password
        return(new_pass)

    
    elif u_num == "on" and u_spec == "on" and u_let == "off":
        for i in range(pass_len):
            decider = random.randint(0,1)
            if decider == 0:
               store.append(nums[random.randint(0, 8)]) 

            if decider == 1:
               store.append(chars[random.randint(0, len(chars) - 1)])

        new_pass = ''.join(store)
        final_pass = password
        return(new_pass)


    elif u_let == "on" and u_num == "off" and u_spec == "off":
        for i in range(pass_len):
            count = random.randint(0, 2)
            store.append(let[random.randint(0, 51)])

        new_pass = ''.join(store)
        final_pass = password
        return(new_pass)


    elif u_let == "off" and u_num == "on" and u_spec == "off":
        for i in range(pass_len):
            count = random.randint(0, 2)
            store.append(nums[random.randint(0, 8)])

        new_pass = ''.join(store)
        final_pass = password
        return(new_pass)


    elif u_let == "off" and u_num == "off" and u_spec == "on":
        for i in range(pass_len):
            count = random.randint(0, 2)
            store.append(chars[random.randint(0, len(chars) - 1)])

        new_pass = ''.join(store)
        final_pass = password
        return(new_pass)


    

#print(generate_password_file(pass1, 15, s1, s2, s3))
    






