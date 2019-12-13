class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        
        nums3 = []
        if len1 == 0:
            nums3 = nums2
        elif len2 == 0:
            nums3 = nums1
        elif nums1[-1] < nums2[0]:
            nums3 = nums1 + nums2
        elif nums2[-1] < nums1[0]:
            nums3 = nums2+nums1
        else:
            l1 = 0
            l2 = 0
            while (l1<len1) and (l2<len2):
                if nums1[l1] < nums2[l2]:
                    nums3.append(nums1[l1])
                    l1 += 1
                else:
                    nums3.append(nums2[l2])
                    l2 += 1
            if l1 == len1:
                nums3.extend(nums2[l2:])
            else:
                nums3.extend(nums1[l1:])
            
        len3 = len1 + len2
        if len3%2 != 0:
            return nums3[len3//2]
        else:
            return (nums3[len3//2-1] + nums3[len3//2])/2