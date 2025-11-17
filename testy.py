

def hello(name: str):
    return f"czesc {name}"

def max2(a,b):
    if a>b:
        return f"{a} jest wieksze"
    else:
        return f"{b} jest wieksze"

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def factoria(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

def samogoloski(s):
    licznik = 0
    samogoloski1 = ["a","e","i","o","u","y"]
    for litera in s.lower():
        if litera in samogoloski1:
            licznik += 1
    return  licznik


def rev_w(s):
    slowa = s.split()
    slowa.reverse()
    return ' '.join(slowa)


def sum_parzyste(nums: list[int]):
    suma = 0
    for liczba in nums:
        if liczba % 2 == 0:
            suma += liczba
    return suma

print(sum_parzyste([1,2,3,4,6]))