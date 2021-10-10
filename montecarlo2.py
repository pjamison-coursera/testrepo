import random
from matplotlib.pyplot import hist, plot, show


def ChangeInBalance(initial_balance):
    rate = random.uniform(0.0, 0.06)
    return initial_balance*rate

#Set initial conditions
number_sims = 1000
final_balances = []
balance = 1000
number_year= 10

for i in range(number_sims):
    #Set initial conditions
    time = 0
    balance = 1000
    while (time < number_year):
        #Increase balance and time
        balance += ChangeInBalance(balance)
        time += 1
    final_balances.append(balance)

#Output the simulation results
hist(final_balances, bins=20)
show()
