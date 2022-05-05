---
title: "The Security Token Service is not available (SharePoint Server)"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 8/30/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: fb4e9a7d-1ad2-4a89-ad90-85d61b44f56d
description: "Learn how to resolve the SharePoint Health Analyzer rule: The Security Token Service is not available, for SharePoint Server."
---

# The Security Token Service is not available (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]
  
 **Rule Name:** The Security Token Service is not available. 
  
 **Summary:** The Security Token Service is not issuing tokens. 
  
 **Cause:** The service could be malfunctioning or in a bad state, some assemblies are missing when you deploy the custom claims provider, or the STS certificate has expired. 
 
  **Resolution: Restart the Security Token Service application pool.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. Identify the server on which this event occurs. On the SharePoint Central Administration website, in the **Monitoring** section, click **Review problems and solutions**, and then find the name of the server in the **Failing Servers** column. If there are multiple failing servers in a server farm, you must repeat the following steps on each failing server. 
    
3. Verify that the user account that is performing the following steps is a member of the Administrators group on the local computer that you identified in the previous step.
    
4. Log on to the server on which this event occurs.
    
5. Open **Server Manager**, click **Tools**, and then click **Internet Information Services (IIS) Manager**.
    
6. In the Internet Information Services management console, in the **Connections** pane, expand the tree view, and then click **Application Pools**.
    
7. In the **Application Pools** list, right-click **SecurityTokenServiceApplicationPool**, and then click **Start**. If the application pool is started already, click **Stop** and then, in the **Action** pane, click **Start** to restart it. 
    
**Resolution: Install the missing assemblies into the global assembly cache (GAC) manually.**
  
1. Check the event logs and ULS logs on all servers to find out which assemblies of the custom claims provider are missing.
    
2. Install the missing assemblies into the global assembly cache manually. For more information, see [How to: Install an Assembly into the Global Assembly Cache](/dotnet/framework/app-domains/install-assembly-into-gac).

**Resolution: Replace the STS certificate.**

1. Check in the Application Event Log for the Event ID 8311 to confirm that the STS certificate is expired.

2. Replace the STS certificate. For more information, see [Replace the STS certificate for SharePoint Server](../administration/replace-the-sts-certificate.md).
    
**Resolution: Update the STS certificate**

 Confirm whether the STS certificate has expired by looking for Windows Application event log Event ID 8311 for source "SharePoint Foundation", category Topology, and with "NotTimeValid" in the message. This indicates an expired STS certificate. For more information on updating the STS certificate, please see [Replace the STS certificate for SharePoint Server](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint/blob/live/SharePoint/SharePointServer/administration/replace-the-sts-certificate.md).