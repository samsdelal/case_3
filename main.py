
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
    while month < 13:
        summ_month = percent_bank * capital_start / 100
        new_capital = capital_start * (percent_bank / 100 + 1)
        round(summ_month, 1)
        round(new_capital, 1)
        print("|", month, "| ", initial_capital, " | ", summ_month, " | ", new_capital, " |")
        month += 1
        initial_capital = capital_start * (percent_bank / 100 + 1) + investment_give






