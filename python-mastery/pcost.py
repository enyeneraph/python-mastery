
with open('Data/portfolio.dat', 'rb') as f:
    sum = 0
    for line in f:
        row = line.decode()
        company, num, price = row.split()
        sum += float(num)*float(price)

        print(sum)
