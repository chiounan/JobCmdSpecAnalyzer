'''
Created on 2013/2/4

@author: chiounan
'''
import PM_JobAgent_BackupCreate
import PM_JobWorker_BackupCreate
import Data_ClientDisk
import PM_JobAgent_BackupUpdate
import PM_JobAgent_BackupDelete
import PM_JobAgent_BackupSnapshot


client_num = len(PM_JobWorker_BackupCreate.clientsAttributes)
#client_disk_num = len(Data_ClientDisk.disksAttributes)
#sourcedisk_num = len(PM_JobWorker_BackupCreate.sourcedisk_id)
#print (sourcedisk_num)
#print ('Wrk: client id: %s' % PM_JobWorker_BackupCreate.client_id)
#print ('Agt: client id: %s' % PM_JobAgent_BackupCreate.client_id)
#print ('Wrk: client name: %s' % PM_JobWorker_BackupCreate.client_name)
#print ('Data_ClientDisk: disk id: %s' % Data_ClientDisk.disk_id)

def compare_array(array_i, array_j):
    found_array = []
    num_i = len(array_i)
    num_j = len(array_j)
    for i in range(num_i):
        for j in range(num_j):
            if array_i[i] == array_j[j]:
                found_array.append(array_i[i])
    return found_array

# The same function with compare_array, but not work for compare dictionary
def compare_sets(set1, set2):
    return set(set1) & set(set2)

def compare_dicts(dict1, dict2):
    diffdict = {}
    for keys in dict1:
        if dict1[keys] != dict2[keys]:
            diffdict[keys] = dict1[keys] + ' -> ' + dict2[keys]
    return diffdict

#for i in range(client_num):
#    client_id = PM_JobWorker_BackupCreate.clientsAttributes[i]['id']
#    if PM_JobAgent_BackupCreate.clientId == client_id:
#        print ('client id: %s found' % client_id)

client_id_found_array = compare_array(PM_JobAgent_BackupCreate.client_id, PM_JobWorker_BackupCreate.client_id)
#print ('Client id found: %s' % client_id_found_array)

##print (PM_JobWorker_BackupCreate.sourcedisk_id)
#for i in range(client_disk_num):
#    for j in range(sourcedisk_num):
#        disk_id = PM_JobWorker_BackupCreate.sourcedisk_id[j]
#        if Data_ClientDisk.disk_id[i] == disk_id:
#            print ('disk id: %s found' % disk_id)        
## better way is use comapre_loop
## compare disk id between Data_ClientDisk and PM_JobWorker_BackupCreate
disk_id_found_array = compare_array(Data_ClientDisk.disk_id, PM_JobWorker_BackupCreate.sourcedisk_id)
#print ('Found disk id: %s' % disk_id_found_array)

client_id_found_set = compare_sets(Data_ClientDisk.client_id, PM_JobWorker_BackupCreate.client_id)
#print ('Client id found: %s' % client_id_found_set)

disk_id_found_set = compare_sets(Data_ClientDisk.disk_id, PM_JobWorker_BackupCreate.sourcedisk_id)
#print ('Found disk id: %s' % disk_id_found_set)

#job_attribute_found_set = compare_sets(PM_JobWorker_BackupCreate.jobAttributes, PM_JobAgent_BackupCreate.jobAttributes)
#print ('Found job attribute: %s' % job_attribute_found_set) 
    
def compare_job_attributes(spec1, spec2):
    job_attribute_diff_dict = compare_dicts(spec1.jobAttributes, spec2.jobAttributes)
    if job_attribute_diff_dict:
        print ('job attribute is different, key : value1 -> value2: %s' % job_attribute_diff_dict)
    else:
        print ('job attribute is the same')

def compare_client_attributes(spec1, spec2):
    client_attribute_diff_dict = compare_dicts(spec1.clientAttributes, spec1.clientAttributes)
    if client_attribute_diff_dict:
        print ('client attribute is different, key : value1 -> value2: %s' % client_attribute_diff_dict)
    else:
        print ('client attribute is the same')

def compare_option_attributes(spec1, spec2):
    option_attribute_diff_dict = compare_dicts(spec1.optionAttributes, spec1.optionAttributes)
    if option_attribute_diff_dict:
        print ('option attribute is different, key : value1 -> value2: %s' % option_attribute_diff_dict)
    else:
        print ('option attribute is the same')
        
def find_sourcedisk_id(spec1, spec2):
    foundarray = compare_sets(spec1, spec2)
    if foundarray:
        print ('disk id found: %s' % foundarray)
    else:
        print ('!!! ERROR: disk id not exist !!!')