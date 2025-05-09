'''Task: You are given an array of integers nums and an integer
 target, return indices of the two numbers such that they add up to target.

 You may assume that each input would have exactly one solution,
  and you may not use the same element twice.

  You can return the answer in any order.'''

class TwoSumBruteForce:

    def __init__(self, nums: list[int], target: int):
        self.nums = nums
        self.target = target

    def twoSum(self) -> list[int]:
        num_map = []
        for i in range(len(self.nums)):
            for j in range(i+1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    num_map.append((i, j))
        return num_map


class TwoSumHashMap:
    def __init__(self, nums: list[int], target: int):
        self.nums = nums
        self.target = target
        self.num_map = {}  # Value -> Index

    def twoSum(self) -> list[int]:
        for i, num in enumerate(self.nums):
            complement = self.target - num
            if complement in self.num_map:
                return [i, self.num_map[complement]]
            self.num_map[num] = i

        return []





obj = TwoSumBruteForce([2, 3, 3, 4], 6)
result = obj.twoSum()
print(result)
