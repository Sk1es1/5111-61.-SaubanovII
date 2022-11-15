num=float(input("Введите значение магнитуды: "))
if num<2:
    print("Минимальное")
elif 3>num>=2:
    print("Очень слабое")
elif 4>num>=3:
    print("Слабое")
elif 5>num>=4:
    print("Промежуточное")
elif 6>num>=5:
    print("Умеренное")
elif 7>num>=6:
    print("Сильное")
elif 8>num>=7:
    print("Очень сильное")
elif 10>num>=8:
    print("Огромное")
elif num>10:
    print("Разрушительное")