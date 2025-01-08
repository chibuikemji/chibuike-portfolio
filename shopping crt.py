foods = []
prices = []
total = 0

def get_food():
    while True:
        food = input("enter the food you like(q to quit):").lower()
        if food == "q":
            break
        else:
            while True: 
                price = input(f"enter the price of the {food}: $")
                if price.isdigit():
                    price = int(price)
                    if price >= 1:
                        break
                    else:
                        print("price must be greater than 0") 
                else:
                    print("price must be a digit") 
            foods.append(food)
            prices.append(price)

def main():
    get_food()

if __name__ == "__main__":
    main()

print('---your cart---')
for i in foods:
    print(i)

for price in prices:
    total += price
print(f'your total is: ${total}')