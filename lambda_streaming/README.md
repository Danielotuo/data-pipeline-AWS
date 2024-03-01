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
- Python3 in lambda functions

### Storage

- S3: Store parquet data
- DynamoDB: Store data with two tables (Customer & Invoice tables)

### BI Analytics

- Jupyter notebook : Connect to S3
- Tableau: Connect to DynamoDB (Not added yet)

### Stream Processing Pipelines

- Constantly pulling Raw data in CSV into the pipe lines
- Transformed data can be stored in the storage such as S3, redshift and DynamoDB
- The data in the storage can be connected to Business analytics tools such as Tableau, Athena and Jupyter notebook
- A customer can send a query to check transaction data in DynamoDB with API and primary key (InvoiceNO & Stockcode)

# Conclusion

The data pieplines established can carry out ETL process and enable to get insights through analysis. It is also possible to connect to BI analytics tools to visualize the data. I will make more updates to this project.
