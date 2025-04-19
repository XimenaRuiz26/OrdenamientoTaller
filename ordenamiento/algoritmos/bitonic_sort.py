class BitonicSort:
    def ordenar(self, arr):
        from math import log2
        def compare_and_swap(a, i, j, direction):
            if (direction == 1 and a[i] > a[j]) or (direction == 0 and a[i] < a[j]):
                a[i], a[j] = a[j], a[i]

        def bitonic_merge(a, low, cnt, direction):
            if cnt > 1:
                k = cnt // 2
                for i in range(low, low + k):
                    compare_and_swap(a, i, i + k, direction)
                bitonic_merge(a, low, k, direction)
                bitonic_merge(a, low + k, k, direction)

        def bitonic_sort_rec(a, low, cnt, direction):
            if cnt > 1:
                k = cnt // 2
                bitonic_sort_rec(a, low, k, 1)
                bitonic_sort_rec(a, low + k, k, 0)
                bitonic_merge(a, low, cnt, direction)

        n = len(arr)
        power_of_two = 1 << (n - 1).bit_length()
        a = arr.copy() + [max(arr)] * (power_of_two - n)
        bitonic_sort_rec(a, 0, power_of_two, 1)
        return a[:n]
