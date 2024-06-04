import os
import re
import sys

def search_in_txt_files(directory, regex_pattern):
    pattern = re.compile(regex_pattern)
    print(f'検索ディレクトリ: {directory}')
    print(f'正規表現パターン: {regex_pattern}')
    
    for root, dirs, files in os.walk(directory):
        print(f'ディレクトリ: {root}, ファイル数: {len(files)}')
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                print(f'ファイルを検索中: {file_path}')
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        for line in lines:
                            if pattern.search(line):
                                print(f'ファイル: {file_path}')
                                print(f'一致した行: {line.strip()}')
                                print('---')
                except Exception as e:
                    print(f'ファイル {file_path} を開くときにエラーが発生しました: {e}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使い方: python findre.py <ディレクトリ> <正規表現パターン>")
        sys.exit(1)
    
    directory = sys.argv[1]
    regex_pattern = sys.argv[2]

    search_in_txt_files(directory, regex_pattern)

