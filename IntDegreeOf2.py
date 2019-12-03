# По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N.
# Выведите показатель степени и саму степень.
# Операцией возведения в степень, а так же функцией возведения в степень пользоваться НЕЛЬЗЯ!
#
# Например:
# 50          5 32            2 ** 5 = 32
# 10          3 8             2 ** 3 = 8
# 8           3 8             2 ** 3 = 8
# 7           2 4             2 ** 2 = 4
# 1           0 1             2 ** 0 = 1
# 2           1 2             2 ** 1 = 2
# 3           1 2             2 ** 1 = 2
# 4           2 4             2 ** 2 = 4
# 5           2 4             2 ** 2 = 4
# 100         6 64            2 ** 6 = 64
# 1025        10 1024         2 ** 10 = 1024
# 15431543    23 8388608      2 ** 23 = 8388608

k = 2
n = 50
result = 1
length = 0

while result:
    result = k
    k *= 2
    if result < n:
        # print(result)
        length += 1
    else:
        break

result //= 2
# print("наибольшая целая степень двойки: ",result)
# print("Степень:",length)
# print("показатель степени:", result // length)
print(n,'\t\t',str(length), str(result),'\t\t','2 **',length, '=', result)

k = 2
n = 10
result = 1
length = 0

while result:
    result = k
    k *= 2
    if result < n:
        length += 1
    else:
        break
result //= 2

print(n,'\t\t',str(length), str(result),'\t\t','2 **',length, '=', result)

k = 2
n = 8
result = 1
length = 0

while result:
    result = k
    k *= 2
    if result < n:
        length += 1
    else:
        break
result //= 2

print(n,'\t\t',str(length), str(result),'\t\t','2 **',length, '=', result)


k = 2
n = 7
result = 1
length = 0

while result:
    result = k
    k *= 2
    if result < n:
        length += 1
    else:
        break
result //= 2

print(n,'\t\t',str(length), str(result),'\t\t','2 **',length, '=', result)


k = 2
n = 1
result = 1
length = 0

while result:
    result = k
    k *= 2
    if result < n:
        length += 1
    else:
        break
result //= 2

print(n,'\t\t',str(length), str(result),'\t\t','2 **',length, '=', result)


k = 2
n = 2
result = 1
length = 0

while result:
    result = k
    k *= 2
    if result < n:
        length += 1
    else:
        break
result //= 2

print(n,'\t\t',str(length), str(result),'\t\t','2 **',length, '=', result)


k = 2
n = 3
result = 1
length = 0

while result:
    result = k
    k *= 2
    if result < n:
        length += 1
    else:
        break
result //= 2

print(n,'\t\t',str(length), str(result),'\t\t','2 **',length, '=', result)


k = 2
n = 4
result = 1
length = 0

while result:
    result = k
    k *= 2
    if result < n:
        length += 1
    else:
        break
result //= 2

print(n,'\t\t',str(length), str(result),'\t\t','2 **',length, '=', result)


k = 2
n = 5
result = 1
length = 0

while result:
    result = k
    k *= 2
    if result < n:
        length += 1
    else:
        break
result //= 2

print(n,'\t\t',str(length), str(result),'\t\t','2 **',length, '=', result)


k = 2
n = 100
result = 1
length = 0

while result:
    result = k
    k *= 2
    if result < n:
        length += 1
    else:
        break
result //= 2

print(n,'\t',str(length), str(result),'\t\t','2 **',length, '=', result)


k = 2
n = 1025
result = 1
length = 0

while result:
    result = k
    k *= 2
    if result < n:
        length += 1
    else:
        break
result //= 2

print(n,'\t',str(length), str(result),'\t','2 **',length, '=', result)


k = 2
n = 15431543
result = 1
length = 0

while result:
    result = k
    k *= 2
    if result < n:
        length += 1
    else:
        break
result //= 2

print(n,str(length), str(result),' 2 **',length, '=', result)