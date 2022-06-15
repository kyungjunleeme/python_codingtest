#첫번째방법
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif not target in nums:
            test_list = []
            if nums[-1] < target:
                nums.append(target)
                return nums.index(target)
            else:
                for num in nums:
                    if num < target:
                        test_list.append(num)
                    elif num > target:
                        if not target in test_list:
                            test_list.append(target)
                return test_list.index(target)


#두번째 방법
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            # target 보다 작은 리스트로 구성되어 있으니, 
            # 그 리스트의 길이를 구하면 그게 곧 target이 삽입 될 경우의 index
            return len([i for i in nums if i < target])
