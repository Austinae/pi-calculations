import sys
import time
import numpy
import math
import decimal

# def ArctanDenom(d, ndigits):
#     # Calculates arctan(1/d) = 1/d - 1/(3*d^3) + 1/(5*d^5) - 1/(7*d^7) + ...
#     total = term = (10**ndigits) // d
#     n = 0
#     while term != 0:
#         n += 1
#         term //= -d*d
#         total += term // (2*n + 1)
#     print('ArctanDenom({}) took {} iterations.'.format(d, n))
#     return total
#
# if __name__ == '__main__':
#     if len(sys.argv) != 3:
#         print('USAGE: picrunch.py ndigits outfile')
#         sys.exit(1)
#
#     xdigits = 10             # Extra digits to reduce trailing error
#     ndigits = int(sys.argv[1])
#     outFileName = sys.argv[2]
#
#     start = time.time()
#
#     # Use Machin's Formula to calculate pi.
#     pi = 4 * (4*ArctanDenom(5,ndigits+xdigits) - ArctanDenom(239,ndigits+xdigits))
#
#     # We calculated extra digits to compensate for roundoff error.
#     # Chop off the extra digits now.
#     pi //= 10**xdigits
#
#     # Write the result to a text file.
#     with open(outFileName, 'wt') as outfile:
#         # Insert the decimal point after the first digit '3'.
#         text = str(pi)
#         outfile.write(text[0] + '.' + text[1:] + '\n')
#
#     print('Wrote to file {}'.format(outFileName))
#     end = time.time()
#     totTime = end - start
#     print(round(totTime/60, 3), "minutes or ", round(totTime, 2), "seconds")
#     sys.exit(0)

# Wallis formula

def WallisPi(n):
    pi = 1
    for i in range(1, n):
        if i % 2 == 0:
            pi += 1 / ((i * 2) + 1)
        else:
            pi -= 1/((i*2) + 1)
    return pi * 4


# Archimedes formula

def pi_archimedes(n):
    """
    Calculate n iterations of Archimedes PI recurrence relation
    """
    polygon_edge_length_squared = 2.0
    polygon_sides = 4
    for i in range(n):
        polygon_edge_length_squared = 2 - 2 * math.sqrt(1 - polygon_edge_length_squared / 4)
        polygon_sides *= 2
    return polygon_sides * math.sqrt(polygon_edge_length_squared) / 2

def main():
    """
    Try the series
    """
    for n in range(16):
        result = pi_archimedes(n)
        error = result - math.pi
        print("%8d iterations %.10f error %.10f" % (n, result, error))

def ramanujanPi(r):
    denominator = 0
    for n in range(r):
        denominator += (numpy.math.factorial(4*n)/numpy.math.pow(numpy.math.factorial(n), 4))*((1103+26390*n)/(numpy.math.pow(396, 4*n)))
    return 9801/(2*math.sqrt(2)*denominator)

print(decimal.Decimal(ramanujanPi(30)))