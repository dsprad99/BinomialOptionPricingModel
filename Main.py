from math import exp

#timestep: 0.25
dt = .25 

#initial asset price: 178.78
S = 178.78

#the risk-free discount rate: 1
r = 1

#option strike price: 180
K = 180   

#the asset growth probability p: 1
p = 1   

#asset growth factor u: 1.2
u = 1.7   

#the number of timesteps until expiration: 2
N = 2   

# Input whether this is a call or a put option
call = True

def price(k, us):
    """ Compute the stock price after ’us’ growths and ’k - us’ decays. """
    return S * (u ** (2 * us - k))

def bopm(k, us):
    """
    Compute the option price for a node ’k’ timesteps in the future
    and ’us’ growth events. Note that thus there are ’k - us’ decay events.
    """

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
