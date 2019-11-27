import time

start_time = time.time()

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
count = 0
results = open('results.txt', 'w')

print("test vector < " + a + ", " + b +" > ")
results.write("test vector < " + a + ", " + b +" > \n")

a = int(a)
b = int(b) 


for l in lines:
    for m in mLines:
        expected = eval(l)
        actual = eval(m)
        if(len(l) == len(m) and (l[0] == m[0])):
            if(expected != actual):
                count += 1
                results.write("mutant killed! \n""expression: %s" %l + "\t expected: %f\n" %expected + "expression: %s" %m + "\t actual: %f" %actual +"\n")
                print("mutant killed! \n""expression: %s" %l + "\t expected: %f\n" %expected + "expression: %s" %m + "\t actual: %f" %actual)
denom = len(mLines)
percent = count/ len(mLines)
results.write("Percentage of mutants killed: %d " %count + "/ %d " %len(mLines) +  "= %f"  %percent + "\n")
print("Percentage of mutants killed: %d " %count + "/ %d " %len(mLines) +  "= %f"  %percent)
results.write("--- %s seconds ---" % (time.time() - start_time))
results.close()