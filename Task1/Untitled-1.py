letters="aeiou"
questions=input("Введите букву: ")
if letters[0:5].__contains__(questions[0:5]):
    print("Вы ввели гласную букву")
elif questions=='y':
    print("Буква может быть, как гласной, так и согласной")
else:
    print("Вы ввели согласную букву")