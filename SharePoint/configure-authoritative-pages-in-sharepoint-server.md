---
title: Configure authoritative pages in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 6bf64b3d-edf0-4d2a-a1f5-b53318a24a1a
---


# Configure authoritative pages in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-14* **Summary:** Learn how to specify authoritative pages and non-authoritative URLs and sites. Search uses the list of authoritative pages to calculate the ranking of results.Static rank determines the relative importance of a page, and it is computed as the smallest number of clicks it would take a user to navigate from an authoritative page to a document. The closer a document is to the most authoritative page, the higher its static rank is.An administrator provides a small set of authoritative pages. An example of an authoritative page could be the home page of a company portal. An administrator with specific knowledge of an area can influence the relative importance of pages by specifying additional authoritative and non-authoritative pages. An example of non-authoritative pages could be URLs of sites that contain outdated information that are kept for record-keeping In this article:
-  [Before you begin](#begin)
    
  
-  [Specify pages as authoritative or non-authoritative](#BKMK_SpecifyWebPagesAsAuthoritative)
    
  

## Before you begin
<a name="begin"> </a>


> [!NOTE:]
>  [Plan browser support](https://go.microsoft.com/fwlink/p/?LinkId=246502)> **Accessibility for SharePoint 2013**>  [Accessibility features in SharePoint 2013 Products](https://go.microsoft.com/fwlink/p/?LinkId=246501)>  [Keyboard shortcuts](https://go.microsoft.com/fwlink/p/?LinkID=246504)>  [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506)
  
    
    

Before you begin this operation, review the following information about prerequisites:
- Create a Search service application.
    
  

## Specify pages as authoritative or non-authoritative
<a name="BKMK_SpecifyWebPagesAsAuthoritative"> </a>

Use the following procedure to specify pages as authoritative or non-authoritative. **To specify pages as authoritative or non-authoritative**
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
  
3. Click the Search service application.
    
  
4. On the Search Administration page, in the Quick Launch, click **Authoritative Pages**.
    
  
5. On the Specify Authoritative Pages page, in the **Most authoritative pages** box in the **Authoritative Web Pages** section, type the URLs of pages that are the most authoritative. Separate the URLs with returns so that there is one URL per line.
    
  
6. In the **Second-level authoritative pages** box, type the URLs of any pages that should be seen as second-level.
    
  
7. In the **Third-level authoritative pages** box, type the URLs of any pages that should be seen as third-level.
    
  
8. In the **Non-authoritative Sites** section, in the **Sites to demote** box, type the URLs of any sites that you want to be ranked lower than all of the other sites. Type one URL per line.
    
    All URLs whose prefix matches the prefix of a URL in the **Sites to demote** box are demoted. Example: Entering **http://archive/** demotes the rank of all URLs that begin with **http://archive/**.
    
  
9. In the **Relevance Ranking Analytics** section, select the **Refresh now** check box to run the ranking analytics you have defined or that you have updated.
    
    If you clear the check box, ranking analytics run later according to a defined schedule.
    
  
10. Click **OK**.
    
  

