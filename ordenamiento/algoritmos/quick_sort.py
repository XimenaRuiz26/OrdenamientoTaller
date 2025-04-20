class QuickSort:
    def ordenar(self, arr):
        return self._quick_sort(arr)

    def _quick_sort(self, arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]  # Elegimos un pivote más balanceado
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return self._quick_sort(left) + middle + self._quick_sort(right)
