def depositProfit(deposit, rate, threshold):
    year = 0
    while deposit < threshold:
        deposit += deposit * rate / 100
        year += 1
    return year

print(depositProfit(deposit=50, rate=25, threshold=100))

'''
You have deposited a specific amount of money into your bank account. 
Each year your balance increases at the same growth rate. 
With the assumption that you don't make any additional deposits, find out how long it would take 
for your balance to pass a specific threshold. 
Of course you don't want to wait too long, so you know that the answer is not greater than 6.'''