import hashlib

from time import sleep

def load():

	def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
		percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
		filledLength = int(length * iteration // total)
		bar = fill * filledLength + '-' * (length - filledLength)
		print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
		if iteration == total:
			print()

	items = list(range(0, 30))
	l = len(items)

	loadbar(0, l, prefix='Progress:', suffix='Complete', length=l)
	for i, item in enumerate(items):
		sleep(0.2)
		loadbar(i + 1, l, prefix='Progress:', suffix='Complete', length=l)



flag = 0

pass_hash = input('\n[~] Enter your encrypted data: ')
wordlist = input('\n[~] Enter your wordlist path: ')
try:
	pass_file = open(wordlist, 'r')

except:
	print('\nWordlist is not found\n')
	quit()

print()
load()
sleep(1)
for word in pass_file:
	enc_wrd = word.encode('utf-8')
	digest = hashlib.sha1(enc_wrd.strip()).hexdigest()
	print()
	print()
	print(word)
	print(digest)
	print(pass_hash)
	if digest == pass_hash:
		print('\n[*] Original word is found\n')
		print('[*] Word is >> ' + word)
		flag = 1
		break
if flag == 0:
	print('\n[!] Word is not found in the wordlist\n')

