class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        ans = []
        for i in range(len(nums) - 2):
            
            a = nums[i]
            if i>0 and nums[i]==nums[i-1]:
                pass
            else:
                s = i + 1
                e = len(nums) - 1

                while s < e:
                    if a + nums[s] + nums[e] == 0:
                        ans.append((a,nums[s],nums[e]))
                        s += 1
                        e -= 1
                        while s < len(nums) and nums[s] == nums[s-1]:
                            s += 1
                        while e > 0 and nums[e] == nums[e+1]:
                            e -= 1
                    elif a + nums[s] + nums[e] < 0:
                        s += 1

                    elif a + nums[s] + nums[e] > 0:
                        e -= 1
        return sorted(set(ans))