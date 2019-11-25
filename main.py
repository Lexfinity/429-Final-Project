f=open("inputs.txt", "r")

if f.mode == 'r':
    contents = f.readlines()
    lines = [content.replace('\n', '') for content in contents]
    print(lines)

f.close()

injectedMutants = []
counter = 0

# for i in range(2):
#     for l in lines:
#         print("Current line: " + l)
#         print("Count: %d" %counter)

#         if '+' in l:
#             mutant = l.replace('+', '-', 1)
#             injectedMutants[counter] = mutant
#             print("Injected '-' operator")
    
#         if '-' in l:
#             mutant = l.replace('-', '+', 1)
#             injectedMutants[counter] = mutant
#             print("Injected '+' operator")

#         if '/' in l:
#             mutant = l.replace('/', '*', 1)
#             injectedMutants[counter] = mutant
#             print("Injected '*' operator")

#         if '*' in l:
#             mutant = l.replace('*', '/', 1)
#             injectedMutants[counter] = mutant
#             print("Injected '/' operator")

#         counter = counter + 1
    
for l in lines:
    print("Current line: " + l)
    print("Count: %d" %counter)


    if '/' in l:
        answer = eval(l)
        mutant = l.replace('/', '-', 1)
        mutantAnswer = eval(mutant)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '-' operator")
        counter += 1
        if (answer != mutantAnswer):
            print("mutant killed!\n Expected: %d" %answer + "\n Actual: %d" %mutantAnswer)
        mutant = l.replace('/', '*', 1)
        mutantAnswer = eval(mutant)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '*' operator")
        counter += 1
        if (answer != mutantAnswer):
            print("mutant killed!\n Expected: %d" %answer + "\n Actual: %d" %mutantAnswer)
        mutant = l.replace('/', '+', 1)
        mutantAnswer = eval(mutant)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '+' operator")
        counter += 1
        if (answer != mutantAnswer):
            print("mutant killed!\n Expected: %d" %answer + "\n Actual: %d" %mutantAnswer)

    if '-' in l:
        mutant = l.replace('-', '/', 1)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '/' operator")
        counter += 1
        mutant = l.replace('-', '*', 1)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '*' operator")
        counter += 1
        mutant = l.replace('-', '+', 1)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '+' operator")
        counter += 1

    if '+' in l:
        mutant = l.replace('+', '/', 1)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '/' operator")
        counter += 1
        mutant = l.replace('+', '*', 1)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '*' operator")
        counter += 1
        mutant = l.replace('+', '-', 1)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '-' operator")
        counter += 1

    if '*' in l:
        mutant = l.replace('*', '/', 1)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '/' operator")
        counter += 1
        mutant = l.replace('*', '-', 1)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '-' operator")
        counter += 1
        mutant = l.replace('*', '+', 1)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '+' operator")
        counter += 1
        
print(injectedMutants)

outfile= open("mutants.txt","w")
for line in injectedMutants:
    outfile.write(line)
    outfile.write('\n')
outfile.close()
