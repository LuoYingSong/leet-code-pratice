rate_list = list(map(lambda x: int(x), input().split(' ')))
data_count = int(input())

saver = {}

oneday_cost = 60 * sum(rate_list)
def caculate_money(on_date, off_date):
    on_date_list = list(map(lambda x: int(x), on_date.split(':')))[1:]
    off_date_list = list(map(lambda x: int(x), off_date.split(':')))[1:]
    on_date_cost_money = oneday_cost * on_date_list[0] + sum(rate_list[:on_date_list[1]]) * 60 + rate_list[
        on_date_list[1]] * \
                         on_date_list[2]
    off_date_cost_money = oneday_cost * off_date_list[0] + sum(rate_list[:off_date_list[1]]) * 60 + rate_list[
        off_date_list[1]] * \
                          off_date_list[2]
    # print(on_date_cost_money,off_date_cost_money)
    on_date_minute = int(on_date_list[2]) + 60 * int(on_date_list[1]) + 60 * 24 * int(on_date_list[0])
    off_date_minute = int(off_date_list[2]) + 60 * int(off_date_list[1]) + 60 * 24 * int(off_date_list[0])
    return (off_date_cost_money-on_date_cost_money) / 100, off_date_minute-on_date_minute


for i in range(data_count):
    name, date, status = input().split(' ')
    if name not in saver:
        saver[name] = {}
    if date[:2] not in saver[name]:
        saver[name][date[:2]] = {'on-line': [], 'off-line': []}
    saver[name][date[:2]][status].append(date)
for name in saver.keys():
    for month in saver[name].keys():
        for status in saver[name][month].keys():
            saver[name][month][status] = sorted(saver[name][month][status])
output_saver = {}  #
# print(saver)
for name in saver.keys():
    output_saver[name] = {}
    for month in saver[name].keys():
        output_saver[name][month] = []
        data_info = saver[name][month]
        on_index = len(data_info['on-line']) - 1
        off_index = len(data_info['off-line']) - 1
        flag = False
        # print(name)
        while on_index >= 0 and off_index >= 0:
            # print(on_index, off_index, flag)
            if data_info['on-line'][on_index] < data_info['off-line'][off_index]:
                off_index -= 1
                flag = True
                if off_index == -1:
                    output_saver[name][month].append(
                        [data_info['on-line'][on_index], data_info['off-line'][off_index + 1]])
            else:
                if flag:
                    output_saver[name][month].append(
                        [data_info['on-line'][on_index], data_info['off-line'][off_index + 1]])
                    on_index -= 1
                    flag = False
                else:
                    on_index -= 1
# print(sorted(output_saver.keys()))
for name in sorted(output_saver.keys()):
    for month in sorted(output_saver[name].keys()):
        if len(output_saver[name][month]):
            print(name + ' ' + month)
        total_money = 0
        for data in reversed(output_saver[name][month]):
            money, minute = caculate_money(data[0],data[1])
            total_money += money
            print('{} {} {} ${:.2f}'.format(data[0][3:],data[1][3:],minute,money))
        if len(output_saver[name][month]):
            print('Total amount: ${:.2f}'.format(total_money))
