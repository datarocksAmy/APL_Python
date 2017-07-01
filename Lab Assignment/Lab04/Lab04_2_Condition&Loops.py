'''
  * Python Programming for Data Scientists and Engineers
  * LAB #4-2 Conditional Statement + Loops.
  * #11 Chia-Hui Amy Lin
'''

# 4-2-a Find Max and Min value in a Set
numberSet = set([2, 4, 6, 8, 10, 12, 14, 16])

print("< 4-2-a Max + Min Values of a Set >")
print("- Number Set :", numberSet)
print("Max :", max(numberSet))
print("Min :", min(numberSet))
print("--------------------------------------------------------")

# 4-2-b Create a symmetric difference
CS = set(["coffee", "code", "programming", "book", "glasses"])
FIN = set(["coffee", "Bloomberg", "Morningstar", "book", "glasses"])

print("< 4-2-b Symmetric Difference of CS & FIN >")
print("- CS  Set :", CS)
print("- FIN Set :", FIN, "\n")
print("--> Symmetric Difference:", CS ^ FIN)
