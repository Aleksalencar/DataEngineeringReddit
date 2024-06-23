# Data Pipeline do Reddit
Projeto de um pipeline de dados desenvolvido como parte de um tutorial para aprender ferramentas de uma stack moderna de engenharia de dados como Python, Pyspark, Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift.

## Melhorias e Personalizações
- Adilção de testes unitarios

# Arquitetura
- **Python**: Desenvolvimento dos ETLs, Criação dos DAG's e Operators, integração com Amazon S3
- **Apache Airflow & Celery**: Orquestramento do processo ETL e gerencia a distribuição de tarefas.
- **Docker**: Suporte para rodar o Airflow, criação do docker-compose e Dockerfile
- **API Reddit**: Fonte dos dados, requisitado via praw
- **PostgreSQL**: Armazenamento temporário e gerenciamento de metadados.
- **Amazon S3**: Armazenamento de dados brutos.
- **AWS Glue**: Catalogação de dados e trabalhos de ETL, uso do pyspark.
- **Amazon Athena**: Transformação de dados baseada em SQL. (Work in progress)
- **Amazon Redshift**: Armazenamento e análise de dados. (Work in progress)

# Airflow
![RedditDataEngineering.png](assets%2FAirflow.png)

# S3
![](https://github.com/Aleksalencar/DataEngineeringReddit/blob/main/assets/s3.png)

## Agradecimentos
Agradeço ao autor do tutorial, Yusuf Ganiyu, por fornecer um recurso tão valioso. O tutorial original está disponível [aqui](https://www.youtube.com/watch?v=LSlt6iVI_9Y&t=16s&ab_channel=CodeWithYu).
