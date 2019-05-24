---
title: "Plan Excel Services Global Settings in SharePoint Server 2013"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/23/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 955084c9-91e1-4f66-9ec4-09d2816c5c6f
description: "Learn how to choose authorization (impersonation or process account) and encryption (IPsec or SSL) options for Excel Services in SharePoint Server."
---

# Plan Excel Services Global Settings in SharePoint Server 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
When you deploy Excel Services, you need to plan for the following Global Settings:
  
- [File access method for Excel Services](#FileAccessMethod)
    
- [Connection encryption for Excel Services](#ConnectionEncryption)
    
For information about configuring these settings, see [Manage Excel Services global settings (SharePoint Server 2013)](manage-excel-services-global-settings.md).
  
## File access method for Excel Services
<a name="FileAccessMethod"> </a>

In Excel Services Global Settings, there are two options for file access method: **Impersonation** or **Process account**.
  
The **Impersonation** option enables a thread to run in a security context other than the context of the process that owns the thread. Select **Impersonation** to require Excel Services to authorize users when they try to access workbooks that are stored in UNC and HTTP locations. Selecting this option does not affect workbooks that are stored in SharePoint Server 2013 databases. In most server farm deployments in which front-end web servers and Excel Services application servers run on different computers, impersonation requires constrained Kerberos delegation. 
  
The **Process Account** option specifies that the user account is not impersonated, and the process account is used when Excel Services opens workbooks from UNC shares or HTTP Web sites. 
  
## Connection encryption for Excel Services
<a name="ConnectionEncryption"> </a>

You can use Internet Protocol Security (IPsec) or Secure Sockets Layer (SSL) to encrypt data transmission among Excel Services application servers, data sources, client computers, and front-end web servers. By default, connection encryption is not required. If you choose to require connection encryption, the Excel Services application server will only enable data transmission between client computers and front-end web servers over SSL connections.
  
If you decide to require encrypted data transmission, you will have to manually configure IPsec or SSL. You can require encrypted connections between client computers and front-end web servers while enabling connections that are not encrypted between front-end web servers and Excel Services application servers.
  

