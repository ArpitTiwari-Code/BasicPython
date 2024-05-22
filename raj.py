#WAP for  bill of 5 products1
product1=float(input("enter the price of product 1"))
product2=float(input("enter the price of product 2"))
product3=float(input("enter the price of product 3"))
product4=float(input("enter the price of product4 "))
product5=float(input("enter the price of product 5"))
total_price=product1+product2+product3+product4+product5
print("total bill of costumer ",total_price)
print("total bill of costumer " ,int(total_price))
discount=int(input("discount on total price" ))
total_discount=total_price/100*discount
print(" total discount",total_discount)
last_amount=total_price-total_discount
print("last amount to pay",last_amount)
print('thanks gannu')

