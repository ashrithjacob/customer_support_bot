FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive

RUN echo "==> Upgrading apk and installing system utilities ...." \
 && apt-get -y update \
 && apt-get install -y wget \
 && apt-get -y install sudo

RUN echo "==> Installing Python3 and pip ...." \  
 && apt-get install python3 -y \
 && apt-get install python3-pip -y

RUN echo "==> Installing packages ...." \
    && pip install --break-system-packages boto3==1.35.37\
    && pip install --break-system-packages botocore==1.35.37\
    && pip install --break-system-packages fuzzywuzzy==0.18.0\
    && pip install --break-system-packages numpy==2.1.2\
    && pip install --break-system-packages pandas==2.2.3\
    && pip install --break-system-packages pydantic==2.9.2\
    && pip install --break-system-packages python-dotenv==1.0.1\
    && pip install --break-system-packages streamlit==1.39.0\
    && pip install --break-system-packages streamlit_autorefresh==1.0.1\
    && pip install --break-system-packages groq==0.12.0\
    && pip install --break-system-packages python-Levenshtein==0.26.1


WORKDIR /customer_support_bot
COPY ./src ./src
COPY .env .env


EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
