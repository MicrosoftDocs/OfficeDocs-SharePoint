---
title: "XLIFF translations for the Machine Translation Service is disabled (SharePoint Server)"
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
ms.assetid: c145579b-fc8b-4ab4-bc80-95c3202deae2
description: "Learn how to resolve the SharePoint Health Analyzer rule: XLIFF translation for the Machine Translation Service is disabled, for SharePoint Server."
---

# XLIFF translations for the Machine Translation Service is disabled (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** XLIFF translation for the Machine Translation Service is disabled. 
  
 **Summary:** There are several features in SharePoint Server that rely on the Machine Translation Service processing the XLIFF file format. If the .xlf extension is disabled, these features don't function correctly. 
  
 **Cause:** The .xlf file name extension is disabled for the Machine Translation Service. 
  
 **Resolution: Enable the .xlf file name extension for the Machine Translation Service.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Service Applications page, in the list of service applications, click **Machine Translation Service**.
    
4. In the **Enabled File Extensions** section, select the check box for the .xlf file name extension under the **XLIFF Parser**.
    
5. Click **OK**.
    

