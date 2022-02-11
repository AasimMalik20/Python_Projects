def move_zeros_to_left(A):
    if len(A) < 1:
        return
    
    #declaring variables
    LengthA = len(A)
    write_ind = LengthA - 1
    read_ind = LengthA - 1

    #shiftng if readindex isnt equal to 0
    while(read_ind >= 0):
        if A[read_ind]!= 0:
            A[write_ind] = A[read_ind]
            write_ind -= 1
        read_ind -=1
    #if readindex is 0 then skip
    while(write_ind >= 0):
        A[write_ind]=0
        write_ind -=1
        
S = [1,2,0,5,0,4,8,0,6]
print("Original array is:", S )

move_zeros_to_left(S)
print("New array is:", S)