---
title: "Verify that OAuth is configured correctly for the Machine Translation Service application (SharePoint Server)"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 8/31/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 335af336-da96-4b50-9901-4c4ef151c790
description: "Learn how to resolve the SharePoint Health Analyzer rule: Verify that OAuth is configured correctly for the Machine Translation Service application, for SharePoint Server."
---

# Verify that OAuth is configured correctly for the Machine Translation Service application (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)] 
  
 **Rule Name:** Verify that OAuth is configured correctly for the Machine Translation Service application. 
  
 **Summary:** The Machine Translation Service application that is provisioned on the farm can function correctly only when OAuth is correctly configured. 
  
 **Cause:** OAuth isn't configured correctly for the Machine Translation Service application. 
  
 **Resolution: Ensure that a default User Profile Service Application proxy exists in the default farm service application proxy group.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, click **Application Management**.
    
3. On the Application Management page, in the **Service Applications** section, click **Configure service application associations**.
    
4. In the **Application Proxy Group** column, click the proxy group for the Web application or service application that you want to configure. Usually it is the **default** Application Proxy Group. 
    
5. Select the **User Profile Service Application Proxy** check box. 
    

