import random
import time
import signal

# タイムアウトのためのシグナルハンドラ
def timeout_handler(signum, frame):
    raise TimeoutError

# シグナルハンドラを登録
signal.signal(signal.SIGALRM, timeout_handler)

number_of_questions = 10
correct_answers = 0

for question_number in range(number_of_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = f'#{question_number + 1}: {num1} x {num2} = '

    # 回答の試行回数
    attempts = 0
    while attempts < 3:
        try:
            # タイムアウトを8秒に設定
            signal.alarm(8)
            answer = input(prompt)
            signal.alarm(0)  # タイムアウト解除

            if answer == str(num1 * num2):
                print('正解！')
                correct_answers += 1
                break
            else:
                print('不正解!')
                attempts += 1

        except TimeoutError:
            print('時間切れ!')
            attempts += 1
        except ValueError:
            print('無効な入力です。もう一度試してください。')
            attempts += 1

        if attempts == 3:
            print('回数制限超え！')

    time.sleep(1)

print(f'得点: {correct_answers} / {number_of_questions}')

