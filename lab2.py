n = int(input())
lines = [[j for j in input().split()] for i in range(n)]
# for i in range(len(lines)):            #вывод на экран файлы и их доступные операции
#     for j in range(len(lines[i])):
#         print(lines[i][j] + " ")

m = int(input())
for i in range(m):
    str = input().split()
    operation = ''
    if (str[0] == 'read'):
        operation = 'R'
    elif (str[0] == 'write'):
        operation = 'W'
    else:
        operation = 'X'
    file = 0
    for j in range(len(lines)):
        if (str[1] == lines[j][0]):
            file = j
            break
    if operation in lines[file]:
        print('OK')
    else:
        print('Access denied')

