# 4000nn is a group of messages from 400000 through 400051.
# The only distinction for them is a code of an error.

import json
from error_messages_parser import get_severety_data


def main():
    severety_data = get_severety_data()
    data = []

    for number in range(400000, 400051):
        data.append(
            {
                'code': number,
                'severety': (severety_data[str(number)]
                             if str(number) in severety_data
                             else 'Undefined'),
                'errorMessage': (
                    '%PIX|ASA-4-4000nn: IPS:number string from '
                    'IP_address to IP_address on interface interface_name'
                ),
                'explanation': (
                    'Messages 400000 through 400051 are Cisco Intrusion '
                    'Prevention Service signature messages.'
                ),
                'recommendedAction': '''See the Cisco Intrusion Prevention Service User Guide on Cisco.com. Not all
signature messages are supported by the ASA in this release. IPS messages all
start with 4-4000nn and have the following format:
- number - The signature number. For more information, see the Cisco Intrusion
Prevention Service User Guide on Cisco.com.
- string - The signature message—approximately the same as the NetRanger
signature message.
- IP_address - The local to remote address to which the signature applies.
- interface_name - The name of the interface on which the signature originated.'''
            }
        )

    json.dump(
        data,
        open('4000nn.json', 'w', encoding='utf-8'),
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    main()
