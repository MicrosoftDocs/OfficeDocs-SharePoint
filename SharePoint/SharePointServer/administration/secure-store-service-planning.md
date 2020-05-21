---
title: "Plan the Secure Store Service in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/7/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: e1196de0-1eb9-4c50-aeca-93e0eba7be0d
description: "Plan to store authorization credentials in an encrypted database by using the Secure Store Service in SharePoint Server."
---

# Plan the Secure Store Service in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
The Secure Store Service is a claims-aware authorization service that includes an encrypted database for storing credentials.
    
## About the Secure Store Service
<a name="AboutTheSecureStoreService"> </a>

The Secure Store Service is an authorization service that runs on SharePoint Server. The Secure Store Service provides a database that is used to store credentials. These credentials usually consist of a user identity and password, but can also contain other fields that you define. For example, SharePoint Server can use the Secure Store database to store and retrieve credentials for access to external data sources. The Secure Store Service provides support for storing multiple sets of credentials for multiple back-end systems.
  
Usage scenarios for Secure Store include the following:
  
- **Excel Online in Office Online Server** can use Secure Store to provide access to external data sources in workbooks published in SharePoint Server 2016. This can be used as a substitute to passing a user's credentials to the data source, a process which often requires configuring Kerberos constrained delegation. 
    
- **Excel Services in SharePoint Server 2013** can use Secure Store to provide access to external data sources in published workbooks. This can be used as a substitute to passing a user's credentials to the data source, a process which often requires configuring Kerberos delegation. Excel Services requires Secure Store if you want to configure an unattended service account for data authentication. 
    
- **Visio Services** can use Secure Store to provide access to external data sources in published data-connected diagrams. This can be used as a substitute to passing a user's credentials to the data source, a process which often requires configuring Kerberos constrained delegation. Visio Services requires Secure Store if you want to configure an unattended service account for data authentication. 
    
- **PerformancePoint Services** can use Secure Store to provide access to external data sources. PerformancePoint Services requires Secure Store if you want to configure an unattended service account for data authentication. 
    
- **Power Pivot** requires Secure Store for scheduled refresh of PowerPivot workbooks. 
    
- **Microsoft Business Connectivity Services** can use Secure Store to map the user's credentials to a set of credentials for an external system. You can either map each user's credentials to a unique account on the external system or you can map a set of authenticated users to a single group account. Business Connectivity Services can also use Secure Store to store certificates for accessing an on-premises data source from SharePoint. 
    
- **SharePoint runtime** can use Secure Store to store credentials necessary to communicate with Azure services, if any of the user apps require SharePoint runtime to provision and use Azure Services. 
    
## Secure store service preparation
<a name="SecureStoreServicePreparation"> </a>

When you prepare to deploy the Secure Store Service, be aware of the following important guidelines:
  
- Before you generate a new encryption key, back up the Secure Store database. You should also back up the Secure Store database after it is initially created, and again each time credentials are reencrypted. When a new key is generated, the credentials can be re-encrypted with the new key. If the key refresh fails, or the passphrase is forgotten, the credentials will not be useable.
    
- Back up the encryption key after initially setting up Secure Store, and back up the key again each time it is regenerated.
    
- Do not store the backup media for the encryption key in the same location as the backup media for the secure store database. If a user obtains a copy of both the database and the key, the credentials stored in the database could be compromised.
    
Because Secure Store is used to store sensitive information, for better security we recommend that you consider the following guidelines:
  
- Run the Secure Store Service in a separate application pool that is not used for any other service.
    
- Create the Secure Store database on a separate server running SQL Server. Do not use the same SQL Server instance that contains content databases.
    
## Target applications in Secure Store
<a name="TargetApplications"> </a>

A target application is a collection of information that maps a user or users to a set of encrypted credentials stored in the Secure Store database. Target applications contain the following information that you define: 
  
- Whether this is an individual or group mapping. 
    
- What fields to store in the Secure Store database. (The default is Windows User Name and Windows Password, but additional field types can be selected, depending on the application.)
    
- Users with permissions to administer the target application.
    
- The individual or group to whom you are mapping the credentials.
    
Each target application has a unique application ID that you define that is used to reference the target application from external applications such as Excel Online or SharePoint Designer. 
  
## Secure store credential mappings
<a name="SecureStoreServiceMappings"> </a>

The Secure Store Service supports individual mappings and group mappings. In a group mapping, every user who is a member of a specific domain group is mapped to the same set of credentials. In an individual mapping, each individual user is mapped to a unique set of credentials. Individual mappings are useful if you need logging information about individual user access to shared resources. For group mappings, a security layer maps credentials for multiple domain users against a single set of credentials that are stored in the secure store database. Group mappings are easier to maintain than individual mappings, and can provide improved performance.
  
## Secure store service and claims authentication
<a name="ClaimsAuthentication"> </a>

The Secure Store Service is a claims-aware service. It can accept security tokens and decrypt them to get the application ID, and then perform a lookup. When a SharePoint Server Security Token Service (STS) issues a security token in response to an authentication request, the Secure Store Service decrypts the token and reads the application ID value. The Secure Store Service uses the application ID to retrieve credentials from the secure store database. The credentials are then used to authorize access to resources.
  
## See also
<a name="ClaimsAuthentication"> </a>

#### Other Resources

[Configure the Secure Store Service in SharePoint Server](/SharePoint/administration/configure-the-secure-store-service)

