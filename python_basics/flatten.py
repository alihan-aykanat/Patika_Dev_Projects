input = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def deco_list(func):
    def inner(*args, **kwargs):
        return list(func(*args, **kwargs))    
    return inner    
            
@deco_list
def flatten(list):
    
    for i in list:
        if hasattr(i, "__iter__") and not isinstance(i, (str,bytes)):
            yield from flatten(i)
        else:
            yield i
    

print(flatten(input))


