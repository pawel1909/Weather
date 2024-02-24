

def createLog(l):
    
    with open('log.txt', 'w') as f:
        for i in l:
            f.write(f"{i} \n")