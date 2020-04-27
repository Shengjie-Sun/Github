def combine(S):
    if not S:
        return None
    elif len(S)<2:
        return S
    
    S = list(S)

    pre = S.pop(0)
    count = 1

    result = ""
    while S:
        cur = S.pop(0)
        if cur == pre:
            count += 1
        elif cur != pre:
            if count==1:
                result += pre
            else:
                result += pre+str(count)
            count = 1
            pre = cur
    
    result += pre+str(count)
    return result

if __name__=="__main__":
    S = "aaaabbccadefff"
    print(combine(S))
