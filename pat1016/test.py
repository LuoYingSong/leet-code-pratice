rate_list = list(map(lambda x: int(x), input().split(' ')))

oneday_cost = 24 * 60 * sum(rate_list)


def caculate_money(on_date, off_date):
    on_date_list = list(map(lambda x: int(x), on_date.split(':')))[1:]
    off_date_list = list(map(lambda x: int(x), off_date.split(':')))[1:]
    on_date_cost_money = oneday_cost * (on_date_list[0]-1) + sum(rate_list[:on_date_list[1]]) * 60 + rate_list[
        on_date_list[1]] * \
                         on_date_list[2]
    off_date_cost_money = oneday_cost * (off_date_list[0]-1) + sum(rate_list[:off_date_list[1]]) * 60 + rate_list[
        off_date_list[1]] * \
                          off_date_list[2]
    on_date_minute = int(on_date_list[2]) + 60 * int(on_date_list[1]) + 60 * 24 * int(on_date_list[0])
    off_date_minute = int(off_date_list[2]) + 60 * int(off_date_list[1]) + 60 * 24 * int(off_date_list[0])
    return (off_date_cost_money-on_date_cost_money) / 100, off_date_minute-on_date_minute

print(caculate_money('1:01:06:01','1:01:08:03'))
