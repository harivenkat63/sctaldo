message=input()
res = ""
   count = 1
    res += message[0]
    for i in range(len(message)-1):
        if(messsage[i] == message[i+1]):
            count+=1
        else:
            if(count > 1):
                res += str(count)
            res += message[i+1]
            count = 1
    if(count > 1):
        res += str(count)
    print( res)
