class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0,0,0]
        for i in nums:
            counts[i] += 1

        R,W,B = counts
        
        nums[:R] = [0] * R
        nums[R:R+W] = [1] * W
        nums[R+W:] = [2] * B
            
    