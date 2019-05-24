---
title: "SharePoint Online provided Azure containers and queues for SPO Migration API"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 7/18/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
ms.custom: 
ms.assetid: 742b5502-08e8-47f8-83c4-afb521725cb2

---

# SharePoint Online provided Azure containers and queues for SPO Migration API

## Overview

One of the requirements for using the SharePoint Online Migration API is the use of an Azure container for temporary storage. The cost of an Azure container is now free; the free default Azure container is now part of the basic SharePoint online offering. Every tenant who signs up for SharePoint Online will get this for free.
  
Important key aspects include:
  
- The containers and queues are unique per request and not reused. Once a container is given to a customer this container will not be reused or shared.
    
- The containers and queue are automatically deleted. As per the standard SharePoint Online Compliance, Microsoft will automatically destroy the container within 30 to 90 days .
    
- The containers and queues are in the customer's datacenter location. We make sure to provision containers that are in the same physical location as their SharePoint online tenant.
    
- The containers and queues can be obtained programmatically through SharePoint Online.
    
## Encryption process

Before the Migration API can accept a migration job from a SPO provided Azure container, the data must be encrypted at rest using the AES CBC 256 standard.
  
> [!NOTE]
> You can still provide your own Azure account if you prefer to not use encryption. 
  
No one has direct access to the storage accounts or the containers. The SPO service has access to the storage accounts; and while a select number of engineers can run maintenance commands against them, they also don't have direct access to the accounts. Datacenter technicians are not prepped with knowledge of how data is laid out on disk, and do not have ready access to equipment to mount disks. All drives are physically destroyed before leaving the datacenter. Physical security is also in place across all of our datacenters.
  
Each container is dedicated to the customer who it was provided to and not reused. The data is stored in the Azure blob anywhere from 30 to 90 days after which it is deleted.
  
When the data is deleted, the files are de-linked and later soft deleted from disk. A file in an account and on-disk are may be shared across many servers. The same process is used for replicas, including backup copies (geo-replicated data if it applies).
  
> [!NOTE]
> Due to data churn, it is likely that all or parts of the file will be overwritten at some point following soft delete. 
  
## Key to the container

The default key is generated programmatically, and is only valid for 3 days. This key is the only way to gain access to the container. It is generated randomly and not reused. The container itself lives longer than the key, as the container is purged using SPO standard methods between 30-90 days from creation. SPO never stores the key, though potentially they could find the container. The container is housed in a shared Microsoft storage, technically outside the tenant (but within the region), and is protected using the API key.
  
Only those who have the key have access. Other users in the subscription or the tenant do not have access.
  
If your key is lost or obtained by someone else, there are two defenses in place that protect you. First, the container has only read/write operations. The container has no list, which means you would need to know the details of the files stored in the container in order to read or write to them. Secondly, the files are encrypted at rest with AES 256 in CBC mode.
  
## How to use the container

### Getting containers

public SPProvisionedMigrationContainersInfo ProvisionMigrationContainers()

>[!NOTE]
> This call can be made in C# using the SharePoint client side object model. See, [Complete basic operations using SharePoint client library code](/sharepoint/dev/sp-add-ins/complete-basic-operations-using-sharepoint-client-library-code).
  
The call will return an object that contains two strings containing two SAS token for accessing the two required containers and a byte array for the AES256CBC encryption. This key must be used when encrypting the data. Once we give you the key it is forgotten by Microsoft. You need to keep it and pass it again for the SubmitMigrationJob call.
  
- Uri DataContainerUri
    
- Uri MetadataContainerUri
    
- byte[] EncryptionKey
    
### Getting a queue

public SPProvisionedMigrationQueueInfo ProvisionMigrationQueue()
  
This method will return a string containing the SAS token for accessing the Azure queue. The Queue can be reused across multiple migration jobs so this call should not be used as frequently as the SPProbisionnedMigrationContainersInfo() call.
  
- Uri JobQueueUri
    

