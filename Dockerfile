FROM python:3.8

COPY . /opt/app
WORKDIR /opt/app

RUN pip3 install -r requirements.txt
ENTRYPOINT [ "streamlit","run"]
CMD [ "app.py" ]
EXPOSE 8501
