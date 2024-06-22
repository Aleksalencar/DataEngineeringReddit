# Data Pipeline
Com Reddit, Airflow, Celery, Postgres, S3, AWS Glue, Athena, and Redshift

# Arquitetura
1. **Python**: Desenvolvimento dos ETLs, Criação dos DAG's e Operators, integração com Amazon S3
1. **API Reddit**: Fonte dos dados, requisitado via praw
2. **Apache Airflow & Celery**: orquestramento do processo ETL e gerencia a distribuição de tarefas.
3. **PostgreSQL**: armazenamento temporário e gerenciamento de metadados.
4. **Amazon S3**: armazenamento de dados brutos.
5. **AWS Glue**: catalogação de dados e trabalhos de ETL.
6. **Amazon Athena**: transformação de dados baseada em SQL.
7. **Amazon Redshift**: armazenamento e análise de dados.
