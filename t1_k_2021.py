'''
Ребята собрали экспериментального всепогодного дрона доставки на большие расстояния, который может трансформироваться, подстраиваясь под разные условия окружающей среды. Для «боевого» тестирования они решили отправить дрона по самому непредсказуемому пути, пролегающему вблизи множества территорий с различными погодными условиями.

Ваша задача: написать программу, которая будет определять необходимость смены формы дрона по данным с датчиков. Так как обработка данных с датчиков дрона осуществляется на домашнем (удалённом от дрона) сервере, и данные передаются по каналу связи с дроном, имеется вероятность возникновения ошибочных данных, которые необходимо исправить. Ошибки проявляются в виде смены знака для значений температуры и влажности одновременно.  Считается, что возможность встретить область с температурой 0 ºC или влажностью 50% пренебрежительно мала, как и возможность встретить область с протяжённостью меньше 50 отчётов датчика дрона.

Режимы дрона:
1.«Буран». Для зон с влажностью более 50% и температурой менее 0ºC.
2.«Альтруист». Для зон с влажностью менее 50% и температурой более 0ºC.
3.«Теплоход». Для зон с влажностью более 50% и температурой более 0ºC.
4.«МорозКо». Для зон с влажностью менее 50% и температурой менее 0ºC.

Входной формат: произвольные N строк данных (до 7000). В каждой строке через пробел приводятся влажность и температура с единицами измерения. Например,
34% 15ºC
17% 25ºC
73% -12ºC
51% -3ºC
9% 33ºC

Выходной формат: N строк данных. В каждой строке цифра, соответствующая необходимому режиму дрона. Например,
4
4
1
1
1
3
3
'''

for i in range(50, 7000):
  hydra, temp = map(input(), split(' '))