#lst=[1, 3, 5] #=> 30
lst=[6] #=> 36
#lst=[] #=> 0

new_lst=[]
i=0
if not lst:
    print(0)
else:
    while i < len(lst):
        new_lst.append(lst[i])
        i+=2
    print(sum(new_lst)*lst[-1])
