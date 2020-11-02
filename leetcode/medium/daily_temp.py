"""
MEDIUM

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""

def dailyTemperatures(T):
# first-pass solution: works, but is too slow
    # for i, v in enumerate(T):
    #     warmer = next((d for d in T[i:] if d > v), None)
    #     print(warmer)
    
    #     if warmer:
    #         T[i] = T.index(warmer, i) - i
    #     else:
    #         T[i] = 0
        
    # return T

# optimized solution
    # create list of 0's to account for days without warmer temps
    days = [0] * len(T)

    # set warmest day to be unbounded
    warmer = float("-inf")
    
    # iterate thorugh temperatures
    for i in range(len(T) - 1, -1, -1):
        t = T[i]
        # if temperature is warmer, set warmer to new warmest temp
        if warmer <= t:
            warmer = t
        # else, increment days until a warmer temp
        else:
            days_until = 1
            # increase days counter until the warmer temp is reached
            while T[i + days_until] <= t:
                days_until += days[i + days_until]
            # set days_until warmer temp to days list
            days[i] = days_until
    
    return days