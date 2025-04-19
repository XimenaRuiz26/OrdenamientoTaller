class QuickSort:
    def ordenar(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            left = self.ordenar([x for x in arr[1:] if x < pivot])
            right = self.ordenar([x for x in arr[1:] if x >= pivot])
            return left + [pivot] + right
