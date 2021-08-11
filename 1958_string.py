import sys

seq1 = sys.stdin.readline().rstrip()
seq2 = sys.stdin.readline().rstrip()
seq3 = sys.stdin.readline().rstrip()
dp = [[[0]*(len(seq3)+1) for _ in range(len(seq2)+1)] for _ in range(len(seq1)+1)]

for i in range(1,len(seq1)+1):
    for j in range(1,len(seq2)+1):
        for k in range(1,len(seq3)+1):
            if seq1[i-1] == seq2[j-1] == seq3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[-1][-1][-1])