n = int(input("Enter a No: "))
list = [0, 1]
i = 2
while(len(list)<n):                         # 1st time len(list) == 2 and in next increase
    list.append(list[i-2]+list[i-1])        # FOR 1st ITERATION (list[i-2] == list[0]) & (list[i-2] == list[0])
    i += 1
print(list)
"""multi-line String"""
