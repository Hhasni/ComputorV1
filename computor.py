#!/usr/bin/python
import sys
import math


RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
STOP = '\033[0m'
BOLD = "\033[1m"

def  	ft_is_ascii(c):#libc isascii
	if (ord(c) >= 65 and ord(c) <= 90):
		return (1)
	elif (ord(c) >= 97 and ord(c) <= 122):
		return (1)
	return (0)

def  	ft_to_list(my_string):#Parse and store in a fresh list
	my_list_x = []

	i = 0
	nb = 0
	exp = 0
	sign = 0
	len_max = len(my_string)
	while (i < len_max):
		if (my_string[i] == '-'):
			sign = 1
		if (my_string[i] >= '0' and my_string[i] <= '9'):
			while (i < len_max and my_string[i] >= '0' and my_string[i] <= '9'):
				nb *= 10
				nb += int(my_string[i])
				i += 1
			if (sign == 1):
				nb = -nb
				sign = 0
			if (i + 3 < len_max and my_string[i] == '*' and ft_is_ascii(my_string[i + 1]) and my_string[i + 2] == '^'):
				i += 3
				while (i < len_max and my_string[i] >= '0' and my_string[i] <= '9'):
					exp *= 10
					exp += int(my_string[i])
					i += 1
			elif (i + 2 <= len_max and my_string[i] == '*' and ft_is_ascii(my_string[i + 1])):
				i += 2
				exp = 1
			my_list_x.append([nb, exp])
			nb = 0
			exp = 0
		elif (i < len_max):
			i += 1;
	return (my_list_x)

def 	ft_to_one_list(my_list_left, my_list_right):# merge list to have [XXXXX] = 0
	nb_tmp = 0
	for mini_list in my_list_right:
		mini_list[0] = -mini_list[0]
		my_list_left.append(mini_list)
	return my_list_left

def		ft_simply_left(my_list_left):#symplify the left list
	symply_left = []
	for x in xrange(0,len(my_list_left)):
		if (x+1 < len(my_list_left) and my_list_left[x][2] == my_list_left[x+1][2]):
			if (my_list_left[x][0] == my_list_left[x+1][0]):
				my_list_left[x][2] += my_list_left[x+1][2]
		symply_left.append(my_list_left[x])

def  	ft_simply(l):#simplify all
	tmp_list = []
	final_list = []
	ret = False
	while (len(l) > 0):
		tmp_list = l[0]
		l.pop(0)
		for i in l:
			if (i[1] == tmp_list[1]):
				tmp_list[0] += i[0]
				i[0] = 0
				i[1] = 0
		if ((tmp_list[0]) != 0):
			final_list.append(tmp_list)
	return final_list

def 	ft_display_simply(my_list):# display the simplify list
	my_str ="Simplify : " 
	tmp = []
	if not my_list:
		my_str += "0" 
	for x, i in enumerate(my_list):
		if (i[0] > 0 and x != 0):
			my_str += "+"
		my_str += str(i[0])
		if (i[1] != 0):
			my_str += "X^"
			my_str += str(i[1])
		tmp.append(i[1])
	my_str += " = 0"
	print  BLUE + my_str + STOP
	if not tmp:
		print GREEN + "\tAll Real numbers are solution." + STOP
		exit(0)
	tab = ["none", "first", "second", "third", "fourth", "pentakill"]
	# print "LEN tmp =" + str(max(tmp))+ "\n"
	# print "LEN tab =" + str(len(tab))+ "\n"
	if (max(tmp) > 3):
		print RED + "This is a Fucking " + str(max(tmp)) + " degree equation"
		print "DO YOU REALLY BELIEVED THAT I CAN SOLVE THIS SHIT!!!!!!!" + STOP
	else:
		print YELLOW + "This is a " + tab[max(tmp)] + " degree equation" + STOP
	return (max(tmp))

def		ft_first_degree(one_list): #First Degree resolution equation
	my_str = "ft_first_degree : "
	nb_x = 0
	num = 0
	res = 0
	for i in one_list:
		if (i[1] == 1):
			nb_x = i[0]
			if (i[0] < 0):
				nb_x = -i[0]
		else:
			num = i[0]
	if (num and nb_x):
		res = float(num) / nb_x
	print GREEN + "\tX = " + str(res) + STOP
	return (0)

def 	ft_no_solution(disc , a, b): #No Real Solution solv
	print PURPLE + "- The discriminant is negative, no real solution exist" + STOP
	soltmp1 = -(b)/2
	soltmp2 = (math.sqrt(-disc))/2
	print GREEN + "\tx1 = -" + str(b) + " - i sqrt(" + str(-disc) + ") / " + str(2*a) + STOP
	print GREEN + "\tx2 = -" + str(b) + " + i sqrt(" + str(-disc) + ") / " + str(2*a) + STOP
	print ""
	print GREEN + "\tx1 = " + str(soltmp1) + " " + str(-soltmp2) + " i" + STOP
	print GREEN + "\tx2 = " + str(soltmp1) + " +" + str(soltmp2) + " i" + STOP
	return 0

def 	ft_one_solution(a, b): # One Real Soluion
	solution = (-b)/(float(2)*a)
	print PURPLE + "- The discriminant is nul" + STOP
	print GREEN + "\tThe unique solution is " + str(solution) + STOP
	return 1

