# Automl

## Goals 
- Test automl ci/cd pipeline.
- Test retrain models on a frequent basis.

## References
- https://towardsdatascience.com/artificial-intelligence-made-easy-187ecb90c299
- http://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/h2o.html
- https://towardsdatascience.com/bookmark-this-if-you-are-new-to-python-especially-if-you-self-learn-python-54c6e7b5dad8
- http://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/frame.html
- Bigquery ML query sample: https://codelabs.developers.google.com/codelabs/bqml-intro/index.html?index=..%2F..index#3

`#standardSQL
CREATE OR REPLACE MODEL `bqml_codelab.sample_model` 
OPTIONS(model_type='logistic_reg') AS
SELECT
  IF(totals.transactions IS NULL, 0, 1) AS label,
  IFNULL(device.operatingSystem, "") AS os,
  device.isMobile AS is_mobile,
  IFNULL(geoNetwork.country, "") AS country,
  IFNULL(totals.pageviews, 0) AS pageviews
FROM
  `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20160801' AND '20170631'
LIMIT 100000;`

- Random Grid Search in h2o: http://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html#random-grid-search-parameters