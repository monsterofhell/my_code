def print_it(input_mat):
	count1 = 0
	print("_____________________")
	for i in input_mat:
		count = 0 
		for j in i:
			print(j,end=" ")
			count += 1
			if(count==3):
				print("|",end="")
				count = 0
			
		print()
		count1 += 1
		if(count1 == 3):
			print("---------------------")
			count1 = 0

def sudoku(input_mat):
	done = False
	print_it(input_mat)
	while(not done):
		num4 = 0
		for i in range(0,9):
			for j in range(0,9):

				l1 =[]
				for t in range(0,9):
					if(input_mat[i][t] != 0):
						l1.append(input_mat[i][t])


				l3 =[]
				for t1 in range(0,9):
					if(input_mat[t1][j] != 0):
						l3.append(input_mat[t1][j])

				l2 = []
				new_base = i - i%3
				new_tread = j - j%3
				for s in range(new_base,new_base+3):
					for r in range(new_tread,new_tread+3):
						if(input_mat[s][r] != 0):
							l2.append(input_mat[s][r])
			
				ite = []
				for num1 in range(1,10):
					if((num1 not in l1) and (num1 not in l3) and (num1 not in l2)):
						ite.append(num1)
				
				
				if(input_mat[i][j] == 0 ):
					if(len(ite) == 1):
						input_mat[i][j] = ite[0]
				

				if(input_mat[i][j] != 0):
					num4 += 1

		if(num4 == 81):
			done = True
			print_it(input_mat)

	
sample = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
sudoku(sample)
