import os

def find_large_files(directory, size_threshold):
    """
    指定されたサイズを超えるファイルをディレクトリツリー内から探し出して表示します。

    Parameters:
    directory (str): 検索を開始するディレクトリのパス
    size_threshold (int): ファイルサイズの閾値（バイト単位）
    """
    # ディレクトリツリーを歩く
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # ファイルサイズを取得
                file_size = os.path.getsize(file_path)
                # サイズが閾値を超える場合
                if file_size > size_threshold:
                    print(f"{file_path} - {file_size / (1024 * 1024):.2f} MB")
            except FileNotFoundError:
                # ファイルが見つからない場合（リンク切れなど）
                print(f"File not found: {file_path}")
            except PermissionError:
                # パーミッションエラーを無視
                print(f"Permission denied: {file_path}")

