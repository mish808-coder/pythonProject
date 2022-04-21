weight = int(input('Weight: '))
unit = input('(l)bs or (k)g : ')
if unit.upper() =="L" :
    converted = weight * 0.45
    print(f"You are{converted} kilos")
else:
    converted = weight / 0.45
    print(f" You are {converted} pounds")

weight = int (input('Sport:'))
Type_sport = input('Hands or Legs:')
if Type_sport.upper()== 'Hands':
    choice = weight * 1.25
    print(f" That's a  sporty {choice} I say!")
else:
    choice = weight /1.25
    print(f" Well, that {choice} is acceptable - I guess!")
#At this rate I'm going nowhere!

secret_number = 5
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print('You won ,you little champ!')
        break
else:
    print('You failed , you tried though!')
#This is a single step for MISH and a giant leap for mankind!

command = " "
started = False
while True:
    command = input(" > ").lower()
    if command == "start":
        if started:
         print("The car is already started.")
        else:
         started = True
        print(" car starts ")
    elif command == "stop":
        if not started:
            print("The car already stopped.")
        else:
            started = False
            print(" Car stopped.")
    elif command == "help":
        print("""
    start - car starts
    stop - car stops
    quit - exit game   
        """)

    elif command == "quit":
        print(" exit game .")
        break
else:
   print(" I don't understand that *_* ")




