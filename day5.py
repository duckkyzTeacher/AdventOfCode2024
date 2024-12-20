fileInput = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

rules = {}
goodLine = []
badLine = []
goodLineMiddleSum = 0


def checkIfValid(line, rules):
    shouldAdd = True
    for num in line.split(","):
        if num in rules:
            for post in rules[num]:
                if post in line:
                    #print(f"\t{num} index: {line.index(num)} >= {post} index: {line.index(post)}")
                    if line.index(num) >= line.index(post):
                        shouldAdd = False
    return shouldAdd



for line in fileInput.splitlines():
    #print(line)
    if "|" in line:
        if not(str(line.split("|")[0]) in rules):
            rules[str(line.split("|")[0])] = []
        rules[line.split("|")[0]].append(line.split("|")[1])
    else:
        #print(rules)
        if "," in line:
            
            shouldAdd = checkIfValid(line, rules)#True
            if(shouldAdd):
                goodLine.append(line)
                goodLineMiddleSum += int(line.split(",")[int((len(line.split(","))/2))])
            else:
                newLine = line.split(",")
                while(not shouldAdd):
                    #update newLine to swap rules that violate?
                    for num in newLine:
                        if num in rules:
                            for post in rules[num]:
                                if post in newLine:
                                    if newLine.index(num) >= newLine.index(post):
                                        #Swap indexs
                                        #print(f"{newLine[0:newLine.index(post)] = }") 
                                        #print(f"{newLine[newLine.index(post)+1:newLine.index(num)] = }")
                                        #print(f"{newLine[newLine.index(post)+1:newLine.index(num)] = }")
                                        #print(f"{newLine[newLine.index(num)+1:] = }")

                                        newLine = newLine[0:newLine.index(post)] + newLine[newLine.index(post)+1:newLine.index(num)] + newLine[newLine.index(post)+1:newLine.index(num)] + newLine[newLine.index(num)+1:]
                                        break
                    
                    
                    shouldAdd = checkIfValid(newLine, rules)

                badLine.append(newLine)



#print(rules)
#print(goodLine)
print(goodLineMiddleSum)
