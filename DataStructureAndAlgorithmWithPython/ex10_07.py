# 구구단 출력을 재귀 호출로 구현

def gugu(dan, num) :
	print("%d x %d = %d" % (dan, num, dan*num))
	if num < 9:
		gugu(dan, num+1)

for dan in range(2,10) :
	print("## %d단 ##" % dan)
	gugu(dan, 1)