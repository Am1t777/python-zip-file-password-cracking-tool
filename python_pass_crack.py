import zipfile


def main():
	"""
	Zipfile password cracker using a brute-force dictionary attack
	Task Fom GCI 2019
	Fedora Project
	"""
	zipfilename = 'tool_buy.zip'
	dictionary = 'password.txt'

	password = None
	zip_file = zipfile.ZipFile(zipfilename)
	with open(dictionary, 'r') as f:
		for line in f.readlines():
			password = line.strip('\n')
			try:
				zip_file.extractall(pwd=password)
				password = 'Password found: %s' % password
			except:
				print("GCI 2019 Trying To Crack A Password >>>>>>>>>>>>>>")


        
	print("***********")
	print("Password Found : %s" % password)

if __name__ == '__main__':
	main()
