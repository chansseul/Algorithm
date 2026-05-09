def solution(n):
    # col[i]: i번째 행에 놓인 퀸의 열 번호
    col = [0] * n
    count = 0

    def is_valid(r, c):
        for i in range(r):
            # 1. 같은 열에 있는지 확인
            # 2. 대각선에 있는지 확인 (행 차이 == 열 차이)
            if col[i] == c or abs(col[i] - c) == abs(i - r):
                return False
        return True

    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return

        for c in range(n):
            if is_valid(row, c):
                col[row] = c
                backtrack(row + 1)

    backtrack(0)
    return count