# /bin/bash/python !

import os
import time
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

banner = ('''    ____                      __    _  __
   / __ \___  _________  ____/ /__ | |/ /
  / / / / _ \/ ___/ __ \/ __  / _ \|   /
 / /_/ /  __/ /__/ /_/ / /_/ /  __/   |
/_____/\___/\___/\____/\__,_/\___/_/|_|
   ..:: Created by: MrHacker-X ::..
''')

main_menu = ('''[##] Select an option:

[01] MD5
[02] SHA1
[03] SHA224
[04] SHA256
[05] SHA384
[06] SHA512
[99] Exit

[~] alex: ''')

pass_select = ('''\n[##] What kind of word list would you like to use:

[01] Custom
[02] Default
[95] Back
[99] Exit

[~] alex: ''')

os.system('clear')
print(banner)
menu = input(main_menu)

if menu == '01' or menu == '1':
	while True:
		pas = input(pass_select)
		if pas == '01' or pas == '1':
			print()
			os.system('python .alex/md5.py')
			break
		elif pas == '02' or pas == '2':
			print()
			os.system('python .alex/md5_auto.py')
			break
		elif pas == '95':
			print('\nComing back\n')
			time.sleep(1)
			os.system('python decodex.py')
			break
		elif pas == '99':
			print("\nExiting...\n")
			time.sleep(1)
			exit()
			
		else:
			print('\nInvalid input\n')
			time.sleep(1)
		
elif menu == '02' or menu == '2':
	while True:
		paas = input(pass_select)
		if paas == '01' or paas == '1':
			print()
			os.system('python .alex/sha1.py')
			break
		elif paas == '02' or paas == '2':
			print()
			os.system('python .alex/sha1_auto.py')
			break
		elif paas == '95':
			print('\nComing back\n')
			time.sleep(1)
			os.system('python decodex.py')
			break
		elif paas == '99':
			print("\nExiting...\n")
			time.sleep(1)
			exit()
			
		else:
			print('\nInvalid input\n')
			time.sleep(1)

elif menu == '03' or menu == '3':
	while True:
		pasa = input(pass_select)
		if pasa == '01' or pasa == '1':
			print()
			os.system('python .alex/sha224.py')
			break
		elif pasa == '02' or pasa == '2':
			print()
			os.system('python .alex/sha224_auto.py')
			break
		elif pasa == '95':
			print('\nComing back\n')
			time.sleep(1)
			os.system('python decodex.py')
			break
		elif pasa == '99':
			print("\nExiting...\n")
			time.sleep(1)
			exit()
			
		else:
			print('\nInvalid input\n')
			time.sleep(1)

elif menu == '04' or menu == '4':
	while True:
		pa = input(pass_select)
		if pa == '01' or pa == '1':
			print()
			os.system('python .alex/sha256.py')
			break
		elif pa == '02' or pa == '2':
			print()
			os.system('python .alex/sha256_auto.py')
			break
		elif pa == '95':
			print('\nComing back\n')
			time.sleep(1)
			os.system('python decodex.py')
			break
		elif pa == '99':
			print("\nExiting...\n")
			time.sleep(1)
			exit()
			
		else:
			print('\nInvalid input\n')
			time.sleep(1)

elif menu == '05' or menu == '5':
	while True:
		paa = input(pass_select)
		if paa == '01' or paa == '1':
			print()
			os.system('python .alex/sha384.py')
			break
		elif paa == '02' or paa == '2':
			print()
			os.system('python .alex/sha384_auto.py')
			break
		elif paa == '95':
			print('\nComing back\n')
			time.sleep(1)
			os.system('python decodex.py')
			break
		elif paa == '99':
			print("\nExiting...\n")
			time.sleep(1)
			exit()
			
		else:
			print('\nInvalid input\n')
			time.sleep(1)

elif menu == '06' or menu == '6':
	while True:
		pasp = input(pass_select)
		if pasp == '01' or pasp == '1':
			print()
			os.system('python .alex/sha512.py')
			break
		elif pasp == '02' or pasp == '2':
			print()
			os.system('python .alex/sha512_auto.py')
			break
		elif pasp == '95':
			print('\nComing back\n')
			time.sleep(1)
			os.system('python decodex.py')
			break
		elif pasp == '99':
			print("\nExiting...\n")
			time.sleep(1)
			exit()
			
		else:
			print('\nInvalid input\n')
			time.sleep(1)



elif menu == "99":
	print("\nExiting...\n")
	time.sleep(1)
	exit()

else:
	print('\nInvalid input\n')
	time.sleep(1)
	os.system('python decodex.py')


