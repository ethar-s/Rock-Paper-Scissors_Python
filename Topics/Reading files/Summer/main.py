summers = open('data/dataset/input.txt', 'r', encoding='cp1252')
i = 0
for summer in summers:
    if summer == 'summer\n':
        i += 1

summers.close()

print(i)