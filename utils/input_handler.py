from datetime import datetime

def get_user_input() -> str:
    """
    Prompts the user for a timestamp and validates the input format.

    """

    while True:

        print("Enter a timestamp of the form YYYY-MM-DD HH:MM")
        input_timestamp = input("Timestamp: ")

        try:
            print(f"Valid timestamp entered: {input_timestamp}")
            return input_timestamp

        except ValueError:
            print("Invalid Format. Please enter again in the form YYYY-MM-DD HH:MM")


