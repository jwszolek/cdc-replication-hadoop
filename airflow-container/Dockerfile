FROM puckel/docker-airflow:latest as airflow

COPY bash_examole_jwszo.py /usr/local/airflow/dags
COPY hive_runner.py /usr/local/airflow/dags

RUN airflow scheduler 2> /dev/null &

EXPOSE 8080