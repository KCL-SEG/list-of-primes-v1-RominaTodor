"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
     list=[]
     num=2

     while len(list)<number_of_primes:
          prime=True
          for prime_num in range(2, int(num**0.5)+1):
               if num%prime_num==0:
                    prime=False
                    break
          if prime:
               list.append(num)
          num+=1
     return list
