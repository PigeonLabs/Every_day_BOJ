N = int(input())

total_scores = [0] * 3
three_counts = [0] * 3
two_counts = [0] * 3

for _ in range(N):
    scores = list(map(int, input().split()))

    for i in range(3):
        total_scores[i] += scores[i]

        if scores[i] == 3:
            three_counts[i] += 1
        if scores[i] == 2:
            two_counts[i] += 1

best_score = 0
best_three_count = 0
best_two_count = 0
winner = -1

for i in range(3):
    if best_score < total_scores[i]:
        best_score = total_scores[i]
        best_three_count = three_counts[i]
        best_two_count = two_counts[i]
        winner = i

    elif best_score == total_scores[i]:
        if best_three_count < three_counts[i]:
            best_three_count = three_counts[i]
            best_two_count = two_counts[i]
            winner = i

        elif best_three_count == three_counts[i]:
            if best_two_count < two_counts[i]:
                best_two_count = two_counts[i]
                winner = i

            elif best_two_count == two_counts[i]:
                winner = -1

if winner == -1:
    print(0, best_score)
else:
    print(winner + 1, best_score)