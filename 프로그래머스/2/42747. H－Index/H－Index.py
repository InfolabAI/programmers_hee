#def solution(ct):
#    return
# 240318
def solution(ct):
    ct = sorted(ct, key=lambda x:x, reverse=True)
    for i, c in enumerate(ct):
        if i >= c:
            return i
    
    return i+1



















#def solution(citations):
#    citations.sort(reverse=True)
#    for i, c in enumerate(citations):
#        if i >= c:
#            return i
#    return (i+1)

#def solution(citations):
#    citations=[7,7,7]
#    citations.sort(reverse=True)
#    for i, c in enumerate(citations):
#        print(i, c)
#        if i >= c:
#            return i
#            
#    return (i+1)

# 240314
#def solution(citations):
#    ct = sorted(citations, key=lambda x:x, reverse=True)
#    print(ct)
#    for i, c in enumerate(ct):
#        if c<=i:
#            return i
#    return i+1 # NOTE 틀린부분. 한번도 if 문에 들어가지 않았다면 i+1 을 리턴해야 함. 예를 들어, c가 모두 i 보다 컸다는 얘기.

# 240315
#def solution(citations):
#    ct = sorted(citations, key=lambda x:x, reverse=True)
#    for i, c in enumerate(ct):
#        #print(i, c)
#        if c<=i:
#            return i
#        
#    return i+1


