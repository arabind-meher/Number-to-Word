number = {
	'h': 0,
	't': 0,
	'o': 0
}

ones = {
	0: '',
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine'
}

tens_1 = {
    0: 'ten',
	1: 'eleven',
	2: 'twelve',
	3: 'thirteen',
	4: 'fourteen',
	5: 'fiveteen',
	6: 'sixteen',
	7: 'seventeen',
	8: 'eightteen',
	9: 'nineteen'
}

tens_2 = {
	2: 'twenty',
	3: 'thirty',
	4: 'fourty',
	5: 'fifty',
	6: 'sixty',
	7: 'seventy',
	8: 'eighty',
	9: 'ninety'
}

for num in range(1000):
    a = num
    l = [0, 0, 0]
    i = 0
    while(a != 0):
        n = a%10
        l[i] = n
        a = int(a/10)
        i = i+1

    number['o'] = l[0]
    number['t'] = l[1]
    number['h'] = l[2]

    if number['h'] == 0:
        if number['t'] == 0 and number['o'] == 0:
            text = 'zero'
        elif number['t'] == 0:
            text = ones[number['o']]
        elif number['t'] == 1:
            text = tens_1[number['o']]
        else:
            text = tens_2[number['t']] + ' ' + ones[number['o']]

    else:
        if number['t'] == 0 and number['o'] == 0:
            text = ones[number['h']] + ' hundred '
        elif number['t'] == 0:
            text = ones[number['h']] + ' hundred ' + ones[number['o']]
        elif number['t'] == 1:
            text = ones[number['h']] + ' hundred ' + tens_1[number['o']]
        else:
            text = ones[number['h']] + ' hundred ' + tens_2[number['t']] + ' ' + ones[number['o']]

    print(num, '-', text)
