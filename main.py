month = 0
years = int(input("Срок размещения капитала (лет):"))
invest_start = int(input("Начальный капитал ($):"))
percent = int(input("Процентная ставка (%/мес.):"))
invest_river = int(input("Инвестиционные вливания ($/мес.):"))
percent_month = percent / 100
capital = 0
period = 1
all_periods = 12
i = 0
months = 0
months_1 = 0
while months_1 != years * 12:
    Total_per_month = invest_start * (1 + percent * (period / all_periods)) + invest_river             #Нужен вывод
    summ_month = invest_start * percent                                                                #Нужен вывод

    print(Total_per_month)
    months += 1
    period += 1
    i += 1
    months_1 += 1
    if months == 12:
        months = 0
        print('new_year')





