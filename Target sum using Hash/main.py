class Solution(object):
    def twoSum(self, nums, target):

        numbers={}
            
        for i ,num in enumerate(nums):    

            if target - num in numbers:
                return (numbers[target-num],i)
            else:
                numbers[num]= i

        return (-1,-1)            




        
        

        