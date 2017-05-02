T = int(input("Please enter Test Case Number: "))
Eligible=[]

for i in range(T):
	print("Test Case ",i+1)
	#N = int(input("Please enter Candidate Number: "))
	#P = int(input("Please enter Threshold Value: "))
	N,P = input("Please enter Candidate Number and Threshold Value(separated by space): ").split()
	N=int(N)
	P=int(P)

	#Score=[]
	E=0
	for j in range(N):
		S= int(input("Please enter Score Value: "))
		if S>=P:
			E += 1
		#Score.append(S)
	#print(Score)
	#print(E)
	Eligible.append(E)
	
#print("\nList of eligible astronouts for each test case:")
#print(Eligible)
print("\n")
for i in range(T):
	print("Number of eligible astronouts for Test Case {} is {}".format(i+1,Eligible[i]))
	#print(Eligible[i])


