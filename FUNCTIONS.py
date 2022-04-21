def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name} !")
    print("Welcome aboard")


print("start")
greet_user("John", last_name="Smith")
greet_user("Mary", "McDowell")
print("finish")


def square(number):
    return number * number


print(square(3))


def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        "smiley": ":)",
        "sadface": ":("
    }
    output = ""
    for word in emojis:
        output += emojis.get(word, word) + " "
        return output


message = input(">")
print( emoji_converter(message))

try:
    age = int(input( "Age: "))
    income = 2000/age
    print(age)
    print(income)
except ValueError:
    print("InvalidValue")
