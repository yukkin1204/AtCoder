# Practical Computing
# パスカルの三角形を表示する問題
N = int(input())
m = []

for i  in range(N):
    l = m
    m = []
    for j in range(i + 1):
        if j == 0 or j == i:
            m.append(1)
        else:
            m.append(l[j - 1] + l[j])
    print(' '.join(map(str, m)))
