FROM python:3.8-slim-buster

WORKDIR /app

COPY api/requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt
COPY api/ ./api
COPY model/model2.pkl ./model/model2.pkl
COPY initializer2.sh .
RUN chmod +x initializer2.sh
EXPOSE 8000
ENTRYPOINT ["/bin/bash", "/app/initializer2.sh"]