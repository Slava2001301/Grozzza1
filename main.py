import math

def shiftArrMax(arr):
    max_val = max(arr)
    index_max_value = arr.index(max_val)

    arr[index_max_value] = 0
    return [max_val, arr]


arr = list()

for i in range(50):
    while True:
        try:
            value = int(input("Input number " + str(i + 1) + ": "))
        except ValueError:
            print('Введное значение должно быть числом!')
            continue
        if type(value) == int and 0 < int(value):
            arr.append(int(value))
            break
        else:
            print('Введное значение должно быть числом и быть больше 0!')

[a, arr] = shiftArrMax(arr)
[b, arr] = shiftArrMax(arr)
[c, arr] = shiftArrMax(arr)

p = (a + b + c) / 2
print("p = ", p)

if p - a > 0 and p - b > 0 and p - c > 0:
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("s = ", s)
else:
    print('Найденные максимальные числа некорректные для вычисления площади треугольника!')
