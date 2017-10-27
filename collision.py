#!/usr/bin/env python
# Copyright 2017 Harish N Sathishchandra harishns@bu.edu
# Copyright 2017 Keval Khara kevalk@bu.edu
# Copyright 2017 Donato Kava dkava@bu.edu

import math
import numpy as np
import sys
obj=[]
obj_app=[]
obj_new=[]
#Time input constraint
for i in range(1,len(sys.argv)):
	try:
		float(sys.argv[i])
		if float(sys.argv[i])>=0:
			flag_time_str = 0
		else:
			sys.exit(2)
	except:
		flag_time_str = 1
		sys.exit(2)

if len(sys.argv) == 1 or flag_time_str == 1:
	sys.exit(2)
else:
	while True:
		try:
			input_str=input()
			if len(input_str.split()) != 5:
				sys.exit(1)
			else:
				for j in range(1,5):
					try:
						float(input_str.split()[j])
					except:
						sys.exit(1)
					else:
						pass
				obj.append([input_str])
				obj_spl=[str(j) for j in input_str.split()]
				obj_app.append(obj_spl)	#obj_app=[['one','1','2','3','4']['two','5','6','7','8']]
		except EOFError:
			
			name=[]
			x=[]
			y=[]
			vx=[]
			vy=[]
			x_new=[]
			y_new=[]
			vx_new=[]
			vy_new=[]
			x_coll=[]
			y_coll=[]
			coll=[]
			for i in range(0,len(obj_app)):
				name.append(obj_app[i][0])
				x.append(float(obj_app[i][1]))
				y.append(float(obj_app[i][2]))
				vx.append(float(obj_app[i][3]))
				vy.append(float(obj_app[i][4]))
				
			if len(obj_app) == 1:
				time_list=[]
				for i in range(1,len(sys.argv)):
					time_list.append(float(sys.argv[i]))
				time_list.sort()
				for time in time_list:
					name=[]
					x=[]
					y=[]
					vx=[]
					vy=[]
					for i in range(0,len(obj_app)):
						print(time)
						name.append(obj_app[i][0])
						x.append(float(obj_app[i][1]))
						y.append(float(obj_app[i][2]))
						vx.append(float(obj_app[i][3]))
						vy.append(float(obj_app[i][4]))

						x_new=x[0]+vx[0]*time
						y_new=y[0]+vy[0]*time
						vx_new=vx[0]
						vy_new=vy[0]
						obj_new=[name[0],x_new,y_new,vx_new,vy_new]
						print(obj_new[0]+' '+str(obj_new[1])+' '+str(obj_new[2])+' '+str(obj_new[3])+' '+str(obj_new[4]))
				sys.exit(0)

