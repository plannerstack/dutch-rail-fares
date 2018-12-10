Export railfares
================

Creating a mapping.csv from stopplaces and uic codes in the format

```
placeref,uic
NL:S:ht,8400319
```

Obtain the latest NS tariefdata from http://data.ndovloket.nl/tarieven/ns/

Extract the zip file (rename the tab file to tab.csv)

Create an SQLite3 database:

sqlite3 railfares.sqlite3
```sql
CREATE TABLE distances("tariefgebied" INTEGER,"startuic" TEXT,"enduic" TEXT,"startdate" TEXT,"enddate" TEXT,"first" TEXT,"second" TEXT,"onlysecond" TEXT);
.import tab.csv distances
.separator ','
.import mapping.csv mapping
delete from distances where startuic in (select startuic from distances except select uic from mapping) or startuic in (select enduic from distances except select uic from mapping);
delete from distances where enduic in (select startuic from distances except select uic from mapping) or enduic in (select enduic from distances except select uic from mapping);
.header on
.output /tmp/rail_matrix.csv
select b.placeref as startplaceref, c.placeref as endplaceref, first as distance, 'IFF:NS' as operatorref, 'NS:HRN' as fareref from distances as a left join mapping as b on (a.startuic = b.uic) left join mapping as c on (a.enduic = c.uic) where cast(strftime('%Y%m%d') as integer) >= startdate and (enddate is null or cast(strftime('%Y%m%d') as integer) <= enddate) order by startplaceref, endplaceref;
.quit
```

Copy /tmp/rail_matrix.csv to RID
psql -d ridprod
```sql
delete from fare.rail_matrix where operatorref = 'IFF:NS';
\copy fare.rail_matrix from '/tmp/rail_matrix.csv' csv header;
```

Export external
===============

Extract kilometernew.dat from http://data.ndovloket.nl/ns/ns-latest.zip

Define your routes in tarief.py
Run tarief.py > extra.csv

Copy the output to RID
psql -d ridprod
```sql
delete from fare.rail_matrix where operatorref IN ('IFF:BN', 'IFF:RNET');
\copy fare.rail_matrix from '/tmp/extra.csv' csv header;
```
