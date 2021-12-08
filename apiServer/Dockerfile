FROM python:3.5
RUN pip3 install django
RUN pip3 install djangorestframework
WORKDIR /usr/src/app
COPY . .
CMD ["python3", "manage.py", "runserver", "0:8000"]
EXPOSE 8000
   