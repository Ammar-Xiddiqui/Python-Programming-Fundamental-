#program to take input card number and type and then display its name and color
card_number1=int(input('enter card number :'))
card_type1=int(input('enter  card type : '))
if card_number1==2: print('two',end=' ')
if card_number1==3: print('three',end=' ')
if card_number1==4: print('four',end=' ')
if card_number1==5: print('five',end=' ')
if card_number1==6: print('six',end=' ')
if card_number1==7: print('seven',end=' ')
if card_number1==8: print('eight',end=' ')
if card_number1==9: print('nine',end=' ')
if card_number1==10: print('ten',end=' ')
if card_number1==11: print('king',end=' ')
if card_number1==12: print('queen',end=' ')
if card_number1==13: print('jack',end=' ')
if card_number1==1: print('ace',end=' ')


if card_type1==1 : print('of diamond',end=' and its color is red ')
if card_type1==2 : print('of heart',end=' and its color is red')
if card_type1==3 : print('of spade',end=' and its color is black ')
if card_type1==4 : print('of club',end=' and its color is black')