# Darren Stults

def sumDigits(num):
	# check for invalid inputs
	if num is None:
		return 'Error: Null value'
	if num == '':
		return 'Error: Empty value'
	if int(num) > (2 ** 55) - 1: # 7 bytes - 1 bit for sign ?
		return 'Error: Out of range (max: ' + str((2 ** 55) - 1) + ')' # 7 bytes - 1 bit for sign ?
	
	# sanitize all other inputs -- decimal digits are accepted, negative should be ignored
	num = str(num).replace('.', '').replace('-', '')
	num = int(num, 10) # make number again

	# actual process
	sum = 0
	while (num > 0):
		sum += num % 10
		#print('sum +' + str(num % 10) + ' = ' + str(sum))
		num //= 10

	return sum

# string-only version (simple demo, no exception handling)
def sumDigits2(num):
	sum = 0
	while (num != ''):
		sum += int(num[0:1])
		#print('sum +' + num[0:1] + ' = ' + str(sum))
		num = num[1:]
	return sum

# program tests
print('\n=========== Darren\'s SumDigits ===========\n')

print(sumDigits(0)) # actual testCC cases
print(sumDigits(1))
print(sumDigits(12))
print(sumDigits(123))
print(sumDigits(1001))

print(sumDigits(1234)) # 1234 in 5 flavors
print(sumDigits(-1234))
print(sumDigits('1234'))
print(sumDigits(1.234))
print(sumDigits(12.34))

print(sumDigits('')) # error testCC cases
print(sumDigits(None))
#print(sumDigits())
#print(sumDigits(2/0))
#print(sumDigits(-2/0))

print(sumDigits(36028797018963967)) # 91 extremes
print(sumDigits2('360287970189639671')) # 92
print(sumDigits(111111111111111111))
print(sumDigits2('111111111111111111'))
