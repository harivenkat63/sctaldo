def compare(name1,name2):
    result=""
    for i in range(len(name1)):
        if name1[i] in name2:
            continue
        else:
            result=result+name1[i]
    return result
