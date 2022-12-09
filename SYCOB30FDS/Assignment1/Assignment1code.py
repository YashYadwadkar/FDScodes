def accept_set(list_name,set_name): 
   n = int(input(f"Enter the total no. of student who play {set_name}: "))
   for i in range(n):
      z = input(f"Enter the name of student {i+1} who play {set_name}: ")
      list_name.append(z)

def display_set(list_name,set_name):
    print(f"{set_name}:{list_name}")
    
def search_set(second_set,element_of_set1) :
    n = len(second_set)
    for i in range(n):
       if(second_set[i] == element_of_set1) :
          return (1)
    return (0)

def find_intersection_set(set1,set2,store_intersection_set):
   for i in range(len(set1)): 
      flag = search_set(set2,set1[i]);
      if(flag == 1) :
          store_intersection_set.append(set1[i])

def find_difference_set(set1,set2,store_difference_set):
    for i in range(len(set1)): 
      flag = search_set(set2,set1[i]);
      if(flag == 0) :
          store_difference_set.append(set1[i])    

def find_union_set(set1,set2,store_union_set):
   for i in range(len(set1)):
      store_union_set.append(set1[i])
   for i in range(len(set2)): 
      flag = search_set(set1,set2[i]);
      if(flag == 0) :
          store_union_set.append(set2[i])    
       
def Main() :
   Group_A = []
   Group_B = []
   Group_C = []
   
   while True :
       print ("1 : Accept the Information")
       print ("2 : List of students who play both cricket and badminton")
       print ("3 : List of students who play either cricket or badminton but not both")
       print ("4 : Number of students who play neither cricket nor badminton")
       print ("5 : Number of students who play cricket and football but not badminton")
       print ("6 : Exit")
       choice = int(input("Enter your choice : "))
       common = []       
       if (choice==6):
           print ("End of Program")
           break
       elif (choice==1):
           accept_set(Group_A,"Cricket")
           accept_set(Group_B,"Badminton")
           accept_set(Group_C,"Football")
           display_set(Group_A,"Cricket")
           display_set(Group_B,"Badminton")
           display_set(Group_C,"Football")           
       elif (choice==2):
           display_set(Group_A,"Cricket")
           display_set(Group_B,"Badminton")
           find_intersection_set(Group_A,Group_B,common)
           display_set(common,"both Cricket and Badminton")
       elif (choice==3):
           display_set(Group_A,"Cricket")
           display_set(Group_B,"Badminton")
           union = []
           find_union_set(Group_A,Group_B,union)
           intersection = []
           find_intersection_set(Group_A,Group_B,intersection)
           difference = []
           find_difference_set(union,intersection,difference)
           display_set(difference," either cricket or badminton but not both")
       elif (choice==4):
           display_set(Group_A,"Cricket")
           display_set(Group_B,"Badminton")
           display_set(Group_C,"Football")
           union=[]
           find_union_set(Group_A,Group_B,union)
           Group_D=[]
           find_difference_set(Group_C,union,Group_D)
           display_set(Group_D," neither cricket nor badminton")
           print(f"Number of students who play neither cricket nor badminton = {len(Group_D)}")
       elif (choice==5):
           display_set(Group_A,"Cricket")
           display_set(Group_C,"Football")
           display_set(Group_B,"Badminton")
           intersection = []
           find_intersection_set(Group_A,Group_C,intersection)
           difference=[]
           find_difference_set(intersection,Group_B,difference)           
           display_set(difference,"cricket and football but not badminton")
           print(f"Number of students who play cricket and football but not badminton = {len(difference)}")                 
       else :
           print ("Enter appropriate choice!")

Main()