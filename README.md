In PROD we keep each monthly backup for 12 months. 

After 14 months we have 12 backups: 

T-1, T-2, T-3, T-4, T-5, T-6, T-7, T-8, T-9. T-10, T-11, T-12


A quick skim of https://en.wikipedia.org/wiki/Backup_rotation_scheme does not really help. 

I find it easier to try to enumerate the failure modes and what the action would be to fix it. 

•	Whole data set dies
o	Restore from T-1
•	Corruption of some data from now to T-1
o	Copy data back from T-1
•	Corruption of data now-3 months noticed now
o	Copy data from T-3

The important backup is T-1. The remainders are to remediate against undetected corruption in the past. 
We might wish to have a copy of the uncorrupted record from more than 12 months ago. 

I think we could do well with a Fibonacci sequence: 
T-1, T-2, T-3, T-5, T-8, T-13, T-21



