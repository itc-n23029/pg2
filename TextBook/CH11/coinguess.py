import random

def coin_toss_game():
    guess = ''
    valid_inputs = ('表', '裏')
    
    # ユーザーの最初の入力を検証
    while guess not in valid_inputs:
        print('コインの表裏を当てて下さい。表か裏を入力してください:')
        guess = input()
    
    # コインのトス結果を生成
    toss = random.choice(valid_inputs)
    
    # 最初の比較
    if toss == guess:
        print('当たり')
    else:
        print('はずれ！もう一回当てて！')
        guess = ''
        
        # 再入力を検証
        while guess not in valid_inputs:
            guess = input()
        
        # 再度比較
        if toss == guess:
            print('当たり')
        else:
            print('はずれ。このゲームは苦手ですねｗ')

# ゲームを実行
coin_toss_game()

