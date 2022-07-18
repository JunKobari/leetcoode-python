from __future__ import annotations


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums)-1
        while start <= end:
            pos = (start+end)//2
            if nums[pos] > target:
                end = pos
            elif nums[pos] < target:
                start = pos
            elif target == nums[pos]:
                return pos
            else:
                return -1


if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    nums = [5]
    target = 5
    print(sol.search(nums, target))
