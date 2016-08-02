import unittest

def snail(array):
	if(array == [[]]):
		return []
	result = []
	array_len = len(array)
	j,k = 0,0
	m = array_len
	m_stat = array_len*4-4
	abc = 0
	while len(result) < array_len**2:
		result.append(array[k][j])
		if k == m-1 and j == m-1:
			while len(result) < array_len**2 and len(result) < m_stat-1:
				j-= 1
				result.append(array[k][j])
				if j == array_len-m:
					break
		if j == array_len-m and len(result) > abc+1:
			k -= 1
		elif j == m-1:
			k += 1
		else:
			j += 1
		if len(result) == m_stat:
			m-=1
			j+=1
			k+=1
			m_stat += m*2
			abc = m_stat-3
	return result
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
print(snail(array))
print("---------------------------")
array = [[ 1, 2, 3,4],
		 [12,13,14,5],
		 [11,16,15,6],
		 [10, 9, 8,7]]
print(snail(array))
print("---------------------------")
array = [[ 1,  2,  3,  4, 5],
		 [16, 17, 18, 19, 6],
		 [15, 24, 25, 20, 7],
		 [14, 23, 22, 21, 8],
		 [13, 12, 11, 10, 9]]
print(snail(array))
print("---------------------------")
array = [[1, 2, 3, 4, 5, 6],
		 [20,21,22,23,24,7],
		 [19,32,33,34,25,8],
		 [18,31,36,35,26,9],
		 [17,30,29,28,27,10],
		 [16,15,14,13,12,11]]
print(snail(array))

class TestSnailArray(unittest.TestCase):
	def test_array_three(self):
		array = [[1,2,3],
				 [4,5,6],
				 [7,8,9]]
		expected = [1,2,3,6,9,8,7,4,5]
		self.assertEqual(snail(array), expected)
	def test_array_four(self):
		array = [[1,3,5,4],
				 [2,8,6,2],
				 [7,3,2,3],
				 [7,8,4,3]]
		expected = [1,3,5,4,2,3,3,4,8,7,7,2,8,6,2,3]
		self.assertEqual(snail(array), expected)
	def test_array_five(self):
		array = [[1, 2, 3, 4, 5],
				 [6, 7, 8, 9, 10],
				 [11, 12, 13, 14, 15],
				 [16, 17, 18, 19, 20],
				 [21, 22, 23, 24, 25]]
		expected = [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
		self.assertEqual(snail(array), expected)

	def test_array_six(self):
		array = [[1, 2, 3, 4, 5, 6],
				 [20,21,22,23,24,7],
				 [19,32,33,34,25,8],
				 [18,31,36,35,26,9],
				 [17,30,29,28,27,10],
				 [16,15,14,13,12,11]]
		expected = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
		self.assertEqual(snail(array), expected)
#unittest.main()