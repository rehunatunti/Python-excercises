rows = 9 
cols = 9
array=[[1]*cols,[1]*cols,[1]*cols,[1]*cols,[1]*cols,[1]*cols,[1]*cols,[1]*cols,[1]*cols]

print (f"{'| 0':3s} {'| 1':3s} {'| 2':3s} {'| 3':3s} {'| 4':3s} {'| 5':3s} {'| 6':3s} {'| 7':3s} {'| 8':3s} {'| 9':3s}")

i = 0
while i < rows:
	j = 0
	while j < cols:
		array[i][j] = (i + 1) * (j + 1)		
		j = j + 1
	i = i + 1

i = 0
while i < rows:
	print (f"{i+1:3d}", end=" ")
	j = 0
	while j < cols:
		if j == cols - 1:
			print (f"{array[i][j]:3d}")
		else:	
			print (f"{array[i][j]:3d}", end=" ")
		j = j + 1
	i = i + 1

print(array)
