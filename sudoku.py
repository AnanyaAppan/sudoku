import random

def genSudoku():
	l=[]
	for i in range(9):
		l.append([])
		for j in range(9):
			l[i].append(0)

	for i in range(9):
		listOfNos=[1,2,3,4,5,6,7,8,9]
		j = 0
		count = 0
		while j!= 9:
				num=random.choice(listOfNos)
				if((num not in GenCheckListSquare(l)[GetSqNum(i,j)]) and  (num not in GenCheckListCol(l)[j])):
					l[i][j]=num
					listOfNos.remove(num)
					j += 1
				else:
					count += 1
				if count>100:
					return genSudoku()
	l1=[]
	
	#creating incomplete sudoku based on complete sudoku
	for i in range(9):
		l1.append([])
		for j in range(9):
			l1[i].append(0)
	
	for i in range(9):
		listOfIndices=[1,2,3,4,5,6,7,8,0]
		for j in range(2):
			num=random.choice(listOfIndices)
			l1[i][num]=l[i][num]
			listOfIndices.remove(num)
	
	return (l,l1)

def GetSqNum(i,j):
	'''
	returns the number of the square in the sudoku depending on the row and column
	'''
	if(i<3 and j<3):
		return 0		
	elif(i<3 and j<6):
		return 1
	elif(i<3 and j<9):
		return 2		
	elif(i<6 and j<3):
		return 3
	elif(i<6 and j<6):
		return 4
	elif(i<6 and j<9):
		return 5
	elif(i<9 and j<3):
		return 6
	elif(i<9 and j<6):
		return 7
	else:
		return 8


def GenCheckListSquare(sudoku):
	'''
	this generates a list of numbers which are already present in the squares of the sudoku
	'''
	lSquare=[]
	for i in range(9):
		lSquare.append([])
	for i in range(9):
		for j in range(9):
			lSquare[GetSqNum(i,j)].append(sudoku[i][j])
	#print lSquare
	return lSquare


def GenCheckListRow(sudoku):
	'''
	this generates a list of numbers which are already present in the rows of the sudoku
	'''
	lRow=[]	
	for i in range(9):
		lRow.append(sudoku[i])
	return lRow

def GenCheckListCol(sudoku):
	'''
	this generates a list of numbers which are already present in the columns of the sudoku
	'''
	lCol=[]	
	for i in range(9):
		lCol.append([])	
	for i in range(9):
		for j in range(9):
			lCol[j].append(sudoku[i][j])
	return lCol

def check(num,sudoku,x,y):
	l1 = GenCheckListRow(sudoku)
	l2 = GenCheckListCol(sudoku)
	l3 = GenCheckListSquare(sudoku)
	return not ((num in l1[x]) or (num in l2[y]) or (num in l3[GetSqNum(x,y)]))  
		
def playGame():
	print 'generating sudoku....'
	completeSudoku,hiddenSudoku=genSudoku()
	print 'done!'
	print("hi!! let's play sudoku!!")
	while(True):
		
		for i in range(9):
			if i%3 == 0:
				print '-'*27
			for j in range(9):
				if j%3 == 0:
					print '|'+str(hiddenSudoku[i][j]),
				else:
					print ' '+str(hiddenSudoku[i][j]),
			print
		x=input('enter first index:')
		y=input('enter second index:')
		num=input('enter number:')
		if(check(num,hiddenSudoku,x,y)):
			hiddenSudoku[x][y]=num
			print('sudoku got updated!')
			if(hiddenSudoku==completeSudoku):
				print('You Won!!')
				choice=input('enter option \n 1.New Game \n 2.exit \n')
				if(choice==1):
					playGame()
				elif(choice==2):
					print 'Thank you for playing!!'
					return
		else:
			print('wrong input :(')
			num=input('press 0 if u wanna quit and any other number to continue:')
			if(num==0):
				print 'Thank you for playing!!'
				return

playGame()

		
		
		

