# Read input values
initial_hour, initial_minute, final_hour, final_minute = map(int, input().split())

# Calculate total minutes
start_time = initial_hour * 60 + initial_minute
end_time = final_hour * 60 + final_minute

# Handle the case where the game ends on the next day
if end_time < start_time:
    end_time += 24 * 60

# Calculate duration
duration_minutes = end_time - start_time

# Check for a full 24-hour game duration
if duration_minutes == 0:
    duration_hours = 24
    duration_minutes = 0
else:
    duration_hours = duration_minutes // 60
    duration_minutes = duration_minutes % 60

# Print the result
print(f"O JOGO DUROU {duration_hours} HORA(S) E {duration_minutes} MINUTO(S)")
