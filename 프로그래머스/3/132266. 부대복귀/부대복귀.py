def solution(n, roads, sources, destination):
    answer = []
    return answer

# ref
import heapq

INF = 987654321
def dijkstra(start, adj, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        # 메모된 거리가 dist보다 짧다면 더 이상 탐색할 필요가 없다.
        if distance[node] < dist:
            continue

        for nxt in adj[node]:
            nxt_distance = dist + 1

            if distance[nxt] > nxt_distance:
                distance[nxt] = nxt_distance
                heapq.heappush(q, (nxt_distance, nxt))

def solution(n, roads, sources, destination):
    adj = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    answer = []

    # create graph
    for a, b in roads:
        adj[a].append(b)
        adj[b].append(a)

    # get distance array
    dijkstra(destination, adj, distance)

    # return value by sources
    for source in sources:
        value = distance[source]
        answer.append(value if value < INF else -1)

    return answer