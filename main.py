month = 0
invest_start = int(input())
percent = int(input())
percent_month = percent / 100
capital = 0
years = int(input())
period = 1
all_periods = 12
i = 0
u_1 = 0
while u_1 != years * 12:
    Total_per_month = invest_start * (1 + percent * (period/all_periods)) ** (all_periods * i)
    summ_month = invest_start * percent
    print(Total_per_month)

    period += 1
    i += 1
    u_1 += 1
