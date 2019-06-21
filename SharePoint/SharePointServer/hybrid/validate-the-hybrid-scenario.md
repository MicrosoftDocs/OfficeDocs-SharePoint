---
title: "Validate the Business Connectivity Services hybrid scenario"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/22/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- IT_SharePoint_Hybrid_Top
- M365-collaboration
ms.assetid: 48a1c449-7bf6-4f12-a5f3-1933caadf713
description: "How to validate the Business Connectivity Services (BCS) hybrid solution is working."
---

# Validate the Business Connectivity Services hybrid scenario

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]
  
Now that you have created an external list or deployed an app for SharePoint in SharePoint Online, you need to test the security you put in place. Every account that will be accessing and manipulating the external data must have three properties:
  
- It must have user or greater permissions to the SharePoint Online site and the external list or app for SharePoint.
    
- It must be a federated account.
    
- It must be a member of the on-premises global security group that you are using to control access to the OData service endpoint. For example, it must be a member of **ODataGroup**.
    
In this procedure, you will open the SharePoint Online site and the external list or app for SharePoint with four different accounts.
  
## 

 **To validate security on the BCS hybrid**
  
1. Identify or create one account for each of the account types listed in the following table.
    
|**Account**|**Expected outcome**|**Troubleshooting step**|
|:-----|:-----|:-----|
|**Account A** <br/>  Has site/list/app permissions.  <br/>  Is federated.  <br/>  Is a member of the on-premises global security group ( **ODataGroup**).  <br/> |External data displayed and editable.  <br/> |If the external data does not display or you cannot edit it, check the site permissions, your federation setup, and the membership of your on-premises global security group; for example, the **ODataGroup**.  <br/> |
|**Account B** <br/>  Does not have site/list/app permissions.  <br/>  Is federated.  <br/>  Is a member of the on-premises global security group ( **ODataGroup**).  <br/> |External data does not display.  <br/> |If the external data does display and you can edit it, check the site/list/app permissions.  <br/> |
|**Account C** <br/>  Has site/list/app permissions.  <br/>  Is not federated (is an Office 365 account only).  <br/>  Cannot be added to the on-premises global security group ( **ODataGroup**).  <br/> |External data does not display.  <br/> |If the external data does display and you can edit it, check your federation setup and membership of your on-premises global security group ( **Odata Group**).  <br/> |
|**Account D** <br/>  Has site/list/app permissions.  <br/>  Is federated.  <br/>  Is not a member of your on-premises global security group ( **ODataGroup**).  <br/> |External data does not display.  <br/> |If the external data does display and you can edit it, check the membership of your on-premises global security group ( **ODataGroup**) and the permissions that you set on the OData service endpoint that you configure in [Deploy a Business Connectivity Services hybrid solution in SharePoint](/sharepoint/hybrid/deploy-a-business-connectivity-services-hybrid-solution) <br/> |
   
2. Open (by using In-Private browsing if possible) the SharePoint Online site that contains the external list or app for SharePoint by using each of the accounts in turn. Be sure to completely log out and close your browser in between tests.
    
3. If you don't see the expected outcome, refer to the troubleshooting step in the previous table, fix the issue, and repeat all four tests until you achieve the expected outcome.
    
If you see the error message:
  
ResourceBudgetExceeded, sending throttled status code. Exception=Microsoft.SharePoint.SPResourceBudgetExceededException: ResourceBudgetExceeded at Microsoft.SharePoint.SPResourceTally.Check(Int32 value) at Microsoft.SharePoint.SPAggregateResourceTally.Check(SPResourceKind kind, Int32 value) at Microsoft.SharePoint.Client.SPClientServiceHost.OnBeginRequest()
  
You can either remove the throttling:
  
```
$webapp = Get-SPWebApplication -Identity http://<URL of your on-premises farm>
$rule = $webapp.AppResourceTrackingSettings.Rules.Get([Microsoft.SharePoint.SPResourceKind]::ClientServiceRequestDuration)
$rule.Remove()

```

Or change the throttling value:
  
```
$webapp = Get-SPWebApplication -Identity http://<URL of your on-premises farm>
$webapp. AppResourceTrackingSettings.Rules.Add([Microsoft.SharePoint.SPResourceKind]::ClientServiceRequestDuration, 150000, 150000)
$webapp.AppResourceTrackingSettings.WindowCount = 10
$webapp.AppResourceTrackingSettings.WindowSize = [System.TimeSpan]::FromSeconds(30)
$webapp.Update()

```

where the 150000 means 150 seconds.
  
## See also

#### Concepts

[Deploy a Business Connectivity Services hybrid solution in SharePoint](deploy-a-business-connectivity-services-hybrid-solution.md)

