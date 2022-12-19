dict = {'A': 'a','C': 'e',  'L': 's','F':'y','W':'c','E':'t','N':'f','P':'h','J':'i','X':'n','M':'d','I':'o','S':'l','Y':'b','O':'g','G':'u','D':'r',' ':' ','!':'!','/':'}',';':'{','_':'_','.':'.','Z':'v','T':'m',':':':','Q':'j','U':'w','H':'p'}

cipher ="FI! XJWCYIUSINLIGH QGLE TAMC A XCU NSAO NID EPC WEN AXM JL EIEASSF HDIGM IN JEL JXOCXGJEF. EPJL JL ASLI EPC LCWIXM HDIYSCT CZCD TAMC NID CALFWEN. PCDC: CALFWEN;EPJL_JL_AX_CALF_NSAO_EI_OGCLL/ GLC WAHJEAS SCEECDL."
plain=""
for i in cipher :
	value=0
	for key in dict :
		if i==key :
			plain+=dict[key]
			value=1

	if value==0: plain+=key


print plain.upper()
