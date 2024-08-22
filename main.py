from datetime import datetime
from utils.input_handler import get_user_input
from schedule_optimizer import ScheduleOptimizer
import argparse


def main():

    optimizer = ScheduleOptimizer()

    user_timestamp = get_user_input()

    print(f"User provided timestamp: {user_timestamp}")
    optimizer.optimizeSchedule(user_timestamp)


if __name__ == "__main__":
    main()