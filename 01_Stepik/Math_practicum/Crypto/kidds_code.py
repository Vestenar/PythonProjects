def kidds_encryption(text, reverse=False):
    code_char = '8 	; 	4 	‡ 	) 	* 	5 	6 	( 	1 	† 	0 	9 	2 	: 	3 	? 	¶ 	- 	.'.split()
    word_char = 'e 	t 	h 	o 	s 	n 	a 	i 	r 	f 	d 	l 	m 	b 	y 	g 	u 	v 	c 	p'.split()
    if reverse: code_char, word_char = word_char, code_char
    kidds_dict_crypt = dict(zip(word_char, code_char))
    crypted = "".join([kidds_dict_crypt[i] for i in text])
    return crypted




print(kidds_encryption('ethosnairfdlmbyguvcp'))