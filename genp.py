import random
import string


def generate_password(length=random.randint(12, 16)):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    puncts = string.punctuation
    digits = string.digits

    # all_characters = uppercase+lowercase+puncts+digits

    character_list = []
    iteration_number = 1
    for i in range(length):
        if iteration_number == 1:
            character = random.choice(uppercase)
        elif iteration_number == 2:
            character = random.choice(lowercase)
        elif iteration_number == 3:
            character = random.choice(puncts)
        elif iteration_number == 4:
            character = random.choice(digits)
        else:
            iteration_number = 1
        # character = random.choice(all_characters)
        character_list.append(character)
        iteration_number += 1

    random.shuffle(character_list)
    password = "".join(character_list)

    return password


if __name__ == '__main__':

    while True:
        print(generate_password(int(input('Enter password length: '))))
