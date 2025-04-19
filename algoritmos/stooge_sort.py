class StoogeSort:
    def ordenar(self, arr):
        a = arr.copy()
        def sort(l, h):
            if l >= h:
                return
            if a[l] > a[h]:
                a[l], a[h] = a[h], a[l]
            if h - l + 1 > 2:
                t = (h - l + 1) // 3
                sort(l, h - t)
                sort(l + t, h)
                sort(l, h - t)
        sort(0, len(a) - 1)
        return a
