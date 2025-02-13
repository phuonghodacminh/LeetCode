class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        if nums[0] >= k:
            return 0
        else:
            if len(nums) == 2:
                return 1
            else:
                new = [nums[0] * 2 + nums[1]]
                count = 1
                newIndex = 0
                numsIndex = 2
                while (numsIndex < n and nums[numsIndex] < k) or (newIndex < len(new) and new[newIndex] < k):
                    if numsIndex < n and (newIndex >= len(new) or nums[numsIndex] < new[newIndex]):
                        min1 = nums[numsIndex]
                        numsIndex += 1
                    else:
                        min1 = new[newIndex]
                        newIndex += 1
                    
                    if numsIndex < n and (newIndex >= len(new) or nums[numsIndex] < new[newIndex]):
                        min2 = nums[numsIndex]
                        numsIndex += 1
                    else:
                        min2 = new[newIndex]
                        newIndex += 1
                    
                    new.append(min1 * 2 + min2)
                    count += 1
                
                return count
                                        


        

        
        
        