'''
Гениальный инженер Винтик может собрать из любых подручных материалов модель троллейбуса, но не может сварить яйцо всмятку. Как бы он ни пытался — получается либо вкрутую, либо почти сырое. На каком-то форуме он вычитал, что чтобы сварить яйцо всмятку, нужно с большой точностью выдержать температуру по определённому графику (график прилагался).

Воодушевлённый возможностью решить нерешаемую задачу, Винтик взялся за дело. Он построил специальную печь с управляемым нагревом, а чтобы точно выдержать температурный режим и исключить влияние даже сквозняка — подключил к ней ПИД-регулятор. Также он провёл испытания печи и построил её математическую модель. Однако его экзистенциальная несовместимость с яйцами всмятку снова проявила себя в том, что у него никак не получается подобрать параметры ПИД-регулятора! В прошлом он решал такие задачи тысячи раз, он может подобрать эти три несчастных числа для чего угодно, но только не для яиц всмятку. В отчаянии он выложил все параметры задачи на форум, включая матмодель печи, описание ПИД-регулятора и даже матмодель сквозняков! Помогите ему, подобрав параметры ПИД-регулятора для его задачи до того, как он решит, что яйца всмятку — мировой заговор и их не существует.

Входной формат: единственное целое число — затравка генератора сквозняка (см. код).

Выходной формат: три числа через пробел — коэффициенты P, I и D регулятора.
'''

"""
Проект: Аккуратный Нагрев в Условиях Сквозняка
(С) 2021 Инженер Винтик
Лицензия: MyPrecious
"""
import random

# TODO: портировать под квантовый суперкомпьютер

maxTime = 1000  # количество отсчётов
dt = 1  # интервал отсчётов (в секундах)
minVal, maxVal = -1000, 1000  # интервал допустимых управляющих воздействий
integral, prevErr = 0, 0

#########
SEED = 410915411 # затравка для генератора сквозняков

# TODO: подобрать коэффициенты (я кушать хочу :( )
KP = 1.0
KI = 0.0
KD = 0.0
##########

def rand_wind(n, seed=None):
    """Генерирует график сквозняков.

    n — количество отсчётов
    seed — затравка для генератора случайных чисел
    """
    if seed:
        random.seed(seed)
    a = []
    x = random.uniform(-5, 5)
    dx = 0
    dt = 0
    while len(a) < n:
        if dt == 0:            
            mode = random.randint(1, 3)
            sgn = random.choice((-1, 1))
            if mode == 1:
                dt = random.randint(20, 30)
                dx = sgn * random.uniform(2, 3) / 10
            elif mode == 2:
                dt = random.randint(10, 20)
                dx = sgn * random.uniform(3, 5) / 10
            elif mode == 3:
                dt = random.randint(5, 10)
                dx = sgn * random.uniform(5, 10) / 10
        a.append(x)
        x += dx
        dt -= 1
    return a

external = rand_wind(maxTime, seed=SEED)
steadyT, activeT = 150, 300
setpoint = (
    [25 + x/250 * (steadyT-25) for x in range(250)] +
    [steadyT for x in range(250)] +
    [steadyT + x/150 * (activeT-steadyT) for x in range(150)] +
    [activeT for x in range(maxTime-800)] +
    [activeT - x/150 * (activeT-steadyT) for x in range(150)]
)


def pid_compute(target, setpoint):
    """ Вычисляет управляющее воздействие нагревателя.

    target — текущая температура в печи
    setpoint — необходимая температура
    """

    """
    TODO: реализовать ПИД-регулятор по формуле
    k(t) = kp * (e(t) + ki * dt * sum(e(t)) + kd * (e(t)-e(t-1)) / dt)
    Интегральная часть не ограничивается.
    А вот выходное значение — ограничивается!
    """

    return 0


def calc(externals, targets, controls, newControl):
    """ Вычисляет новую температуру печи.

    externals – история температуры сквозняка (в т.ч. текущее значение)
    targets – история температуры печи (в т.ч. текущее значение)
    controls – предыдущие значения из ПИД-регулятора
      (во всех списках последнее значение — справа)
    newControl – текущее значение ПИД-регулятора

    Изобретения хорошего инженера законам реальности не подчиняются,
    а любая достаточно продвинутая технология неотличима от магии.
    """
    # Хвост по обратной связи
    tf = 0
    n = 0
    trailLength = 10
    trailWidth = 0.9
    for i in range(min(trailLength,len(targets))):
        scale = trailWidth ** i
        tf += externals[-(i+1)] * scale
        n += scale
    tf /= n

    # Хвост по внешнему воздействию
    te = 0
    nc = 0
    for i in range(min(trailLength,len(externals))):
        scale = trailWidth ** i
        te += externals[-(i+1)] * scale
        nc += scale
    te /= nc + 1
    
    # Возведение в степень
    def pw(x,p):
        if x>0:
            return x ** p
        else:
            return -(abs(x) ** p)

    # Как-бы производная по внешнему воздействию
    if len(externals) < 2:
        de = 0
    else:
        de = externals[-1] - externals[-2]
        de = pw(de,1.2)
        de = de.real

    # Как-бы производная по обратной связи
    if len(targets) < 2:
        df = 0
    else:
        df = targets[-1] - targets[-2]
        df = pw(df,0.85)
        df = df.real
    
    # Как-бы производная по управлению
    if len(controls) < 1:
        dc = 0
    else:
        dc = newControl - controls[-1]
        dc = pw(dc,1.1)
        dc = dc.real
    
    newTarget = ( 0
        + tf
        + te
        + de
        + df
        + dc
        + newControl
    )
    return newTarget

def get_targets(data=None):
    """ Считает график температуры внутри печи.
    """
    if data is not None:
        global KP, KI, KD, integral, prevErr
        integral, prevErr = 0, 0
        KP, KI, KD = data
    
    targets, externals, controls = [], [], []
   
    value = 25
    for (set_p, ext) in zip(setpoint, external):
        externals.append(ext)
        targets.append(value)
        newControl = pid_compute(value, set_p)
        controls.append(newControl)
        value = calc(externals, targets, controls, newControl)
    
    return targets, controls
