#BEST TIME TO BUY AND SELL STOCKS 

a=[7,1,5,3,6,4] # prices of stock on each day
n=len(a)

min=a[0]
max_profit=0

for i in a:
    if i<min:
        min=i
    elif i-min>max_profit:
        max_profit=i-min
print("Max profit is :",max_profit)
    