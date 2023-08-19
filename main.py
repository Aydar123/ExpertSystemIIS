import sys
import pygame as pg
from heapq import *
from Boxes import Box
from AllStreet import Street
from time import sleep
from tqdm import trange
from random import *
from colorama import Fore, Style
import pandas as pd
from tabulate import tabulate
from AllTime import Time

print(Fore.BLUE + '\nДобро пожаловать! Представляем вашему вниманию ассортимент заказов, доставляемых при помощи '
                  'робота-курьера или дрона!' + Style.RESET_ALL)

b1 = Box('Box 1', 10140, 7.4, 499)
b2 = Box('Box 2', 20477, 5, 2999)
b3 = Box('Box 3', 31510, 1.5, 900)
b4 = Box('Box 4', 41111, 0.9, 350)

masNameBox = [b1.nameBox, b2.nameBox, b3.nameBox, b4.nameBox]
masNumOrder = [b1.num, b2.num, b3.num, b4.num]
masWeight = [b1.w, b2.w, b3.w, b4.w]
masPrice = [b1.price, b2.price, b3.price, b4.price]


def ViewTable(n, num, w, p):  # Функция для печати данных (в виде таблицы)
    view = pd.DataFrame({'Название': n,
                         '№ заказа': num,
                         'Вес (кг)': w,
                         'Цена (руб)': p
                         })
    view.index = (view.index + 1)  # Нумерация строк в таблице теперь с единицы (т.е индексация теперь с единицы)
    print(tabulate(view, tablefmt='fancy_grid', headers='keys', stralign='center'))
    return view


ex0 = ViewTable(masNameBox, masNumOrder, masWeight, masPrice)
_Box = []
_Box.append(int(input(Fore.RED + 'Выберите товар. Просто введите номер соответствующего пункта: ' + Style.RESET_ALL)))

_Question0 = str(input('Хотите что-нибудь еще? Введите "д", если хотите, введите "н", если нет: '))
while _Question0 == 'д':
    _Box.append(int(input(Fore.RED + 'Выберите товар. Просто введите номер '
                                     'соответствующего пункта: ' + Style.RESET_ALL)))
    _Question0 = str(input('Хотите что-нибудь еще? Введите "д", если хотите, введите "н", если нет: '))
    if _Question0 == 'н':
        break

sum_kg = []  # Список для суммарного веса
sum_price = []  # Список для итоговой стоимости доставки
for i in range(len(_Box)):
    # print(_Box[i])
    if _Box[i] == 1:
        print(f'Вы выбрали: {b1.nameBox} | № {b1.num} | {b1.w} кг | {b1.price} руб')
        sum_kg.append(b1.w)
        sum_price.append(b1.price)
    elif _Box[i] == 2:
        print(f'Вы выбрали: {b2.nameBox} | № {b2.num} | {b2.w} кг | {b2.price} руб')
        sum_kg.append(b2.w)
        sum_price.append(b2.price)
    elif _Box[i] == 3:
        print(f'Вы выбрали: {b3.nameBox} | № {b3.num} | {b3.w} кг | {b3.price} руб')
        sum_kg.append(b3.w)
        sum_price.append(b3.price)
    elif _Box[i] == 4:
        print(f'Вы выбрали: {b4.nameBox} | № {b4.num} | {b4.w} кг| {b4.price} руб')
        sum_kg.append(b4.w)
        sum_price.append(b4.price)


def listsum(mas):
    if len(mas) == 1:
        return mas[0]
    else:
        return mas[0] + listsum(mas[1:])


# mas[1:] - т.е. просматриваем весь массив, кроме нулевого элемента, т.к. mas[0] просматривается отдельно

res_sum_kg = listsum(sum_kg)
res_sum_price = listsum(sum_price)

myRand = choices([True, False])
newMyRand = 0
inputRandom = int(input('\nВведите исправность (1) / неисправность (0): '))

