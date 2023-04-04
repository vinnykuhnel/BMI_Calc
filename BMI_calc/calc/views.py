from django.shortcuts import render
from django.http import HttpResponse
from . import test_BMI
# Create your views here.
def calc(request):
    if request.method == 'GET':
        return render(request, 'calc.html')
    elif request.method == 'POST':
        heightStr = request.POST['height']
        weightStr = request.POST['weight']
        calculator = test_BMI.BMICalc()
        weight = calculator.validateWeight(weightStr)
        if(weight == 0):
                returnError = "Looks like your inputs were invalid!"
                return render(request, 'calc.html', {'returnError': returnError})
        ftStr, inStr = calculator.formatString(heightStr)
        if(ftStr == "" or inStr == ""):
                returnError = "Looks like your inputs were invalid!"
                return render(request, 'calc.html', {'returnError': returnError})
        feet, inches = calculator.convertStringToInt(ftStr, inStr)
        if(feet == 0 or (feet == 0 and inches == 0)):
                returnError = "Looks like your inputs were invalid!"
                return render(request, 'calc.html', {'returnError': returnError})
        heightInches = calculator.calculateHeightInches(feet, inches)
        
        
        bmi = calculator.calculateBMI(heightInches, weight)
        classification = calculator.classifyBMI(bmi)
        return render(request, 'calc.html', {'bmi': bmi, 'classification': classification})
    else:
        return HttpResponse("Looks Like there was an error!")
