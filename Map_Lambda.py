cube = lambda n: n**3

#def fibonacci(n):
    
def fibonacci(n):
    
    
    sequence = [0, 1]
    

    any(map(lambda _: sequence.append(sum(sequence[-2:])), range(2, n)))
    

    return sequence[:n]

#print(fibonacci(n))
