import math as m

while True:
	Bu = int(input('请选择你要进行的计算\n1.三角形边长计算\n2.坐标正运算\n3.坐标逆运算\n'))
	if Bu == 1:
		A = int(input('请输入角A的值:\n'))
		B = int(input('请输入角B的值:\n'))
		c  = int(input('请输入边c的值:\n'))
		C = 3000 - (A+B)
		if C>0:
			TA = 0.06*A*(m.pi/180)
			TB = 0.06*B*(m.pi/180)
			TC = 0.06*C*(m.pi/180)
			a = round((c/(m.sin(TC)))*m.sin(TA),2)
			b = round((c/(m.sin(TC)))*m.sin(TB),2)
			print('value a is %.1f,value b is %.1f' % (a,b))
			Bu2 = input('if you want to continue please press "y" or "n"\n  ')
			if Bu2 == 'y':
				continue
			else:
				break
		else:
			print('输入错误')
		
	if Bu == 2:
		ZAx = int(input('please input A-X ray\n'))
		ZAy = int(input('please input A-Y ray\n'))
		A = int(input('please input the angle A\n'))
		L = int(input('please input the length\n'))
		if ZAy < 0 and ZAx <0 :
			print('input error')
		else:
			TA = 0.06*A*(m.pi/180)
			x = round(m.cos(TA)*L,2)
			y = round(m.sin(TA)*L,2)
			TZAx = ZAx + x
			TZAy = ZAy + y
			print('new add is (%.1f,%.1f)' % (TZAx,TZAy))
			Bu2 = input('if you want to continue please press "y" or "n"\n')
			if Bu2 == 'y':
				continue
			else:
				break