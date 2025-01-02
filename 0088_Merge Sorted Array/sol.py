class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # result array index
        r = m+n-1

        m -= 1
        n -= 1

        while n >= 0:
            #print("Trying to insert at idx",r)
            #print("checking idx",m, "value(nums1):",nums1[m],"against(nums2):",nums2[n])
            if nums1[m] > nums2[n] and m >= 0:
                #print("Number from nums1 goes in")
                nums1[r] = nums1[m]
                m -= 1
            else:
                #print("Number from nums2 goes in")
                nums1[r] = nums2[n]
                n -= 1
            r -= 1
            #print("After inserting",nums1,"\n")
        #print(nums1)