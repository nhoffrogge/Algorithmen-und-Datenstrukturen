def large_cont_sum(arr):
    
    if len(arr) == 0:
        return 0
    
    max_sum = currnet_sum = arr[0]
    
    for num in arr[1:]:
        
        currnet_sum = max(current_sum + num, num)

large_cont_sum([1,2-1,3,4,10,10,-10,-1])