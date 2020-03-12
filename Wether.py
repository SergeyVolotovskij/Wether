#ДЛЯ УТОЧНЕНИЯ ПОГОДЫ 
#СКАЧИВАЕМ МОДУЛЬ PIP PYOWM
#ИМПОРТИРУЕМ
import pyowm

#ДЛЯ КРАСИВОГО ЦВЕТА ИМПОРТИРУЕМ
from colorama import init
from colorama import Fore, Back, Style
init()

#КОПИРУЕМ ЭТИ СТРОЧКИ КОДА + регимся на сате и получаем API
#weathermap.org
owm = pyowm.OWM('27d057065c7fb12eb132fe31b42c2195', language = "ru")

#РАСКРАШИВАЕМ шрифт
print( Fore.GREEN )

#Спрашиваем
town = input("В КАКОМ ГОРОДЕ ПОСМОТРИМ ПОГОДУ ? ")

#СКОПИРОВАННЫЕ СТРОКИ КОДА С PIP OWM
observation = owm.weather_at_place(town)
w = observation.get_weather()

#получим температуру в цельсиях (примеры на PIP OWM!!!)
temp = w.get_temperature('celsius') ["temp"]

tempmin = w.get_temperature('celsius') ["temp_min"]

tempmax = w.get_temperature('celsius') ["temp_max"]

speed = w.get_wind() ["speed"]
#РАСКРАШИВАЕМ
print( Fore.YELLOW )

#ВЫВОДИМ РЕЗУЛЬТАТ
#print(w)
print("В ГОРОДЕ " + town + " СЕЙЧАС: " + w.get_detailed_status())
print("МИНИМАЛЬНАЯ ТЕМПЕРАТУРА СОСТАВИТ: " + str(tempmin) + " C0")
print("ТЕКУЩАЯ ТЕМПЕРАТУРА СОСТАВЛЯЕТ: " + str(temp)+ " C0")
print("МАКСИМАЛЬНАЯ ТЕМПЕРАТУРА СОСТАВИТ: " + str(tempmax)+ " C0")
print("СКОРОСТЬ ВЕТРА СОСТАВЛЯЕТ: " + str(speed) + " М/С")

input()
