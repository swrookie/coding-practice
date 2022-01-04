class Solution:
    def decimal_to_binary(self, n):
        remainder = []

        while n > 0:
            remainder.insert(0, n % 2)
            n //= 2

        return remainder

    def binary_to_decimal(self, l):
        bn = 0
        coeff = 0
        for i in range(len(l) - 1, -1, -1):
            if l[i] != 0:
                bn += 2 ** coeff
            coeff += 1

        return bn

    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        bn_as_list = self.decimal_to_binary(n)

        for i in range(0, len(bn_as_list)):
            bn_as_list[i] = int(not bn_as_list[i])

        # bn = "".join(bn_as_list)

        complement_n = self.binary_to_decimal(bn_as_list)

        return complement_n


if __name__ == "__main__":
    print(Solution().bitwiseComplement(n=5))
