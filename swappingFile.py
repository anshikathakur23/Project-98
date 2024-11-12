def swapFileData (file1, file2):
    
    name = input ("Name of file")
    
    file1.write (data_a)
    file2.write (data_b)

    with open (file1, 'r') as a:
        data_a = a.read ()

    with open (file1, 'w') as a:
        a.write (data_b)


    print ("Data swapped")

swapFileData ()