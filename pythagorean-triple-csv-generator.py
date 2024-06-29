import math
from fractions import Fraction

distances = 100
n = 100

def csv_print(*args, log):
    log.append(','.join(map(str, args)))
    # print(*args, sep=",")


for k in range(1, distances+1):
    data = []
    data_fractions = []
    csv_print("a", "b", "c", log=data)
    csv_print("a", "b", "c", log=data_fractions)
    for b in range(n+1):
        if b <= k:
            continue
        c = (1/2) * (math.pow(b, 2) / k + k)
        a = (1/2) * (math.pow(b, 2) / k - k)
        is_triple = math.pow(c, 2) == math.pow(a, 2) + math.pow(b, 2)
        csv_print(a, b, c, log=data)
        csv_print(Fraction(a), Fraction(b), Fraction(c), log=data_fractions)

    with open(f"pythagorean-triple-csv-generator_{k}.csv", 'w') as csvfile:
        csvfile.write('\n'.join(data))

    # I do this to handle issues with precision handling but it's not great in python
    # reason: is_triple = math.pow(c, 2) == math.pow(a, 2) + math.pow(b, 2)
    # is_triple will show false due to precision mismatch on the power and not be correct
    # I have checked and the function works fine, this will be my suffering for using python, lol
    with open(f"pythagorean-triple-csv-generator_fractions_{k}.csv", 'w') as csvfile:
        csvfile.write('\n'.join(data_fractions))
