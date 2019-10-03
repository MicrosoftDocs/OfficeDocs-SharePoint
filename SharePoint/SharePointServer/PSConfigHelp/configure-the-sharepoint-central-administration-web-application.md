---
title: "Configure the SharePoint Central Administration web application"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/1/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ROBOTS: NOINDEX
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 0328b2a3-9309-42f7-9f12-996ba95d67f7
description: "Summary: Learn how to configure the SharePoint Central Administration web application and security settings in SharePoint Server."
---

# Configure the SharePoint Central Administration web application

 **Summary:** Learn how to configure the SharePoint Central Administration web application and security settings in SharePoint Server. 
  
You can configure the SharePoint Central Administration web application and security settings.
  
## Port number

The SharePoint Central Administration web application enables you to manage the configuration settings for your SharePoint farm. The first server that you add to your server farm hosts this web site. If you need to specify a port number, you can use any number from 1 to 65535, although we recommend that you avoid a number from the range of well-known ports.
  
Port numbers fall into the following three ranges:
  
- Well-known ports are from 0 to 1023.
    
- Registered ports are from 1024 to 49151.
    
- Dynamic or private ports are from 49152 to 65535.
    
If you need to change the port number at a later time, you must run the SharePoint 2016 Products Configuration Wizard again. The configuration wizard will update the port number in the configuration database and create a job that will update the port number in each SharePoint Central Administration web application on other servers in this farm.
  
> [!NOTE]
> Manually changing the port number of the SharePoint Central Administration web application in Internet Information Services (IIS) Manager is not supported. Instead, you must run the configuration wizard again. 
  
## Security Settings

Both NTLM and Kerberos authentication protocols are supported.
  
### NTLM

The default setting, NTLM protocol, is based on a challenge-response mechanism for client authentication. NTLM is available in SharePoint products to communicate with systems that are able to use only NTLM authentication.
  
### Negotiate (Kerberos)

The Kerberos version 5 protocol is the primary security protocol for authentication within a domain. Kerberos authentication uses a service ticket system that verifies the identity of the user and of the network services. This dual verification is known as mutual authentication. The system attempts to negotiate authentication over the Kerberos protocol first. If it is not successful, the NTLM protocol is used.
  
To enable Kerberos authentication, you must perform additional configuration. For more information, see [Kerberos](https://go.microsoft.com/fwlink/?LinkID=197060).
  

