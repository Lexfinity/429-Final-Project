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
    if(len(l) == len(m)):
        if(expected != actual):
                print("mutant killed! \n""expression: %s" %l + "\t expected: %f\n" %expected + "expression: %s" %m + "\t actual: %f" %actual)



a = 1
b = 2

for l in lines:
    for m in range(len(mLines) - 3): 
        t = threading.Thread(target=threadingloop, args=(l, mLines[m], ))
        t2 = threading.Thread(target=threadingloop, args=(l, mLines[m + 1], ))
        t3 = threading.Thread(target=threadingloop, args=(l, mLines[m + 2] , ))
   
        t.start()
        t2.start()
        t3.start()


        