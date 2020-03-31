---
title: "Accounts needed for hybrid configuration and testing"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/20/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- M365-collaboration
- SPO_Content
ms.assetid: c824fa0f-bae9-4791-92ee-38d8e70140ec
description: "Learn about the accounts you need to use when you configure a SharePoint Server hybrid solution."
---

# Accounts needed for hybrid configuration and testing

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]
  
When you configure a SharePoint Server hybrid environment, you need several user accounts in both your on-premises Active Directory and Office 365. These accounts also need different permissions and group or role memberships. Some of these accounts are used to deploy and configure software, and some are used to test specific functionality to help ensure that security and authentication systems are working as expected.
  
In a hybrid environment, some or all user accounts in Active Directory are synchronized with Azure AD directory services. We refer to these accounts as federated users. SharePoint Server and SharePoint Online are configured with a server-to-server (S2S) trust relationship, and service applications can be configured to enable federated users to access content and resources from both farms using a single identity. Because user accounts and credentials are synchronized between SharePoint Server and SharePoint Online, list and library content security can be applied in both farms using the same set of users and groups.
  
> [!NOTE]
> This table does not include service accounts, which may have specific requirements for service applications and features in certain SharePoint Server hybrid solutions. For more information about the requirements for each supported solution, see the solution configuration articles at [Configure a hybrid solution for SharePoint Server](configure-a-hybrid-solution.md). 
  
**Table: Accounts needed for SharePoint hybrid configuration and testing**

|**Account**|**Identity provider**|**Role**|
|:-----|:-----|:-----|
|Global Administrator  <br/> |Office 365 and Azure Active Directory  <br/> |Use an Office 365 work account that has been assigned to the Global Administrator role for Office 365 configuration tasks such as configuring SharePoint Online features, running Azure AD and SharePoint Online PowerShell commands, and testing SharePoint Online.  <br/> |
|AD Domain Administrator  <br/> |On-premises AD  <br/> |Use an AD account in the Domain Admins group to configure and test AD, ADFS, DNS, and certificates and to do other tasks that require elevation.  <br/> |
|SharePoint Farm Administrator  <br/> |On-premises AD  <br/> | Use an AD account in the Farm Administrators SharePoint group for SharePoint Server configuration tasks such as running PowerShell commands in the SharePoint Management Shell to configure S2S trusts, create and configure web applications and site collections, deploy and configure SQL Server databases, and troubleshoot SharePoint Server.  <br/>  This account must also have additional privileges to use the SharePoint Management Shell:  <br/>  Membership in the **securityadmin** fixed server role on the SQL Server instance.  <br/>  Membership in the **db_owner** fixed database role on all databases that are to be updated.  <br/>  Membership in the Administrators group on the server on which you are running the PowerShell cmdlets.  <br/> |
|Federated Users  <br/> |On-premises AD  <br/> |Use AD accounts that have been synchronized with Office 365 to test access to specific resources in both SharePoint Server and SharePoint Online.  <br/> These accounts, or groups of which they are members, must have permissions to SharePoint Server site collections and resources in both environments and have the appropriate product licenses assigned in the Microsoft 365 subscription. They also must be set to use the alternative domain UPN suffix that you specify for federated users during the planning process.  <br/> You can configure multiple federated accounts with different permissions or group memberships to test for appropriate security trimming and access to site resources.  <br/> |
   

