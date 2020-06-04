# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
x1, x2 = map(int, input().split())
v, a, d = map(int, input().split())

left = min(x1, x2)
right = max(x1, x2)
distance = right - left

collision_speed = v + a*distance
if collision_speed >= d:
	print(1)
else:
	print(0)