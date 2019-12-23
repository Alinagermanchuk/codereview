'''Вивести суму чисел списку і рядок, шо складається з даних типу str'''


list = [1,2,4,7,2,'a',1,'і']
sum=0
string=str()
for i in range(0,len(list)):
    if isinstance(list[i], int):
        sum +=int(list[i])

    elif isinstance(list[i],str):
                string += list[i]
print(sum)
print(string)