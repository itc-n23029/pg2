import re

def detect_and_validate_date(text):
    pattern = r"\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([12][0-9]{3})\b"
    matches = re.findall(pattern, text)
    
    valid_dates = []
    for match in matches:
        day, month, year = map(int, match)
        # 月の日数やうるう年のチェックは行わない
        valid_dates.append((day, month, year))
    
    return valid_dates

# テキストから日付を検出して、正しい日付かどうかをチェック
text = "今日の日付は 23/05/2024 ですが、昨日の日付は 22/05/24 でした。また、02/29/2023 も検出されますが、正しい日付ではありません。"
dates = detect_and_validate_date(text)
for day, month, year in dates:
    is_valid = day <= 31 and month <= 12 and 1000 <= year <= 2999
    print(f"日付: {day}/{month}/{year} は{'正しい' if is_valid else '不正な'}日付です。")

