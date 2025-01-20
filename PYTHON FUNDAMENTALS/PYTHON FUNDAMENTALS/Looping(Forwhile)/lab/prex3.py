List1=['apple','banana','mango']
search_fruit='banana'
found=False
for fruit in List1:
    if fruit==search_fruit:
        found=True
        print(f"{search_fruit} is found in the list")
        break
    
    if not found:
         print(f"{search_fruit} is not found in the list.")