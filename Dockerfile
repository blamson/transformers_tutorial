FROM python:3.11
LABEL authors="brady_lamson"

WORKDIR /app

COPY requirements.txt .

RUN apt update && pip3 install --no-cache-dir -r requirements.txt \
	&& pip3 install torch --index-url https://download.pytorch.org/whl/cpu \
  && pip3 install multi-model-server sagemaker-inference

COPY . .

ENV SM_MODEL_DIR /opt/ml/model

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8080", "app:app", "-n"]