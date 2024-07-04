import heapq

N = int(1e5) + 10
INF = int(1e9) + 10
g = [[] for _ in range(N)]

def dijkstra(source, n):
    dis = [INF] * N
    pred = [-1] * N
    dis[source] = 0
    pq = [(0, source)]
    while pq:
        dist, v = heapq.heappop(pq)
        if dist > dis[v]:
            continue
        for child_v, wt in g[v]:
            if dis[v] + wt < dis[child_v]:
                dis[child_v] = dis[v] + wt
                pred[child_v] = v
                heapq.heappush(pq, (dis[child_v], child_v))
    
    ans = 0
    ans_node = -1
    for i in range(1, n + 1):
        if dis[i] == INF:
            print(-1)
            return
        if dis[i] > ans:
            ans = dis[i]
            ans_node = i
    path = []
    at = ans_node
    while at != -1:
        path.append(at)
        at = pred[at]
    path.reverse()
    print(' '.join(map(str, path)))

def main():
    n, m = map(int, input().split())
    for _ in range(m):
        x, y, wt = map(int, input().split())
        g[x].append((y, wt))
    dijkstra(1, n)

if __name__ == "__main__":
    main()
