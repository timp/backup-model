A naive backup strategy is to keep each monthly backup for 12 months. 

After 14 months we have 12 backups: 

T-1, T-2, T-3, T-4, T-5, T-6, T-7, T-8, T-9. T-10, T-11, T-12


A quick skim of https://en.wikipedia.org/wiki/Backup_rotation_scheme does not really help. 

When thinking of backup lets try to enumerate the failure modes and what the action would be to fix it. 

* Whole data set dies
    - Restore from T-1
* Corruption of some data from now to T-1
    - Copy data back from T-1
* Corruption of data 3 months ago noticed now
   - Copy data from T-3

The important backup is T-1. The remainders are to remediate against undetected corruption in the past. 
We might wish to have a copy of the uncorrupted record from more than 12 months ago. 

Possibly we could do well with a Fibonacci sequence: 
```
T-1, T-2, T-3, T-5, T-8, T-13, T-21
```
Just 7 datasets kept, 5 less than the naive strategy but with a coverage back to nearly twice as long.

I tried to explore a model of stores, deletion and shifting, based upon an imagined set of shelves and physical snapshots. 
I got bogged down in the code, needed a doubly linked list and ran away. 

What we _actually_ need, in the AWS world, is to be able to set the expiriy date on the snapshot dataset at the time of its creation, given only the month number from the start. 

This is much easier to model, especially if we go away from Fibonacci and use powers of two. 

````
   if creationMonthNumber % 32  == 0 :
        return 32
    elif creationMonthNumber % 16  == 0 :
        return 16
    elif creationMonthNumber % 8  == 0 :
        return 8
    elif creationMonthNumber % 4  == 0 :
        return 4
    else :
      return 2
````      


Iterated for 256 months this results in the following datasets:

````
creation:224, age:32, expiry:32
creation:240, age:16, expiry:16
creation:248, age:8, expiry:8
creation:252, age:4, expiry:4
creation:254, age:2, expiry:2
creation:255, age:1, expiry:2
````
Only 6 data sets but an oldest set between 16 and 32 months old. 


