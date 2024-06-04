def replace_keywords(file_path):
    # キーワードリスト
    keywords = {
        "ADJECTIVE": "形容詞",
        "NOUN": "名詞",
        "ADVERB": "副詞",
        "VERB": "動詞"
    }

    # テキストファイルを読み込む
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 各キーワードに対してユーザーに入力を求める
    for english_keyword, japanese_keyword in keywords.items():
        replacement = input(f"Enter an {english_keyword.lower()} ({japanese_keyword}): ")
        content = content.replace(english_keyword, replacement)

    # 置換された文章を表示
    print("\n置換された文章:")
    print(content)

# プログラムを実行
replace_keywords('path_to_your_text_file.txt')

