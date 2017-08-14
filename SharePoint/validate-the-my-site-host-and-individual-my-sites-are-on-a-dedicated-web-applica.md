---
title: Validate the My Site Host and individual My Sites are on a dedicated Web application and separate URL domain (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: b5f098eb-219a-4483-adee-75d7b6b3089a
---


# Validate the My Site Host and individual My Sites are on a dedicated Web application and separate URL domain (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Validate the My Site Host and individual My Sites are on a dedicated Web application and separate URL domain., for SharePoint Server 2016. **Rule Name:**    Validate the My Site Host and individual My Sites are on a dedicated Web application and separate URL domain. **Summary:**    For performance and manageability reasons, we recommend that the My Site host and individual My Sites be deployed in a dedicated Web application. The owner of each individual My Site is the site collection administrator for that My Site. Having a dedicated Web application for the My Site host and individual My Sites reduces the security risk that a My Site owner can introduce same-domain scripting attacks on other sites that are hosted on the same Web application. **Cause:**    The My Site host and individual My Sites are deployed in the same Web application as the root site collection. If the User Profile Service was configured by using the Farm Configuration Wizard, this is how My Sites are set up. **Resolution:   Set up a dedicated Web application**
- We recommend that you have a separate, dedicated Web application to host the My Site host and individual My Sites.
    
    For more information, see **Create a web application in SharePoint Server**.
    
  

# See also

#### 

 [Configure My Sites in SharePoint Server](html/configure-my-sites-in-sharepoint-server.md)
  
    
    

  
    
    

