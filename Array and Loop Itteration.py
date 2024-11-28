numbers = [[1, 2, 3], [4, 5, 6]]

cnt = 0
for i in numbers:
    for j in i:
        print('iteration', cnt, end=': ')
        print(j)
        cnt = cnt + 1


# will provide the following output, note the block comment not actual data from the algorithim above:

'''
#PS C:\Users\oakto\.vscode\extensions> & C:/Users/oakto/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/oakto/OneDrive/Documents/PyGuy/Array and Loop Itteration.py"
iteration 0: 1
iteration 1: 2
iteration 2: 3
iteration 3: 4
iteration 4: 5
iteration 5: 6
'''
