def pair_sum(arr: list, ref: int) -> list:
    
    if len(arr) < 2:
        return
    
    seen = set()
    output = set()

    for num in arr:
        target = ref-num
        
        if target not in seen:
            seen.add(num)
            
        else:
            output.add((min(num,target),(max(num,target))))
            
    return len(output)
        

pair_sum([1,3,2,2], 4)   
