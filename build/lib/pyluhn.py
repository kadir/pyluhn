__all__ = ['verify']

def luhn_algorithm(target, base):
    digits = list(map(int,target))
    odd_numbers = sum(digits[-1::-2]) # Calculation for Odd digit numbers
    even_numbers = sum([sum(divmod(2 * k, base)) for k in digits[-2::-2]]) # Calculation for Even Digit Numbers
    return ((odd_numbers + even_numbers) % base ) == 0


def verify(target,base=10):
    # Verify the Given String if it is Valid for Luhn Algorithm in mod N
    # Default N is 10.
    # >>> verify("1234")
    # False
    # >>> verify("26")
    # True
    return luhn_algorithm(target,base) 
