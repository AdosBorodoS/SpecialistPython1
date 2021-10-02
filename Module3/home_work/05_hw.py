# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

index_max_len=" "
i=0
len_mas=[]

while i<=len(names)-1:
    len_mas.append(len(names[i]))
    i+=1

index_max_len=len_mas.index(max(len_mas))

print(names[index_max_len])
