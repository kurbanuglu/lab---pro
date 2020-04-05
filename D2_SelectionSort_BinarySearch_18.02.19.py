
#Selection Sort ile diziyi küçükten büyüğe sıralama
#Binary Search ile arama


def MySelectionSort(my_array):
    swap_number=0

    for i in range(len(my_array)-1,0,-1):
        positionOfMax=0
        for location in range(1,i+1):

            if(my_array[location]>my_array[positionOfMax]):
                positionOfMax=location
        temp=my_array[location]
        my_array[location]=my_array[positionOfMax]
        my_array[positionOfMax]=temp
        swap_number=swap_number+1

    print("swap number: ",swap_number)
    return


my_arrays=[12,18,65,26,47,23,64,85,90,37]
MySelectionSort(my_arrays)
print(my_arrays)




def MyBinarySearch(MySortedArray,item):
    first=0
    last=len(MySortedArray)-1
    found=False
    s=0

    while first<=last and not found:
        midpoint=(first+last)//2
        print("First-Last : ",first,last)
        s=s+1
        if(MySortedArray[midpoint]==item):
            found=True
        else:
            if(item<MySortedArray[midpoint]):
                last=midpoint-1
            else:
                first=midpoint+1

    return  found,midpoint,s



my_arrays_2=[55,26,78,45,36,12,20]
print(MyBinarySearch(my_arrays_2,26))
