import os

def sql_query():
    sql_query = f"""
                SELECT
                date,
                country_region,
                SUM(deaths) AS death_sum
                FROM
                `{os.getenv('BIGQUERY_DATASET_SUMMARY')}`
                GROUP BY
                date,
                country_region
                ORDER BY
                date DESC, 
                death_sum DESC
                """
    return sql_query
