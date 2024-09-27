def add_one(some_list):
    st = "".join([str(numb) for numb in some_list])
    numb = int(st)
    result = str(numb + 1)
    new_lst = [int(char) for char in result]
    return new_lst

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
