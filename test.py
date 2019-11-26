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

mutantindex = len(mLines)
currCount = 0
index = len(lines)
tracker = 0
charMult = 0
charDiv = 0
charAdd = 0
charSub = 0

for line in lines:
    actual = eval(line)
    if (line.find('*') != -1):
        charMult=charMult+1
    if(line.find('+') != -1):
        charAdd=charAdd+1
    if(line.find('-') != -1):
        charSub=charSub+1
    if(line.find('/') != -1):
        charDiv=charDiv+1
    currCount = 3 * (charDiv + charMult + charSub + charAdd)
    
    
    for i in range((tracker + currCount)):
        expected = eval(mLines[i])
        if(expected != actual and (line[0] == mLines[i][0]) ):
            print("mutant killed! \n""expression: %s" %line + "\t expected: %f\n" %actual + "expression: %s" %mLines[i] + "\t actual: %f" %expected)
    
    tracker += currCount


# for l in lines:
#     for m in mLines:
#         expected = eval(l)
#         actual = eval(m)
#         if(len(l) == len(m)):
#             if(expected != actual):
#                 print("mutant killed! \n""expression: %s" %l + "\t expected: %f\n" %expected + "expression: %s" %m + "\t actual: %f" %actual)