class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = [1] * len(nums)
        p=1
        for i in range(0,len(nums)):
            op[i]=p
            p*=nums[i]
        p=1
        for i in range(len(nums)-1,-1,-1):
            
            op[i]*=p
            p*=nums[i]
        return op