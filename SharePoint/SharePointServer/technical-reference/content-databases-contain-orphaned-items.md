---
title: "Content databases contain orphaned items (SharePoint Server)"
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
ms.assetid: 636d25e9-be42-4b66-a354-9b9af570f907
description: "Learn how to resolve the SharePoint Health Analyzer rule: Content databases contain orphaned items, for SharePoint Server."
---

# Content databases contain orphaned items (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
 **Rule Name:** Content databases contain orphaned items. 
  
 **Summary:** The SharePoint Health Analyzer has detected some sites in a content databases that are not referenced in the configuration database. These sites may not be accessible. 
  
 **Cause:** A restore operation that was not completed can result in sites in a content database that are not referenced in the SharePoint configuration database. 
  
 **Resolution: Decrease the number of days to store log files**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, click **Monitoring**, in the **Health Analyzer** section, click **Review problems and solutions**.
    
3. On the Review problems and solutions page, click the alert for the failing rule, and then click **Fix Now**. Keep the dialog box open so you can run the rule again to confirm the resolution.
    
    > [!NOTE]
    > The Fix Now feature removes all orphans from the content database. 
  
4. After following the steps in the **Remedy** section, in the **Review problems and solutions** dialog box for the alert, click **Re-analyze Now** to confirm the resolution. If the problem is resolved, the rule is not flagged as a failing rule on the Review problems and solutions page. 
    

