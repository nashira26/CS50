sum = 0
while (sum < 50):
    print("Amount Due:", 50 - sum)
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        sum += coin
    else:
        continue

print("Change Owed:", sum - 50)
