count = int(input('сколько участников?'))
i = count
list_friends =[]
while i > 0:
    name = input('Как их зовут?')
    list_friends.append(name)
    i -= 1
print(list_friends)