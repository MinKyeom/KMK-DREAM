# 내 풀이
def solution(book_time):
    import heapq
    book_time.sort(key=lambda x: (x[0].split(":")))
    heap_start = []
    heap_finish = []
    room_count = 0
    if len(book_time) == 1:
        return 1
    for a, b in book_time:
        c = a.split(":")
        c_num = int(c[0]) * 60 + int(c[1])
        d = b.split(":")
        d_num = int(d[0]) * 60 + int(d[1])
        if len(heap_finish) == 0:
            heapq.heappush(heap_finish, d_num + 10)
            continue
        if c_num >= heap_finish[0]:
            heapq.heappop(heap_finish)
            heapq.heappush(heap_finish, d_num + 10)
        else:
            heapq.heappush(heap_finish, d_num + 10)
        if room_count < len(heap_finish):
            room_count = len(heap_finish)

    return room_count

# 다른 사람 풀이
def solution(book_time):
    time_table = [0 for _ in range(60 * 24)]
    for start, end in book_time:
        start_minutes = 60 * int(start[:2]) + int(start[3:])
        end_minutes = 60 * int(end[:2]) + int(end[3:]) + 10

        if end_minutes > 60 * 24 - 1:
            end_minutes = 60 * 24 - 1

        for i in range(start_minutes, end_minutes):
            time_table[i] += 1
    return max(time_table)