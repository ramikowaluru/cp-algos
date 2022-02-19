class Tribonacci:
    def trib(self,nth_val):
        def dp(i):
            if i==0:
                return 0
            if i==1:
                return 1
            if i==2:
                return 1
            if i in mem:
                return mem[i]
            mem[i]= dp(i-3)+dp(i-2)+dp(i-1)

            return mem[i]
        mem = {}

        return dp(nth_val)

if __name__ == '__main__':
    trib = Tribonacci()
    print(trib.trib(10))