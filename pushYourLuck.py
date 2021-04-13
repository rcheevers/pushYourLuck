matrix = [[0] * 8192] * 8192

def storeResult(List,EV):
    Lower = "0"
    Higher = "0"
    for x in range(1,14):
        if(x not in List):
            if(x<List[-1]):
                Lower += "1"
                Higher += "0"
            else:
                Higher += "1"
                Lower += "0"
        else:
            Lower += "0"
            Higher += "0"
    matrix[int(Lower,2)][int(Higher,2)] = EV

def retrieveResult(List):
    Lower = "0"
    Higher = "0"
    for x in range(1,14):
        if(x not in List):
            if(x<List[-1]):
                Lower += "1"
                Higher += "0"
            else:
                Higher += "1"
                Lower += "0"
        else:
            Lower += "0"
            Higher += "0"
    return matrix[int(Lower,2)][int(Higher,2)]



def EV(List):
    EVBank = sum(List)
    if(EVBank == 91):
        return 91
    stored = retrieveResult(List)
    if(stored != 0):
        return stored
    EVLower = 0
    EVHigher = 0
    for x in range(1,14):
        if(x not in List):
            if(x<List[-1]):
                EVLower += EV(List+[x])
            else:
                EVHigher += EV(List+[x])
    EVLower = EVLower/(13-len(List))
    EVHigher = EVHigher/(13-len(List))
    
    return max(EVBank,EVLower,EVHigher)

def action(List):
    EVBank = sum(List)
    if(EVBank == 91):
        return 91
    EVLower = 0
    EVHigher = 0
    for x in range(1,14):
        if(x not in List):
            if(x<List[-1]):
                EVLower += EV(List+[x])
            else:
                EVHigher += EV(List+[x])
    EVLower = EVLower/(13-len(List))
    EVHigher = EVHigher/(13-len(List))
    print("bank ev: ",EVBank)
    print("lower ev: ",EVLower)
    print("higher ev: ",EVHigher)
    if(max(EVBank,EVLower,EVHigher)==EVBank):
        return "Bank"
    if(max(EVBank,EVLower,EVHigher)==EVLower):
        return "Lower"
    if(max(EVBank,EVLower,EVHigher)==EVHigher):
        return "Higher"

def EVApprox(List,depth):
    EVBank = sum(List)
    if(depth == 0):
        return EVBank
    if(EVBank == 91):
        return 91
    stored = retrieveResult(List)
    if(stored != 0):
        return stored
    EVLower = 0
    EVHigher = 0
    for x in range(1,14):
        if(x not in List):
            if(x<List[-1]):
                EVLower += EVApprox(List+[x],depth-1)
            else:
                EVHigher += EVApprox(List+[x],depth-1)
    EVLower = EVLower/(13-len(List))
    EVHigher = EVHigher/(13-len(List))
    
    return max(EVBank,EVLower,EVHigher)

def actionApprox(List,depth):
    EVBank = sum(List)
    if(EVBank == 91):
        return 91
    EVLower = 0
    EVHigher = 0
    for x in range(1,14):
        if(x not in List):
            if(x<List[-1]):
                EVLower += EVApprox(List+[x],depth-1)
            else:
                EVHigher += EVApprox(List+[x],depth-1)
    EVLower = EVLower/(13-len(List))
    EVHigher = EVHigher/(13-len(List))
    print("bank ev: ",EVBank)
    print("lower ev: ",EVLower)
    print("higher ev: ",EVHigher)
    if(max(EVBank,EVLower,EVHigher)==EVBank):
        return "Bank"
    if(max(EVBank,EVLower,EVHigher)==EVLower):
        return "Lower"
    if(max(EVBank,EVLower,EVHigher)==EVHigher):
        return "Higher"

