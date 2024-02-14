import time

def countdown(total_seconds):
    try:
        while total_seconds > 0:
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f"Time Left: {hours:02d}:{minutes:02d}:{seconds:02d}", end='\n')
            time.sleep(1)
            total_seconds -= 1

        print("\nTime's up!")
    except KeyboardInterrupt:
        print("\nCountdown interrupted!")

def get_total_seconds(time_str):
    try:
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * 3600 + minutes * 60 + seconds
    except ValueError:
        raise ValueError("Invalid time format. Please use 'h:m:s' format.")


def main():
    user_input = input("Enter the time in format 'h:m:s': ")
    try :
        total_seconds = get_total_seconds(user_input)
    except :
        print("Wrong format !!!")
        return
    countdown(total_seconds)


if __name__ == "__main__":
    main()

