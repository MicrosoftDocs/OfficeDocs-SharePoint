---
title: Update Workflow in SharePoint Server 2013
ms.prod: SHAREPOINT
ms.assetid: de173e89-b6d8-4d9e-8516-865c2735bfff
---


# Update Workflow in SharePoint Server 2013
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013*  * **Topic Last Modified:** 2017-07-24* **Summary:** Walks through the steps required to keep workflow up to date in SharePoint Server 2013.
## Run cmdlets after software updates are installed

It is important that any Cumulative Updates (CU) for SharePoint Server 2013 and Workflow Manager are installed in a coordinated fashion. After an update has been performed, several Microsoft PowerShell cmdlets must be run in order to maintain the connection between the SharePoint Server 2013 farm and the Workflow Manager farm.Run the following PowerShell cmdlets as an administrator from the SharePoint Administration Shell after the updates have been installed for SharePoint Server 2013, Workflow Manager, and Workflow Manager Client.
> [!IMPORTANT:]

  
    
    




```

$credential = [System.Net.CredentialCache]::DefaultNetworkCredentials
$site = Get-SPSite(<siteUri>)
$proxy = Get-SPWorkflowServiceApplicationProxy
$svcAddress = $proxy.GetWorkflowServiceAddress($site)
Copy-SPActivitiesToWorkflowService -WorkflowServiceAddress $svcAddress -Credential $credential -Force $true

```


> [!NOTE:]

  
    
    


## Troubleshooting steps for workflow updates


- Make sure all components are on the latest patch level. This includes SharePoint Server 2013, Workflow Manager, and Workflow Manager Client.
    
  
- Verify the $proxy connection settings using the following commands:
    
  ```
  
$proxy = Get-SPWorkflowServiceApplicationProxy
$site = Get-SPSite(<siteUri>)
$proxy.GetWorkflowServiceAddress($site)
  ```

- Inspect any errors displayed in the SharePoint Designer user interface or any errors shown in the SharePoint Workflow Status user interface.
    
  

