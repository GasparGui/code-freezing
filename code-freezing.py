import datetime
import logging
import os
import sys
import yaml


CONFIG_FILE = "config.yml"

GITLAB_USER_LOGIN = os.environ["GITLAB_USER_LOGIN"]

logging.basicConfig(
    format="[%(asctime)s] [%(levelname)s] - %(message)s",
    datefmt="%m-%d-%Y %I:%M:%S",
    level=logging.DEBUG
)


def get_config(filename: str) -> dict:
    with open(filename) as f:
        return yaml.safe_load(f)


def unpack_config(config: dict) -> tuple:
    try:
        bypass_group = config["bypass_group"]
        freezing_dates = config["freezing_dates"]
    except KeyError:
        logging.error("One of the fields are note present: 'bypass_group' or 'freezing_dates'")
        sys.exit(1)
    return bypass_group, freezing_dates

def is_user_in_bypass_group(username: str, bypass_group: list) -> bool:
    return username in bypass_group

def is_today_within_freezing_date(date_from: datetime.date, date_to: datetime.date) -> bool:
    date_today = datetime.date.today()
    return date_from <= date_today <= date_to


def main():
    config = get_config(CONFIG_FILE)
    bypass_group, freezing_dates = unpack_config(config)

    if is_user_in_bypass_group(GITLAB_USER_LOGIN, bypass_group):
        logging.info(f"{GITLAB_USER_LOGIN} is in bypass group, exiting")
        #sys.exit(0)
    else:
        for period, date in freezing_dates.items():
            date_from = date.get("from")
            date_to = date.get("to")
            logging.info(f"Validating {period} that goes from {date_from} to {date_to}")
            if is_today_within_freezing_date(date_from, date_to):
                logging.warning(f"The current date falls under '{period}', blocket due to freezing period")
                sys.exit(1)

if __name__ == '__main__':
      main()
