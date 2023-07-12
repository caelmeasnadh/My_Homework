expected_profit = [1000, 1000, 1200, 1400, 1600, 1800, 2000]
our_profit = [800, 900, 1500, 1400, 2500, 2600, 2800]
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for expected_value, our_value, day2 in zip(expected_profit,our_profit,day) :
    print(f' The expected profit on {day2} was {expected_value}₴, but we got {our_value}₴, our clear profit is {our_value - expected_value}₴')
