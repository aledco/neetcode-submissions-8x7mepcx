class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices = []

    def next(self, price: int) -> int:
        def bruteForce(self, price):
            self.stack.append(price)
            res = 0
            for i in range(len(self.stack)-1, -1, -1):
                if self.stack[i] <= price:
                    res += 1
                else:
                    break
            return res
        
        # return bruteForce(self, price)

        def optimized(self, price):
            # observation: if price is less than the last price, we reset to 1
            # observation: if price is greater than or equal to the last price, we return to the end of the span of the last price, and continue looking
            if len(self.prices) == 0 or price < self.prices[-1]:
                self.prices.append(price)
                self.stack.append(1)
            else:
                s = 1
                # print(self.prices)
                # print(self.stack)
                while len(self.stack) > 0 and price >= self.prices[-s]:
                    s += self.stack.pop()
                    # print(s, self.prices[-s])
                # print()
                self.prices.append(price)
                self.stack.append(s)
            return self.stack[-1]
        
        return optimized(self, price)




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)