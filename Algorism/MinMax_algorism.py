"""
예시
function alphabeta(node, depth, α, β, maximizingPlayer)
      if depth = 0 or node is a terminal node
          return the heuristic value of node
      if maximizingPlayer
          v := -∞
          for each child of node
              v := max(v, alphabeta(child, depth - 1, α, β, FALSE))
              α := max(α, v)
          return v
      else
          v := ∞
          for each child of node
              v := min(v, alphabeta(child, depth - 1, α, β, TRUE))
              β := min(β, v)
          return v
"""