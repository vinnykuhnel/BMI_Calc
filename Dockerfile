#Dockerfile

FROM python:3.8.1

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY BMI_calc BMI_calc
WORKDIR /BMI_calc

EXPOSE 8000

ENTRYPOINT ["python3", "manage.py"]

CMD ["runserver", "0.0.0.0:8000"]
