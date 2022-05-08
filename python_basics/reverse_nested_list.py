input =  [[1, 2], [3, 4], [5, 6, 7]]

def reverse_nested_list(input):
    li = []
    for i in input:
        if isinstance(i,list):
            li.append(reverse_nested_list(i))
        else:
            li.append(i)
    li.reverse()
    return li
            
print(reverse_nested_list(input))

