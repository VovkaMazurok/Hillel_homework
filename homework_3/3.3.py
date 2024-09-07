import  math

lst = [1, 2, 3, 4, 5, 6] # [[1, 2, 3], [4, 5, 6]]
#lst = [1, 2, 3] # [[1, 2], [3]]
#lst = [1, 2, 3, 4, 5] # [[1, 2, 3], [4, 5]]
#lst = [1] # [[1], []]
#lst = [] # [[], []]

if len(lst)==0:
    print([[],[]])
else:
    half_lst = math.ceil(len(lst)/2)
    print([lst[:half_lst],lst[half_lst:]])
