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
