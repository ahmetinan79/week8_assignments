with open("numbers.txt", "w") as file:
    list_numbers = [i for i in range(1,11)]
    for num in list_numbers:
        file.write(str(num)+" ")