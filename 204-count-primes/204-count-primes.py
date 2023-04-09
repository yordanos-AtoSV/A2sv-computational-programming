class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1: return 0
        is_prime = [True for _ in range(n)]
        is_prime[0] = is_prime[1] = False

        i = 2

        while i * i < n:
            if is_prime[i]:
                is_prime[i] = True
                j = i * i
                while j < n:
                    is_prime[j] = False
                    j += i
            i += 1
        is_prime = is_prime[2:]
    
        count = Counter(is_prime)
        return count[True]
    