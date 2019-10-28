import math as m
import local as lc

MONTH = 1
CAPITAL = 0

year = int(input("Срок размещения капитала (лет): "))
print(lc.TEXT_END)
capital_start = float(input("Начальный капитал ($): "))
print(lc.TEXT_END)
percent_bank = float(input("Процентная ставка (%/мес.): "))
print(lc.TEXT_END)
investment_give = float(input("Инвестиционные вливания ($/мес.): "))

for year_print in range(year):
    month = 0
    year_print += 1
    print("")
    print(year_print, "ГОД / YEAR")
    print(lc.TEXT_END)
    print("| month |   основа   | сумма %  |         |")
    print("| месяц | инвестиций | за месяц | капитал |")
    print(lc.TEXT_END)





