f=open("library-of-mutants.txt", "r")

if f.mode == 'r':
    contents = f.readlines()
    lines = [content.replace('\n', '') for content in contents]
    print(lines)

f.close()

inputfile= open("inputs.txt","w")
for l in lines:
    if "/" in l or "+" in l or "-" in l or "*" in l:
        l = l[l.find('\t\t') + 1:].strip()
        inputfile.write(l)
        inputfile.write('\n')
inputfile.close()

injectedMutants = []
# injectedMutants.append([])
# i = 0
counter = 0
    
for l in lines:
    l = l[l.find('\t\t') + 1:].strip()
    print("Current line: " + l)
    print("Count: %d" %counter)

    if '/' in l:
        # answer = eval(l)
        mutant = l.replace('/', '-', 1)
        # mutantAnswer = eval(mutant)
        # injectedMutants[counter] = mutant
        # mutant = mutant[mutant.find('\t\t') + 1:].strip()
        injectedMutants.append(mutant)
        print("Injected '-' operator")
        counter += 1
        # if (answer != mutantAnswer):
        #     print("mutant killed!\n Expected: %d" %answer + "\n Actual: %d" %mutantAnswer)
        mutant = l.replace('/', '*', 1)
        # mutantAnswer = eval(mutant)
        # injectedMutants[counter] = mutant
        # mutant = mutant[mutant.find('\t\t') + 1:].strip()
        injectedMutants.append(mutant)
        print("Injected '*' operator")
        counter += 1
        # if (answer != mutantAnswer):
        #     print("mutant killed!\n Expected: %d" %answer + "\n Actual: %d" %mutantAnswer)
        mutant = l.replace('/', '+', 1)
        # mutantAnswer = eval(mutant)
        # injectedMutants[counter] = mutant
        # mutant = mutant[mutant.find('\t\t') + 1:].strip()
        injectedMutants.append(mutant)
        print("Injected '+' operator")
        counter += 1
        # if (answer != mutantAnswer):
        #     print("mutant killed!\n Expected: %d" %answer + "\n Actual: %d" %mutantAnswer)

    if '-' in l:
        mutant = l.replace('-', '/', 1)
        # injectedMutants[counter] = mutant
        # mutant = mutant[mutant.find('\t\t') + 1:].strip()
        injectedMutants.append(mutant)
        print("Injected '/' operator")
        counter += 1
        mutant = l.replace('-', '*', 1)
        # injectedMutants[counter] = mutant
        # mutant = mutant[mutant.find('\t\t') + 1:].strip()
        injectedMutants.append(mutant)
        print("Injected '*' operator")
        counter += 1
        mutant = l.replace('-', '+', 1)
        # injectedMutants[counter] = mutant
        mutant = mutant[mutant.find('\t\t') + 1:].strip()
        injectedMutants.append(mutant)
        print("Injected '+' operator")
        counter += 1

    if '+' in l:
        mutant = l.replace('+', '/', 1)
        # injectedMutants[counter] = mutant
        # mutant = mutant[mutant.find('\t\t') + 1:].strip()
        injectedMutants.append(mutant)
        print("Injected '/' operator")
        counter += 1
        mutant = l.replace('+', '*', 1)
        # injectedMutants[counter] = mutant
        # mutant = mutant[mutant.find('\t\t') + 1:].strip()
        injectedMutants.append(mutant)
        print("Injected '*' operator")
        counter += 1
        mutant = l.replace('+', '-', 1)
        # injectedMutants[counter] = mutant
        # mutant = mutant[mutant.find('\t\t') + 1:].strip()
        injectedMutants.append(mutant)
        print("Injected '-' operator")
        counter += 1

    if '*' in l:
        mutant = l.replace('*', '/', 1)
        # injectedMutants[counter] = mutant
        # mutant = mutant[mutant.find('\t\t') + 1:].strip()
        injectedMutants.append(mutant)
        print("Injected '/' operator")
        counter += 1
        mutant = l.replace('*', '-', 1)
        # injectedMutants[counter] = mutant
        # mutant = mutant[mutant.find('\t\t') + 1:].strip()
        injectedMutants.append(mutant)
        print("Injected '-' operator")
        counter += 1
        mutant = l.replace('*', '+', 1)
        # injectedMutants[counter] = mutant
        # mutant = mutant[mutant.find('\t\t') + 1:].strip()
        injectedMutants.append(mutant)
        print("Injected '+' operator")
        counter += 1
    # i += 1
        
print(injectedMutants)

outfile= open("mutants.txt","w")
for line in injectedMutants:
    outfile.write(line)
    outfile.write('\n')
outfile.close()
