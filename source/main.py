'''
Created on 2013/2/23

@author: chiounan
'''
import Data_ClientDisk
import PM_JobWorker_BackupCreate
import PM_JobAgent_BackupCreate
import PM_JobAgent_BackupUpdate
import PM_JobAgent_BackupDelete
import PM_JobAgent_BackupSnapshot

from comparer import compare_job_attributes
from comparer import compare_client_attributes
from comparer import compare_option_attributes
from comparer import find_sourcedisk_id

usage = '''
Job Worker/Agent Command Spec Analyzer
This tool will help QA to analyze the correctness of Job Worker operation.
It compare the input and output XML files of Job Worker, and check some 
specific contents are correct:
Ex: session id, client id, server id, disk id,...  
 
Usage: 
1. put XML files in the "xmlfiles" folder:
    Data_ClientDisk.xml
    PM_JobWorker_BackupCreate.xml
    PM_JobAgent_BackupCreate.xml
    PM_JobAgent_BackupDelete.xml
    PM_JobAgent_BackupSnapshot.xml
    PM_JobAgent_BackupUpdate.xml

2. run "main.py" with python (Windows or Linux)    
'''    

print ('%s' % usage)
input ('Press Enter to continue...')

print ('')
print ('*** Check: job attributes ***')
print ('PM_JobWorker_BackupCreate -> PM_JobAgent_BackupCreate')
compare_job_attributes(PM_JobWorker_BackupCreate, PM_JobAgent_BackupCreate)    
print ('PM_JobWorker_BackupCreate -> PM_JobAgent_BackupUpdate')
compare_job_attributes(PM_JobWorker_BackupCreate, PM_JobAgent_BackupUpdate)    
print ('PM_JobWorker_BackupCreate -> PM_JobAgent_BackupDelete')
compare_job_attributes(PM_JobWorker_BackupCreate, PM_JobAgent_BackupDelete)    
print ('PM_JobWorker_BackupCreate -> PM_JobAgent_BackupSnapshot')
compare_job_attributes(PM_JobWorker_BackupCreate, PM_JobAgent_BackupSnapshot)    

print ('')
print ('*** Check client attributes ***')
print ('Data_ClientDisk -> PM_JobAgent_BackupCreate')
compare_client_attributes(Data_ClientDisk, PM_JobAgent_BackupCreate)
print ('Data_ClientDisk -> PM_JobAgent_BackupUpdate')
compare_client_attributes(Data_ClientDisk, PM_JobAgent_BackupUpdate)
print ('Data_ClientDisk -> PM_JobAgent_BackupDelete')
compare_client_attributes(Data_ClientDisk, PM_JobAgent_BackupDelete)
print ('Data_ClientDisk -> PM_JobAgent_BackupSnapshot')
compare_client_attributes(Data_ClientDisk, PM_JobAgent_BackupSnapshot)

print ('')
print ('*** Check option attributes ***')
print ('PM_JobWorker_BackupCreate -> PM_JobAgent_BackupCreate')
compare_option_attributes(PM_JobWorker_BackupCreate, PM_JobAgent_BackupCreate)

print ('')
print ('*** Check disk id: find disk id which in JobWorker around JobAgent Command specs')
print ('PM_JobWorker_BackupCreate -> PM_JobAgent_BackupCreate')
find_sourcedisk_id(PM_JobWorker_BackupCreate.sourcedisk_id, PM_JobAgent_BackupCreate.disk_id)
print ('PM_JobWorker_BackupCreate -> PM_JobAgent_BackupUpdate')
find_sourcedisk_id(PM_JobWorker_BackupCreate.sourcedisk_id, PM_JobAgent_BackupUpdate.disk_id)
print ('PM_JobWorker_BackupCreate -> PM_JobAgent_BackupDelete')
find_sourcedisk_id(PM_JobWorker_BackupCreate.sourcedisk_id, PM_JobAgent_BackupDelete.disk_id)
print ('PM_JobWorker_BackupCreate -> PM_JobAgent_BackupSnapshot')
find_sourcedisk_id(PM_JobWorker_BackupCreate.sourcedisk_id, PM_JobAgent_BackupSnapshot.disk_id)
print ('PM_JobWorker_BackupCreate -> Data_ClientDisk')
find_sourcedisk_id(PM_JobWorker_BackupCreate.sourcedisk_id, Data_ClientDisk.disk_id)
