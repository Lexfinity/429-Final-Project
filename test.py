infile= open("inputs.txt","r")
readL = infile.readlines()
lines = [line.replace('\n', '') for line in readL]
infile.close()
count = 0
charIndex = 0
print("Each arithmetic operator can have 3 other possible operators as mutants")
print("+, -, *, /")
print()

for line in lines:
    print(line)
    print("Line %d under test:" % count)
    
    if '+' in line:
        print("Line %d has '+' operator" % count)
        newline = line.replace('+', '-', 1)
        lines[count] = newline
        print("Injecting '-' operator as a mutant")
        
        
    if '-' in line:
        print("Line %d has '-' operator" % count)
        newline = line.replace('-', '+', 1)
        lines[count] = newline
        print("Injecting '+' operator as a mutant")

    if '*' in line:
        print("Line %d has '*' operator" % count)
        newline = line.replace('*', '/', 1)
        lines[count] = newline
        print("Injecting '/' operator as a mutant")
    
    if '/' in line:
        print("Line %d has '/' operator" % count)
        newline = line.replace('/', '*', 1)
        lines[count] = newline
        print("Injecting '*' operator as a mutant")

    count += 1
    print()

#print(lines)

outfile= open("output.txt","w")
for line in lines:
    outfile.write(line)
    outfile.write('\n')
outfile.close()

