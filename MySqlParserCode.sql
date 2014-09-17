Drop table metaStatus;

CREATE TABLE metaStatus  ( 
tkey  integer, 
ipAddr   character varying(30) NOT NULL, 
healthtime timestamp, 
numConnections integer, 
policyStatus integer, 
activityFlag integer,
CONSTRAINT metaStatus_pk PRIMARY KEY (tkey));


LOAD DATA infile 'D:/metaDB-csv-3-7/metaStatus-3-7.csv'
INTO table metastatus
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS

