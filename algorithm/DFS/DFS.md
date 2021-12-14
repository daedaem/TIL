# DFS

작성일: 2021년 12월 10일 오후 6:27
**DFS**

Depth First Search의 약자로 **깊이 우선 탐색**

### **1. 스택 (Stack)**

스택은 선입 후출(First In Last Out)의 구조입니다. 스택은 박스 쌓기에 비유해 볼 수 있습니다.

박스를 아래에서 위로 차곡차곡 쌓은 후에 박스를 치우기 위해서는 위에서부터 치워야 합니다.

그림으로 보면 다음과 같습니다.

![https://blog.kakaocdn.net/dn/HU8Vk/btrbOJNo13g/GraV0z5NNWbVhbSzVc81A0/img.png](https://blog.kakaocdn.net/dn/HU8Vk/btrbOJNo13g/GraV0z5NNWbVhbSzVc81A0/img.png)

스택 구조

파이썬에서는 스택에 **데이터를 삽입**할 때 **stack.append()** 를 사용하고 **삭제**할 때는 **stack.pop()** 를 사용합니다.

- 재귀 함수가 내부적으로 스택 자료구조와 동일하다는 것을 알아두면 DFS 알고리즘을 이해하는데 도움이 됩니다.

### **2. 그래프**

**그래프는 노드와 간선으로 표현**되고 이때 노드를 정점이라고도 말합니다.

**그래프 탐색이란 하나의 노드에서 시작하여 다른 다수의 노드를 방문하는 것**을 말합니다.

그래프는 크게 2가지 방식으로 표현할 수 있습니다.

**① 인접 행렬** : 2차원 배열로 그래프의 연결 관계를 표현하는 방식

![https://blog.kakaocdn.net/dn/dsZYZy/btrbR3xzR0P/RreRJsNJKLkq3iKoxEdDok/img.png](https://blog.kakaocdn.net/dn/dsZYZy/btrbR3xzR0P/RreRJsNJKLkq3iKoxEdDok/img.png)

[좌] 그래프    [우] 그래프를 인접 행렬로 표현

**② 인접 리스트** : 리스트로 그래프의 연결 관계를 표현하는 방식

![https://blog.kakaocdn.net/dn/cXH3yV/btrbPaDYLR9/oDYYOKeKlpn4rkOD9Alt40/img.png](https://blog.kakaocdn.net/dn/cXH3yV/btrbPaDYLR9/oDYYOKeKlpn4rkOD9Alt40/img.png)

그래프를 인접 리스트로 표현

이 두 방식에는 어떤 차이가 있을까요?

메모리 측면에서 살펴보면 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비되게 됩니다.

하지만 인접 리스트 방식은 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용할 수 있습니다.

따라서, 특정 노드와 연결된 모든 노드를 순회해야 하는 경우 인접 리스트 방식이 인접 행렬 방식에 비해 메모리 공간의 낭비가 적다고 볼 수 있습니다.

이제 DFS 알고리즘에 필요한 스택 구조와 그래프의 기본 구조에 대해 알아보았으니 DFS 알고리즘에 대해 자세히 알아보도록 하겠습니다.

**DFS의 동작 과정**은 다음과 같습니다.

① 탐색을 시작할 노드를 스택에 삽입하고 방문 처리를 한다.

② 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 인접 노드가 모두 방문 처리되어있을 경우에는 스택에서 다음 최상단 노드를 꺼낸다.

③  2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.



```python
import sys
sys.setrecursionlimit(99999)


def dfs(v):


    visited[v] = 1
    course.append(v)
    for w in range(N+1):
        if arr[v][w] == 1 and visited[w] == 0:

            dfs(w)

    return course

N,M,V =  map(int,input().split())

arr = [[0]*(N+1) for _ in range((N+1))]
visited = [0]*(N+1)
course = []
for i in range(M):
    start, end = map(int,input().split())
    arr[start][end] = 1
    arr[end][start] = 1


print(*dfs(V))

```

