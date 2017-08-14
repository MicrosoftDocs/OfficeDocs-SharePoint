---
title: Validate the Business Connectivity Services hybrid scenario
ms.prod: SHAREPOINT
ms.assetid: 48a1c449-7bf6-4f12-a5f3-1933caadf713
---


# Validate the Business Connectivity Services hybrid scenario
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-06-22* **Summary: ** How to validate the Business Connectivity Services (BCS) hybrid solution is working.Now that you have created an external list or deployed an app for SharePoint in SharePoint Online, you need to test the security you put in place. Every account that will be accessing and manipulating the external data must have three properties:
- It must have user or greater permissions to the SharePoint Online site and the external list or app for SharePoint.
    
  
- It must be a federated account.
    
  
- It must be a member of the on-premises global security group that you are using to control access to the OData service endpoint. For example, it must be a member of **ODataGroup**.
    
  
In this procedure, you will open the SharePoint Online site and the external list or app for SharePoint with four different accounts.
## 

 **To validate security on the BCS hybrid**
1. Identify or create one account for each of the account types listed in the following table.
    
### 

Account Expected outcome Troubleshooting step **Account A** <br/>  Has site/list/app permissions. <br/>  Is federated. <br/>  Is a member of the on-premises global security group ( **ODataGroup** ). <br/> External data displayed and editable.  <br/> If the external data does not display or you cannot edit it, check the site permissions, your federation setup, and the membership of your on-premises global security group; for example, the **ODataGroup**. <br/> **Account B** <br/>  Does not have site/list/app permissions. <br/>  Is federated. <br/>  Is a member of the on-premises global security group ( **ODataGroup** ). <br/> External data does not display.  <br/> If the external data does display and you can edit it, check the site/list/app permissions.  <br/> **Account C** <br/>  Has site/list/app permissions. <br/>  Is not federated (is an Office 365 account only). <br/>  Cannot be added to the on-premises global security group ( **ODataGroup** ). <br/> External data does not display.  <br/> If the external data does display and you can edit it, check your federation setup and membership of your on-premises global security group ( **Odata Group** ). <br/> **Account D** <br/>  Has site/list/app permissions. <br/>  Is federated. <br/>  Is not a member of your on-premises global security group ( **ODataGroup** ). <br/> External data does not display.  <br/> If the external data does display and you can edit it, check the membership of your on-premises global security group ( **ODataGroup** ) and the permissions that you set on the OData service endpoint that you configure in **OBSOLETE Prepare the SharePoint Online environment for the Business Connectivity Services hybrid scenario** <br/> 2. Open (by using In-Private browsing if possible) the SharePoint Online site that contains the external list or app for SharePoint by using each of the accounts in turn. Be sure to completely log out and close your browser in between tests.
    
  
3. If you don’t see the expected outcome, refer to the troubleshooting step in the previous table, fix the issue, and repeat all four tests until you achieve the expected outcome.
    
  
If you see the error message:ResourceBudgetExceeded, sending throttled status code. Exception=Microsoft.SharePoint.SPResourceBudgetExceededException: ResourceBudgetExceeded at Microsoft.SharePoint.SPResourceTally.Check(Int32 value) at Microsoft.SharePoint.SPAggregateResourceTally.Check(SPResourceKind kind, Int32 value) at Microsoft.SharePoint.Client.SPClientServiceHost.OnBeginRequest()You can either remove the throttling:


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
# See also

#### 

 [Deploy a Business Connectivity Services hybrid solution in SharePoint](html/deploy-a-business-connectivity-services-hybrid-solution-in-sharepoint.md)
  
    
    

  
    
    