if res_sum_kg <= 5:
    print('Проверим техническое состояние дрона:')
    for i in trange(100, leave=True, disable=False, ncols=110, desc='Проверка...'):
        sleep(0.05)
    # leave = False (после окончания проверки данный process bar удалится)
    # disable = True (удаляет process bar, остаются только цифры)
    if inputRandom == 1:
        print('\nДрон исправен.\nВес соответствует норме.\nЗаказ будет доставлен дроном!')
    else:
        print('\nК сожалению, дрон неисправен.\nНо мы можем осуществить доставку роботом-курьером.')
        _Question1 = str(input(Fore.BLUE + 'Осуществить доставку роботом-курьером? Введите "д", если согласны,'
                                           ' введите "н", если не согласны: ' + Style.RESET_ALL))
        if _Question1 == 'д':
            print('\nПроверим техническое состояние робота-курьера:')
            newInputRandom = int(input('Введите исправность (1) / неисправность (0): '))
            for i in trange(100, leave=True, disable=False, ncols=110, desc='Проверка...'):
                sleep(0.05)
            # newMyRand = choices([True, False], weights=[80, 20])
            if newInputRandom == 1:
                print('\nРобот-курьер исправен.\nВес соответствует норме.\nЗаказ будет доставлен' + Fore.GREEN +
                      ' РОБОТОМ-КУРЬЕРОМ!' + Style.RESET_ALL)
            else:
                print('Приносим свои извинения робот-курьер также неисправен. Ждем Вас снова в другое время!')
                sys.exit()  # Завершаем работу программы
        elif _Question1 == 'н':
            print('Заказ отменен. Ждем Вас снова!')
            sys.exit()

elif res_sum_kg > 5:
    print('Проверим техническое состояние робота-курьера:')
    for i in trange(100, leave=True, disable=False, ncols=110, desc='Проверка...'):
        sleep(0.05)
    if inputRandom == 1:
        print('\nРобот-курьер исправен.\nВес соответствует норме.\nЗаказ будет доставлен роботом-курьером!')
    else:
        print('\nК сожалению, робот-курьер неисправен.\nНо мы можем осуществить доставку дроном.')
        _Question2 = str(input(Fore.BLUE + 'Осуществить доставку дроном? Введите "д", если согласны, введите "н", если '
                               'не согласны: ' + Style.RESET_ALL))
        if _Question2 == 'д':
            print('Проверим техническое состояние дрона:')
            newInputRandom = int(input('Введите исправность (1) / неисправность (0): '))
            for i in trange(100, leave=True, disable=False, ncols=110, desc='Проверка...'):
                sleep(0.05)
            # newMyRand = choices([True, False], weights=[60, 40])
            if newInputRandom == 1 and res_sum_kg <= 5:
                print('\nДрон исправен.\nВес соответствует норме.\nЗаказ будет доставлен ' + Fore.GREEN + ' ДРОНОМ!'
                      + Style.RESET_ALL)
            else:
                print('Приносим свои извинения дрон также неисправен. Ждем Вас снова в другое время!')
                sys.exit()  # Завершаем работу программы
        elif _Question2 == 'н':
            print('Заказ отменен. Ждем Вас снова!')
            sys.exit()

print(Fore.BLUE + '\nСписок адресов:' + Style.RESET_ALL)
s1 = Street('Тукая', 22, 1)
s2 = Street('Толстого', 5, 2)
s3 = Street('Пушкина', 34, 3)
s4 = Street('Ленина', 19, 4)
s5 = Street('Баумана', 10, 5)

masNameStreet = [s1.nameStreet, s2.nameStreet, s3.nameStreet, s4.nameStreet, s5.nameStreet]
masNumHome = [s1.numHome, s2.numHome, s3.numHome, s4.numHome, s5.numHome]
masNumPod = [s1.podyezd, s2.podyezd, s3.podyezd, s4.podyezd, s5.podyezd]


def ViewTable1(n, num_h, num_p):  # Функция для печати данных (в виде таблицы)
    view = pd.DataFrame({'Название улицы': n,
                         '№ дома': num_h,
                         '№ подъезда': num_p,
                         })
    view.index = (view.index + 1)  # Нумерация строк в таблице теперь с единицы (т.е индексация теперь с единицы)
    print(tabulate(view, tablefmt='fancy_grid', headers='keys', stralign='center'))
    return view


ex1 = ViewTable1(masNameStreet, masNumHome, masNumPod)


def Data_Entry_Validation_St():  # Метод для проверки ввода данных
    while type:
        getNumber = input(Fore.RED + 'Выберите адрес доставки. Просто напишите номер '
                                     'соответствующего пункта: ' + Style.RESET_ALL)  # Ввод числа
        try:                                  # Проверка что getNumber преобразуется в число без ошибки
            getTempNumber = int(getNumber)    # Преобразуем из str в int
        except ValueError:                    # Проверка на ошибку неверного формата (введены буквы)
            print('"' + getNumber + '"' + ' - не является числом')
        else:  # Если getTempNumber преобразован в число без ошибки, выход из цикла while
            break
    return abs(getTempNumber)  # Возвращает модуль getTempNumber (для искл. отрицат. чисел)


