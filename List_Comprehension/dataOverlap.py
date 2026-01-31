fwith open("List_Comprehension/file1.txt", "r") as f1:
    list1 = [int(num) for num in f1.readlines()]
    
with open("List_Comprehension/file2.txt", "r") as f2:
    list2 = [int(num) for num in f2.readlines()]

result = [num for num in list1 if num in list2]
print(result)
