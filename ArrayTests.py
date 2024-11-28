from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
print("Remove the first occurrence of 3 from the said array:")
array_num.remove(3)
print("New array: "+str(array_num))

#Compiled Code:

#PS C:\Users\oakto\.vscode\extensions> & C:/Users/oakto/OneDrive/Documents/PyGuy/python.exe c:/Users/oakto/OneDrive/Documents/PyGuy/ArrayTests.py
#Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
#Remove the first occurrence of 3 from the said array:
#New array: array('i', [1, 5, 3, 7, 1, 9, 3])
#PS C:\Users\oakto\.vscode\extensions> 
