#def solution(sizes):
#    return
# 240328
def solution(sizes):
    min_ = [min(x) for x in sizes]
    max_ = [max(x) for x in sizes]
    
    return max(min_) * max(max_)


























#def solution(sizes):
#    max_list = [max(x[0], x[1]) for x in sizes]
#    min_list = [min(x[0], x[1]) for x in sizes]
#    return max(max_list) * max(min_list)

#def solution(sizes):
#    x = [max(n) for n in sizes]
#    m = [min(n) for n in sizes]
#    #print(x, m) 
#    return max(x)*max(m)

