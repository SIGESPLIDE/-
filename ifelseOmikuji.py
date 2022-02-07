#おみくじ変数にrandomな変数を代入
import random
print("あなたの運勢は")
#大吉, 吉, 中吉, 小吉, 半吉, 末吉, 末小吉, 平, 凶, 小凶, 半凶, 末凶, 大凶
omikuji = random.randint(1,13)
if omikuji == 1:
    print("大吉です")
elif omikuji == 2:
    print("吉です")
elif omikuji == 3:
    print("中吉です")
elif omikuji == 4:
    print("半吉です")
elif omikuji == 5:
    print("末吉です")
elif omikuji == 6:
    print("末小吉です")
elif omikuji == 7:
    print("平です")
elif omikuji == 8:
    print("凶です")
elif omikuji == 9:
    print("小凶です")
elif omikuji == 10:
    print("半凶です")
elif omikuji == 11:
    print("末凶です")
elif omikuji == 12:
    print("大凶です")
elif omikuji == 13:
    print("小吉です")
