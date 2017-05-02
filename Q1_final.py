T = int(input("Please enter Test Case Number: "))
Eligible=[]
for i in range(T):
	print("Test Case ",i+1)
	N,P = input("Please enter Candidate Number and Threshold Value(separated by space): ").split()
	N=int(N)
	P=int(P)
	E=0
	for j in range(N):
		S= int(input("Please enter Score Value: "))
		if S>=P:
			E += 1
	Eligible.append(E)
print("\n")
for i in range(T):
	print("Number of eligible astronouts for Test Case {} is {}".format(i+1,Eligible[i]))
