import glob
import json
import re


def main():
    severety_levels = {
        1: 'Alert',
        2: 'Critical',
        3: 'Error',
        4: 'Warning',
        5: 'Notification',
        6: 'Information',
        7: 'Debugging'
    }

    data = dict()

    for file in sorted(glob.glob('./files/severety/level_*.txt')):
        with open(file, 'r') as f:
            text = f.read()
            pattern = r'%ASA-(\d)-(\d+):.*?\n'

            matches = re.findall(pattern, text)

            for match in matches:
                level, code = match
                level, code = int(level), int(code)
                data[code] = severety_levels[level]

    json.dump(data, open('severety.json', 'w'), indent=4)


if __name__ == '__main__':
    main()
