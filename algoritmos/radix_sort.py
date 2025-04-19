class RadixSort:
    def ordenar(self, arr):
        a = arr.copy()
        def counting_sort(exp):
            n = len(a)
            output = [0] * n
            count = [0] * 10
            for i in range(n):
                index = (a[i] // exp) % 10
                count[index] += 1
            for i in range(1, 10):
                count[i] += count[i - 1]
            for i in reversed(range(n)):
                index = (a[i] // exp) % 10
                output[count[index] - 1] = a[i]
                count[index] -= 1
            for i in range(n):
                a[i] = output[i]

        max_val = max(a)
        exp = 1
        while max_val // exp > 0:
            counting_sort(exp)
            exp *= 10
        return a