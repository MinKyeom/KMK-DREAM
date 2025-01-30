"""
트라이(Trie)란?
트라이(Trie)란 문자열을 저장하고 효율적으로 탐색하기 위한 트리 형태의 자료구조다. 래딕스 트리(radix tree)나 접두사 트리(prefix tree)라고도 한다.
retrieval(탐색)에서 trie를 따왔다고도 한다.
이 자료구조를 활용해 검색어 자동완성, 사전에서 찾기 그리고 문자열 검사 등을 한다고 한다.

사용 목적
문자열의 탐색을 할 때, 단순하게 하나씩 비교하면서 탐색을 하는것보다 시간복잡도 측면에서 훨씬 효율적이다. 단, 빠르게 탐색이 가능하다는 장점이 있지만 각 노드에서 자식들에 대한 포인터들을 배열로 모두 저장하고 있다는 점에서 저장 공간의 크기가 크다는 단점도 있다.

시간 복잡도
제일 긴 문자열의 길이를 L 총 문자열들의 수를 M이라 할 때 시간복잡도는 아래와 같다.

생성 시간 복잡도 : O(M*L), 모든 문자열들을 넣어야하니 M개에 대해서 트라이 자료구조에 넣는건 가장 긴 문자열 길이만큼 걸리니 L만큼 걸려서 O(M*L)만큼 걸립니다. 물론 삽입 자체만은 O(L)만큼 걸린다.
탐색 시간 복잡도: O(L), 트리를 타고 들어가봤자 가장 긴 문자열의 길이만큼만 탐색하기 때문에 O(L)만큼 걸린다.
"""
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 문자열 삽입
    def insert(self, string):
        curr_node = self.head

        # 삽입할 String 각각의 문자에 대해 자식Node를 만들며 내려간다.
        for char in string:
            # 자식Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            # 같음 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            curr_node = curr_node.children[char]

        # 문자열이 끝난 지점의 노드의 data값에 해당 문자열을 표시
        curr_node.data = string


    # 문자열이 존재하는지 탐색!
    def search(self, string):
        # 가장 아래에 있는 노드에서부터 탐색 시작한다.
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        # 탐색이 끝난 후에 해당 노드의 data값이 존재한다면
        # 문자가 포함되어있다는 뜻이다!
        if curr_node.data is not None:
            return True

