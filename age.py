driving = input('有沒有開過車:')
if driving != '有' and driving != '沒有':
	input('只能輸入有/沒有')
	raise SystemExit

age = input('請輸入年齡')
age = int(age)
if driving == '有':
	if age >= 18:
		print('合格')
	else:
		print('不合法')
elif driving  == '沒有':
	if age >= 18:
		print('符合資格')
	else:
		print('年齡未到不符合資格')