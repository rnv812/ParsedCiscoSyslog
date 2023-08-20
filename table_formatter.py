from textwrap import wrap

cells = [
    '''Time-out activated
''',
    '''The SSH session timed out because the
duration specified by the ssh timeout
command was exceeded.
''',
    '''Restart the SSH connection. You can use
the ssh timeout command to increase the
default value of 5 minutes up to 60 minutes
if required.
'''
]

sizes = [16, 30, 34]

rows = []

for cell, size in zip(cells, sizes):
    rows.append(wrap(cell, width=size - 1))


rows_count = len(max(rows, key=len))

text = ''
for i in range(rows_count):
    offset = 0
    line = ' ' * sum(sizes)
    for column_idx, column in enumerate(rows):
        try:
            column_text = column[i]
        except IndexError:
            column_text = ''
        spaces_remains = (sizes[column_idx] - len(column_text))
        line = line[:offset] + column_text + line[offset + len(column_text) + spaces_remains:]
        offset += sizes[column_idx]
    text += line + '\n'

print(text)
