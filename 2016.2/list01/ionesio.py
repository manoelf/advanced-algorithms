#coding:utf-8

inp = raw_input()
inp = inp.split()
for i in range(len(inp)):
	inp[i] = int(inp[i])
inp.sort()

if(inp[0] == inp[1] and inp[0] == inp[2]):
	inter = 400
else:
	if(inp[0] + 200 == inp[1] and inp[1] + 200 == inp[2]):
		inter = 0
	if(inp[1] < inp[0] + 200 and inp[2] > inp[0] + 200 and inp[2] > inp[1] + 200):
		inter = abs(inp[0] + 200 - inp[1])
	if(inp[2] < inp[0] + 200):
		inter = abs(inp[0] + 200 - inp[2])
		inter = (2* 200 - inter) + inter
	if(inp[0] + 200 < inp[1] and inp[1] + 200 > inp[2]):
		inter = abs(inp[1] + 200 - inp[2])
	if(inp[0] + 200 > inp[1] and inp[1] + 200 > inp[2] and inp[0] + 200 < inp[2]):
		inter1 = abs(inp[0] + 200 - inp[1])
		inter2 = abs(inp[1] + 200 - inp[2])
		inter = inter1 + inter2
	if(inp[0] + 200 == inp[1] and inp[1] + 200 > inp[2]):
		inter = abs(inp[1] + 200 - inp[2])
		inter = 600 - (2*( 200 - inter) + inter +200 )
	if(inp[0] + 200 > inp[1] and inp[1] + 200 == inp[2]):
		inter = abs(inp[0] + 200 - inp[2])
		inter = 600 - (2 *(200 - inter) + inter +200 ) - 600

areaVazia = inter * 100

print areaVazia
