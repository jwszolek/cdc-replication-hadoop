# hive-cdc-orcfile
Keep in sync RDB table with Hive structured store. Added Kafka as a buffer between those two tables.


## Purpose 
The purpose of this project is to create a solution that gives you the ability to synchronize RDB (MySQL, Oracle, Postgres) tables with Hive equivalents. Synchronization process should be done by using CDC (change data capture) logs. By using this technique we should get almost real-time synchronization between source and destination table.

## Requirements
* RDB changes are sent over CDC logs
* Kafka buffer to keep CDC logs in small chunks
* Hive 2.3.2 with ACID support
* Spark 2.3
* OrcFile format

## Diagram

The diagram below shows the architecture concept. There are three main parts presented below:
* Relational database cluster, configured to generate CDC logs. 
* Logs are sent to the Kafka buffer 
* Spark streaming job lets to get raw data and push (in a structured way) to the Hive staging table
* Merge process is done in Hive. To make it work we need to use transaction support in hive

![cdc logs](img/cdc-logs.png)


#### Tests


#### Links
