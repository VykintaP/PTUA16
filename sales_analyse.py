import csv

# sukuriame zodyna, kuriame bus saugoma produktas:suma

product_sales = {}

with open('sales.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # praleidziu antraste

    # reikia iteruoti per eilutes ir reiksmes isskaidyti - produktas:suma

    for row in reader:
        product = row[1]
        sales = int(row[2])

        # produktus prideti i zodyna, jei yra - pardavimus

        if product in product_sales:
            product_sales[product] += sales  # take values [sales] ir prideti
        else:
            product_sales[product] = sales

# surasti su diziausiais pardavimais

highest_selling = max(product_sales, key=product_sales.get)
# get. - the key whose value you want to retriev


# atspausdinti

print("Total sales:")

for product, sales in product_sales.items():
    print(f"{product}: {sales}")

# produktas su max pardavimais

print(f"Highest selling product: {highest_selling}")
