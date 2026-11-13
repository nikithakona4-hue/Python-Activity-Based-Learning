players = {"Asha":[50,60,70], "Ravi":[80,70,90], "Priya":[60,60,60]}
results = []
for name, scores in players.items():
    avg = sum(scores)/len(scores)
    trend = "Improving" if scores[-1]>scores[0] else "Declining" if scores[-1]<scores[0] else "Stable"
    results.append((name, avg, max(scores), trend))
    print(name, "Average:", avg, "Range:", max(scores)-min(scores), trend)
results.sort(key=lambda x: (x[1], x[2]), reverse=True)
print("Final Ranking:")
for i, r in enumerate(results, 1):
    print(i, r[0], r[1])
