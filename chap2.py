base_price = int(input('Enter the base price:'))
tax = 0.05 * base_price
car_license = 0.01 * base_price
dealer_prep = 100
destination_charge = 50
actual_price = tax+car_license+dealer_prep+destination_charge
print('Total cost for car is: ', actual_price)
