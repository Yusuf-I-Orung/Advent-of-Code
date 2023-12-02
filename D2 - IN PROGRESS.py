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
