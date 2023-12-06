partNo = "1"
calibrationInputs = open('CalibrationInputs.txt', 'r')
calibrationLines = calibrationInputs.readlines() 
#calibrationLines = ["6oneighthlf"]
while partNo != "0":

    partNo = input("Which Part? (Type 0 to exit): ")

    if partNo == "1":
        calibrationInputs = open('CalibrationInputs.txt', 'r')
        calibrationLines = calibrationInputs.readlines()

        calibrationValue = 0

        for line in calibrationLines:
            calibrationNumber = ""
            firstChar = ''
            secondChar = ''
            for char in line:
                if 58 > ord(char) > 47:
                    if firstChar == '':
                        firstChar = char
                    else:
                        secondChar = char
            calibrationNumber = (firstChar + secondChar)
            if len(calibrationNumber) == 1:
                calibrationNumber = (calibrationNumber*2)
            calibrationValue += int(calibrationNumber)

        print(calibrationValue)
        
    if partNo == "2":

        calibrationValue = 0
        stringCheckList = ["one", "two", "three","four","five","six","seven","eight","nine"]
        for line in calibrationLines:
            
            calibrationNumber = ""
            firstChar = ''
            secondChar = ''
            stringSequence = ""

            for char in line:
                #if char is a number
                if 58 > ord(char) > 47:
                    stringSequence = ""
                    if firstChar == '':
                        firstChar = char
                    else:
                        secondChar = char
                #if char is char
                
                else:
                    stringSequence += char
                    if stringSequence != "":
                        numberFound = 0
                        highestIndex = -1
                        for index, value in enumerate(stringCheckList):
                            if stringSequence.find(value) != -1 and stringSequence.find(value) > highestIndex:
                                numberFound = index + 1
                                highestIndex = stringSequence.find(value)
                                if firstChar == '':
                                    firstChar = str(numberFound)
                                else:
                                    secondChar = str(numberFound)
                        

            calibrationNumber = (firstChar + secondChar)
            if len(calibrationNumber) == 1:
                calibrationNumber = (calibrationNumber*2)
            print(line + " - " + calibrationNumber)
            calibrationValue += int(calibrationNumber)
        print(calibrationValue)

    if partNo == "3":
        calibrationValue = 0
        stringCheckList = ["one", "two", "three","four","five","six","seven","eight","nine"]
        for line in calibrationLines:
            
            calibrationNumber = ""
            firstChar = ''
            secondChar = ''
            stringSequence = ""

            for char in line:
                if firstChar != '':
                    break
                if 58 > ord(char) > 47:
                    firstChar = str(char)
                    stringSequence = ""

                else:
                    stringSequence += char
                    for index, value in enumerate(stringCheckList):
                        if stringSequence.find(value) != -1:
                            firstChar = str(index + 1)
                            stringSequence = ""
                            break
            
            for char in reversed(line):
                if secondChar != '':
                    break
                if 58 > ord(char) > 47:
                    secondChar = str(char)
                    stringSequence = ""
                else:
                    stringSequence += char
                    RstringSequence = stringSequence[::-1]
                    for index, value in enumerate(stringCheckList):
                        if RstringSequence.find(value) != -1:
                            secondChar = str(index + 1)
                            stringSequence = ""
                            break
                        
            calibrationNumber = (firstChar + secondChar)
            if len(calibrationNumber) == 1:
                calibrationNumber = (calibrationNumber*2)
            print(line + " - " + calibrationNumber)
            calibrationValue += int(calibrationNumber)
        print(calibrationValue)