_Street = Data_Entry_Validation_St()

_X = 0
_Y = 0
if _Street == 1:
    print(f'Вы выбрали: Улицу {s1.nameStreet} | Дом {s1.numHome} | Подъезд {s1.podyezd}')
    _X = 22
    _Y = 7
elif _Street == 2:
    print(f'Вы выбрали: Улицу {s2.nameStreet} | Дом {s2.numHome} | Подъезд {s2.podyezd}')
    _X = 22
    _Y = 0
elif _Street == 3:
    print(f'Вы выбрали: Улицу {s3.nameStreet} | Дом {s3.numHome} | Подъезд {s3.podyezd}')
    _X = 14
    _Y = 0
elif _Street == 4:
    print(f'Вы выбрали: Улицу {s4.nameStreet} | Дом {s4.numHome} | Подъезд {s4.podyezd}')
    _X = 9
    _Y = 11
elif _Street == 5:
    print(f'Вы выбрали: Улицу {s5.nameStreet} | Дом {s5.numHome} | Подъезд {s5.podyezd}')
    _X = 2
    _Y = 1

galochka = '✔'
negalochka = 'X'

randForTime1 = choices([galochka, negalochka])
t1 = Time('09.00-11.00', randForTime1)

randForTime2 = choices([galochka, negalochka])
t2 = Time('11.00-13.00', randForTime2)

randForTime3 = choices([galochka, negalochka])
t3 = Time('13.00-15.00', randForTime3)

randForTime4 = choices([galochka, negalochka])
t4 = Time('15.00-17.00', randForTime4)

randForTime5 = choices([galochka, negalochka])
t5 = Time('17.00-19.00', randForTime5)

randForTime6 = choices([galochka, negalochka])
t6 = Time('19.00-21.00', randForTime6)


masTotalTime = [t1.total_time, t2.total_time, t3.total_time, t4.total_time, t5.total_time, t6.total_time]
masStatus = [t1.status, t2.status, t3.status, t4.status, t5.status, t6.status]


def ViewTable2(tt, status):  # Функция для печати данных (в виде таблицы)
    view = pd.DataFrame({'Время': tt,
                         'Статус': status
                         })
    view.index = (view.index + 1)  # Нумерация строк в таблице теперь с единицы (т.е индексация теперь с единицы)
    print(tabulate(view, tablefmt='fancy_grid', headers='keys', stralign='center'))
    return view


print(Fore.BLUE + '\nСписок свободного времени:' + Style.RESET_ALL)
ex2 = ViewTable2(masTotalTime, masStatus)


def Data_Entry_Validation_Time():  # Метод для проверки ввода данных
    while type:
        getNumber = input(Fore.RED + 'Выберите желаемое время доставки. ✔ - время свободно; Х - занято; '
                                     '\nПросто напишите номер соответствующего пункта: ' + Style.RESET_ALL)  # Ввод числ
        try:                                  # Проверка что getNumber преобразуется в число без ошибки
            getTempNumber = int(getNumber)    # Преобразуем из str в int
        except ValueError:                    # Проверка на ошибку неверного формата (введены буквы)
            print('"' + getNumber + '"' + ' - не является числом')
        else:  # Если getTempNumber преобразован в число без ошибки, выход из цикла while
            break
    return abs(getTempNumber)  # Возвращает модуль getTempNumber (для искл. отрицат. чисел)


_Time = Data_Entry_Validation_Time()


if _Time == 1 and t1.status == [galochka]:
    print(f'Предположительное время доставки: {t1.total_time}')
elif t1.status == [negalochka] and _Time == 1:
    _Time = [negalochka]
elif _Time == 2 and t2.status == [galochka]:
    print(f'Предположительное время доставки: {t2.total_time}')
elif t2.status == [negalochka] and _Time == 2:
    _Time = [negalochka]
elif _Time == 3 and t3.status == [galochka]:
    print(f'Предположительное время доставки: {t3.total_time}')
elif t3.status == [negalochka] and _Time == 3:
    _Time = [negalochka]
