---
title: "Update Workflow in SharePoint Server 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/3/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 6bd28a0d-ae1d-4330-bc69-31841ea98b37
description: "Walks through the steps required to keep workflow up to date in SharePoint Server 2013."
---

# Update Workflow in SharePoint Server 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
## Run cmdlets after software updates are installed

It is important that any Cumulative Updates (CU) for SharePoint Server 2013 and Workflow Manager are installed in a coordinated fashion. After an update has been performed, several Microsoft PowerShell cmdlets must be run in order to maintain the connection between the SharePoint Server 2013 farm and the Workflow Manager farm.
  
Run the following PowerShell cmdlets as an administrator from the SharePoint Management Shell after the updates have been installed for SharePoint Server 2013, Workflow Manager, and Workflow Manager Client.
  
> [!IMPORTANT]
> The latest update level must be installed on SharePoint Server 2013, Workflow Manager, and Workflow Manager Client before you run the update cmdlets. 
  
```
$credential = [System.Net.CredentialCache]::DefaultNetworkCredentials
$site = Get-SPSite(<siteUri>)
$proxy = Get-SPWorkflowServiceApplicationProxy
$svcAddress = $proxy.GetWorkflowServiceAddress($site)
Copy-SPActivitiesToWorkflowService -WorkflowServiceAddress $svcAddress -Credential $credential -Force $true

```

> [!NOTE]
> Because workflow supports environments with multiple Site Subscriptions, the  `$site` Site Collection address determines the proper configuration location for workflow settings. 
  
## Troubleshooting steps for workflow updates

- Make sure all components are on the latest patch level. This includes SharePoint Server 2013, Workflow Manager, and Workflow Manager Client.
    
- Verify the $proxy connection settings using the following commands:
    
  ```
  $proxy = Get-SPWorkflowServiceApplicationProxy
  $site = Get-SPSite(<siteUri>)
  $proxy.GetWorkflowServiceAddress($site)
  ```

- Inspect any errors displayed in the SharePoint Designer user interface or any errors shown in the SharePoint Workflow Status user interface.
    

