
# BiNARY SEARCH

def my_binary_search(my_sorted_array,item):
    first=0
    last=len(my_sorted_array)-1
    found=False
    s=0
    while first<=last and not found:
        midpoint=(first+last)//2
        print(" First-last : ",first,last)
        s=s+1
        if(my_sorted_array[midpoint]==item):
            found = True
        else:
            if(item<my_sorted_array[midpoint]):
                last=midpoint-1
            else:
                first=midpoint+1
    return found,midpoint,s



my_arr=[45,68,12,58,89,32,26]
print(my_binary_search(my_arr,58))
