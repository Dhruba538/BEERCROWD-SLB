# Function to get the input for the event details and calculate the duration
def get_event_duration():
    # Get the input for the beginning day of the event
    beginning_day = input("")
    # Get the input for the start time of the event
    start_time = input("")
    # Get the input for the ending day of the event
    ending_day = input("")
    # Get the input for the end time of the event
    end_time = input("")

    # Extract day numbers from the inputs
    beginning_day_number = int(beginning_day.split()[1])
    ending_day_number = int(ending_day.split()[1])

    # Parse the start and end times into hours, minutes, and seconds
    start_hour, start_minute, start_second = map(int, start_time.split(':'))
    end_hour, end_minute, end_second = map(int, end_time.split(':'))

    # Calculate total seconds from the start and end times
    start_total_seconds = (beginning_day_number * 86400) + (start_hour * 3600) + (start_minute * 60) + start_second
    end_total_seconds = (ending_day_number * 86400) + (end_hour * 3600) + (end_minute * 60) + end_second

    # Calculate the duration in seconds
    total_seconds = end_total_seconds - start_total_seconds

    # Calculate days, hours, minutes, and seconds from total_seconds
    days = total_seconds // 86400
    total_seconds %= 86400
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    # Print the output
    print(f"{days} dia(s)")
    print(f"{hours} hora(s)")
    print(f"{minutes} minuto(s)")
    print(f"{seconds} segundo(s)")

# Call the function to run the program
get_event_duration()
