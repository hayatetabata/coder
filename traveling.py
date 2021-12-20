def is_even(num):
    return num % 2 == 0

def validate(diff_t, dis_x, dis_y):
    # 起点からx, yまでの差の絶対値の合計がtを下回る
    if dis_x + dis_y > diff_t:
        return False

    # tが奇数なら距離の合計は必ず奇数、そうでなければ偶数
    if is_even(diff_t) is True:
        if is_even(dis_x + dis_y) is False:
            return False

    if is_even(diff_t) is False:
        if is_even(dis_x + dis_y) is True:
            return False

    return True

N = int(input())

pre_t = 0
pos_x = 0
pos_y = 0
ans = ""

for i in range(0, N):
    if ans == "No":
        continue

    t, x, y = list(map(int, input().split()))
    dis_x = abs(pos_x - x)
    dis_y = abs(pos_y - y)
    diff_t = t - pre_t

    if validate(diff_t, dis_x, dis_y) is True:
        pos_x = x
        pos_y = y
        pre_t = t
        continue

    ans = "No"

if ans == "":
    ans = "Yes"
print(ans)
