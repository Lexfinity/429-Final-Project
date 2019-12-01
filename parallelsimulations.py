import threading
import time
import os
import sys

start_time = time.time()
try:
    # check args
    start_time = time.time()
    if len(sys.argv) != 4:
        print("Invalid arguments: Please put SUT as first argument")
    
    aliveMutants = []
    killedMutants = []
    
    # redirect stdout to file
    sys.stdout = open('parallel-mutant-generated-output.txt', 'w')

    # store all filenames of mutants folder in files list
    files = os.listdir("mutants")

    # write the correct answer on first line of the file
    # print("Expected value the software under test: ")
    exec(open(sys.argv[1]).read(), {'a' : sys.argv[2] , 'b': sys.argv[3]})
    # print("\n")

    # write the name of file then the output of the script
    for file in files:
        print("Actual value of the mutant file: " + file)
        exec(open("mutants/" + file).read(), {'a' : sys.argv[2] , 'b': sys.argv[3]})
    
    # redirect stdout back to normal
    sys.stdout = sys.__stdout__

    # store in list all lines
    with open("parallel-mutant-generated-output.txt") as f1:
        lines = f1.readlines()

    # remove '\n' chars from list
    for i in range(0, len(lines)):
        lines[i] = lines[i].replace('\n', '')

    rightAnswer = lines[0]

    # iterate through every second line to check if mutant killed or still alive
    
    

except IOError:
    type, value, traceback = sys.exc_info()
    print('Error opening %s: %s' % (value.filename, value.strerror))
    print("Error with file")


def threadingloop(l): 

        if  float(l) != float(rightAnswer):
            #print("Killed Mutant", l)
            killedMutants.append(l)

        else:
            #print("Mutant Alive", l)
            aliveMutants.append(l)

linelgt = len(lines)+(6-len(lines)%6)
print(linelgt)

for l in range(0, linelgt, 6):
    #print(l)
    try: 
        t1 = threading.Thread(target=threadingloop, args=[lines[l]])
        t2 = threading.Thread(target=threadingloop, args=[lines[l+2]])
        t3 = threading.Thread(target=threadingloop, args=[lines[l+4]])

        t1.start()
        t2.start()
        t3.start()
        

    except IndexError as error: 

        t4 = threading.Thread(target=threadingloop, args=[lines[l]])
        t4.start()

        #getting rid of the right answer value 
        aliveMutants.pop(0)

        print("Killed Mutants")
        print(killedMutants)

        print("Alive Mutants")
        print(aliveMutants)

        output = open("parallel-mutant-generated-output.txt", 'a')

percentage = len(killedMutants) / (len(killedMutants) + len(aliveMutants))
output.write("Mutants killed: %d\n" %len(killedMutants))
output.write("List of killed mutants: \n" + str(killedMutants) + "\n")
output.write("Mutants alive: %d\n" %len(aliveMutants))
output.write("List of alive mutants: \n" + str(aliveMutants) + "\n")
output.write("\n mutants killed using test vector: <" + sys.argv[2] + "," + sys.argv[3] + ">\n")
output.write("Percentage of mutants killed: %d" %len(killedMutants) + "/ %d" %(len(killedMutants) + len(aliveMutants)) + "= %f\n" %percentage)
output.write("\nTIME:\n")
output.write("--- %s seconds ---" % (time.time() - start_time))
output.close()


