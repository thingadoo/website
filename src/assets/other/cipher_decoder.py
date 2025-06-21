import sys
import math

cipher_dict = {
  "e": 2,
  "a": 3,
  "r": 5,
  "i": 7,
  "o": 11,
  "t": 13,
  "n": 17,
  "s": 19,
  "l": 23,
  "c": 29,
  "u": 31,
  "d": 37,
  "p": 41,
  "m": 43,
  "h": 47,
  "g": 53,
  "b": 59,
  "f": 61,
  "y": 67,
  "w": 71,
  "k": 73,
  "v": 79,
  "x": 83,
  "z": 89,
  "j": 97,
  "q": 101
}
special_characters = "!@#$%^&*()_+{}|:<>?-=[];',./"

cipher_dict_swapped = {v: k for k, v in cipher_dict.items()}

inpu: str = input("input message to be decoded: ")
li = list(str(inpu).split(" "))
for n in li:
    n = int(n)
  # from https://www.geeksforgeeks.org/python/python-program-for-efficient-program-to-print-all-prime-factors-of-a-given-number/
    # Print the number of two's that divide n
    while n % 2 == 0:
        sys.stdout.write("e")
        n = n // 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
        # while i divides n , print i ad divide n
        while n % i== 0:
            sys.stdout.write(cipher_dict_swapped[i])
            n = n // i

  # Condition if n is a prime
  # number greater than 2
    if n > 2:
        sys.stdout.write(str(cipher_dict_swapped[int(n)]))

    sys.stdout.write(" ")
