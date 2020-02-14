import pandas as pd

orders = pd.read_csv('orders.csv', sep=';')
products = pd.read_csv('Products.csv', sep=';')

prlst = pd.merge(orders, products, how='left', left_on='ID товара', right_on='Product_ID')

payed = prlst[(prlst['Product_ID'] < 105) & (prlst['Product_ID'] > 85) & (prlst['Оплачен'] == 'Да')]
payed = payed[['Количество', 'Product_ID', 'Price']]

print(sum(payed['Количество'] * payed['Price']))
