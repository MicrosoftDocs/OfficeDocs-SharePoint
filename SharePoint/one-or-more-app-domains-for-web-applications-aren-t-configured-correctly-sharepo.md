---
title: One or more app domains for web applications aren't configured correctly (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 76a4e2e3-7e10-41da-b3a8-fe62e193dc24
---


# One or more app domains for web applications aren't configured correctly (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "One or more app domains for web applications aren't configured correctly" for SharePoint Server 2016. **Rule Name:**   One or more app domains for web applications aren't configured correctly. **Summary:**    This health rule checks to see if the multiple app domains feature is enabled by looking at the state of the *Microsoft.SharePoint.Administration.SPWebService.ContentService.SupportMultipleAppDomains*  property. If this is enabled, the health rule then checks to see if there are multiple web application zones in each web application. If there are, it continues to check if there is an app domain defined for each web application zone. The health rule alert is triggered if the final condition is not met. It is also triggered if the web application and app domain are not using the same Internet Information Services (IIS) port binding, web application zone, application pool account, and authentication type. **Cause:**   The SharePoint Server 2016 environment is not set to use multiple app domain, or the web application is incorrectly configured for multiple web application zones. **Resolution:**
1. You have to configure the app domains for web applications. For more information, see **Enable apps in AAM or host-header environments for SharePoint 2016**.
    
  

