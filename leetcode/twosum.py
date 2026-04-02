class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        kamus = {}

        for indeks, isi in enumerate(nums):
            selisih = target - isi
            if selisih in kamus:
                return [kamus[selisih],indeks]
            kamus[isi] = indeks