def Outcode(tipo):
	#opcode = tipo[0:6]

	if(tipo[0]=='a' and tipo[1]=='d' and tipo[2]=='d'):
		print"add"

	elif(tipo[0]=='s' and tipo[1]=='t' and tipo[2]=='l'):
		print"slt"

	elif(tipo[0]=='l' and tipo[1]=='w'):
		print"lw"

	elif(tipo[0]=='b' and tipo[1]=='e' and tipo[2]=='q'):
		print"beq"

	elif(tipo[0]=='b' and tipo[1]=='n' and tipo[2]=='e'):
		print"bne"

	elif(tipo[0]=='s' and tipo[1]=='w'):
		print"sw"

	elif(tipo[0]=='j'):
		print"j"

	elif(tipo[0]=='s' and tipo[1]=='l' and tipo[2]=='l'):
		print"sll"

	elif(tipo[0]=='s' and tipo[1]=='r' and tipo[2]=='l'):
		print"srl"

	elif(tipo[0]=='a' and tipo[1]=='d' and tipo[2]=='d'):
		print"addi"

	elif(tipo[0]=='a' and tipo[1]=='n' and tipo[2]=='d'):
		print"and"

#with open("text3.txt") as f:			#this File works too!
with open("text2.txt") as f:			#this File works too!
	with open('textwrite.txt', 'a') as fw:
		s = f.readline()
		while s != '':
			s = f.readline()
			wr= s.strip()
			wr= wr.split("\t")
			counterall=1100001101010000000
			if(s != ''):
				if(wr[0]=='#'):
					print "comment THIS WONT BE WRITEN INTO THE FILE.TXT"
					#fw.write("comment"+"\n")

				elif(wr[0]=='column:' or wr[0]=='data:' or wr[0]=='loop:' or wr[0]=='print:' or wr[0]=='out:'):
					counterall= counterall+1001110001000000

				elif(wr[0]=='add'):
					print counterall,"100000 #add"
					fw.write("%d"%counterall)
					fw.write("100000")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[0]=='slt'):
					print counterall, "101010 #slt"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[0]=='lw'):
					print counterall, "100011 #lw"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[0]=='sw'):
					print counterall, "101011 #sw"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[0]=='bne'):
					print counterall, "000101 #bne"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[0]=='beq'):
					print counterall,"000100 #beq"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[0]=='j'):
					print counterall,"000010 #j"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[0]=='srl'):
					print counterall,"000010 #srl"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[0]=='sll'):
					print counterall,"000000 #sll"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[0]=='addi'):
					print counterall,"001000 #addi"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[0]=='and'):
					print counterall,"100100 #and"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[1]=='add'):
					print counterall,"100000 #add"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[1]=='slt'):
					print counterall,"101010 #slt"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[1]=='lw'):
					print counterall,"100011 #lw"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[1]=='sw'):
					print counterall,"101011 #sw"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[1]=='bne'):
					print counterall,"000101 #bne"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[1]=='beq'):
					print counterall,"000100 #beq"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[1]=='j'):
					print counterall,"000010 #j"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[1]=='srl'):
					print counterall,"000010 #srl"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[1]=='sll'):
					print counterall,"000000 #sll"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[1]=='addi'):
					print counterall,"001000 #addi"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[1]=='and'):
					print counterall,"100100 #and"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[1]=='sub'):
					print counterall,"100010 #sub"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[1]=='la'):
					print counterall,"011001 #la"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[1]=='li'):
					print counterall,"101101 #li"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[1]=='or'):
					print counterall,"100101 #or"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")

				elif(wr[1]=='move'):
					print counterall,"101001 #move"
					fw.write("%d"%counterall)
					fw.write("101010")
					#fw.write(counterall)
					fw.write("\n")
			else:
				break

		print "Program terminated"
		print "Tomas Venere productions :)"
		f.close()
