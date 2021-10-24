apple = int(input("How many apples do you want to buy? "))
NumberOfApple_X_ApplePrice= apple*20
print(f"20 Pesos X {apple} = {NumberOfApple_X_ApplePrice} Pesos")

orange = int(input("How many oranges do you want to buy? "))
NumberOfOrange_X_OrangePrice= orange*25
print(f"25 Pesos X {orange} = {NumberOfOrange_X_OrangePrice} Pesos")

total_amount = NumberOfApple_X_ApplePrice + NumberOfOrange_X_OrangePrice

print(f"{NumberOfApple_X_ApplePrice} Pesos + {NumberOfOrange_X_OrangePrice} Pesos = {total_amount} Pesos")
print(f"The total amount is {total_amount} Pesos.")