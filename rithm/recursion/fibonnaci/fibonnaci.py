class Fibonnaci:
    @classmethod
    def fib(self, n: int, debug: bool = False) -> int:
        if n <= 1:
            return n
        else:
            if debug:
                print(f"Calculating fib({n}) = fib({n - 1}) + fib({n - 2})")
            return self.fib(n - 1, debug=debug) + self.fib(n - 2, debug=debug)

    @classmethod
    def fib_memo(self, n: int, debug: bool = False, memo=None) -> int:
        if n <= 1:
            return n

        if memo is None:
            memo = {}

        if n not in memo:
            if debug:
                print(
                    f"Calculating fib_memo({n}) = fib_memo({n - 1}) + fib_memo({n - 2})"
                )
            memo[n] = self.fib_memo(n - 1, debug, memo) + self.fib_memo(
                n - 2, debug, memo
            )

        return memo[n]

    @classmethod
    def fib_print(self, n: int) -> int:
        for i in range(n + 1):
            print(Fibonnaci.fib(i), end=" ")


if __name__ == "__main__":
    n = 10  # Example input
    # result = Fibonnaci.fib(n, debug=True)
    # print(f"The {n}th Fibonacci number is: {result}")
    result = Fibonnaci.fib_memo(n, debug=True)
    print(f"The {n}th Fibonacci number is: {result}")
    Fibonnaci.fib_print(n)
