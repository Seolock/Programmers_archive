def solution(nums):
    
    arr = []
    for i in nums:
        if not i in arr:
            arr.append(i)
            
    answer = len(arr) if len(arr)<len(nums)//2 else len(nums)//2
    
    return answer