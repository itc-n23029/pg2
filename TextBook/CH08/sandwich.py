import pyinputplus as pyip

def main():
    # 各選択肢の価格設定
    prices = {
        'パン': {'小麦パン': 100, '白パン': 100, 'サワー種': 150},
        'タンパク質': {'チキン': 100, 'ターキー': 150, 'ハム': 100, '豆腐': 100},
        'チーズ': {'なし': 0.0, 'チェダー': 100, 'スイス': 100, 'モツァレラ': 100},
        'トッピング': {'マヨネーズ': 50, 'からし': 50, 'レタス': 50, 'トマト': 50}
    }

    print("サンドイッチを作りましょう！")
    
    # パンの種類を尋ねる
    bread = pyip.inputMenu(['小麦パン', '白パン', 'サワー種'], numbered=True, prompt='パンの種類を選んでください:\n')
    
    # タンパク質の種類を尋ねる
    protein = pyip.inputMenu(['チキン', 'ターキー', 'ハム', '豆腐'], numbered=True, prompt='タンパク質の種類を選んでください:\n')
    
    # チーズが必要かどうか尋ねる
    cheese_required = pyip.inputMenu(['はい', 'いいえ'], numbered=True, prompt='チーズが必要ですか？\n')
    if cheese_required == 'はい':
        cheese = pyip.inputMenu(['チェダー', 'スイス', 'モツァレラ'], numbered=True, prompt='チーズの種類を選んでください:\n')
    else:
        cheese = 'なし'
    
    # トッピングを尋ねる
    mayo = pyip.inputMenu(['はい', 'いいえ'], numbered=True, prompt='マヨネーズを追加しますか？\n')
    mustard = pyip.inputMenu(['はい', 'いいえ'], numbered=True, prompt='からしを追加しますか？\n')
    lettuce = pyip.inputMenu(['はい', 'いいえ'], numbered=True, prompt='レタスを追加しますか？\n')
    tomato = pyip.inputMenu(['はい', 'いいえ'], numbered=True, prompt='トマトを追加しますか？\n')

    # サンドイッチの個数を尋ねる
    num_sandwiches = pyip.inputInt('サンドイッチはいくつほしいですか？（1以上の数字）\n', min=1)

    # 合計金額を計算
    total_cost = (
        prices['パン'][bread] +
        prices['タンパク質'][protein] +
        prices['チーズ'][cheese] +
        (prices['トッピング']['マヨネーズ'] if mayo == 'はい' else 0) +
        (prices['トッピング']['からし'] if mustard == 'はい' else 0) +
        (prices['トッピング']['レタス'] if lettuce == 'はい' else 0) +
        (prices['トッピング']['トマト'] if tomato == 'はい' else 0)
    ) * num_sandwiches

    # サンドイッチの注文内容と合計金額を表示
    print("\nご注文のサンドイッチの詳細:")
    print(f"パン: {bread}")
    print(f"タンパク質: {protein}")
    print(f"チーズ: {cheese}")
    print(f"マヨネーズ: {'はい' if mayo == 'はい' else 'いいえ'}")
    print(f"からし: {'はい' if mustard == 'はい' else 'いいえ'}")
    print(f"レタス: {'はい' if lettuce == 'はい' else 'いいえ'}")
    print(f"トマト: {'はい' if tomato == 'はい' else 'いいえ'}")
    print(f"サンドイッチの個数: {num_sandwiches}")
    print(f"合計金額: ¥{total_cost:.2f}")

if __name__ == "__main__":
    main()


