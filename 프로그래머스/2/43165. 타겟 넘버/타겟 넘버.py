def solution(numbers, target):
    
    answer = 0
    tree = [0,0]
    level = 1
    
    for i in numbers:
        for j in range(level):
            tree.append(tree[len(tree)//2]+i)
            tree.append(tree[len(tree)//2]-i)
        level = level * 2
    
    for i in range(len(tree)//2,len(tree)):
        if tree[i] == target:
            answer += 1
    
    return answer