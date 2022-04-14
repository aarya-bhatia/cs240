## CS240 Lecture 3/24/22: Data Storage

## In-process memory

//todo

## File Storage

Why?

Pros
1. Files exist beyond the time frame of a process 
2. Shareable between users and processes
3. Storage is now limited to local storage space ~ TiB

Cons
1. File access is slower than RAM
2. Only available on a local system
3. Harder to program 

How?
1. Programming language libraries 
2. Utilise the OS File System


## Object Storage (Cloud object storage)

Why?

1. Access any data from anywhere with cloud access
2. Greater access control
3. Exists on both public and private clouds

How?

1. Access: REST API - via HTTP Requests


## Key Value Store

Why?

1. A common access of data in programs is to look up a single value.
2. String ~> Data
3. Cloud-based in-memory 
4. Fast, Efficient

How?

1. REDIS: In-memory Key-Value store - HTTP API

## Document Data Storage

Why?

1. Allows storage of JSON/JSON-like objects
2. Search queries are key/values inside each JSON

```{}
{ 'user': 'waf', 'name': 'wade', 'rewardPts': 20 }
{ 'user': 'user2', 'name': 'user 2', 'rewardPts': 30 }
```

* No-SQL Database

How?

1. MongoDB

## Relational Data Store (Database)

Why?

1. Strict organization of data in a pre-defined schema
2. SQL Queries

How?

1. MySQL - Most common open source db
2. Postgresql
3. Mariodb

## Specialised data stores

* Ex. Neo4j -> Graph data store
  * Graphs, GIS/Location, BioMed/DNA
* Sometimes you need an optimized data structure
