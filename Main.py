from math import exp

 # Input stock parameters

 #time interval for the binomial model
dt = input("Enter the timestep: ")

#initial asset price (current stock price)
S = input("Enter the initial asset price: ")

#Risk Free Discount Rate (interest rate used for discounting future cash flows)
r = 1.03

#Option strike price
K = input("Enter the option strike price: ")

#factor by which the underlying asset's price decreases over a single time step
#1 is a temp val
d = 1

#Asset growth factor u (the factor by which the stock price goes up).
u = input("Enter the asset growth factor u: ")

#N: Number of timesteps until expiration (the number of time intervals until the option 
N = input("Enter the number of timesteps until expiration: ")

#Asset growth probablity (probablity the stock will go up)
p = (exp(r * dt) - d) / (u - d)

# Input whether this is a call or a put option
call = raw_input("Is this a call or put option? (C/P) ").upper().startswith("C")




def price(k, us):
# Compute the stock price after ’us’ growths and ’k - us’ decays. """
    return S * (u ** (2 * us - k))

def bopm(k, us):

#Compute the option price for a node ’k’ timesteps in the future
#and ’us’ growth events. Note that thus there are ’k - us’ decay events.
#"""

# Compute the exercise profit
    stockPrice = price(k, us)
    if call: exerciseProfit = max(0, stockPrice - K)
    else: exerciseProfit = max(0, K - stockPrice)

    # Base case (this is a leaf)
    if k == N: return exerciseProfit

    # Recursive case: compute the binomial value
    decay = exp(-r * dt)
    expected = p * bopm(k + 1, us + 1) + (1 - p) * bopm(k + 1, us)
    binomial = decay * expected

# Assume this is an American-style option
    return max(binomial, exerciseProfit)

print ('Computed option price: $%.2f' % bopm(0, 0))
