import datetime
import sys
now = datetime.datetime.now()
date_time = now.strftime('%Y-%m-%d %I:%M:%S %p')

# Our items in dictionary, flavors as the key and prices as value
cake = {'chocolate': 500,
        'vanilla': 450,
        'mocha': 400,
        'redvelvet': 600,
        'darkchoco': 700,
        'carrot': 400,
        'cheese': 300,
        'caramel': 350}

# Empty variables
item = []
item_item = {}
quantity = 0
total = 0
change = 0
subtotal = 0
vat = 0
vatable = 0
cash = 0

# List of cakes and its prices
while True:
    print("********** Welcome to Juan Bikeri *********")
    print('NOTE: PRICES BELOW DOES ALREADY HAVE TAX ')
    print('****** This are the available flavor ******')
    print('CAKE                               -  PRICE')
    for flavor, price in cake.items():
        tax = price * 0.12
        display = price + tax
        print(f'{flavor:35}- ₱{display}')

    # User/Customer Input for purchasing
    print('*******************************************')
    while True:
        pick = input("Choose a cake (type 'end' to stop): ").lower()
        if cake.get(pick) is not None:
            while True:
                try:
                    quantity = int(input('Quantity: '))
                except ValueError:
                    print('Invalid Input!')
                    continue
                if quantity <= 0:
                    print('Please enter how many!')
                    continue
                else:
                    break
            if pick in item_item:
                item_item[pick] += quantity
            else:
                item_item[pick] = quantity
            item.append([pick, quantity])
        elif pick == 'end':
            break
        else:
            print('Invalid Input!')

    # Calculation of vatable, vat, and total
    print('*******************************************')
    for pick, quantity in item:
        vatable += cake.get(pick) * quantity
        vat = vatable * 0.12
        total = vatable + vat

    # User/Customer Input for discount
    print('A - PWD / Senior / Coupon (5%)')
    print('B - Regular')
    while True:
        status = input('Choose a Discount: ').lower()
        if status == 'a':
            discount = total * 0.05
            break
        elif status == 'b':
            discount = 0
            break
        else:
            print('Invalid Input!')

    # User/Customer Input for payment
    print('***************** Payment *****************')
    print(f'Total (w/tax & w/o discount): {round(total, 2)}')
    while True:
        try:
            cash = float(input('Please enter your payment: '))
        except ValueError:
            print('Invalid Input!')
            continue
        if cash >= total:
            change = (cash - total) + discount
            break
        else:
            print('Invalid Payment!')
    print('*******************************************\n\n')

    # Official Receipt
    print('======================= RECEIPT =========================')
    print("                      JUAN BIKERI")
    print('                OWNED AND OPERATED BY:')
    print('         PAR, NICOL, GASCON, BITANCOR, JAVIER')
    print('               CAVITE STATE UNIVERSITY')
    print('                     IMUS,CAMPUS')
    print('         REGISTERED VAT TIN. 091-234-567-890')
    print('---------------------------------------------------------')
    print('NAME:')
    print('CASHIER: Python')
    print('PROCESSED BY: Python')
    print(f'DATE: {date_time}')
    print('---------------------------------------------------------')
    print('ITEM                 QUANTITY                 SUB-TOTAL')
    # Display of items purchased, quantity, and its subtotal
    for pick, quantity in item_item.items():
        subtotal = cake.get(pick) * quantity
        per_item = subtotal * 0.12
        sub_tax = subtotal + per_item
        print(f'{pick:15} {quantity:10} {round(sub_tax, 2):25}', end=' ')
        print()
    print('---------------------------------------------------------')
    print(f'TOTAL    :                                    {round(total, 2):1}')
    print(f'CASH     :                                    {round(cash, 2):1}')
    print(f'DISCOUNT :                                    {round(discount, 2):1}')
    print(f'CHANGE   :                                    {round(change, 2):1}')
    print('---------------------------------------------------------')
    print(f'VATable  :                                    {round(vatable, 2):1}')
    print(f'12% VAT  :                                    {round(vat, 2):1}')
    print('---------------------------------------------------------')
    print('                       THANK YOU!')
    print("             FOR PURCHASING AT JUAN BIKERI")
    print('                 HOPE TO SEE YOU AGAIN')
    print(f'                DATE ISSUED: {date_time[0:10]}')
    print('           TEL # 0912-345-6789 / (123) - 4567')
    print('=========================================================\n')

    # Condition for repeating the transaction
    while True:
        proceed = input('Would you like to retry transaction? (yes/no): ').lower()
        if proceed == 'yes' or proceed == 'y':
            item.clear()
            item_item.clear()
            total -= total
            vatable -= vatable
            vat -= vat
            break
        elif proceed == 'no' or proceed == 'n':
            print('\nThank You!')
            sys.exit()
        else:
            print('Invalid Input!')
    print('\n')
