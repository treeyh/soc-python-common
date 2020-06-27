


class Solution:
    def twoSum(self, nums, target):

        tmpMap = {}
        index = 0
        for i in nums:
            if i not in tmpMap.keys():
                tmpMap[i] = []
            tmpMap[i].append(index)
            index += 1

        for i in nums:
            diff = target - i
            if diff == i and len(tmpMap[i]) > 1:
                return [tmpMap[i][0], tmpMap[diff][1]]
            if diff != i and diff in tmpMap.keys():
                return [tmpMap[i][0], tmpMap[diff][0]]
        return []

if __name__ == '__main__':
    s = Solution()
    val = s.twoSum([-1,-2,-3,-4,-5], -8)
    print(val)
