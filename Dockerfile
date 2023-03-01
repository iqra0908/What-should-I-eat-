FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN spacy download en_core_web_sm
COPY . .
CMD [ "python", "app.py" ]
