class QuickSort():

    def __init__(self, nums, l, r):
        self.nums = nums

    def partition(self, l, r):
        pivot = self.nums[r]
        split, j = l, l
        while j < r:
            if self.nums[j] <= pivot:
                self.nums[split], self.nums[j] = self.nums[j], self.nums[split]
                split += 1
            j += 1
        self.nums[split], self.nums[r] = self.nums[r], self.nums[split]
        return split

    def quick(self, l, r):
        if r > l:
            split = self.partition(l, r)
            self.quick(l, split-1)
            self.quick(split+1, r)

        return self.nums
                

if __name__ == "__main__":
    # Test Case
    nums = [3, 5, 4, 1, 2, 5, 6, 3, 4, 6]
    l, r = 0, len(nums)-1

    sort = QuickSort(nums, l, r)
    print(sort.quick(l, r))