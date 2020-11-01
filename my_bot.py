def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def color():
    print('Now tell me more about you.')
    print('Which colour do you like ?.')
    y = input()
    print("You love the colour", y)


def phone():
    print('Lets see which phone you use ?.')
    phones = ["Apple", "Samsung", "Micromax", "Oppo", "Vivo", "Oneplus", "GooglePixel"]
    for x in range(len(phones)):
        print((x + 1), '. ', phones[x])

    y = int(input())
    if y <= 0 or y > len(phones):
        print('Please choose correct option !')
        return True
    else:
        print("You own  the phone brand", phones[y - 1])
        return False


def broadband():
    brands = ['Airtel', 'Jio', 'Vodafone', 'Idea', "At@T"]
    print("Let's test your home usage of Broadband.")
    print("Which broadband do you use ?")
    for x in range(len(brands)):
        print((x + 1), '. ' + brands[x])
    y = int(input())
    if y <= 0 or y > len(brands):
        print('Please choose correct option !')
        return True
    else:
        print("Welcome to", brands[y - 1], ", have a nice day!")
        return False


def end():
    print('Congratulations, have a nice day!, We will meet you again')


greet('India', '2020')  # change it as you need
remind_name()
guess_age()
color()
while phone():
    phone()
while broadband():
    broadband()
# ...
end()
