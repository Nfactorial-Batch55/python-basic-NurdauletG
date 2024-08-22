#ex 1
a = 1
b = 2
summ = a + b
print(summ)
#ex 2
string = "nur"[::-1]
print(string)
#ex 3
string1 = "nurd"
lenstring = len(string1)
print(lenstring)
#ex 4
string11 = "nur"
string22 = "daulet"
print(string11 + string22)
#ex 5 
character = 'a'
vowels = 'aeiouy'
if character.lower() in vowels:
    res = 'тут есть гласные'
else:
    res = 'тут нет гласных'
print(res)
#ex 6
nurda = 'nurdaulet'
if len(nurda) > 1:
    aurdn = nurda[-1] + nurda[1:-1] + nurda[0]
else: aurdn = nurda
print(aurdn)
#ex 7
nu = 'nurdaulet'
nur = nu.upper()
print(nur)
#ex 8
def area(a, b):
    c = a * b
    return(c)
print(area(5, 3))
#ex 9
a = 48
if a % 2 == 0:
    print("четный")
else:
    print("не четный")
#ex 10
nurdaulet = 'Нурдаулет'
nur = nurdaulet[0] + nurdaulet[1] + nurdaulet[2]
print(nur)
#ex 11
name = 'nurdaulet'
age = 18
HelloNur = f'Меня зовут {name} и мне {age} лет'
print(HelloNur)
#ex 12
nurdaulet = 'nurdaulet'
rdau = nurdaulet[2:6]
print(rdau)
#ex 13
nomera = '18'
nomer = int(nomera)
print(nomer)
#ex 14
nurdaulet = 'nurdaulet'
nurdauletx3 = nurdaulet * 3
print(nurdauletx3)
#ex 15
a = 5
b = 2
quotient = a // b
remainder = a % b
print(quotient)
print(remainder)
#ex 16
a = 5
b = 2
c = a/b
print(float(c))
#ex 17
nurdaulet = 'nurdaulet'
CountOfN = nurdaulet.count('n')
print(CountOfN)
#ex 18
nurdaulet = "My name is \"Nurdaulet\""
print(nurdaulet)
#ex 19
nurdaulet = '''Меня
зовут
Нурдаулет'''
print(nurdaulet)
#ex 20
base = 2
exponent = 3
result = base ** exponent
print(result)
#ex 21
palindrome = 'nurdaulet'
checkP = palindrome[::-1]
if checkP == palindrome:
    print('Это палиндром')
else:
    print('Это не палиндром')