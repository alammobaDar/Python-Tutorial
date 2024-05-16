# fibonnacci sequence

def fibonacci_sequence(num):
    if num <= 1:
        return num
    else:
        return fibonacci_sequence(num -1) + fibonacci_sequence(num -2)
    fib_seq = [0,1]
    return fib_seq.append([fibonacci_sequence(i) in range(num)])



print(fibonacci_sequence(4))

