FROM python:3.8
ADD crypto.py .
# ADD commodity.py .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY run_python.sh run_python.sh
RUN chmod +x run_python.sh
# CMD [ "python", "./crypto.py" ]
# CMD [ "python", "./commodity.py" ]
CMD [ "./run_python.sh" ]