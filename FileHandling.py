import datetime
#InputFilePath = "C:\\Users\\arijh\\OneDrive - Careeria\\Kurssit\\Python\\Harjoitukset\\Input.txt"
#OutputFilePath = "C:\\Users\\arijh\\OneDrive - Careeria\\Kurssit\\Python\\Harjoitukset\\output.txt"

InputFilePath = "C:\\Users\\Ari\\OneDrive - Careeria\\Kurssit\\Python\\Harjoitukset\\Input.txt"
OutputFilePath = "C:\\Users\\Ari\\OneDrive - Careeria\\Kurssit\\Python\\Harjoitukset\\output.txt"


ifh = open(InputFilePath, "r")
#print(ifh.read())
ofh = open(OutputFilePath, "w")
OutputLine = "Enimi\tSnimi\tIkä\n"
ofh.writelines(OutputLine)

x = datetime.datetime.now()
TamaVuosi = x.year
for l in ifh:
	InputLine = l.split("\t")
	Ika = TamaVuosi - int(InputLine[2])
	OutputLine = InputLine[0].strip() + "\t" + InputLine[1].strip() + "\t" + str(Ika).strip() + "\n"
	ofh.writelines(OutputLine)
ifh.close
ofh.close