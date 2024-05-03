#def solution(phoneBook):
#    return
# 240322
def solution(phoneBook):
    phoneBook.sort()
    for i in range(1, len(phoneBook)):
        if phoneBook[i].startswith(phoneBook[i-1]):
            return False
    return True










#def solution(phoneBook):
#    sorted_p = sorted(phoneBook)
#    #print(sorted_p)
#    
#    for p1, p2 in zip(sorted_p, sorted_p[1:]):
#        #print(p1, p2)
#        if p2.startswith(p1):
#            return False
#        
#    return True

# 240322
#def solution(phoneBook):
#    phoneBook.sort(reverse=True)
#    #print(phoneBook)
#    for p1, p2 in zip(phoneBook, phoneBook[1:]):
#        if p1.startswith(p2):
#            return False
#    return True



