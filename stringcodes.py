if __name__==__main__:
	input_bytes=b'\xff\xfe4\x001\x003\x00\x00i\x00s\x00\x00i\x00n\x00.\x00'
	input_characters=input_bytes.decode('ascii')
	print(repr(input_characters))
	
	output_characters='We copy you down,Eagle.\n'
	output_bytes=output_characters.encode('ascii')
	with open('eagle.txt','wb') as f:
		f.write(output_bytes)
