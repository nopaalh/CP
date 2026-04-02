class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        panjangList = len(nums)
        hasil = []
        for indices , isi in enumerate(nums):
            selisih = target - isi
            for index , sasaran in enumerate(nums[indices + 1:]):
                if sasaran == selisih:
                    hasil.append(indices)
                    hasil.append(index + indices + 1)

        return hasil


        return hasil
        