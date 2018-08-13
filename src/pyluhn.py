__all__ = ['verify']

def luhn_algorithm(target, base):
    digits = list(map(int,target))
    odd_numbers = sum(digits[-1::-2])
    even_numbers = sum([sum(divmod(2 * k, base)) for k in digits[-2::-2]])
    return ((odd_numbers + even_numbers) % base ) == 0

def verify(target,base=10):
    return luhn_algorithm(target,base) 