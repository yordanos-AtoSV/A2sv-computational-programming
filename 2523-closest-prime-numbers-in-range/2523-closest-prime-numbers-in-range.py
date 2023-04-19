class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
            is_prime = [True for _ in range(right + 1)]
            is_prime[0], is_prime[1] = False, False
               
            i = 2

            while i * i < right + 1:
                if is_prime[i]:
                    is_prime[i] = True
                    j = i * i
                    while j < right + 1:
                        is_prime[j] = False
                        j += i
                i += 1
               
            ans = [-1, -1]
            primes = []
            for i in range(left, right + 1):
                if is_prime[i]:
                    primes.append(i)
      
            dist = float(inf)
            for i in range(len(primes) - 1):
                temp = primes[i + 1] - primes[i]
                if temp < dist:
                    dist = temp
                    ans[0] = primes[i]
                    ans[1] = primes[i + 1]
            return ans
                
                    
                