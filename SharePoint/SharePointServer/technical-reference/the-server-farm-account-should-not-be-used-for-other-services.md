---
title: "The server farm account should not be used for other services (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/31/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 57592cbe-47c1-44c7-8f57-38fa192df4f7
description: "Learn how to resolve the SharePoint Health Analyzer rule: The server farm account should not be used for the other services, for SharePoint Server."
---

# The server farm account should not be used for other services (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** The server farm account should not be used for the other services. 
  
 **Summary:** The account that is used to run the SharePoint Server Timer service and other system services in the SharePoint farm should not be used for other services in the farm. 
  
 **Cause:** The farm account, which is used for the SharePoint Server Timer service and the SharePoint Central Administration website, is highly privileged and should not be used for other services on any computers in the server farm. Services in the farm were found to use this account. 
  
> [!NOTE]
> You can ignore this event if using the User Profile Synchronization service. The User Profile Synchronization service must run as the farm account in SharePoint Server. 
  
 **Resolution: Change the account that is used for other services.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. In Central Administration , in the **Security** section, click **Configure service accounts**.
    
3. On the Service Accounts page, in the **Credential Management** section, in the drop-down list, click the service that you want to update credentials. 
    
4. In the **Select an account for this component** list, click the domain account that you want to associate with this service. 
    
5. If you want to register the account that you selected on the SharePoint Server farm, click **Register new managed account**.
    
6. Click **OK**.
    
For more information, see [Account permissions and security settings in SharePoint Server 2016](../install/account-permissions-and-security-settings-in-sharepoint-server-2016.md) and [Account permissions and security settings in SharePoint 2013](../install/account-permissions-and-security-settings-in-sharepoint-2013.md).
  

