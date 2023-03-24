def sort_cards(input_lines: Optional[Iterator[str]] = None) -> str:
    """❔ get Minimum sum of the number of comparisons to sort cards ; https://www.acmicpc.net/problem/1715
    Time Complexity (Worst-case): O(n(log n))
        - O(n) from heapify function
        - O(n-1) from loop  *  3*O(log n) from Hip (pop | push)
    Space Complexity (Worst-case): O(1)
    Definition
        - n: the number of card stack groups.
        - CardStacks(i): the number of cards of i-th card stack.
        - Sum(i): sum of the number of comparisons to cards until i-th merge.
    Recurrence relation
        - Sum(i) ::=
            - if n == 1, 0
            - if n > 1, Sum(i-1) + ( Sum(i-1) + CardStacks(i) )
    Purpose
        - to minimize Sum(x), it requires to select minimum CardStacks(x) in lower merge level.
    Implementation
        - Used data structure: Heap
            - If n == 1, It is not need to compare card stacks. so <result> is 0.
            - If n > 1, Regardless of the number of remained card stacks is odd or even
                , it required to merge with two smallest cards stack in sequence.
    """
    import heapq
    import sys

    if input_lines:
        input_ = lambda: next(input_lines)
    else:
        input_ = sys.stdin.readline

    # Title: input
    # condition: (1 ≤ N ≤ 100,000)
    n: int = int(input_())
    # condition: (1 ≤ CardStacks(i) ≤ 1000)
    card_stack_list: list[int] = [int(input_()) for _ in range(n)]
    minimum_total_comparison_count: int = 0

    # Title: solve
    heapq.heapify(card_stack_list)
    # merge
    while len(card_stack_list) > 1:
        a, b = heapq.heappop(card_stack_list), heapq.heappop(card_stack_list)
        merge_value: int = a + b
        minimum_total_comparison_count = minimum_total_comparison_count + merge_value
        heapq.heappush(card_stack_list, merge_value)

    # Title: output
    print(minimum_total_comparison_count)
    return str(minimum_total_comparison_count)


def test_sort_cards() -> None:
    test_case = unittest.TestCase()
    for input_lines, output_lines in [
        [["4", "30", "40", "50", "100"], ["410"]],
        [["4", "30", "40", "50", "60"], ["360"]],
        [["8", "30", "40", "50", "20", "10", "100", "60", "120"], ["1160"]],
        [["8", "30", "40", "50", "20", "10", "100", "60", "10"], ["860"]],
        [["4", "120", "40", "100", "20"], ["500"]],
    ]:
        start_time = time.time()
        test_case.assertEqual(sort_cards(iter(input_lines)), "\n".join(output_lines))
        print(f"elapsed time: {time.time() - start_time}")
