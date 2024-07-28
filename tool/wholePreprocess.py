#  --> ch_simple2tradi --> regularTime --> to csv

from jsonCombine import combine
from ch_simple2tradi import convert_text
from regularTime import modify_dates
from to_csv import to_csv
import sys


def main(name):

    try:
        convert_text(name)
        modify_dates(name)
        to_csv(name)
        print(f"{name} done")
    except Exception as e:
        print(f"{name}: {e}")


if __name__ == '__main__':
    print(sys.argv[1])
    main(sys.argv[1])
