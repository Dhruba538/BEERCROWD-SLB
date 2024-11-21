start_time,end_time =map(int, input().split())

if end_time > start_time:
    duration = end_time - start_time
else:
    duration = (24 - start_time) + end_time

print(f"O JOGO DUROU {duration} HORA(S)")
