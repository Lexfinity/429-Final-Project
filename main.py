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
        mutant = l.replace('+', '-', 1)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '-' operator")
        counter += 1
        mutant = l.replace('-', '*', 1)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '*' operator")
        counter += 1
        mutant = l.replace('*', '/', 1)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '-' operator")
        counter += 1

    if '-' in l:
        mutant = l.replace('-', '*', 1)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '*' operator")
        counter += 1
        mutant = l.replace('*', '/', 1)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '-' operator")
        counter += 1
        mutant = l.replace('+', '-', 1)
        # injectedMutants[counter] = mutant
        injectedMutants.append(mutant)
        print("Injected '-' operator")
        counter += 1
    
    # if '-' in l:
    #     mutant = l.replace('-', '+', 1)
    #     lines[counter] = mutant
    #     print("Injected '+' operator")

    # if '/' in l:
    #     mutant = l.replace('/', '*', 1)
    #     lines[counter] = mutant
    #     print("Injected '*' operator")

    # if '*' in l:
    #     mutant = l.replace('*', '/', 1)
    #     lines[counter] = mutant
    #     print("Injected '/' operator")


        
print(injectedMutants)

outfile= open("mutants.txt","w")
for line in lines:
    outfile.write(line)
    outfile.write('\n')
outfile.close()
