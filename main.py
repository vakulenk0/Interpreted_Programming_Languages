s = input().replace(' ', '').upper()
dict = {}

for i in range(len(s)):
    if(dict.get(s[i]) != None):
        k = str(int(dict.setdefault(s[i])) + 1)
        dict.update({s[i]: k})
    else:
        dict.update({s[i]: "1"})
k1 = 0 #кол-во элементов с 1 вхождением
kn = 0 #кол-во элементов с нечётным вхождением
for i in range(len(dict)):
    if(int(dict.setdefault(s[i])) % 2 == 1):
        kn += 1

if (kn > 1):
    print("Нет")
else:
    print("Да")
    KolOdd = 0
    letter = ""
    word = ""
    for i in dict:
        if (int(dict.setdefault(i)) % 2 == 1):
            letter = i
            KolOdd = int(dict.setdefault(i))
        else:
            word += i*(int(dict.setdefault(i))//2)
    word += letter*(KolOdd//2)
    word += letter + word[::-1]
    print(word)

#tggtjjjjjjj
#tgjjjjjjgt




