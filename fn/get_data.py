import os
import time
import pandas as pd
from datetime import datetime
from google.cloud import bigquery
from fn import sql_query as qr

class DailyData:
    def __init__(self):
        self.today = datetime.today().strftime('%Y-%m-%d')
        self.ts = time.time()
    
    def bigquery_query(self, sql_query):
        self.bigquery_client = bigquery.Client()
        self.bigquery_job = self.bigquery_client.query(sql_query)
        self.bigquery_result = self.bigquery_job.result()
        self.bigquery_dataframe = self.bigquery_result.to_dataframe
        return self.bigquery_dataframe

    def main(self):
        self.sql_query = qr.sql_query()
        self.dataframe = self.bigquery_query(self.sql_query)
        return self.dataframe
