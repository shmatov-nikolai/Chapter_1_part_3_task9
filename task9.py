'''
9.Напишите программу (используя функции!), Которая запрашивает у пользователя длинную
строку, содержащую несколько слов. Выведите обратно пользователю ту же строку, Но уже в
обратном порядке. Например, скажем, я набрал строку:
My name is Emir
Output:
Emir is name My
'''
strochka = input('Введите текст для реверса: ')
# Привет Мир, всем питонистам - удачи !
print(strochka)

def reverce_str():
    global strochka
    listok = strochka.split(' ')
    strochka = ' '.join(listok[::-1])
    return strochka
   

reverce_str()

print (strochka)
