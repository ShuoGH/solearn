def morseNum(oriStr):
	dic={    'A':".-",
    'B':"-...",
    'C':"-.-.",
    'D':"-..",
    'E':".",
    'F':"..-.",
    'G':"--.",
    'H':"....",
    'I':"..",
    'J':".---",
    'K':"-.-",
    'L':".-..",
    'M':"--",
    'N':"-.",
    'O':"---",
    'P':".--.",
    'Q':"--.-",
    'R':".-.",
    'S':"...",
    'T':"-",
    'U':"..-",
    'V':"...-",
    'W':".--",
    'X':"-..-",
    'Y':"-.--",
    'Z':"--..",
    '1':".----",
    '2':"..---",
    '3':"...---",
    '4':"....-",
    '5':".....",
    '6':"-....",
    '7':"--...",
    '8':"---..",
    '9':"----.",
    '0':"-----",
    '.':".━.━.━",
    '?':"..--..",
    '!':"-.-.--",
    '(':"-.--.",
    '@':".--.-.",
    ':':"---...",
    '=':"-...-",
    '-':"-....-",
    ')':"-.--.-",
    '+':".-.-.",
    ',':"--..--",
    '\'':".----.",
    '_':"..--.-",
    '$':"...-..-",
    ';':"-.-.-.",
    '/':"-..-.",
    '\"':".-..-.",
    '&':"...."
	}
	word=oriStr.split()
	conStr=''
	for i in word:
		for key in dic.keys():
			if(i==dic[key]):
				conStr+=key
	print(conStr)

str=input("please input your morse code: ")
morseNum(str)


