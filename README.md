# hive-cdc-orcfile
Keep in sync RDB table with Hive structured store. Added Kafka as a buffer between those two tables.


#### Purpose 
The purpose of this project is to create a solution that gives you the ability to synchronize RDB (MySQL, Oracle, Postgres) tables with Hive equivalents.

#### Requirements
* RDB changes are sent over CDC logs
* Kafka buffer to keep CDC logs in small chunks
* Hive 2.3.2 with ACID support
* Spark 2.3
* OrcFile format

#### Diagram


#### Tests


#### Links
