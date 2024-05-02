from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}

        for i, num in enumerate(nums):
            if target - num in pair:
                return [pair[target - num], i]
            pair[num] = i


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Test Case 1:")
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {solution.twoSum(nums1, target1)}")  # Expected output: [0, 1]

    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print("\nTest Case 2:")
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {solution.twoSum(nums2, target2)}")  # Expected output: [1, 2]

    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print("\nTest Case 3:")
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {solution.twoSum(nums3, target3)}")  # Expected output: [0, 1]
