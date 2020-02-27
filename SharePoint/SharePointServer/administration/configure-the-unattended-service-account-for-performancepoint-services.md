---
title: "Configure the unattended service account for PerformancePoint Services"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 411e0fa7-2a27-4883-93ac-a2fd228e40d8
description: "Learn how to configure the unattended service account for PerformancePoint Services."
---

# Configure the unattended service account for PerformancePoint Services

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
The unattended service account is an Active Directory account that is used for accessing PerformancePoint Services data sources. This account is used by PerformancePoint Services on behalf of authorized users to provide access to external data sources for the purposes of creating and using dashboards and other PerformancePoint Services content. To configure the unattended service account, see [Configure the unattended service account for PerformancePoint Services](#section1) in this article. 
  
> [!NOTE]
> The unattended service account is a universal account that provides equal data access to all authorized users. If you need more fine-grained data access, see [Configure Secure Store for use with PerformancePoint Services](configure-secure-store-for-use-with-performancepoint-services.md). 
  
PerformancePoint Services uses Secure Store Service to store the unattended service account password. Before using the Unattended Service Account, make sure that Secure Store has been configured. 
  
## Configure the unattended service account for PerformancePoint Services
<a name="section1"> </a>

Use the following procedure to configure the unattended service account for PerformancePoint Services.
  
 **To configure the unattended service account for PerformancePoint Services**
  
1. On the SharePoint Central Administration Web site, in the **Application Management** section, click **Manage Service Applications**, and then click the PerformancePoint Services service application.
    
2. On the Manage PerformancePoint Services page, click **PerformancePoint Service Application Settings**.
    
3. In the **Secure Store and Unattended Service Account** section, enter the user name and password for the account that you want to use as the unattended service account. 
    
4. Click **OK**.
    
You will see the Secure Store Service name and the user name that represents the unattended service account. 
  
Once the unattended service account has been configured, you must grant that account access to your data sources:
  
- For SQL Server data, the account must have a SQL logon with **db_datareader** permissions on each database that you want to access. 
    
- For SQL Server Analysis Services data, the account must have read access to the cube or an appropriate portion of the cube, depending on your needs.
    
- For Excel Services data, the account must have access to the Excel workbook in a SharePoint document library.
    
- For data in a SharePoint list, the account must have read access to the list.
    

