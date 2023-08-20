import json


syslog: dict = json.load(open('syslog.json', 'r', encoding='utf-8'))
err_4000nn: dict = json.load(open('4000nn.json', 'r', encoding='utf-8'))

syslog.update(err_4000nn)

json.dump(
    syslog,
    open(
        'syslog_result.json',
        'w',
        encoding='utf-8'
    ),
    indent=4,
    ensure_ascii=False
)
