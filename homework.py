#1.Create a list with fruits name 
#```["apple","banana","mango","grapes","guava"]
#-print the listitem with serial number
#-ex. o/p-1.apple
#-2.banana
# print the list item



#2.Replace the mango item with orange in list
#3.Input new fruit name from user and insert that item after grapes.
#4.print king of fruit mango is present in the list if mango is present else king not present.
#-----------------------------------------------------
list=['apple','banana','mango','grapes','guava']
print(list)

#--------------------------------------------------------
list[2]='banana'
list[1]='mango'
print(list)
#-----------------------------------------------------
list1=input("enter a fruit name")
print('added fruit name is',list1)
list.append(list1)
print(list)

#--------------------------------------------------------------- 
if 'mango' in list:
 print("king of fruit mango is present in the list")
else: 
 print("king of fruit mango is not present in the list")


 #question-5 take 3 number from user and find maximum number

 #do now---------done    

first_number=input("enter first number")
second_number=input("enter 2nd number")
third_number=input("enter 3rd number")
numberList=[first_number,second_number,third_number]
maximum_number=max(numberList)

print(maximum_number)

  

