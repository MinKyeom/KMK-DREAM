"""
문제
수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다.

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

수강신청 대충한 게 찔리면, 선생님을 도와드리자!

입력

첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000) # 신경 유무

이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)

"""
"""
import heapq

n=int(input())# n받기
print("일단 확인",n)
lecture_list=[list(map(int,input().split())) for _ in range(n)]
print("확인")
lecture_list.sort()

lecture_queue=[]
heapq.heappush(lecture_queue,lecture_list[0][1])

for i in range(1,n):
    if lecture_list[i][0]<lecture_queue[0]:
        heapq.headppush(lecture_queue,lecture_list[i][1])

    else:
        heapq.heapop(lecture_queue)
        heapq.headppush(lecture_queue,lecture_list[i][1])

print(len(lecture_queue))
"""

"""
def assign_lecture_room(input_lines: Optional[Iterator[str]] = None) -> str:
"""
# ❔ get Minimum the number of lecture rooms that make all lecture available ; https://www.acmicpc.net/problem/11000
#     Time Complexity (Worst-case): O(n(log n))
#         - O(n(log n)) from Tim sort
#         - O(n-1) from loop  *  ( O(1) comparison  +  O(log n) from Hip (pop | push) at least )
#     Space Complexity (Worst-case): O(n) from Tim sort
#     Definition
#         - n: the number of lectures.
#     Implementation
#         - It uses sort for input data in order to compare <end time> of lecture in order.
#         - Used data structure: Heap (Python heapq library uses min heap)
#             if it uses simple list, it must compare all <end time> as many as lecture rooms. so inefficient.
"""
    import heapq
    import sys
    from typing import NamedTuple

    if input_lines:
        input_ = lambda: next(input_lines)
    else:
        input_ = sys.stdin.readline

    class Period(NamedTuple):
        start: int
        end: int

    # Title: input
    # condition: (1 ≤ N ≤ 200,000)
    n: int = int(input_())
    # condition: (0 ≤ lecture.start < lecture.end ≤ 10^9)
    lecture_period_list: list[Period] = [
        Period(*map(int, input_().split())) for _ in range(n)
    ]
    lecture_end_time_heapq: list[int] = []
    minimum_total_lecture_room: int = 0

    # Title: solve
    lecture_period_list.sort()
    heapq.heappush(lecture_end_time_heapq, lecture_period_list[0].end)
    for i in range(1, n):
        if lecture_end_time_heapq[0] <= lecture_period_list[i].start:
            heapq.heapreplace(lecture_end_time_heapq, lecture_period_list[i].end)
        else:
            heapq.heappush(lecture_end_time_heapq, lecture_period_list[i].end)
    minimum_total_lecture_room = len(lecture_end_time_heapq)

    # Title: output
    print(minimum_total_lecture_room)
    return str(minimum_total_lecture_room)


def test_assign_lecture_room() -> None:
    test_case = unittest.TestCase()
    for input_lines, output_lines in [
        [["3", "1 3", "2 4", "3 5"], ["2"]],
        [["8", "1 8", "9 16", "3 7", "8 10", "10 14", "5 6", "6 11", "11 12"], ["3"]],
    ]:
        start_time = time.time()
        test_case.assertEqual(
            assign_lecture_room(iter(input_lines)), "\n".join(output_lines)
        )
        print(f"elapsed time: {time.time() - start_time}")
"""








