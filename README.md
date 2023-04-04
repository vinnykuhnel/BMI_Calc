# BMI_Calc
Intro to Software Testing and QA
This is a simple BMI calculator that takes height in feet and inches (ex. 6'2") and weight in pounds. It then returns your BMI and classificaiton.
To setup you will need the python interpreter and pytest (pip install pytest).
run python test_BMI.py in command line to start application
run pytest in directory of test_BMI.py from CMD line to runt test cases (make sure to comment out execution of the main function if you are running the test cases (#BMICalc())

Run full website:

pip3 install virtualenv
virtualenv test
source bin/activate
git clone https://github.com/vinnykuhnel/BMI_Calc.git
cd BMI_Calc/
pip3 install -r requirements.txt

Run locally with Django:
python3 BMI_calc/manage.py runserver
Access the application at http://localhost:8000


Run locally with Docker:
sudo service docker start
docker build -t python_django_app_test ./
docker run -it -p 8000:8000 python_django_app_test
Access the application at http://localhost:8000



[![Coverage Status](https://coveralls.io/repos/github/vinnykuhnel/BMI_Calc/badge.svg?branch=main)](https://coveralls.io/github/vinnykuhnel/BMI_Calc?branch=main)
