e=int(input())
if e>1:
	for p in range(2,e):
		if(e%p==0):
			print("no")
			break
	else:
		    print("yes")
else:
	        print("no")
