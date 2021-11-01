# ------------------------------------------------------------------------------
# main.cpp - содержит главную функцию,
# обеспечивающую простое тестирование.
# ------------------------------------------------------------------------------

import container
import sys


# import time


# ------------------------------------------------------------------------------
# Выводит сообщение о некорректном вводе.
def error_message1():
    print("incorrect command line!\n"
          "  Waited:\n"
          "     command -f infile outfile01 outfile02\n"
          "  Or:\n"
          "     command -r number outfile01 outfile02\n")


# ------------------------------------------------------------------------------
# Выводит сообщение о некорректном вводе метода заполнения.
def error_message2():
    print("incorrect qualifier value!\n"
          "  Waited:\n"
          "     command -f infile outfile01 outfile02\n"
          "  Or:\n"
          "     command -r number outfile01 outfile02\n")


# ------------------------------------------------------------------------------
# Точка входа.

# Старт таймера.
# start = time.perf_counter_ns()

# Получение информации о введенных argv
argv = sys.argv

if len(argv) != 5:
    error_message1()
    exit()

print("Start")
c = container.Container()

if argv[1] == "-f":
    # Заполнение контейнера содержимым файла.
    c.in_file(argv[2])
elif argv[1] == "-r":
    if int(argv[2]) < 1 or int(argv[2]) > 10000:
        print("incorrect number of words = " + argv[2] + ". Set 0 < number <= 10000\n")
    else:
        # Заполнение контейнера генератором случайных чисел.
        c.in_rnd(int(argv[2]))

# Вывод содержимого контейнера в файл.
c.out(argv[3], argv[4])
c.clear()

# Остановка таймера.
# stop = time.perf_counter_ns()
print("Stop")
# print("Execution time: " + str((stop - start)/1000)+" microseconds")
