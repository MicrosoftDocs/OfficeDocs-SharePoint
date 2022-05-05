---
title: "Update Workflow in SharePoint Server"
ms.reviewer: 
ms.author: toresing
author: tomresing
manager: serdars
ms.date: 3/8/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.assetid: de173e89-b6d8-4d9e-8516-865c2735bfff
description: "Walks through the steps required to keep workflow up to date in SharePoint Server."
---

# Update Workflow in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]
  
## Run cmdlets after software updates are installed

It is important that any Cumulative Updates (CU) for SharePoint Server and Workflow Manager are installed in a coordinated fashion. After an update has been performed, several Microsoft PowerShell cmdlets must be run in order to maintain the connection between the SharePoint Server farm and the Workflow Manager farm.
  
Run the following PowerShell cmdlets as an administrator from the SharePoint Administration Shell after the updates have been installed for SharePoint Server, Workflow Manager, and Workflow Manager Client.
  
> [!IMPORTANT]
> The latest update level must be installed on SharePoint Server, Workflow Manager, and Workflow Manager Client before you run the update cmdlets. 
  
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

- Make sure all components are on the latest patch level. This includes SharePoint Server, Workflow Manager, and Workflow Manager Client.
    
- Verify the $proxy connection settings using the following commands:
    
  ```
  $proxy = Get-SPWorkflowServiceApplicationProxy
  $site = Get-SPSite(<siteUri>)
  $proxy.GetWorkflowServiceAddress($site)
  ```

- Inspect any errors displayed in the SharePoint Designer user interface or any errors shown in the SharePoint Workflow Status user interface.
    

