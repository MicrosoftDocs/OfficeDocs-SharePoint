---
title: "Databases used by SharePoint have outdated index statistics (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 12/5/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 25970085-39e6-4b1f-83c7-8687a5f8e939
description: "Learn how to resolve the SharePoint Health Analyzer rule: Databases used by SharePoint have outdated index statistics, for SharePoint Server."
---

# Databases used by SharePoint have outdated index statistics (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Databases used by SharePoint have outdated index statistics. 
  
 **Summary:** Outdated index statistics can decrease query performance and cause SharePoint Server 2016 and SharePoint 2013 to respond slowly. 
  
 **Cause:** Index statistics in SharePoint Server databases are out of date. 
  
> [!NOTE]
> This SharePoint Health Analyzer rule is enabled daily by default. 
  
 **Resolution: Edit the rule definition so that the configuration is automatically repaired.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the Central Administration Home page, click **Monitoring**.
    
3. On the Monitoring page, in the **Health Analyzer** section, click **Review rule definitions**.
    
4. On the Health Analyzer Rule Definitions - All Rules page, in the **Category: Performance** section, click the name of the rule. 
    
5. In the **Health Analyzer Rule Definitions** dialog box, click **Edit Item**.
    
6. Select the **Repair Automatically** check box, and then click **Save**.
    
## See also

#### Other Resources

[Index Statistics](http://go.microsoft.com/fwlink/?LinkID=761157&amp;clcid=0x409)

