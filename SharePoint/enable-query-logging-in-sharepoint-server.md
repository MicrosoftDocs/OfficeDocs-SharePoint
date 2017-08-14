---
title: Enable query logging in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 6259e195-2b83-454f-b635-8f228c1fd1ac
---


# Enable query logging in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-24* **Summary:** Learn how to enable or disable query logging.SharePoint Server search collects information about user search queries and search results that users select on their computers. SharePoint Server uses this information to improve the relevance of search results and to improve query suggestions. Site collection administrators, tenant administrators and administrators of the Search service application can also create reports based on this information. Query logging is enabled by default. Use this procedure to enable or disable query logging.In this article:
-  [Before you begin](#begin)
    
  
-  [To enable or disable query logging](#proc1)
    
  

## Before you begin
<a name="begin"> </a>


> [!NOTE:]
>  [Plan browser support](https://go.microsoft.com/fwlink/p/?LinkId=246502)> **Accessibility for SharePoint 2013**>  [Accessibility features in SharePoint Products](https://go.microsoft.com/fwlink/p/?LinkId=246501)>  [Keyboard shortcuts](https://go.microsoft.com/fwlink/p/?LinkID=246504)>  [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506)
  
    
    

Before you begin this operation, review the following information about prerequisites:
- Create a Search service application 
    
  
 **To enable or disable query logging**
1. Verify that the user account performing this procedure is an administrator for the Search service application.
    
  
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
  
3. On the Manage Service Applications page, click the Search service application for which you want to configure query logging.
    
  
4. On the Search Administration page, in the **System Status** section, locate **Query logging**.
    
  
5. The **Query logging** status displays as **Off** **Enable** or **On** **Disable**.
    
  
6. By default, query logging is turned **On**. Click **Disable** to turn off query logging or click **Enable** to turn on query logging.
    
  
The option is set and no other actions are necessary. User search queries and user selected results will no longer be logged if you clicked **Disable**, or will now be logged if you clicked **Enable**.
