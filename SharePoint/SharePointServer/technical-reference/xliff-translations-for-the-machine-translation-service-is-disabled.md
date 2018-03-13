---
title: "XLIFF translations for the Machine Translation Service is disabled (SharePoint Server)"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 12/5/2017
ms.audience: ITPro
ms.topic: troubleshooting
ms.prod: office-online-server
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: c145579b-fc8b-4ab4-bc80-95c3202deae2
description: "Summary: Learn how to resolve the SharePoint Health Analyzer ruleXLIFF translation for the Machine Translation Service is disabledin SharePoint Server 2016 and SharePoint Server 2013."
---

# XLIFF translations for the Machine Translation Service is disabled (SharePoint Server)

 **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "XLIFF translation for the Machine Translation Service is disabled" in SharePoint Server 2016 and SharePoint Server 2013. 
  
 **Rule Name:** XLIFF translation for the Machine Translation Service is disabled. 
  
 **Summary:** There are several features in SharePoint Server that rely on the Machine Translation Service processing the XLIFF file format. If the .xlf extension is disabled, these features don't function correctly. 
  
 **Cause:** The .xlf file name extension is disabled for the Machine Translation Service. 
  
 **Resolution: Enable the .xlf file name extension for the Machine Translation Service.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Service Applications page, in the list of service applications, click **Machine Translation Service**.
    
4. In the **Enabled File Extensions** section, select the check box for the .xlf file name extension under the **XLIFF Parser**.
    
5. Click **OK**.
    

