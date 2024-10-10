from bisect import bisect_left, bisect_right
from collections import defaultdict

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):

    a, b, n, m = line()
    row, col = defaultdict(set), defaultdict(set)
    for _ in range(n):
        x, y = line()
        row[x].add(y)
        col[y].add(x)
    
    rows = [k for k in row.keys()]
    cols = [k for k in col.keys()]
    rows.sort()
    cols.sort()

    alice, bob = 0, 0
    pu, pd, pl, pr = 1, a, 1, b

    for torn in range(m):
        li = input().split()
        c, k = li[0], int(li[1])

        if c == 'U':
            i = bisect_left(rows, pu)
            while i < len(rows) and rows[i] < pu + k:
                if not torn % 2: alice += len(row[rows[i]])
                else: bob += len(row[rows[i]])
                for e in row[rows[i]]:
                    if rows[i] in col[e]: col[e].remove(rows[i])
                i += 1
            pu += k
        elif c == 'D':
            i = bisect_right(rows, pd) - 1
            while i >= 0 and rows[i] > pd - k:
                if not torn % 2: alice += len(row[rows[i]])
                else: bob += len(row[rows[i]])
                for e in row[rows[i]]:
                    if rows[i] in col[e]: col[e].remove(rows[i])
                i -= 1
            pd -= k
        elif c == 'L':
            i = bisect_left(cols, pl)
            while i < len(cols) and cols[i] < pl + k:
                if not torn % 2: alice += len(col[cols[i]])
                else: bob += len(col[cols[i]])
                for e in col[cols[i]]:
                    if cols[i] in row[e]: row[e].remove(cols[i])
                i += 1
            pl += k
        else:
            i = bisect_right(cols, pr) - 1
            while i >= 0 and cols[i] > pr - k:
                if not torn % 2: alice += len(col[cols[i]])
                else: bob += len(col[cols[i]])
                for e in col[cols[i]]:
                    if cols[i] in row[e]: row[e].remove(cols[i])
                i -= 1
            pr -= k
    print(alice, bob)