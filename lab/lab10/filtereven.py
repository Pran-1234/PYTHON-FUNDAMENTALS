def filters():
    numbers=[1,2,3,4,5,6,7,8,9,10,11,12]
    evenno = filter(lambda x: x%2 ==0,numbers)
    evenno_list = list(evenno)
    print("Even numbers:",evenno_list)
filters()