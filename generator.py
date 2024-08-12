
#Code written by Ismail Dlamini
#last updated 2024/08/12

import random

def generate_password_file(password, pass_len, u_let, u_num, u_spec):

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "123456789"
    characters = "!@#$%&"

    choices = []
    password_storage = []
   
    if u_let == "on" : choices.append(letters) # add letters to the choices if selected
    if u_spec == "on" : choices.append(characters) # add special letters to the choices if selected
    if u_num == "off" : choices.append(numbers) # add numbers to the choices if selected

    password_storage = []

    for i in range(pass_len):
            character_set_decider = random.randint(0, len(choices) - 1)
            character_decider = random.randint(0, len(choices[character_set_decider]) - 1)
            password_storage.append(choices[character_set_decider][character_decider])

    return "".join(password_storage)


    #copyright @ reserved Ismail Dlamini 2024
    






