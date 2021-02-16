import time                    #библиотека времени


slide1 = '(^_^)'
slide2 = '(^_~)'
slide3 = '(^_^)'
slide4 = '(о_О)'
slide5 = '(O_O)'
slide6 = 'Hello, World!'

time.sleep(1)     # команда sleep создает задержку перед применением(время в секундах)
print(slide1, end='\r')          # end='\r' команда которая после вывода slide1 удаляет его из терминала.
time.sleep(1)
print(slide2, end='\r')
time.sleep(1)
print(slide3, end='\r')
time.sleep(1)
print(slide4, end='\r')
time.sleep(1)
print(slide5, end='\r')
time.sleep(1)
print(slide6, end='\r')


str1 = """                            
Погода была пасмурной.
Шел дождь.
Но настроение все равно хорошее!
"""
# """ 3 двойных ковычки позволяют создать многострочную строку, это значит что текст напишится в терминале на том количестве строк которые написаны в коде.
print(str1, end='\r')