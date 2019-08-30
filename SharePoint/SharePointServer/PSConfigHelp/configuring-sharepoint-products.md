---
title: "Configuring SharePoint Products"
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
ms.assetid: f8de05c1-ab18-4b73-b47e-0df1edd484cb
description: "Summary: Learn how to use the SharePoint Configuration Wizard to configure SharePoint Server."
---

# Configuring SharePoint Products

 **Summary:** Learn how to use the SharePoint Configuration Wizard to configure SharePoint Server. 
  
The SharePoint 2016 Products Configuration Wizard performs the following configuration tasks:
  
- Configures database access and creates configuration and administration content databases.
    
- Installs and configures features and services.
    
- Configures security.
    
> [!NOTE]
> The time that is taken to complete each configuration task varies. 
  
If the configuration wizard encounters an error while executing a configuration task, the wizard does not proceed to additional configuration tasks. The Configuration Complete page appears with a configuration failure message and a link to the log file that you can use to troubleshoot the issue that caused the failure.
  
If you cancel the configuration wizard, the configuration tasks that have completed are not undone; the remaining configuration tasks must be performed to complete the deployment of the server. To perform the remaining configuration tasks, you must run the configuration wizard again later.
  
## Updating a server farm

If you are updating a server farm, you must use the following process:
  
1. Run Setup, and then run the SharePoint 2016 Products Configuration Wizard on the server that is running the SharePoint Central Administration web site in your farm. 
    
2. When you see the message about running Setup on other servers in the farm, you must run Setup and the SharePoint 2016 Products Configuration Wizard on the other servers to get to the same point.
    
3. When all servers in the farm display the message, return to the first web server, and then click **OK** to continue the upgrade process for the first server. 
    
4. After the wizard has completed on the first server, you can configure each of the other servers.
    
## Security account requirements

To deploy SharePoint products in a server farm environment, you will need a user account that you can use to install the product and run the SharePoint 2016 Products Configuration Wizard. This account must be a unique domain user account that you can specify as the service account. This user account is used to access your configuration database. The database access account will be used for both initial database configuration, and ongoing connections from servers in this farm to the databases. 
  
> [!NOTE]
> Ensure that your domain does not have Group Policy that prohibits the account chosen as your database access account from running as a service. 
  
This account also acts as the application pool identity for the SharePoint Central Administration application pool and it is the account under which the SharePoint Timer service runs. We recommend that you follow the principle of least privilege and do not make this user account a member of any particular security group on your web servers or your database servers.
  

