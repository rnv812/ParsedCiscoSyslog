import json
import glob
import re


def normalize_text(text: str) -> str:
    text = text.strip()
    text = text.replace('“', '"')
    text = text.replace('”', '"')
    text = text.replace("‘", "'")
    text = text.replace("’", "'")
    text = text.replace('—', '-')
    text = text.replace('•', '*')

    return text


def get_severety_data():
    return json.load(open('./files/output/severety.json', 'r'))


def main():
    severety_data = get_severety_data()
    error_messages = []

    for file in sorted(glob.glob('./files/error_messages/*xxxx.txt')):
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            pattern = (
                r'(\d+)(,\s*\d+)*\s*\n\n'
                r'((Error Message\n\n[\S\s]*?\n\n)+)'
                r'Explanation\n\n([\S\s]*?)\n\n'
                r'Recommended\s+Action\n\n([\S\s]*?)\n\n'
            )
            errs_pattern = r'Error Message\n\n([\S\s]*?)\n\n'

            matches = re.findall(pattern, text)

            for match in matches:
                first_number, rest_numbers, errs, _, expl, rec = match

                first_number = int(first_number)
                rest_numbers = (
                    rest_numbers.split(', ')[1:]
                    if rest_numbers
                    else []
                )
                rest_numbers = list(map(lambda s: int(s), rest_numbers))
                numbers = [first_number] + rest_numbers

                errs = re.findall(errs_pattern, errs)

                if len(numbers) == len(errs):
                    for number, err in zip(numbers, errs):
                        error_messages.append(
                            {
                                'code': number,
                                'severety': (severety_data[str(number)]
                                             if str(number) in severety_data
                                             else 'Undefined'),
                                'errorMessage': normalize_text(err),
                                'explanation': normalize_text(expl),
                                'recommendedAction': normalize_text(rec)
                            }
                        )
                else:
                    err = "\n".join(errs)
                    error_messages.append(
                        {
                            'code': numbers[0],
                            'severety': (severety_data[str(number)]
                                         if str(number) in severety_data
                                         else 'Undefined'),
                            'error': normalize_text(err),
                            'explanation': normalize_text(expl),
                            'recommendedAction': normalize_text(rec)
                        }
                    )
    with open('./files/output/4000nn.json', 'r') as f:
        error_messages_4000nn = json.load(f)
        error_messages.extend(error_messages_4000nn)

    # with open('error_messages.json', 'w') as f:
    #     for msg in error_messages:
    #         f.write(json.dumps(msg) + '\n')

    with open('error_messages.json', 'w') as f:
        json.dump(error_messages, f, indent=4)


if __name__ == '__main__':
    main()
