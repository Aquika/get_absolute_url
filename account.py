import os
import time


put = input('Введите ключ (name или account): ').lower()

account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}  #список аккаунтов
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

account_list = ['account1', 'account2', 'account3', 'account4']

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}  #список юзеров
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

user_list = [user1, user2, user3, user4]

try:
    print(f"значение ключа {put} для юзера 1 = {user1[put]}")
    print(f"значение ключа {put} для юзера 2 = {user2[put]}")
    print(f"значение ключа {put} для юзера 3 = {user3[put]}")
    print(f"значение ключа {put} для юзера 4 = {user4[put]}")

except:
    print('Введенный ключ не найден')

#time.sleep(5)         #задержка по времени
#os.system('cls')      #перед очищением терминала

put2 = input('Введите порядковый номер: ')

user = user_list[int(put2)-1]

try:
    print(f"Данные по юзеру № {put2}")
    print(f"имя: {user['name']}")
    print(f"возраст: {user['age']}")
    print(f"логин: {user['account']['login']}")
    print(f"пароль: {user['account']['password']}")

except:
    print('Пользователь с указанным номером не найден')


#time.sleep(5)
#os.system('cls')

put3 = input('какого пользователя переместить в конец: ')

try:
    pfhud = int(put3)
    delete = user_list.pop(pfhud)
    ret = user_list.append(delete)
    print(f"№1 {user_list[0]['name']}")
    print(f"№2 {user_list[1]['name']}") 
    print(f"№3 {user_list[2]['name']}") 
    print(f"№4 {user_list[3]['name']}")

except:
    print('FATAL ERROR')

#time.sleep(5)
#os.system('cls')

average_age = (user1['age'] + user2['age'] + user3['age'] + user4['age']) / 4

print(f"Средний возраст всех юзеров = {average_age}")

