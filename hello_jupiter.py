import random

print("乱数を生成するので、最小値を最大値を順番に入力してください")

min = input("最小値を入力: ")
max = input("最大値を入力: ")

random_int = random.randint(int(min),int(max))

print(min + '〜' + max + "の範囲で乱数を生成しました！")

num = None

while num != random_int:
    num = int(input('数字を当ててください: '))
    if(num == random_int): break
    if(random_int > num): print("❌: それより大きい数字です")
    else: print("❌: それより小さい数字です")

print("✅: 正解です！ 正解は" + str(random_int) + "でした")
