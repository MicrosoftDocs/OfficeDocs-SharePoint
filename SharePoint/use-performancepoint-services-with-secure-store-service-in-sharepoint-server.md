---
title: Use PerformancePoint Services with Secure Store Service in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 1d93093a-4da3-40c0-b0fd-f2567a32d2e9
---


# Use PerformancePoint Services with Secure Store Service in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-06* **Summary:** Learn about the options available for using the Secure Store Service with PerformancePoint Services to connect to and refresh data from external data sources.This series of articles describes how to configure data access in PerformancePoint Services by using the Secure Store Service to map user and group credentials to the credentials of external data sources.In Secure Store you specify a group of users to whom you want to grant access to a data source and a set of credentials that has access to that data source. The user information is stored in a Secure Store  *target application*  and the associated credentials are stored, encrypted, in the Secure Store database. You can then specify the target application in PerformancePoint Dashboard Designer, and PerformancePoint Services will use the stored credentials on behalf of the specified users to access data in Dashboard Designer and in the browser.
> [!NOTE:]

  
    
    

PerformancePoint Services can be used with Secure Store in two primary scenarios:

  
    
    
> **Unattended Service Account:** The *unattended service account*  is an account that is used by PerformancePoint Services to provide broad database access to all users in the farm. Use the unattended service account for accessing data that is not considered sensitive or where you do not want to restrict access to a certain group of users. For information about how to configure this scenario, see [Configure the unattended service account for PerformancePoint Services](html/configure-the-unattended-service-account-for-performancepoint-services.md).
    
  

  
    
    
> **Specified target application:** You can specify a Secure Store target application in Dashboard Designer and Dashboard Designer will use the credential stored in Secure Store to access the selected data source. When you publish your dashboard, PerformancePoint Services will use these credentials to provide data refresh for authorized users. For information about how to configure this scenario, see [Configure Secure Store for use with PerformancePoint Services](html/configure-secure-store-for-use-with-performancepoint-services.md).
    
  

