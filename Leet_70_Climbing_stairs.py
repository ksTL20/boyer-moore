'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

1 <= n <= 45
'''

n: int = 0

#get to 10 by increments of either 1 or 2.

#steps: int = None #Count of either stepping by 1 or 2 to get to n.
#Brute force method: search through every permutation until the termination case is reached
#termination case: smallest steps summed to reached n.
# Use while loop

def num_to_binary(target:int) -> str: #function to generate the binary
    if target == 0:
        return str(0)
    #start = target
    output = ''
    dividend: int = target

    while dividend != 0:
        remainder = dividend % 2
        dividend = dividend // 2

        output = str(remainder) + output
        
    return output


def step_count(step_binary: str, target: int) -> int: #breakdown the binary to perform permutation to reach value of n. If value reached, add 
                                                    #eg: '101' for n=5; permutate through 1, then '10', then '101' 
    pass

print(num_to_binary(n))