---
title: "Accounts used by application pools or service identities are in the local machine Administrators group (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/22/2018
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 5f0f9910-d851-4ffa-832b-f47558e4758c
description: "Learn how to resolve the SharePoint Health Analyzer rule: Accounts used by application pools or service identities are in the local machine Administrators group, for SharePoint Server."
---

# Accounts used by application pools or service identities are in the local machine Administrators group (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
 **Rule Name:** Accounts used by application pools or service identities are in the local machine Administrators group. 
  
 **Summary:** A user account that is used by application pools or services must have permissions of a domain user account and must not be a member of the Farm Administrators group or a member of the Administrators group on the local computer. Using highly privileged accounts for application pools or services poses a security risk to the farm, and could allow malicious code to execute. 
  
 **Cause:** Accounts that are used by application pools or services are members of the Administrators group on the local computer. 
  
 **Resolution: Change the user account to a predefined account, or to a domain user account that is not a member of the Administrators group.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the Central Administration home page, in the **Security** section, click **Configure service accounts**.
    
3. On the Service Accounts page, in the **Select the component to update** list, click the application pool or service that uses the credentials of a member of the Administrators group on the local computer as its security account. 
    
4. In the **Select an account** list, click an appropriate account for this component — for example, the predefined account **Network Service** — or click **Register new managed account**, and then on the Register Managed Account page, specify the credentials and the password change settings that you want.
    
5. Click **OK**.
    
For more information, see [Account permissions and security settings in SharePoint Server 2016](../install/account-permissions-and-security-settings-in-sharepoint-server-2016.md).
  
## See also

#### Concepts

[Plan for administrative and service accounts in SharePoint Server](../security-for-sharepoint-server/plan-for-administrative-and-service-accounts.md)
  
[Plan for least-privileged administration in SharePoint Server](../security-for-sharepoint-server/plan-for-least-privileged-administration.md)

