# app/Dockerfile
# RUN git clone https://github.com/streamlit/streamlit-example.git .
# RUN git clone https://github.com/dataprofessor/dashboard-v2.git .

FROM python:3.8
# FROM python:3.9-slim

WORKDIR /app

ADD streamlit_app.py .

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY style.css style.css
COPY packages.txt packages.txt
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]