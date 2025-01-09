import csv

# sukurti ir atidaryti nauja failą 'products.csv'
with open('products.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product', 'Price', 'Quantity'])  # antraste

    # produktu duomenys
    writer.writerow(['Laptop', 1200, 5])
    writer.writerow(['Mouse', 20, 50])
    writer.writerow(['Keyboard', 45, 20])

