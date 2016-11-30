#http://codeforces.com/problemset/problem/625/A

money = int(raw_input().split())
plastic = int(raw_input().split())
glass = int(raw_input().split())
back = int(raw_input().split())

result = 0
real_price = glass - back
if ((real_price) < plastic):
    if (money <= (real_price)):
        total_bottle = (money - glass) / (glass - back) + 1
        result = total_bottle - (glass - back)
