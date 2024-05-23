import pyperclip, re

phone_regex = re.compile(r"""(
        (0\d{0,3}|\(0\d{0,3}\))
        (\s|-)
        (\d{1,4})
        (\s|-)
        (\d{3,4})
        (\s*(ext|x|ext.)\s*(\d{2,5}))?
        )""", re.VERBOSE)

email_regex = re.compile(r"""(
        [a-zA-Z0-9._%+-]+ #ユーザー名
        @                 #@ 記号
        [a-zA-Z0-9.-]+    #ドメイン名
        (\.[a-zA-Z]{2,4}) #ドットなんとか
        )""", re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])
if len(matches) > 0:
    s = '\n'.join(matches)
    pyperclip.copy(s)
    print('クリップボードにコピーしました:')
    print(s)
else:
    print('電話番号やメールアドレスは見つかりませんでした。')
    
