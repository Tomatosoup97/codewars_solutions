def factorial(n):
	if n < 2:
		return 1
	else:
		return n*factorial(n-1)

def dec2FactString(number):
	result = ""
	k = 0
	for i in  range(35,-1,-1):
		fact = factorial(i)
		if number < fact and k == 0:
			continue
		else:
			k+=1
			for j in range(36,-1,-1):
				if len(result) >= k:
					break
				elif  number < fact * j:
					continue
				else:
					if j > 9:
						result+=chr(65+(j-10))
					else:
						result+=str(j)
					number -= fact * j
	return result

def factString2Dec(number):
	length = len(number)
	result = 0
	for i, digit in enumerate(number):
		if ord(digit) > 60:
			result += (ord(digit)-55) * factorial(length-i-1)
		else:
			result += int(digit) * factorial(length-i-1)
	return result