DNA = {'A':'T','G':'C','T':'A','C':'G'}
seq= input("ENTER THE SEQUENCE:")
complementaryStrand=('')
for i in seq:
	complementaryStrand+=DNA[i]
reverseComplement=complementaryStrand[::-1]
print(reverseComplement)
