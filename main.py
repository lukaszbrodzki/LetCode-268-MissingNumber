class Solution:
    def missingNumber(self, nums: [int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

    def missingNumber2(self, nums: [int]) -> int:
        '''
        VERY SLOW SOLUTION
        '''
        tot = list(range(len(nums) + 1))
        for i in nums:
            tot.remove(i)
        return tot[0]

    def missingNumber3(self, nums: [int]) -> int:
        total_sum = (len(nums) + 1) * (len(nums)) / 2
        array_sum = sum(nums)
        return int(total_sum - array_sum)

    def missingNumbe4r(self, nums: [int]) -> int:
        return int(((len(nums) + 1) * (len(nums)) / 2) - (sum(nums)))


if __name__ == '__main__':
    s = Solution()
    nums = [3,0,1]
    print(s.missingNumber3(nums))
