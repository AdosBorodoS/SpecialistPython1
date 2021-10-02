# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
print("_________________________________________________________________________________")
# Введение переменных
i=0
item_part=[]
item_complex_mas=[]
# формирование коренных для работы массивов
while i <= len(items)-1:
    item_part=[]
    item_part.append(items[i]['name'])
    item_part.append(items[i]['brand'])
    item_part.append(items[i]['price'])
    item_complex_mas.append(item_part)
    i+=1

# ------------------Товары на складе представлены брэндами-------------------------------
print("Товары на складе представлены брэндами: ")
i=0
list_of_brend=[]
while i<=len(item_complex_mas)-1:
    list_of_brend.append(item_complex_mas[i][1])
    i+=1
print(list_of_brend)
print("_________________________________________________________________________________")


# ------------------На складе больше всего товаров брэнда-------------------------------
i=0
count=[]
while i <= len(item_complex_mas)-1:
    try:# Если массив пустой тогда записывается название бренда и его количество

        if count == []:
            count.append(list_of_brend[i])
            count.append(list_of_brend.count(list_of_brend[i]))
        # Если в массиве count найдено совпадение с элементом массива list_of_brend тогда
        elif count.index(list_of_brend[i])>0:
            # Ничего
            b=1
        # В случае ошибки что будет сигналезировать что такой элемент отсуцтует он будет кидать в исключение и дописывать элемент и его количество
    except Exception:
        count.append(list_of_brend[i])
        count.append(list_of_brend.count(list_of_brend[i]))
    i+=1
i=0

# Считает максимальное количество и выдает его вместе с бреном
i2=1
count_number=[]
while i2<=len(count)-1:
    count_number.append(int(count[i2]))
    i2+=2
max_num=max(count_number)
brend=count[count.index(max_num)-1]
print(f"На складе больше всего товаров брэнда(ов) {brend}, {max_num} штуки ")
print("_________________________________________________________________________________")




# ------------------На складе самый дорогой товар брэнда(ов)-------------------------------
#Записывает все цены в один массив
i=0
brends_price=[]
while i <= len(item_complex_mas)-1:
    brends_price.append(int(item_complex_mas[i][2]))
    i+=1
i=0
# Выбирает товар с максимальной ценой
max_price=max(brends_price)
while i<=len(item_complex_mas)-1:
    if item_complex_mas[i][2]==max_price:
        print(f"На складе самый дорогой товар {item_complex_mas[i][0]} брэнда(ов) {item_complex_mas[i][1]}, по цене {item_complex_mas[i][2]} рублей")
    i+=1
