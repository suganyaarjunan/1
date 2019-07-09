r=int(input())
if r>1:
	for s in range(2,r):
		if(r%s==0):
			print("no")
			break
	else:
		    print("yes")
else:
	        print("no")
