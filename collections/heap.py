import heapq
heap = []
heapq.heappush(heap, (5, "rest"))
heapq.heappush(heap, (2, "work"))
heapq.heappush(heap, (4, "study"))
print(heap)

heapq.heappop(heap)
heapq.heapreplace(heap,(2, 'work', 5, "rest"))
print(heap)

heapq.heapify(heap)

print(heap)