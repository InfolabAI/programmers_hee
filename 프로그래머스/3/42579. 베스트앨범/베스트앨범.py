#def solution(genres, plays):
#    return 0
from collections import defaultdict
# 240503
def solution(genres, plays):
    num_for_genres = defaultdict(lambda:0)
    num_in_genres = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        num_for_genres[g] += p
        num_in_genres[g] += [(i, p)]
    
    answer = []
    #print(num_for_genres)
    #print(num_in_genres)
    sorted_num_for_genres = sorted(num_for_genres.items(), key=lambda x:x[1], reverse=True)
    for k, v in sorted_num_for_genres:
        for i, p in sorted(num_in_genres[k], key=lambda x:x[1], reverse=True)[:2]:
        	answer += [i]
    return answer





















# 240308 .
#from collections import defaultdict
#def solution(genres, plays):
#    answer = []
#    set_genre = defaultdict(lambda:0)
#    play_id_genre = defaultdict(list)
#    for i, (g, p) in enumerate(zip(genres, plays)):
#        set_genre[g] += p
#        play_id_genre[g] += [(p, i)]
#        
#    sorted_genre_list = sorted(set_genre, key=lambda x:set_genre[x], reverse=True)
#    for g, play_id_list in play_id_genre.items():
#        play_id_genre[g] = sorted(play_id_list, key=lambda x:x[0], reverse=True)
#    
#    for sg in sorted_genre_list:
#        answer += list(map(lambda x:x[1], play_id_genre[sg][:2]))
#        
#    return answer




#def solution(genres, plays):
#    answer = []
#    d = {e:[] for e in set(genres)}
#    for e in zip(genres, plays, range(len(plays))):
#        d[e[0]].append([e[1] , e[2]])
#    genreSort =sorted(list(d.keys()), key= lambda x: sum(map(lambda y: y[0], d[x])), reverse = True)
#    for g in genreSort:
#        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
#        answer += temp[:min(len(temp),2)]
#    return answer

