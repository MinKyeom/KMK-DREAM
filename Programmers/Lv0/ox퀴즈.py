#
#풀이1

#(아예 못품)

#풀이2

def solution(quiz):
    return ["O" if x else "X" for x in map(eval, map(lambda x: x.replace("=", "=="), quiz))]