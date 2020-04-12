#elif 另外如果(可以有很多個)(用在if底下) #else 否則(只能有一個)(用在if底下) #int 整數
word = input('請輸入你的國家: ')
year = input('請輸入你的年齡: ')
year = int(year)
if word == '台灣':
	if year >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif word == '美國':
		if year >= 16:
			print('你可以考駕照')
		else:
			print('你還不能考駕照')