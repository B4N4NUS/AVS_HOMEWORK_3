import charecterReplacement
import charecterToNumber
import cyclicShift
import random


# ------------------------------------------------------------------------------
# Метод реализации Straight Merge сортировки.
def merge_sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    l, r = arr[:len(arr) // 2], arr[len(arr) // 2:]
    merge_sort(l)
    merge_sort(r)
    n = m = k = 0
    c = [0] * (len(l) + len(r))
    while n < len(l) and m < len(r):
        if l[n] < r[m]:
            c[k] = l[n]
            n += 1
        else:
            c[k] = r[m]
            m += 1
        k += 1
    while n < len(l):
        c[k] = l[n]
        n += 1
        k += 1
    while m < len(r):
        c[k] = r[m]
        m += 1
        k += 1
    for i in range(len(arr)):
        arr[i] = c[i]
    return arr


class Container(object):
    # ------------------------------------------------------------------------------
    # Инициализация класса.
    def __init__(self):
        self.cont = []
        print("Container was created")

    # ------------------------------------------------------------------------------
    # Метод очистки памяти.
    def clear(self):
        del self.cont
        print("Container was cleared")

    # ------------------------------------------------------------------------------
    # Заполнение контейнера из файла.
    def in_file(self, path):
        file = open(path, 'r')
        lines = file.readlines()

        for i in range(len(lines)):
            lines[i] = lines[i].strip('\n')

        for i in range(len(lines) - 1):
            if i % 2 == 1:
                continue
            if lines[i] == "1":
                cr = charecterReplacement.CharecterReplacement()
                cr.message = lines[i + 1]
                cr.encrypt()
                self.cont.append(cr)
            elif lines[i] == "2":
                cs = cyclicShift.CyclicShift()
                tmp = lines[i + 1].split(' ')
                cs.n = int(tmp[0])
                tmp.pop(0)
                cs.message = ' '.join(tmp)
                cs.encrypt()
                self.cont.append(cs)
            elif lines[i] == "3":
                ctn = charecterToNumber.CharecterToNumber()
                ctn.message = lines[i + 1]
                ctn.encrypt()
                self.cont.append(ctn)
        print("Container was filled")

    # ------------------------------------------------------------------------------
    # Случайное заполнение контейнера.
    def in_rnd(self, size):
        i = 0
        while i < size:
            key = random.randint(1, 3)
            if key == 1:
                cr = charecterReplacement.CharecterReplacement()
                cr.in_rnd()
                self.cont.append(cr)
            elif key == 2:
                cs = cyclicShift.CyclicShift()
                cs.in_rnd()
                self.cont.append(cs)
            elif key == 3:
                ctn = charecterToNumber.CharecterToNumber()
                ctn.in_rnd()
                self.cont.append(ctn)
            i += 1
        print("Container was filled randomly")

    # ------------------------------------------------------------------------------
    # Вывод информации о контейнере в файлы.
    def out(self, path, path_sorted):
        file = open(path, 'w')
        file.write("Filled container:\nContainer contains " + str(len(self.cont)) + " elements\n")
        for i in range(len(self.cont)):
            file.write(str(i) + ")" + self.cont[i].out())
        merge_sort(self.cont)
        file_sorted = open(path_sorted, 'w')
        file_sorted.write("Sorted container\nContainer contains " + str(len(self.cont)) + " elements\n")
        for i in range(len(self.cont)):
            file_sorted.write(str(i) + ")\n  Quotient = " + str(self.cont[i]) + " " + self.cont[i].out())
        print("Container printed and sorted")

