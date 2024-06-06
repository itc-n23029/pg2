import os
import shutil

def copy_files_with_extensions(src_dir, dest_dir, extensions):
    """
    指定された拡張子を持つファイルをソースディレクトリからディスティネーションディレクトリにコピーします。

    Parameters:
    src_dir (str): ソースディレクトリのパス
    dest_dir (str): ディスティネーションディレクトリのパス
    extensions (list): コピー対象のファイル拡張子のリスト（例: ['.pdf', '.jpg']）
    """
    # ディスティネーションディレクトリが存在しない場合は作成
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # ディレクトリツリーを歩く
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            # ファイルの拡張子をチェック
            if any(file.endswith(ext) for ext in extensions):
                # ファイルのフルパスを作成
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir, file)
                
                # ファイルをコピー
                shutil.copy2(src_file_path, dest_file_path)
                print(f"Copied: {src_file_path} -> {dest_file_path}")


