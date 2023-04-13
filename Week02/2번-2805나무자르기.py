import sys
input = sys.stdin.readline

a, b = map(int, input().split())
trees = list(map(int, input().split()))


def tree(trees, m):
    left, right = 0, max(trees)
    ans = 0

    while left <= right:
        mid = (left+right)//2
        total = sum([tree - mid for tree in trees if tree > mid])
        # total이 작으면 mid를 줄여서 키워줌
        if total < m:
            right = mid-1
        # total이 크면 mid를 늘려서 줄여줌
        else:
            ans = mid
            left = mid + 1
    return ans


print(tree(trees, b))
