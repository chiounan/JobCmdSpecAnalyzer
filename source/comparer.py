'''
Created on 2013/2/4

@author: chiounan
'''
import PM_JobAgent_BackupCreate
import PM_JobWorker_BackupCreate
import Data_ClientDisk


client_num = len(PM_JobWorker_BackupCreate.clientsAttributes)
#client_disk_num = len(Data_ClientDisk.disksAttributes)
#sourcedisk_num = len(PM_JobWorker_BackupCreate.sourcedisk_id)
#print (sourcedisk_num)
#print ('Wrk: client id: %s' % PM_JobWorker_BackupCreate.client_id)
#print ('Agt: client id: %s' % PM_JobAgent_BackupCreate.client_id)
#print ('Wrk: client name: %s' % PM_JobWorker_BackupCreate.client_name)
#print ('Data_ClientDisk: disk id: %s' % Data_ClientDisk.disk_id)

def compare_loop(array_i, array_j):
    found_array = []
    num_i = len(array_i)
    num_j = len(array_j)
    for i in range(num_i):
        for j in range(num_j):
            if array_i[i] == array_j[j]:
                found_array.append(array_i[i])
    return found_array
                           
#for i in range(client_num):
#    client_id = PM_JobWorker_BackupCreate.clientsAttributes[i]['id']
#    if PM_JobAgent_BackupCreate.clientId == client_id:
#        print ('client id: %s found' % client_id)

client_id_found_array = compare_loop(PM_JobAgent_BackupCreate.client_id, PM_JobWorker_BackupCreate.client_id)
print ('Client id found: %s' % client_id_found_array)

##print (PM_JobWorker_BackupCreate.sourcedisk_id)
#for i in range(client_disk_num):
#    for j in range(sourcedisk_num):
#        disk_id = PM_JobWorker_BackupCreate.sourcedisk_id[j]
#        if Data_ClientDisk.disk_id[i] == disk_id:
#            print ('disk id: %s found' % disk_id)        
## better way is use comapre_loop
## compare disk id between Data_ClientDisk and PM_JobWorker_BackupCreate
disk_id_found_array = compare_loop(Data_ClientDisk.disk_id, PM_JobWorker_BackupCreate.sourcedisk_id)
print ('Found disk id: %s' % disk_id_found_array) 