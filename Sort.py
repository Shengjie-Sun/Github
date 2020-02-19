class Sort():

    def quick_sort(self, array, l, r):

        def partition(array, l, r):
            pivot = array[r]
            split = l - 1
            for j in range(l, r):
                if array[j] <= pivot:
                    split += 1
                    array[split], array[j] = array[j], array[split]
            array[split+1], array[r] = array[r], array[split+1]
            
            return split+1

        if l < r:
            split = partition(array, l, r)
            self.quick_sort(array, l, split-1)
            self.quick_sort(array, split+1, r)
        
        

if __name__ == "__main__":
    # Test Case
    array = [3,2,5,4,6,9,1]
    l = 0
    r = len(array)-1

    sort = Sort()
    sort.quick_sort(array, l, r)
    print(array)