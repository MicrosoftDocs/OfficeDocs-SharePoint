---
title: Enable search alerts in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 73cfd7b3-be90-480a-b415-039fa97d9b89
---


# Enable search alerts in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-24* **Summary:** Learn how to enable or disable search alerts.Search alerts allow end-users to receive e-mail notification when specified search query results are changed or updated. Search alerts should be enabled when you want allow end-users to create alerts for search queries. Search alerts may be configured on the search query page when a search query is completed and results are displayed. Search alerts are created and configured per-user and are only configurable and viewable by the user who creates them. Search alerts are enabled by default. Use this procedure to enable or disable search alerts.In this article:
-  [Before you begin](#begin)
    
  
-  [To enable or disable search alerts](#proc1)
    
  

## Before you begin
<a name="begin"> </a>


> [!NOTE:]
>  [Plan browser support](http://go.microsoft.com/fwlink/p/?LinkId=246502)> **Accessibility for SharePoint 2013**>  [Accessibility features in SharePoint Products](http://go.microsoft.com/fwlink/p/?LinkId=246501)>  [Keyboard shortcuts](http://go.microsoft.com/fwlink/p/?LinkID=246504)>  [Touch](http://go.microsoft.com/fwlink/p/?LinkId=246506)
  
    
    

Before you begin this operation, review the following information about prerequisites:
- Create a Search service application 
    
  
- Create a User Profile service application
    
  
 **To enable or disable search alerts**
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
  
3. On the Manage Service Applications page, click the Search service application for which you want to configure search alerts. 
    
  
4. On the Search Administration page, in the **System Status** section, locate **Search alerts status**.
    
  
5. The search alerts status displays as **Off** **Enable** or **On** **Disable**.
    
  
6. By default, search alerts are turned **On**. Click **Disable** to turn off search alerts or click **Enable** to turn on search alerts.
    
  
The option is now set. Search alerts are sent only if outgoing e-mail is configured. For more information, see  [Configure outgoing email for a SharePoint Server farm](html/configure-outgoing-email-for-a-sharepoint-server-farm.md). If you enabled search alerts, users can create search alerts for search queries that they run. To configure search alerts for search queries, users can click the **Alert Me** link that is located on the bottom of the Search Results page. The **Alert Me** link will appear a few minutes after search alerts are turned on. If search alerts are turned off, this icon does not appear.
