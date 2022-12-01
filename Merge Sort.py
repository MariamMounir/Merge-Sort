def Merge_Sort(arr):
    if len(arr)>1:
        left_arr=arr[:len(arr)//2]
        right_arr=arr[len(arr)//2:]

        #recursion
        Merge_Sort(left_arr)
        Merge_Sort(right_arr)

        #merge
        i=0 #lift arr idx
        j=0 #right arr idx
        k=0 #merged arr idx

        while i<len(left_arr) and j<len(right_arr):

            if left_arr[i]<right_arr[j]:

                arr[k]=left_arr[i]
                i +=1
            else:
                arr[k]=right_arr[j]
                j+=1

            k+=1

            #عشان ف حجات هتبقي باقيه لسه ف واحد منهم        
        while i<len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1
        return arr    


rar=[]
n=int(input("Enter the number of element: "))
for i in range (0,n):
    element=int(input("Enter the element: "))
    rar.append(element)
    
print(Merge_Sort(rar))

