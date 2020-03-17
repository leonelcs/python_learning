
def sum_rec(list_of_values):
    if len(list_of_values) == 0:
        return 0
    else:
        return list_of_values[0] + sum_rec(list_of_values[1:])

def until(n, filter_func, v): 
    if v == n: return [] 
    if filter_func(v): return [v] + until(n, filter_func, v+1) 
    else: return until(n, filter_func, v+1) 

print(sum_rec([0,1,2,3,4,5,6,7,8,9,10]))

print(until(10, lambda x: x%2==0, 0))

print( sum( n for n in range(0,10) if n%2 == 0) )
    