elif _Time == 4 and t4.status == [galochka]:
    print(f'Предположительное время доставки: {t4.total_time}')
elif t4.status == [negalochka] and _Time == 4:
    _Time = [negalochka]
elif _Time == 5 and t5.status == [galochka]:
    print(f'Предположительное время доставки: {t5.total_time}')
elif t5.status == [negalochka] and _Time == 5:
    _Time = [negalochka]
elif _Time == 6 and t6.status == [galochka]:
    print(f'Предположительное время доставки: {t6.total_time}')
elif t6.status == [negalochka] and _Time == 6:
    _Time = [negalochka]

while _Time == [negalochka]:
    _Time = int(input('Ошибка! Данное время недоступно. Попробуйте еще раз или введите "404" для отмены заказа: '))
    if _Time == 404:
        print('Заказ отменен. Ждем Вас снова!')
        sys.exit()

    if _Time == 1 and t1.status == [galochka]:
        print(f'Предположительное время доставки: {t1.total_time}')
        _Time = [galochka]
    elif t1.status == [negalochka] and _Time == 1:
        _Time = [negalochka]
    elif _Time == 2 and t2.status == [galochka]:
        print(f'Предположительное время доставки: {t2.total_time}')
        _Time = [galochka]
    elif t2.status == [negalochka] and _Time == 2:
        _Time = [negalochka]
    elif _Time == 3 and t3.status == [galochka]:
        print(f'Предположительное время доставки: {t3.total_time}')
        _Time = [galochka]
    elif t3.status == [negalochka] and _Time == 3:
        _Time = [negalochka]
    elif _Time == 4 and t4.status == [galochka]:
        print(f'Предположительное время доставки: {t4.total_time}')
        _Time = [galochka]
    elif t4.status == [negalochka] and _Time == 4:
        _Time = [negalochka]
    elif _Time == 5 and t5.status == [galochka]:
        print(f'Предположительное время доставки: {t5.total_time}')
        _Time = [galochka]
    elif t5.status == [negalochka] and _Time == 5:
        _Time = [negalochka]
    elif _Time == 6 and t6.status == [galochka]:
        print(f'Предположительное время доставки: {t6.total_time}')
        _Time = [galochka]
    elif t6.status == [negalochka] and _Time == 6:
        _Time = [negalochka]


# Формирование окружности, т.е. окружности которые показывает путь
def get_circle(x, y):
    return (x * TILE + TILE // 2, y * TILE + TILE // 2), TILE // 4


# Функция для формирования клетки на сетке
def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2


# Определение соседних клеток
def get_next_nodes(x, y):
    check_next_node = lambda x, y: True if 0 <= x < cols and 0 <= y < rows else False  # Проверка на выход вне экр
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    return [(grid[y + dy][x + dx], (x + dx, y + dy)) for dx, dy in ways if check_next_node(x + dx, y + dy)]


# Определение Манхетенского расстояния - насколько мы близки к цели
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


cols, rows = 23, 13
TILE = 50  # Размер диалогового окна

pg.init()
sc = pg.display.set_mode([cols * TILE, rows * TILE])  # Рисуем диалоговое окно
pg.display.set_caption('Реализация доставки')
clock = pg.time.Clock()
# список с препятствиями
grid = ['22222222222222222222212',
        '22222292222911112244412',
        '22444422211112911444412',
        '24444444212777771444912',
        '24444444219777771244112',
        '92444444212777791192144',
        '22229444212777779111144',
        '11111112212777772771122',
        '27722211112777772771244',
        '27722777712222772221244',
        '22292777711144429221244',
        '22922777222144422211944',
        '22222777229111111119222']
grid = [[int(char) for char in string] for string in grid]  # Массив типа str преобразовываем в int
# Формируем граф (и список смежных ребер\клеток)
graph = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)

# Начальные настройки для формирования пути
start = (0, 7)
goal = (_X, _Y)  # 22 and 7
queue = []
heappush(queue, (0, start))  # Добавляет элемент в кучу
cost_visited = {start: 0}
visited = {start: None}

bg = pg.image.load('map.png').convert()
bg = pg.transform.scale(bg, (cols * TILE, rows * TILE))  # Картинка как задний фон

