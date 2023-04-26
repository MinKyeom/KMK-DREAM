from itertools import combinations
a=[[1, 4], [9, 2], [3, 8], [11, 6]]

b=list(combinations(a,2))

print(b)

#[([1, 4], [9, 2]), ([1, 4], [3, 8]), ([1, 4], [11, 6]), ([9, 2], [3, 8]), ([9, 2], [11, 6]), ([3, 8], [11, 6])]
