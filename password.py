password = input("Введите пароль: ")



try:

    blank_password = 1/len(password)

    only_numbers = int(password) + 'a'

except ZeroDivisionError:

    print("Вы ввели пустой пароль")

except TypeError:

    print("Ваш пароль состоит только из цифр")

except:

    print("Требования к паролю соблюдены")



   

