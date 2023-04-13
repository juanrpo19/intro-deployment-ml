FROM python:3.8-slim-buster

WORKDIR /app

COPY api/requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt
COPY api/ ./api
COPY model/model2.pkl ./model/model2.pkl
COPY initializer.sh .
RUN chmod +x inizializer.sh
EXPOSE 8000
ENTRYPOINT ["/bin/bash", "/app/initializer.sh"]