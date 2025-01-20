from functools import reduce
def  re():
    numbers=[1,2,3,4,5]
    product = reduce(lambda x,y:x*y,numbers)
    print("product of the list:",product)
re()
