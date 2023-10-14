from datetime import date, timedelta
# TH1: giá cổ phiếu nhận được là một số thực


def get_max_value_of_the_stock():
    '''
    giá cổ phiếu tối đa đạt được trong mõi ngày từ 09/08/2022 đến 12/08/2022
    '''
    current_date = date(2022, 8, 8)
    start_price = 7.24
    temp_price = start_price
    while current_date.day <= 12:
        current_date += timedelta(days=1)
        if current_date.weekday() in [5, 6]:
            continue
        temp_price *= 1.07
    return f'{(current_date- timedelta(days=1)).strftime("%A,%d/%m/%Y")}: {temp_price}'


def get_date():
    '''
    thời điểm sớm nhất mà giá cổ phiếu chạm mốc 58.69 nghìn đồng
    '''
    max_price = 58.69
    current_date = date(2022, 8, 8)
    start_price = 7.24
    temp_price = start_price
    while temp_price < max_price:
        current_date += timedelta(days=1)
        if current_date.weekday() in [5, 6]:
            continue
        temp_price *= 1.07
    return f'{(current_date - timedelta(days = 1)).strftime("%A,%d/%m/%Y")}: {temp_price}'


# TH2: giá cổ phiếu là 1 chữ số sau dấu thập phân có 2 chữ số
# Ta chỉ cần làm tròn temp_price.
# temp_price= int(temp_price*100)/100
if __name__ == '__main__':
    print(get_max_value_of_the_stock())
    print(get_date())
# Friday,12/08/2022: 9.490163112400001
# Monday,19/09/2022: 58.97061736449431
