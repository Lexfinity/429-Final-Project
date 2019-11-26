import threading

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



def threadingloop(l, m): 

    expected = eval(l)
    actual = eval(m)
    if(len(l) == len(m) and (l[0] == m[0])):
        if(expected != actual):
            print("mutant killed! \n""expression: %s" %l + "\t expected: %f\n" %expected + "expression: %s" %m + "\t actual: %f" %actual)



a = input("Enter value for a : " )
b = input("Enter value for b : " )

print("test vector < " + a + ", " + b +" > ")

a = int(a)
b = int(b) 

for l in (0, len(lines), 3):
    for m in range(len(mLines)): 
        t = threading.Thread(target=threadingloop, args=(lines[l], mLines[m], ))
        t2 = threading.Thread(target=threadingloop, args=(lines[l+1], mLines[m + 1], ))
        t3 = threading.Thread(target=threadingloop, args=(lines[l+2], mLines[m + 2] , ))
   
    
        t.start()
        t2.start()
        t3.start()


        