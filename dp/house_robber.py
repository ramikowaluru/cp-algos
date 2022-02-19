class Robbery:
    def __init__(self):
        pass

    def rob_value(self, worth):

        def dp(i):
            if i == 0:
                return worth[0]
            if i == 1:
                return min(worth[0], worth[1])
            if i in mem:
                return mem[i]
            mem[i] = max(dp(i - 1), dp(i - 2) + worth[i])

            return mem[i]

        mem = {}
        return dp(len(worth) - 1)


if __name__ == '__main__':
    rob = Robbery()
    print(rob.rob_value([1, 2, 3, 1]))
