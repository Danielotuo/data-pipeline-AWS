# AWS Data Pipeline Project

Creating data pipelines on AWS with e-commerce data

# Introduction & Goals

This project leverages e-commerce data to extract valuable market insights through the establishment of efficient data pipelines, facilitating in-depth analysis within BI analytics tools. Notably, no preliminary data preparation is required for seamless implementation. The primary data source for this project is the UCI machine learning repository.

# Contents

- [The Data Set](#the-data-set)
- [Used Tools](#used-tools)
  - [Connect](#connect)
  - [Buffer](#buffer)
  - [Processing](#processing)
  - [Storage](#storage)
  - [Analytics](#analytics)
- [Pipelines](#pipelines)
  - [Stream Processing](#stream-processing)
- [Conclusion](#conclusion)

# The Data Set

InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country
536365,85123A,WHITE HANGING HEART T-LIGHT HOLDER,6,12/1/2010 8:26,2.55,17850,United Kingdom
536365,71053,WHITE METAL LANTERN,6,12/1/2010 8:26,3.39,17850,United Kingdom
536365,84406B,CREAM CUPID HEARTS COAT HANGER,8,12/1/2010 8:26,2.75,17850,United Kingdom

# Used Tools

### Connect

- API gateway: POST (to ingest data) & GET (to send query to DynamoDB) method

### Buffer

- AWS Kinesis(Data streams)

### Processing

- AWS lambda functions

### Storage

- S3: Store parquet data
- DynamoDB: Store data with two tables (Customer & Invoice tables)

### BI Analytics

- Jupyter notebook : Connect to S3
- Tableau: Connect to DynamoDB (Not added yet)

### Stream Processing Pipelines

- Continuous ingestion of raw CSV data is facilitated within the pipelines.
- Processed data can be securely stored in storage solutions like S3 and DynamoDB.
- The stored data interfaces with Business Analytics tools such as Tableau and Jupyter notebook.
- Customers have the capability to query transaction data in DynamoDB using an API and key parameters (InvoiceNO & Stockcode).

# Conclusion

The implemented data pipelines proficiently execute the ETL process, facilitating the extraction of valuable insights through comprehensive analysis. Moreover, seamless connectivity to BI analytics tools empowers efficient data visualization. Further updates including screenshots to enhance the project are in progress.
