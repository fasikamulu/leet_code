class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        arr_p =[]
        arr_s = []
        summ=0
        summ_r =0
        if len(nums)==1:
            return 0
        for i in range(len(nums)):
            arr_p.append(nums[i]+summ)
            summ+=nums[i]
            arr_s.append(nums[len(nums)-i-1]+summ_r)
            summ_r+=nums[len(nums)-i-1]
        arr_s=arr_s[::-1]
        for j in range(len(nums)):
            if j ==0:
                if arr_s[j+1]==0:
                    return j
                else:
                    continue
            if j ==len(nums)-1:
                if arr_p[j-1]==0:
                    return j
                else:
                    continue
            if arr_p[j-1]==arr_s[j+1]:
                return j
            

        return -1
        
        