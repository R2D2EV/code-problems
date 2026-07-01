"""
204. Count Primes
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
"""
class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0

        count_of_primes = 0
        is_prime = []

        for number in range(n):
            is_prime.append(True)

        is_prime[0] = False
        is_prime[1] = False

        p = 2

        while p * p < n:
            if is_prime[p]:
                reference = p * p

                while reference < n:
                    is_prime[reference] = False
                    reference += p
            p += 1

        for i in range(n):
            if is_prime[i]:
                count_of_primes += 1

        return count_of_primes
    
        
number1 = Solution()
print(number1.countPrimes(10))


# This solution is correct but ineffective.
class Solution2(object):
    @staticmethod
    def number_is_prime(m):
        if m < 2:
            return False
        
        for number in range(2, m):
            if m % number == 0:
                return False
            
        return True
            
    def countPrimes(self, n):
        counter = 0
        
        for number in range(2, n):
            if Solution2.number_is_prime(number) == True:
                counter += 1

        return counter

        
number = Solution2()
print(number.number_is_prime(9))
print(number.countPrimes(10))

