# Data Pipeline do Reddit
Pipeline de dados usando diversas ferramentas de uma stack moderna de engenharia de dados como Python, Pyspark, Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift.

# Arquitetura
**Python**: Desenvolvimento dos ETLs, Criação dos DAG's e Operators, integração com Amazon S3
**Apache Airflow & Celery**: Orquestramento do processo ETL e gerencia a distribuição de tarefas.
**Docker**: Suporte para rodar o Airflow, criação do docker-compose e Dockerfile
**API Reddit**: Fonte dos dados, requisitado via praw
**PostgreSQL**: Armazenamento temporário e gerenciamento de metadados.
**Amazon S3**: Armazenamento de dados brutos.
**AWS Glue**: Catalogação de dados e trabalhos de ETL, uso do pyspark.
**Amazon Athena**: Transformação de dados baseada em SQL.
**Amazon Redshift**: Armazenamento e análise de dados.

# Airflow
![RedditDataEngineering.png](assets%2FAirflow.png)


Projeto original de: Yusuf Ganiyu
* A maior parte de codigo foi parafraseado com objetivo fazer o projeto ficar funcional, observar como as tecnologias interagem e estudar novas ferramentas.
