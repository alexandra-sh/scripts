from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        second_list = []
        new_list = []
        for x in range(len(nums) - 1):
            try:
                second_list.append(nums[x + n])
            except IndexError:
                break
        j=0
        for i in range(len(second_list)):
            new_list.insert(j, nums[i])
            new_list.insert(j+1, second_list[i])
            j = j+2

        return new_list


def main():
    solution = Solution()
    result = solution.shuffle([4,5,6,7,8,9,10,11,12,20,21], 4)
    print(result)


if __name__ == "__main__":
    main()




