'''
Created on 2013/2/4

@author: chiounan
'''
import PM_JobAgent_BackupCreate
import PM_JobWorker_BackupCreate


num = len(PM_JobWorker_BackupCreate.clientsAttributes)
print (num)
print ('Wrk: client id: %s' % PM_JobWorker_BackupCreate.client_id)
print ('Agt: client id: %s' % PM_JobAgent_BackupCreate.client_id)

for i in range(num):
    client_id = PM_JobWorker_BackupCreate.clientsAttributes[i]['id']
    if PM_JobAgent_BackupCreate.clientId == client_id:
        print ('%sth is found' % (i + 1))