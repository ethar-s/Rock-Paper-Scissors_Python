answer = input()
answerfloat = []
try:
    while answer != '.':
        answerfloat.append(float(answer))
        answer = input()
except TypeError:
    pass
print(min(answerfloat))


