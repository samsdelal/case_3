import local as lc
import time as t

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
    t.sleep(1)
    print(year_print, "ГОД / YEAR")
    t.sleep(1)
    print(lc.TEXT_END)
    print("| month |   основа   | сумма %  |         |")
    print("| месяц | инвестиций | за месяц | капитал |")
    print(lc.TEXT_END)
    while month < 13:
        round(capital_start, 2)
        summ_month = percent_bank * capital_start / 100
        basement = capital_start * (percent_bank / 100 + 1)
        summ_month = float('{:.1f}'.format(summ_month))
        basement = float('{:.1f}'.format(basement))
        t.sleep(0.01)
        print("|", month, "| ", capital_start, " | ", summ_month, " | ", basement, " |")
        month += 1
        capital_start = capital_start * (percent_bank / 100 + 1) + investment_give
        capital_start = float('{:.1f}'.format(capital_start))






