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
u_1 = 0

while u_1 != years * 12:
    Total_per_month = invest_start * (1 + percent * (period / all_periods)) + invest_river             #Нужен вывод
    summ_month = invest_start * percent                                                                #Нужен вывод

    print(Total_per_month)

    period += 1
    i += 1
    u_1 += 1





