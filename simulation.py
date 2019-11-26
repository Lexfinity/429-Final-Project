f=open("inputs.txt", "r")

if f.mode == 'r':
    contents = f.readlines()
    lines = [content.replace('\n', '') for content in contents]
    print(lines)

f.close()

f=open("mutants.txt", "r")

if f.mode == 'r':
    contents = f.readlines()
    mLines = [content.replace('\n', '') for content in contents]
    print(mLines)

f.close()

a = 1
b = 2

for l in lines:
    for m in mLines:
        expected = eval(l)
        actual = eval(m)
        if(len(l) == len(m)):
            if(expected != actual):
                print("mutant killed! \n""expression: %s" %l + "\t expected: %f\n" %expected + "expression: %s" %m + "\t actual: %f" %actual)