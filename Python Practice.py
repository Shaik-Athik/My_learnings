# You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

# A triangle is called equilateral if it has all sides of equal length.
# A triangle is called isosceles if it has exactly two sides of equal length.
# A triangle is called scalene if all its sides are of different lengths.
# Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

class solution:
def triangleType(self, nums: list[int])-> str:
    nums.sort()
    if nums[0]+nums[1]<=nums[2]:
        return "none"
    s=set(nums)
    if len(s)==1:
        return "equilateral"
    elif len(s)==2:
        return "isosceles"
    elif len(s)==3:
        return "scalene"
    else:
        return "none"

nums=list(map(int,input().split()))
obj = solution()
result = obj.triangleType(nums)
print(result)