import random


def rabin_miller(n):
    # Rabin-Miler algorithm to calc large primes efficiently
    s = n - 1
    t = 0
    while s & 1 == 0:
        s = s / 2
        t += 1
    k = 0
    while k < 128:
        a = random.randrange(2, n - 1)
        v = pow(a, s, n)
        if v != 1:
            i = 0
            while v != (n - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % n
        k += 2
    return True


def is_prime(n):
    # low_primes is an array of small primes. it is used here to speed up the algorithm.
    low_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        , 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179
        , 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269
        , 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367
        , 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461
        , 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571
        , 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661
        , 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773
        , 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883
        , 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    if n >= 3:
        # check if n is not even (even number can't be a prime number)
        if n & 1 != 0:
            for p in low_primes:
                if n == p:
                    return True
                if n % p == 0:
                    return False
            return rabin_miller(n)
    return False


def _is_power_of_2(num):
    return ((num & (num - 1)) == 0) and num != 0


def generate_large_prime(bit_length):
    if not _is_power_of_2(bit_length):
        raise NumberNotPowerOf2Error
    while True:
        # Generate large number in the correct range and return if prime
        n = random.randrange(2 ** (bit_length - 1), 2 ** bit_length)
        if is_prime(n):
            return n


class NumberNotPowerOf2Error(Exception):
    pass
