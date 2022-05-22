def check_phone_number(string):
    if len(string) != 12:
        return False
    for i in range(3):
        if not string[i].isdecimal():
            return False
    if string[3] != '-':
        return False
    for i in range(4, 7):
        if not string[i].isdecimal():
            return False
    if string[7] != '-':
        return False
    for i in range(8, 12):
        return bool(string[i].isdecimal())

string = input("Enter a Sentence: ")

for i in range(len(string)):
    split = string[i:i+12]
    if check_phone_number(split):
        print(f'Phone number has been found! : {split}')