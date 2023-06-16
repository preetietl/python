list=[1,2,3,3,3,4,5,'abc',3.6]  #creating list
total_list_count=list.count(3)               #taking count of an element
print(total_list_count)

last_4_item=list[-4:]                     #Using SLICING to get last 4 values from list
print(last_4_item)

list.append(8)   #to add any value at the end
print(list)

list.insert(6,"preeti") #to insert any value at specific position
print(list)

list.remove(3)
                 #it will remove the element assigned(value) first occurance from the list
print(list)

list.pop()            #remove the last element from the list
print(list)


list1=['ab','dc','abcf',35,98,'kjh',6.6,'yhg']  
#del list1[2]                              # to delete the item from specific position.
print(list1)

#Slicing-access a range of items in a list/tuples by using slicing operator  :

#del list1[2 :]          #slicing #to delete everything from position specified to the end
print(list1)

#del list1[:2]      #to delete everything from position specified from the begining
print(list1)


list1.reverse()   #to reverse the values in list
print(list1)

a=[5,61,2,3,4]
#a.clear()              #to delete everything from list
#del a[:]                #to delete everything from list
print(a)


a.sort()                    #to sort the content in ascending order/ applicable only on integer
print(a)
a.reverse()                 #to reverse the order
print(a)






