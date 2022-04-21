x = "Mish" or "Abigail"
y = ""
while True:
    y = input(f"The road to {x} is full of obstacles:")
    if y == x:
        print("John weds Mish! ")
        break
    elif y != "John":
        y = False
        print(" John breaks up with Mish! ")
        break
    else:
        print(" Powerful couple")
        break
else:
    print("Who will marry Mish ? ")


for item in "Python":
    print(item)
for item in ["pam","Novice","John"]:
    print(item)
for item in range(5,15):
    print(item)
for item in range(5,15,):
    print(item)


prices = [10,20,30]
total = 0
for price in prices:
    total += price
    print(f"total:{total}")
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

numbers = [5,2,5,2,2]
for x in numbers:
    print("x"* x)
print(" Mary has a liitle lamb. ")

numbers = [5,2,5,2,2]
output = ""
for x in numbers:
    output += "x"
    for count in range(x):
        print(output)
print("Humpty dumpty sat on a wall. ")

numbers = [5,2,5,2,2]
for x_count in numbers:
    output= ""
    for count in range(x_count):
        output += "x"
        print (output)
#according to the tutorial
#it is not working well though!
names = ["john","Posh","Kim, Juan, Rodrigo"]
print(names[2:])
print([names[:]])

numbers = [3,5,8,10,]
max = numbers[0]
for number in numbers:
    if number > max :
        max = number
        print(max)
# it is still not working well

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][1] =20
print(matrix[0][1])
for row in matrix:
      for item in row:
          print(item)

numbers = [4,5,8,9]
numbers.append(9)
numbers.insert(0,99)
numbers.remove(5)
print(numbers)
print(50 in numbers)
numbers.sort()
print(numbers)


numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number is not uniques:
        uniques.append(number)
print(uniques)
#it is still not working like in the tutorial!!

coordinates = (2,5,7)
x,y,z = coordinates
print(y)

customer = {
    "name":"Conrad Jenes",
    "age": 40,
    "is_verified":True
}
print(customer["name"])
print(customer.get("birthdate","Jan 1 1990"))

phone = input("Phone: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3":"three",
    "4":"four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch,"!") + " "
print(output)
# still not working

message = input(">")
words = message.split(" ")
emojis = {
    ";)" : "smiley",
    ":(" : " sad face"
}
output =""
for word in words:
   output += emojis.get(word,word)
print(output)