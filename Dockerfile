FROM python:3


WORKDIR /home/ubuntu/projects/Taskmate

COPY requirements.txt .

RUN python3 -m  pip install -r requirements.txt


COPY . .

RUN python3 manage.py migrate

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]


