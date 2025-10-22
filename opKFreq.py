import heapq

def topKFreq(arr, k):
    
    # Dictionary to store frequency of each element
    mp = {}
    for val in arr:
        mp[val] = mp.get(val, 0) + 1

    # Min-heap to keep track of top k frequent elements
    # Each element in heap: [frequency, element]
    pq = []

    for key, freq in mp.items():

        # Push the current element and its frequency into heap
        heapq.heappush(pq, [freq, key])

        # If heap size exceeds k,
        # remove the element with smallest frequency
        if len(pq) > k:
            heapq.heappop(pq)

    res = []

    # Extract elements from heap in descending frequency order
    temp = [0] * len(pq)
    index = len(pq) - 1
    while pq:
        temp[index] = heapq.heappop(pq)[1]
        index -= 1
    for val in temp:
        res.append(val)

    return res

if __name__ == "__main__":
    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    k = 2
    res = topKFreq(arr, k)
    for val in res:
        print(val, end=" ")
