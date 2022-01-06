
def encode(s: bytes) -> bytes:
	p = [1, 2, 4, 8, 16, 32, 64, 128]
	plaintext = []

	for x in s:
		x0, x1, x2, x3 = int(x & p[0] != 0), int(x & p[1] != 0), int(x & p[2] != 0), int(x & p[3] != 0)
		x4, x5, x6, x7 = int(x & p[4] != 0), int(x & p[5] != 0), int(x & p[6] != 0), int(x & p[7] != 0)
		plaintext.append((x0, x1, x2, x3))
		plaintext.append((x4, x5, x6, x7))

	G = [
			[0, 1, 1, 1, 1, 0, 0, 0],
			[1, 0, 1, 1, 0, 1, 0, 0],
			[1, 1, 0, 1, 0, 0, 1, 0],
			[1, 1, 1, 0, 0, 0, 0, 1]
		]

	encoded = []

	for u in plaintext:
		c = 8 * [0]
		c_byte = 0
		for i in range(8):
			for j in range(4):
				c[i] += u[j] * G[j][i]
			c[i] %= 2
			c_byte += c[i] * p[i]
		encoded.append(c_byte)
	print(encoded)
	return bytes(encoded)


'''
def decode(s: bytes) -> bytes:
	p = [1, 2, 4, 8, 16, 32, 64, 128]

	H = [
			[1, 0, 0, 0, 0, 1, 1, 1],
			[0, 1, 0, 0, 1, 0, 1, 1],
			[0, 0, 1, 0, 1, 1, 0, 1],
			[0, 0, 0, 1, 1, 1, 1, 0]
		]

    locator = [
			[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1],
			[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]
		]

	decoded = []

	for c in s:
		c_bits = [int(c & p[i] != 0) for i in range(8)]
		syndrome = 4 * [0]
		for i in range(4):
			for j in range(8):
				syndrome[i] += H[i][j] * c_bits[j]
			syndrome[i] %= 2

		try:
			k = locator.index(syndrome)
			c_bits[k] = (c_bits[k] + 1) % 2
		except:
			pass

		decoded.append(tuple(c_bits[4:]))

	n = len(decoded)

	if n % 2 != 0:
		decoded.append((0, 0, 0, 0))
		n += 1

	output = []

	for i in range(0, n, 2):
		u_byte = 0
		for j in range(4):
			u_byte += decoded[i][j] * p[j]
		for j in range(4, 8):
			u_byte += decoded[i + 1][j - 4] * p[j]
		output.append(u_byte)
	print(decoded)
	return bytes(output)
'''