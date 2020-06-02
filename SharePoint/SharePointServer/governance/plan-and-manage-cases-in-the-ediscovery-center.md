---
title: "Plan and manage cases in the eDiscovery Center"
ms.reviewer: 
ms.author: MARKJJO
author: MARKJJO
manager: pamgreen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: concetpual
ms.prod: office-online-server
localization_priority: Normal
ms.collection: IT_Sharepoint_Server
ms.assetid: d955aeb8-0d48-4291-a8e2-f3b84f17943f
description: "Electronic Discovery, or eDiscovery, is the discovery of content in electronic format for litigation or investigation. This typically requires identifying content spread across laptops, email servers, file servers, and many other sources."
---

# Plan and manage cases in the eDiscovery Center

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

Electronic Discovery, or eDiscovery, is the discovery of content in electronic format for litigation or investigation. This typically requires identifying content spread across laptops, email servers, file servers, and many other sources. 
  
The eDiscovery Center is a SharePoint site collection used to perform electronic discovery actions. In an eDiscovery Center, you can create cases, which are SharePoint sites that allow you to identify, hold, search, and export content from SharePoint sites, and searchable file shares.
  
> [!NOTE]
>  Once you add content sources or queries to an eDiscovery case, changing the regional settings for the site is not supported. >  In order for content to be discovered, it must be crawled by search. For more information about the default file types that are crawled, see the article [Default crawled file name extensions and parsed file types in SharePoint Server 2013](/SharePoint/technical-reference/default-crawled-file-name-extensions-and-parsed-file-types). 
  
## Planning and creating cases
<a name="__top"> </a>

If you anticipate managing multiple cases in your eDiscovery Center, consider whether you want to define consistent processes for people in your organization to follow.
  
- Naming conventions for cases - Could matter if you anticipate a larger number of cases, or different types or classifications of cases, for different departments, 
    
- Additional data to describe cases
    
- Defining and communicating permissions for managing cases.
    
- Guidelines on creating queries
    
- Standard procedures for communicating when content is placed on hold
    
- Standard procedure for retaining and closing cases
    
### Example lifecycle of an eDiscovery case
<a name="__toc329025354"> </a>

- Create the site to manage a case
    
- Add sources
    
- Place sources on hold
    
- Create queries
    
- Export case content
    
- Close case
    

  
## Create a case
<a name="__toc329025355"> </a>

1. In an eDiscovery Center, select **Create new case**.
    
2. Enter a title and description for your case.
    
3. In the **Web Site Address** box, enter the last part of the URL you want for the case, such as ContosovsFabrikam. 
    
4. Under **Select a template**, make sure that **eDiscovery Case** is selected. 
    
5. Under **User Permissions**, select whether to keep the same permissions as the parent site or use unique permissions. If specific people will need access to this case, but not to other cases, you should choose **Use unique permissions**.
    
## Add sources and place them on hold
<a name="__toc329025356"> </a>

1. In the eDiscovery Center, open the case that you want to add a source to.
    
2. Select **eDiscovery Sets**.
    
3. Enter a name for the eDiscovery Set, such as Executive Correspondence.
    
4. Next to **Sources**, select **Add &amp; Manage Sources**.
    
5. Under **Locations**, enter the URL or file share address for the content you want to use as the source. Any content you include must be indexed by search. 
    
6. Select **Save**.
    
7. In the box under **Filter**, enter any keywords you want to use to narrow down the source.
    
8. To narrow down content by a date range, enter the **Start Date** and **End Date**.
    
9. To limit results to the author of a document or list item, or to a specific sender of email messages, in the **Author/Sender** box, enter the names or email addresses. 
    
10. Select **Apply Filter**. 
    
11. Select **Enable In-Place** hold. 
    
12. To verify that you've selected the right content, select **Preview Results**.
    
13. Select **Save**.
    
For more info, see [Add content to a case and place sources on hold in the eDiscovery Center](/SharePoint/governance/add-content-to-a-case-and-place-sources-on-hold-in-the-ediscovery-center).
  
  
## Run queries and export content
<a name="__toc329025357"> </a>

After you have defined your sources, and placed them on hold if necessary, you can run queries to narrow down and extract exactly the content you need for a particular case. SharePoint has some tools that can help you refine your queries.
  
You export content from a case when you are ready to deliver it to an authority or want to work on it with another legal program. The content is exported in a format that is compatible with the Electronic Discovery Reference Model standard. 
  
  
## Close cases
<a name="__toc329025357"> </a>

When you close a case, in-place holds will be released for all of its sources, and you will no longer be able to put sources on hold for this case.
  
1. Select **Settings** ![Microsoft 365 Settings button](../media/a9a59c0f-2e67-4cbf-9438-af273b0d552b.png), and then select **Case Closure**. 
    
2. Select **Close this case**.
    
## Find more info about eDiscovery
<a name="__toc329025357"> </a>

For more info about eDiscovery cases, see the following articles:
    
[Add content to a case and place sources on hold in the eDiscovery Center](/SharePoint/governance/add-content-to-a-case-and-place-sources-on-hold-in-the-ediscovery-center)
  
[Searching and using keywords in the eDiscovery Center](/SharePoint/governance/searching-and-using-keywords-in-the-ediscovery-center)
  
[Default crawled file name extensions and parsed file types in SharePoint Server](/SharePoint/technical-reference/default-crawled-file-name-extensions-and-parsed-file-types)
  
[Overview of crawled and managed properties in SharePoint Server](/SharePoint/technical-reference/crawled-and-managed-properties-overview)
  
[Create and run queries in the eDiscovery Center](/SharePoint/governance/create-and-run-queries-in-the-ediscovery-center)
  
[Export content and create reports in the eDiscovery Center](/SharePoint/governance/export-content-and-create-reports-in-the-ediscovery-center)
  


