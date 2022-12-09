def accept_array(data):
    n = int(input("Enter the total no. of student : "))
    for i in range(n):
         x = float(input("Enter the first year percentage of student %d : "%(i+1)))
         data.append(x)
    print("Array accepted successfully\n\n");

def display_array(data):
    n = len(data)
    if(n == 0):
        print("\nNo records in the database")
    else:
        print("Array of FE MArks : ",end= " ")
        for i in range(n):
            print("%.2f "%data[i], end = " ")
        print("\n");
        
def partition(array,low,high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if(array[j] <= pivot):
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return(i+1)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high) 
    
    

def Main():
    array = []
    n=len(array)
    while True :
        print("\t1 : Accept and Display FE Marks")
        print("\t2 : Quick Sort ascending order and display top scores")
        print("\t3 : Exit")
        ch = int(input("Enter your choice : "))
        if (ch == 3):
            print("End of program")
            quit()
        elif(ch == 1):
            accept_array(array)
            display_array(array)
        elif(ch == 2):
            print("Marks before sorting")
            display_array(array)
            size=len(array)
            quickSort(array,0,size-1)
            print("Marks after sorting")
            display_array(array)
            if(len(array) >= 5):
                print("Top five scores : ")
                for i in range(5):
                    print("\t%.2f"%array[i])
            else:
                print("Top scorers : ")
                for i in range(len(array)):
                    print("\t%.2f"%array[i])
        else:
            print("Wrong choice entered !! Try again")
            
            
Main() 