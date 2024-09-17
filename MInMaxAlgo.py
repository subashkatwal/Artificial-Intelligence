
print("Subash Katwal \n")
def minimax(depth, node_index, maximizing_player, scores, height, path=[]):
    if depth == height:
        print(f"Path: {' -> '.join(map(str, path))} with Score: {scores[node_index]}")
        return scores[node_index]
    
    if maximizing_player:
        left = minimax(depth + 1, node_index * 2, False, scores, height, path + [node_index * 2])
        right = minimax(depth + 1, node_index * 2 + 1, False, scores, height, path + [node_index * 2 + 1])
        return max(left, right)
    else:
        left = minimax(depth + 1, node_index * 2, True, scores, height, path + [node_index * 2])
        right = minimax(depth + 1, node_index * 2 + 1, True, scores, height, path + [node_index * 2 + 1])
        return min(left, right)

# Example usage
scores = [3, 5, 2, 9, 12, 5, 23, 23]
height = 3
print("The optimal value is:", minimax(0, 0, True, scores, height))
