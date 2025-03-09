def minmax(depth, node, is_max, scores, height):
    if depth == height:
        return scores[node]
    
    if is_max:
        return max(minmax(depth + 1, node * 2, False, scores, height),
                   minmax(depth + 1, node * 2 + 1, False, scores, height))
    else:
        return min(minmax(depth + 1, node * 2, True, scores, height),
                   minmax(depth + 1, node * 2 + 1, True, scores, height))


scores = [3, 5, 2, 9, 12, 5, 23, 23]  
height = 3 
optimal_value = minmax(0, 0, True, scores, height)
print("The optimal value is:", optimal_value)
