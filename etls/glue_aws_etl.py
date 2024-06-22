import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import concat_ws
from awsglue import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1718954137770 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": '"', "withHeader": True, "separator": ","}, connection_type="s3", format="csv", connection_options={"paths": ["s3://airscholarreddit/raw/reddit_20240619.csv"], "recurse": True}, transformation_ctx="AmazonS3_node1718954137770")

df = AmazonS3_node1718954137770.toDF()

df_combined = df.withColumn("ESS_update", concat_ws(df["edited"], df["spoiler"], df["stickied"]))
df_combined = df.drop("edited", "spoiler", "stickied")

S3_bucket_node_combined = DynamicFrame.fromDF(df_combined, glueContext, "S3_bucket_node_combined")


# Script generated for node Amazon S3
AmazonS3_node1718954826742 = glueContext.write_dynamic_frame.from_options(frame=S3_bucket_node_combined, connection_type="s3", format="csv", connection_options={"path": "s3://airscholarreddit/transformed/", "partitionKeys": []}, transformation_ctx="AmazonS3_node1718954826742")

job.commit()