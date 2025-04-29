class Solution(object):
        def countSubarrays(self, nums, k):
            maxnum = max(nums)
            ans = 0
            n = len(nums)

            maxind = [-1]
            for i in range(n):
                if nums[i] == maxnum:
                    maxind.append(i)

            indsize = len(maxind)

            for i in range(1, indsize - k + 1):
                l = maxind[i] - maxind[i - 1] - 1
                r = n - 1 - maxind[i + k - 1]
                ans += (l + 1) * (r + 1)

            return ans
        