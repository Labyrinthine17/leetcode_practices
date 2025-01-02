class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        k = 0

        for idx, curr in enumerate(nums):
            if idx == 0:
                # move on if k == 0 (first element)
                counter = 1
            else:
                # second element onwards
                # if different from prev
                if curr!= nums[idx - 1]:
                    # reset counter
                    counter = 1
                    k += 1
                    nums[k] = curr
                else:
                    # if same as previous
                    # check if counter reached 2
                    if counter <2:
                        k += 1
                        nums[k] = curr
                        counter += 1
        # since k represents the number of elements not index, add 1
        k += 1
        return(k)