import art
def portfolio_cost(file_name):
    with open(file_name, 'rb') as f:
        sum = 0
        for line in f:
            try:
                row = line.decode()
                company, num, price = row.split()
                sum += float(int(num))*float(price)
            except ValueError as e:
                print(e)

    return sum

print(portfolio_cost('Data/portfolio3.dat'))
