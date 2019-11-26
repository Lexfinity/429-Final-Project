f=open("inputs.txt", "r")

if f.mode == 'r':
    contents = f.readlines()
    lines = [content.replace('\n', '') for content in contents]
    # print(lines)

f.close()

f=open("mutants.txt", "r")

if f.mode == 'r':
    contents = f.readlines()
    mLines = [content.replace('\n', '') for content in contents]
    # print(mLines)

f.close()

a = input("Enter value for a : " )
b = input("Enter value for b : " )

print("test vector < " + a + ", " + b +" > ")

a = int(a)
b = int(b) 

results = open('results.txt', 'w')
for l in lines:
    for m in mLines:
        expected = eval(l)
        actual = eval(m)
        if(len(l) == len(m) and (l[0] == m[0])):
            if(expected != actual):
                results.write("mutant killed! \n""expression: %s" %l + "\t expected: %f\n" %expected + "expression: %s" %m + "\t actual: %f" %actual +"\n")
                print("mutant killed! \n""expression: %s" %l + "\t expected: %f\n" %expected + "expression: %s" %m + "\t actual: %f" %actual)
results.close()