print('\n\n\n')
print(Fore.GREEN + '\nЗаказ успешно доставлен!\nИтог:' + Style.RESET_ALL)
for ii in range(len(_Box)):
    if _Box[ii] == 1:
        print(f'Вы заказали: {b1.nameBox} | № {b1.num} | {b1.w} кг | {b1.price} руб')
    elif _Box[ii] == 2:
        print(f'Вы заказали: {b2.nameBox} | № {b2.num} | {b2.w} кг | {b2.price} руб')
    elif _Box[ii] == 3:
        print(f'Вы заказали: {b3.nameBox} | № {b3.num} | {b3.w} кг | {b3.price} руб')
    elif _Box[ii] == 4:
        print(f'Вы заказали: {b4.nameBox} | № {b4.num} | {b4.w} кг| {b4.price} руб')

if _Street == 1:
    print(f'Адрес доставки: Улица {s1.nameStreet} | Дом {s1.numHome} | Подъезд {s1.podyezd}')
elif _Street == 2:
    print(f'Адрес доставки: Улица {s2.nameStreet} | Дом {s2.numHome} | Подъезд {s2.podyezd}')
elif _Street == 3:
    print(f'Адрес доставки: Улица {s3.nameStreet} | Дом {s3.numHome} | Подъезд {s3.podyezd}')
elif _Street == 4:
    print(f'Адрес доставки: Улица {s4.nameStreet} | Дом {s4.numHome} | Подъезд {s4.podyezd}')
elif _Street == 5:
    print(f'Адрес доставки: Улиц {s5.nameStreet} | Дом {s5.numHome} | Подъезд {s5.podyezd}')

if _Time == 1 and t1.status == [galochka]:
    print(f'Заказ доставлен с: {t1.total_time}')
elif _Time == 2 and t2.status == [galochka]:
    print(f'Заказ доставлен с: {t2.total_time}')
elif _Time == 3 and t3.status == [galochka]:
    print(f'Заказ доставлен с: {t3.total_time}')
elif _Time == 4 and t4.status == [galochka]:
    print(f'Заказ доставлен с: {t4.total_time}')
elif _Time == 5 and t5.status == [galochka]:
    print(f'Заказ доставлен с: {t5.total_time}')
elif _Time == 6 and t6.status == [galochka]:
    print(f'Заказ доставлен с: {t6.total_time}')

print(f'Вес заказа составляет: {res_sum_kg} кг')

if res_sum_kg <= 5 and myRand == [True]:
    print('Заказ доставлен дроном!')
elif res_sum_kg > 5 and newMyRand == [True]:
    print('Заказ доставлен роботом-курьером!')

if res_sum_kg > 5 and myRand == [True]:
    print('Заказ доставлен роботом-курьером!')
elif res_sum_kg <= 5 and newMyRand == [True]:
    print('Заказ доставлен дроном!')

print(f'Итоговая стоимость заказа составляет: {res_sum_price} руб')
print(Fore.GREEN + 'The End!' + Style.RESET_ALL)

# Оптимальный путь на карте к определенной точке
while True:
    # Заполнить экран
    sc.blit(bg, (0, 0))
    # Рисуем работу алгоритма
    [pg.draw.rect(sc, pg.Color('forestgreen'), get_rect(x, y), 1) for x, y in visited]  # start
    [pg.draw.rect(sc, pg.Color('darkslategray'), get_rect(*xy)) for _, xy in queue]  # path
    pg.draw.circle(sc, pg.Color('purple'), *get_circle(*goal))  # finish

    # Работа алг Дейкстры
    if queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            queue = []  # Обнуляем очередь
            continue

        # Для всех смежных вершин будем рассчитывать новую цену перемещения от текущей вершины
        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[cur_node] + neigh_cost

            # Если новой вершины нет в словаре стоимости пути, то добавим эту вершину в очередь
            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                # Формируем приоритет для соседней вершины, добавляя к цене значение эвристики
                priority = new_cost + heuristic(neigh_node, goal)
                # Отправляем в очередь
                heappush(queue, (priority, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node

    # Рисуем путь
    path_head, path_segment = cur_node, cur_node
    while path_segment:
        pg.draw.circle(sc, pg.Color('brown'), *get_circle(*path_segment))
        path_segment = visited[path_segment]
    pg.draw.circle(sc, pg.Color('blue'), *get_circle(*start))
    pg.draw.circle(sc, pg.Color('magenta'), *get_circle(*path_head))
    # необходимые строки
    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(7)  # Кол-во кадров
