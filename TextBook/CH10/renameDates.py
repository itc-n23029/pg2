import shutil, os, re

# 日付のパターンを定義（アメリカ式: MM-DD-YYYY）
date_pattern = re.compile(r"""^(.*?)
        ((0|1)?\d)-            # 月の部分（1または2桁）
        ((0|1|2|3)?\d)-        # 日の部分（1または2桁）
        ((19|20)\d\d)          # 年の部分（4桁）
        (.*?)$                 # 残りの部分
        """, re.VERBOSE)

# カレントディレクトリ内のファイルをリストアップ
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)

    # パターンに一致しないファイルはスキップ
    if mo is None:
        continue

    # 一致した部分を抽出
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    date_pattern = re.compile(r"""^(1)
        (2 (3) )-
        (4 (5) )-
        (6 (7) )-
        (8)$
        """, re.VERBOSE)

    # ヨーロッパ形式のファイル名を作成（DD-MM-YYYY）
    euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    # ファイル名を表示し、必要に応じてリネーム
    print(f'Renaming "{amer_filename}" to "{euro_filename}"...')
    # 実際にファイルをリネームする
    shutil.move(amer_filename, euro_filename)
