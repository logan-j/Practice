
class numbers():
	def __init__(self, ints):
		self.ints = ints
		self.multiples = {}

		for i in self.ints:
		
			self.multiples[i] = [x for x in self.multiply(i)]


	def multiply(self, i):
		temp = i

		while(temp < 10): temp += i
		while temp <= 987:
			to_add = str(temp)
			size = len(to_add)
			if size <= 3 and self.no_dupes(to_add):
				if size == 3:

					yield to_add

				else:
					yield '0' + to_add
			temp += i


	def no_dupes(self, input):
		ulist = []
		[ulist.append(x) for x in input if x not in ulist]
		return len(ulist) == len(input)

	def find_pan(self):
		temps = self.multiples[17]
		rights = []
		for i in xrange(len(self.ints) - 2, -1, -1):
			for temp in temps:
				for left in self.multiples[self.ints[i]]:
					if temp[:2] == left[-2:]:
						to_add = str(left)[0] + str(temp)
						if self.no_dupes(to_add):
							rights.append(to_add)
						
			temps = rights
			rights = []
		for i in xrange(1, 10):
			for temp in temps:

				to_add = str(i) + str(temp)
				if self.no_dupes(to_add): rights.append(to_add)

		return [int(x) for x in rights]

def main():
	num = numbers([2, 3, 5, 7, 11, 13, 17])
	print sum(num.find_pan())

if __name__ == '__main__':
	main()
