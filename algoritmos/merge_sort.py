class MergeSort:
    def ordenar(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = self.ordenar(arr[:mid])
            R = self.ordenar(arr[mid:])
            return self.merge(L, R)
        else:
            return arr

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
