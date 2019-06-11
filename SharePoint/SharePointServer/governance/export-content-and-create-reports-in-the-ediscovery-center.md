---
title: "Export content and create reports in the eDiscovery Center"
ms.reviewer: 
ms.author: MARKJJO
author: MARKJJO
manager: pamgreen
ms.date: 2/12/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server
ms.assetid: 7b2ea190-5f9b-4876-86e5-4440354c381a
description: "You export content from a case when you are ready to deliver it to an authority or want to work on it with another legal program. You can also create reports to identify the contents of and any search indexing issues with the export. The export includes a load file based on the Electronic Discovery Reference Model standard."
---

# Export content and create reports in the eDiscovery Center

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

You export content from a case when you are ready to deliver it to an authority or want to work on it with another legal program. You can also create reports to identify the contents of and any search indexing issues with the export. The export includes a load file based on the Electronic Discovery Reference Model standard.
  
Before you export content, the case should already have content sources, such as Web sites, and queries. Also, the computer you use to export content has to meet the following system requirements:
  
- 32- or 64-bit version of Windows 7 and later versions
    
- Microsoft .NET Framework 4.5
    
- One of the following supported browsers:
    
  - Internet Explorer 10 and later versions
    
  - Mozilla Firefox or Google Chrome, with the ClickOnce add-in installed
    
When you first export content or create a report, the eDiscovery Download Manager is installed, which exports the SharePoint content and reports to the your local computer. When downloading an eDiscovery export, users must log into SharePoint with the same account that they are logged into on their client machine. If you receive a warning asking whether or not to run the Download Manager, accept the warning and continue.
  
## Export eDiscovery content
<a name="__toc331583108"> </a>

1. If your case is not already open, in an eDiscovery Center, click **Cases**, and then click the case in which you want to export content.
    
2. In the **Search and Export** section, under **Queries**, click the name of the query you want to export. On the query page, you can see the size and contents to be included in the export.
    
3. At the bottom of the query page, click **Export**.
    
4. Type a name for the export. By default, the export is named the same as the query it's based on, but you can change the name.
    
5. On the page that appears, in the **Options** section, select any of the following: 
    
6. To include versions of documents - if your organization tracks versions - select the **Include versions for SharePoint documents** checkbox. 
    
7. To include items that are encrypted or have an unrecognizable format, select the **Include items that are encrypted or have an unrecognized format** check box. 
    
8. Click **OK**.
    
9. Click **Download Results**.
    
10. If you are exporting content for the first time on a computer, you will be prompted to install the Discovery Download Manager. Click **Yes**.
    
11. When you are finished exporting, click **Close**.
  
## Create reports about exported content
<a name="__toc331583110"> </a>

Reports identify the SharePoint content, its location, and other information, as well as any errors, such as content not exported as a result of search indexing issues. The reports are created in comma separated values format, which can be opened in Excel or imported into many types of programs.
  
In Microsoft Excel, you can examine the contents further by sorting and filtering the columns. For example, you could view only PowerPoint slides or sort by Web address or author.
  
1. If your case is not already open, in an eDiscovery Center, click **Cases**, and then click the case in which you want to export content.
    
2. In the **Search and Export** section, under **Queries**, click the name of the query you want to export.
    
3. At the bottom of the query page, click **Export**.
    
4. On the page that appears, in the Options section, select any of the following. The settings won't affect the report itself, but the report will show how the settings would affect your query:
    
5. To include versions of documents - if your organization tracks versions - select the **Include versions for SharePoint documents** checkbox. If your exported content contains many libraries that track versions, and many of your authors use versioning, this could significantly increase the file size of the export. 
    
6. To include items that are encrypted or have an unrecognizable format, select the **Include items that are encrypted or have an unrecognized format** check box. 
    
7. On the page that appears, click **OK**.
    
8. Click **Download Report**.
    
9. If you are exporting content for the first time on a computer, you will be prompted to install the Discovery Download Manager. Click **Yes**.
    
10. When you are finished exporting the report, click **Close**.
    
    The following reports (Excel CSV files) are downloaded to your computer in a folder named Reports.
    
  - **Export Errors** This report lists any errors that occurred during the export process. 
    
  - **SharePoint Index Errors**
    
  - **SharePoint Results** Contains a list of every SharePoint items returned as a search result. This report contains information such as the document type, the document author, the document URL, the URL and name of the site where the document is located, and the date when the document was last modified. 
    
    > [!NOTE]
    > If you don't select the **Include items that are encrypted or have an unrecognized format** option when you export search results or just download the reports, the index error reports are downloaded but they don't have any entries. This doesn't mean there aren't any indexing errors. It just means that unindexed items weren't included in the request to download the reports. 
  
## Find more information about eDiscovery
<a name="__toc331583110"> </a>

For more information about eDiscovery cases, see the following articles:
  
[Scenario: eDiscovery in SharePoint Server 2013 and Exchange Server 2013](/sharepoint/)
  
[Plan and manage cases in the eDiscovery Center](/sharepoint/governance/plan-and-manage-cases-in-the-ediscovery-center)
  
[Add content to a case and place sources on hold in the eDiscovery Center](add-content-to-a-case-and-place-sources-on-hold-in-the-ediscovery-center.md)
  
[Searching and using keywords in the eDiscovery Center](searching-and-using-keywords-in-the-ediscovery-center.md)
  
[Default crawled file name extensions and parsed file types in SharePoint Server 2013](/SharePoint/technical-reference/default-crawled-file-name-extensions-and-parsed-file-types)
  
[Overview of crawled and managed properties in SharePoint Server 2013](/SharePoint/technical-reference/crawled-and-managed-properties-overview)
  
[Create and run queries in the eDiscovery Center](create-and-run-queries-in-the-ediscovery-center.md)
  

  

