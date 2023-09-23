FROM python:3.8
ADD crypto.py .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD [ "python", "./crypto.py" ]