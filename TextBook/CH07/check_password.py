import re

def is_strong_password(password):
    # 8文字以上で、大文字と小文字を含み、1つ以上の数字を含む正規表現パターン
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
    
    # パスワードがパターンにマッチするかを確認
    if re.match(pattern, password):
        return True
    else:
        return False

# パスワードを入力して強さをチェック
password = input("パスワードを入力してください: ")
if is_strong_password(password):
    print("このパスワードは強いです！")
else:
    print("このパスワードは弱いです。。。")

