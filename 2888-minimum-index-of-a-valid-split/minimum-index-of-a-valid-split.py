class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap1 = {}
        hashmap2 = {}
        for i in nums:
            if i not in hashmap1:
                hashmap1[i] = 1
            else:
                hashmap1[i] += 1
        n = len(nums)
        freq = 0
        dom = 0
        size = 0
        for i in nums:
            if i not in hashmap2:
                hashmap2[i] = 1
            else:
                hashmap2[i] += 1
            size += 1
            if hashmap2[i] > freq:
                dom = i
                freq = hashmap2[i]
            if freq * 2 <= size:
                continue
            else:
                freq2 = hashmap1[dom] - hashmap2[dom]
                if freq2 * 2 > n - size:
                    return size - 1

        return -1

        