def 	ft_multi_solution(a, b, disc): # Real an Imaginary Solution
	sol1 = -(b +math.sqrt(disc))/(float(2)*a)
	sol2 = -(b -math.sqrt(disc))/(float(2)*a)
	print PURPLE + "- The discriminant is strictly positive" + STOP
	print GREEN + "\tThe x1 solution is " + str(sol2) + STOP
	print GREEN + "\tThe x2 solution is " + str(sol1) + STOP
	return 1

def		ft_second_degree(one_list): # Second Degree!!
	disc = 0
	a = 0;
	b = 0;
	c = 0;
	for i in one_list:
		if (i[1] == 0):
			c = i[0]
		if (i[1] == 1):
			b = i[0]
		if (i[1] == 2):
			a = i[0]
	disc  = b**2 - float(4)*a*c
	if (disc < 0):
		return (ft_no_solution(disc, a, b))
	if (disc == 0):
		return (ft_one_solution(a, b))
	if (disc > 0):
		return (ft_multi_solution(a, b, disc))
	return (0)

def		ft_third3_degree(one_list): # third Degree Equation
	solution = 0
	disc = 0
	a = 0;
	b = 0;
	c = 0;
	p = 0;
	q = 0;
	p_root = 0;
	q_root = 0;
	for i in one_list:
		if (i[1] == 3):
		 	a = i[0]
		if (i[1] == 2):
			b = i[0]
		if (i[1] == 1):
			c = i[0]
		if (i[1] == 0):
			d = i[0]
	if (a == 0):
		print RED + "Can't resolv this, a is negative" + STOP
		exit(0)
	p = ((float(3)*a*c) - (float(b)**2))/(3*(a**2))
	q = float(2)*(b**3)/(27*(a**3)) + (float(d)/a) - ((b)*c)/(float(3)*(a**2))
	if (p == 0 and q == 0):
		print (GREEN + "P = 0 and Q == 0" + STOP)
		print (GREEN + "(b/3a)^3" + STOP)
		exit(0)
	elif (p == 0):
		print (GREEN + "P = 0" + STOP)
		print (GREEN + "racine cubique de q = 0" + STOP)
		exit(0)
	print "p = " + str(p)
	print "q = " + str(q)
	disc = (q**2)/4 + (p**3)/float(27)
	if disc < 0 :
		print PURPLE + "- The discriminant is strictly negative, the equation has a multiple root and all its roots are real." + STOP
	if disc == 0 :
		print PURPLE + "- The discriminant is nul, the equation has three distinct real roots." + STOP
	if disc > 0 :
		print PURPLE + "- The discriminant is strictly positive, the equation has one real and two complec roots." + STOP
	q_root = (q/float(2))**2
	p_root = (p/float(3))**3
	s_root = q_root + p_root
	t_s_root = 0
	if (s_root < 0):
		s_root = -s_root
		t_s_root = 1
	s_root = math.sqrt(s_root)
	if (t_s_root == 1):
		s_root = -s_root
	u_cube = -q/float(2) + s_root
	v_cube = -q/float(2) - s_root
	t_u = 0
	t_v = 0
	if (u_cube < 0):
		u_cube = -u_cube
		t_u = 1
	if (v_cube < 0):
		v_cube = -v_cube
		t_v = 1
	u = u_cube ** (1.0/3)
	v = v_cube ** (1.0/3)
	if (t_v == 1):
		v = -v
	if (t_u == 1):
		u = -u
	if (b < 0):
		b = -b
	v_x = -b/(float(3)*a)
	x0 = u + v
	x1 = (u+v) - v_x
	x2 = (-(u/2) -(v/2) -(v_x))
	x3 = x2 - 1/2
	x = -b / (3*a)
	print GREEN + "\tx1 = " + str(x1) + STOP
	print GREEN + "\tx2 = " + str(x2) + STOP
	print GREEN + "\tx3 = " + str(x3) + STOP

def		ft_none_degree(one_list): # None Degree Equation
	print RED + "There is not solution for this equation." + STOP

def 	ft_parse(my_str): #Parsing line and recogninze Equation
	my_list_left = []
	my_list_right = []
	one_list = []

	my_str = my_str.replace(' ', '');
	my_list = my_str.split('=')
	my_list_left = ft_to_list(my_list[0])
	my_list_right = ft_to_list(my_list[1])
	one_list = ft_to_one_list(my_list_left, my_list_right)
	one_list = ft_simply(one_list)
	ft_nb = ft_display_simply(one_list)
	if (ft_nb == 0):
		ft_none_degree(one_list)
	if (ft_nb == 1):
		ft_first_degree(one_list)
	if (ft_nb == 2):
		ft_second_degree(one_list)
	if (ft_nb == 3):
		ft_third3_degree(one_list)

def 	main(argv):# is that a fucking main?
	if len(sys.argv) == 2:
		my_list = ft_parse(argv[1])
	else :
		print "Usage : python computor.py \"[equation]\""
	return (0)

if __name__ == "__main__":
	try:
		main(sys.argv)
		pass
	except Exception, e:
		print RED + "ERROR : " + str(e) + STOP
		# raise e
