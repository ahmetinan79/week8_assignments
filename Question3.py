cities=['Kayseri','Istanbul','Izmir',
'Konya','Kars','Kastamonu','Kirklareli','Icel','Kirsehir','Kocaeli']
cities=sorted(cities)
plates = [i for i in range(33,43)]
zipped = list(zip(plates,cities))
with open("sehir.txt", "w") as file:
    for i in zipped:
        file.write(str(i[0])+" "+i[1]+"\n")