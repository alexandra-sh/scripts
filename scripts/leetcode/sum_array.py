from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_arr=[]
        for i in range(len(nums)):
            if i==0:
                sum_arr.append(nums[i])
            else:
                addedn_1=nums[i]
                addedn_2=sum_arr[i-1]
                sum_arr.append(addedn_1+addedn_2)
        return sum_arr

def main():
    solution = Solution()
    result = solution.runningSum([4,5,6,7,8,8.8,-5])
    print(result)


if __name__ == "__main__":
    main()




