# 演習プロジェクト13.14.4 用に、
# テキストファイルspam001.txt～spam009.txtを作成する。

for i in range(1, 10):
    filename = 'spam{:03}.txt'.format(i)
    with open(filename, 'w', encoding='utf-8') as text_file:
        text_file.write(f'''This is
{filename}
File Text.
''')
        for j in range(1, i + 1):
            text_file.write(f'Appropriate data{j}\n')
        text_file.write('last line')
