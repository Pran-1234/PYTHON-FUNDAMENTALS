def sq():
    numbers=[1,2,3,4,5]
    square_numbers=map(lambda x: x**2,numbers)
    square_numbers_list = list(square_numbers)
    print(square_numbers_list)
sq()