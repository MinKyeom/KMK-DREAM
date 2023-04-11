def thieve_jewels(input_lines: Optional[Iterator[str]] = None) -> str:
    """❔ get Maximum sum of value of available jewels ; https://www.acmicpc.net/problem/1202
    Time Complexity (Worst-case): O(n(log n) + O(k log k))
        - O(n(log n)) + O(k(log k)) from Tim sort
            n is the number of jewels, k is the number of bags.
        - O(k) from bag loop  *
            ( O(1) comparison from Jewel consumed iteration  +  O(log k) from Hip (pop | push) )
    Space Complexity (Worst-case): O(n) + O(k) from Tim sort
    Definition
        - n: the number of jewels.
        - k: the number of bags.
    Purpose
        - to maximize value of jewels, a bag should select available Jewel with highest value in each iteration.
    Consideration
        - One bag can select a unique Jewel.
        - ❔ should I check all available Jewels in every bag?
            Inefficient. in the case, if a bag select a jewel it should updates all available Jewels in remained bag.
        - ❔ Which bag should I check a jewel first?
            If a bag with a large allowance is first, it is difficult to choose jewel for a smaller bag.
        - When the number of bag is greater than jewel.
    Implementation
        - Used data structure: Heap
            - Min heap for Jewels.
            - Max heap for available values of Jewels by bag through ad-hoc.
        - To explore <jewel_list> and <bag_list> sorted in ascending order makes that:
            - Once explored jewel's weight will be not important in remained bag's iteration.
                because any added jewel into Max heap can be put in any remained bags.
        - This problem is variant of Knapsack problem.
    """
    import heapq
    import sys
    from typing import NamedTuple

    if input_lines:
        input_ = lambda: next(input_lines)
    else:
        input_ = sys.stdin.readline

    class Jewel(NamedTuple):
        weight: int
        value: int

    class Bag(NamedTuple):
        allowance: int

    # Title: input
    # condition: (1 ≤ N, K ≤ 300,000)
    n, k = map(int, input_().split())
    # condition Jewel: (0 ≤ weight, value ≤ 1,000,000)
    jewel_list: list[Jewel] = [Jewel(*map(int, input_().split())) for _ in range(n)]
    # condition bag: (0 ≤ weight_allowance ≤ 100,000,000)
    bag_list: list[Bag] = [Bag(int(input_())) for _ in range(k)]
    maximum_total_value: int = 0

    # Title: solve
    jewel_list.sort()
    bag_list.sort()
    checked_jewel_value_heapq: list[int] = []
    for bag in bag_list:
        while jewel_list and bag.allowance >= jewel_list[0].weight:
            heapq.heappush(checked_jewel_value_heapq, -jewel_list[0].value)
            heapq.heappop(jewel_list)
        if checked_jewel_value_heapq:
            maximum_total_value += -heapq.heappop(checked_jewel_value_heapq)

    # Title: output
    result: str = str(maximum_total_value)
    print(result)
    return result


def test_thieve_jewels() -> None:
    """Debugging
    =====
    4 3
    2 4 6
    Jewels
    -----
    weight      value
    1            65
    2            99
    5            23
    8            44
    Bag
    -----
    allowance
    2, 4, 6
    2   -> (2, 99)
    4   -> (1, 65)
    10  -> (8, 44)
    """
    test_case = unittest.TestCase()
    for input_lines, output_lines in [
        [["2 1", "5 10", "100 100", "11"], ["10"]],
        [["3 2", "1 65", "5 23", "2 99", "10", "2"], ["164"]],
        [["4 3", "1 65", "2 99", "5 23", "8 44", "2", "4", "10"], ["208"]],
    ]:
        start_time = time.time()
        test_case.assertEqual(thieve_jewels(iter(input_lines)), "\n".join(output_lines))
        print(f"elapsed time: {time.time() - start_time}")

