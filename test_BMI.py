
def getUserString():
    heightStr = input("""Enter your height in feet and inches (ex. 5'9\"): """)
    weightStr = input("""Enter your weight in pounds (ex. 123) """)
    return heightStr, weightStr

def formatString(usrStr):
    if(len(usrStr) == 4):
        feet, inches = usrStr.split("'")
        inches = inches.rstrip(inches[-1])
        return feet, inches
    else:
        return "", ""
        

    

def convertStringToInt(feetStr, inchesStr):
    feet = int(feetStr)
    inches = int(inchesStr)
    if(feet > 0 and feet < 9 and inches > -1 and inches < 13):
        return feet, inches
    else:
        return 0, 0

def calculateHeightInches(feet, inches):
    totalInches = (feet * 12) + inches
    return float(totalInches)

def calculateBMI(height, weight):
    kilos = weight * 0.45
    meters = height * 0.025
    doubledHeight = meters * meters
    return round(kilos / doubledHeight, 1)

def classifyBMI(bmi):
    classification = ""
    if(bmi < 18.5):
        classification = "Underweight"
    elif(bmi <= 24.9):
        classification = "Normal Weight"
    elif(bmi <= 29.9):
        classification = "Overweight"
    else:
        classification = "Obese"
    return classification
    


def BMICalc():
    cont = input("""Calculate new BMI (yes) or exit (no): """)
    while(cont == "yes"):
        heightInput, weightInput = getUserString()
        feetStr, inchesStr = formatString(heightInput)
        if(feetStr == "" or inchesStr == ""):
            print("Check your input format ex(6'4\"): ")
            continue
        feet, inches = convertStringToInt(feetStr, inchesStr)
        if(feet == 0 and inches == 0):
            print("Check bounds, a person can not be taller than 8'11\" or have 0 height!")
            continue
        heightInches = calculateHeightInches(feet, inches)
        bmiResult = calculateBMI(heightInches, int(weightInput))
        bmiClass = classifyBMI(bmiResult)
        print("With a BMI of {}, you are considered {}".format(bmiResult, bmiClass))
        cont = input("""Calculate new BMI (yes) or exit (no): """)
        


#temp, temp2 = formatString("6'2\"")
#print(temp, temp2)

BMICalc()

#testing getUserString function is difficult because there are two blocking calls to retrieve from STDIN

#test the formatString function to ensure that it handles anything outside the boundaries correctly
def test_formatString():
    assert formatString("6'4\"") == ("6", "4")
    assert formatString("") == ("", "")
    assert formatString("6'7\"\"") == ("", "")

#test the conversion function from string to int
def test_convertStringToInt():
    assert convertStringToInt("6", "4") == (6, 4)
    assert convertStringToInt("0", "5") == (0, 0)
    assert convertStringToInt("6", "13") == (0, 0)
    assert convertStringToInt("10", "4") == (0, 0)
    assert convertStringToInt("5", "-1") == (0,0)

#ensure conversion from feet to inches is correct in calculateHeightInches function
def test_calcHeightInches():
    assert calculateHeightInches(6, 2) == 74
    assert calculateHeightInches(1, 0) == 12

#ensure BMI calculation and rounding is correct in calculateBMI function
def test_calculateBMI():
    assert calculateBMI(74, 178) == 23.4

#ensure that the classify function is working properly
def test_classifyBMI():
    assert classifyBMI(18.0) == "Underweight"
    assert classifyBMI(18.5) == "Normal Weight"
    assert classifyBMI(24.9) == "Normal Weight"
    assert classifyBMI(25.0) == "Overweight"
    assert classifyBMI(29.9) == "Overweight"
    assert classifyBMI(30.0) == "Obese" 