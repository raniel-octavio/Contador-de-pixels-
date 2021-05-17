


def descript():
    
	with open(sys.argv[1],'rb') as bmp_file:
		bmp = bmp_file.read()

	start_offset = bmp[10] 

	bits = []
	for i in range(start_offset,len(bmp)):
		bits.append(nth_bit_present(bmp[i],0))

	
	out_bytes = []
	for i in range(0,len(bits),8):
    	if(len(bits) - i > 8):
	    out_bytes.append(bits_to_byte(bits[i:i+8]))


bits = 1010
for bits in data:
    if bits in data:
        print ('A')
bits2 = 1011
for bits2 in data:
    if HEXADECIMAL in data:
        print ("B")        
bits 3 = 1100
if bits3 == 1100:
    print ("C")

      