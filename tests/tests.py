import unittest
from datetime import datetime

import praw

from  etls import  reddit_etl
from etls.reddit_etl import *
from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_api_conect(self):
        instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')

    def test_reddit_pipeline(self):
        file_postfix = datetime.now().strftime("%Y%m%d")
        file_name = f'reddit_{file_postfix}'
        subreddit = 'dataengineering'
        time_filter = 'day'
        limit = 100


        # connecting to reddit instance
        instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
        # extraction
        posts = extract_posts(instance, subreddit, time_filter, limit)
        post_df = pd.DataFrame(posts)
        # transformation
        post_df = transform_data(post_df)
        # loading to csv
        file_path = f'{OUTPUT_PATH}/{file_name}.csv'
        load_data_to_csv(post_df, file_path)

if __name__ == '__main__':
    unittest.main()
