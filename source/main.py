'''
Created on 2013/2/23

@author: chiounan
'''


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

import comparer