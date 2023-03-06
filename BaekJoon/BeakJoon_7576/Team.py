def ripen_tomatoes(input_lines: Optional[Iterator[str]] = None) -> str:
    """🚤 get Elapsed days to all tomatoes to be ripen in conditions ; https://www.acmicpc.net/problem/7576
    Time Complexity (Worst-case): O( Number( BFS(spread_ripened_tomatoes) ) ) from BFS loop
    Space Complexity (Worst-case): O( Number(given_ripened_tomatoes) ) from BFS at least
    Definition
        - n, m: size to create space of tomatoes 2D tank (n*m grid).
        - Number(given_ripened_tomatoes): The number of ripened tomatoes in given n*m grid before ripened state spread.
        - Number( BFS(spread_ripened_tomatoes) ): |V| + |E|; Time occurred from spread ripened tomatoes including given ripened tomatoes in given n*m grid.
            - spread ripened tomatoes are vertexes
            - adjacent tomatoes of a ripened tomato are edges (up to 4 directions in each the cell)
    Implementation
        - Used data structure: Adjacency list in BFS.
        - This solution does not require <is_explored> variable in BFS.
            instead code to compare <is_explored> can be replaced by checking for ripened tomatoes
            , so that code will be simple.
    """
    import sys
    from collections import deque
    from collections.abc import MutableSequence

    if input_lines:
        input_ = lambda: next(input_lines)
    else:
        input_ = sys.stdin.readline

    DIRECTIONS: list[tuple[int, int]] = [
        (-1, 0),  # (-row direction)
        (1, 0),  # (+row direction)
        (0, -1),  # (-column direction)
        (0, 1),  # (+column direction)
    ]

    # Title: input
    # condition: (2 ≤ N, M ≤ 1,000)
    m, n = map(int, input_().split())
    tomato_2d_tank: list[list[int]] = []
    ripe_tomatoes_points: list[tuple[int, int]] = []
    not_ripe_tomatoes_count: int = 0
    for row in range(n):
        # n*m loop
        line: list[int] = list(map(int, input_().split()))
        tomato_2d_tank.append(line)
        for column, x in enumerate(line):
            # EMPTY = -1, NOT_RIPE = 0, RIPE = 1
            if x == 0:
                not_ripe_tomatoes_count += 1
            elif x == 1:
                ripe_tomatoes_points.append((row, column))
    elapsed_day: int = 0

    # Title: solve
    if not_ripe_tomatoes_count > 0:
        elapsed_day += 1
    explored_deque: deque[tuple[int, int]] = deque(ripe_tomatoes_points)

    # simulate
    next_exploration_deque: deque[tuple[int, int]] = deque()
    while not_ripe_tomatoes_count > 0 and len(explored_deque) > 0:
        # add some tomatoes to <next_exploration_deque> from <explored_deque>.
        explored_point = explored_deque.popleft()
        for direction in DIRECTIONS:
            new_point: tuple[int, int] = (
                explored_point[0] + direction[0],
                explored_point[1] + direction[1],
            )

            if (
                0 <= new_point[0] < n
                and 0 <= new_point[1] < m
                and tomato_2d_tank[new_point[0]][new_point[1]] == 0
            ):
                tomato_2d_tank[new_point[0]][new_point[1]] = 1
                not_ripe_tomatoes_count -= 1
                next_exploration_deque.append(new_point)

        # <elapsed_day>-th ends. judge <next_exploration_deque>.
        if len(explored_deque) == 0:
            # when tomatoes can not spread "ripe" state or all tomatoes are ripened.
            if not_ripe_tomatoes_count == 0 or len(next_exploration_deque) == 0:
                break

            # <elapsed_day> ends
            elapsed_day += 1

            # settings for next exploration
            explored_deque = next_exploration_deque.copy()
            next_exploration_deque.clear()

    # when loop is break due to empty <next_exploration_deque> but not ripe tomatoes are remained.
    if not_ripe_tomatoes_count > 0:
        elapsed_day = -1

    # Title: output
    print(elapsed_day)
    return str(elapsed_day)


def test_ripen_tomato() -> None:
    test_case = unittest.TestCase()
    for input_lines, output_lines in [
        [
            [
                "6 4",
                "0 0 0 0 0 0",
                "0 0 0 0 0 0",
                "0 0 0 0 0 0",
                "0 0 0 0 0 1",
            ],
            ["8"],
        ],
        [
            [
                "6 4",
                "0 -1 0 0 0 0",
                "-1 0 0 0 0 0",
                "0 0 0 0 0 0",
                "0 0 0 0 0 1",
            ],
            ["-1"],
        ],
        [
            [
                "2 2",
                "1 -1",
                "-1 1",
            ],
            ["0"],
        ],
    ]:
        start_time = time.time()
        test_case.assertEqual(ripen_tomatoes(iter(input_lines)), output_lines[0])
        print(f"elapsed time: {time.time() - start_time}")
