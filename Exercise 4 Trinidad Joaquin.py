file_text = open("DNA.txt").read()

print"The file has ",len(file_text)," characters"

n=0
for char in file_text:
    if char=='C' or char=='G':
        n= n + 1
        x=(n/18.0)*100
print "The percentage of C and G characters is ",x," in the text."
