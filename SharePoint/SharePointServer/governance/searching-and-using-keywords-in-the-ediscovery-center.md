---
title: "Searching and using keywords in the eDiscovery Center"
ms.reviewer: 
ms.author: MARKJJO
author: MARKJJO
manager: pamgreen
ms.date: 2/12/2018
audience: ITPro
f1.keywords:
- CSH
ms.topic: article
ms.custom:
- DiscoverySearchSyntaxTips
- WSSEndUser_DiscoverySearchSyntaxTips
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server
ms.assetid: c9b29461-20f6-4ae6-84ac-ce9bed3ceabb
description: "Keywords help you narrow down the specific content that you produce through export for an eDiscovery case. By creating focused searches, you increase the likelihood that content is applicable to a case, and reduce the amount of content that you need to manage."
---

# Searching and using keywords in the eDiscovery Center

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

Keywords help you narrow down the specific content that you produce through export for an eDiscovery case. By creating focused searches, you increase the likelihood that content is applicable to a case, and reduce the amount of content that you need to manage. 
  
Your organization may create an eDiscovery case if it receives a request for potential evidence to support litigation, an audit, or an investigation.
  
## Filters and Queries
<a name="__top"> </a>

After you create a case, you add Discovery Sets to it. Discovery Sets contain the content sources - such as SharePoint subsites - that are may be relevant to a case. Filters help you narrow down the source, such as by keywords, a range of start and end dates, domains, or by author or sender. 
  
Once you have identified potential sources, queries help further refine the content that you want to export to review or to provide to counsel and/or the requesting party. You can construct your filter by using keywords, date ranges, author/recipients, domains, and proximity searches. 
  
> [!NOTE]
>  In order for content to be discovered, it must be crawled by search. For more information about the default file types that are crawled, see the article [Default crawled file name extensions and parsed file types in SharePoint Server 2013](/SharePoint/technical-reference/default-crawled-file-name-extensions-and-parsed-file-types). 
  
## Operators and Proximity in Keywords
<a name="__top"> </a>

Special operators, such as Boolean and proximity operators, can be used to create relationships between multiple keywords. The operators must be written in all uppercase letters. If you need to use multiple operators, you can group them with parenthesis to determine the order in which they are applied.
  
For example, you might be looking for content with the term executive, but you don't want to find the term when it appears in the title of a frequent report in your organization called the Executive Summary. When you use the phrase executive NOT summary, you can narrow down the number of items returned from 300 to 188, since you are eliminating any documents that contain the word Summary. 
  
> [!NOTE]
>  When two words are specified with no operator, an implied AND exists. For example: wooly worm is the same as wooly AND worm **.**
  
|**Use**|**To**|**Example**|
|:-----|:-----|:-----|
| `AND` <br/> |Find content that contains all of the words or phrases it separates.  <br/> | `risk AND value AND VAR` finds content that contains all three words.  <br/> |
| `OR` <br/> |Find content that contains either of the words or phrases it separates.  <br/> | `risk OR VAR` finds all the content that contains either word.  <br/> |
| `NOT` <br/> |Exclude content that contains the term within a phrase.  <br/> | `Executive NOT Summary` finds all the content that contains the phrase Executive, unless the content also contains the term Summary.  <br/> |
| `( )` <br/> |Group words or phrases to show the order in which they are applied.  <br/> | `(Risk AND management) OR (VAR OR Value-at-risk)` <br/> |
| `NEAR(n)` <br/> |Finds words that are near each other, where n equals the number of words apart. If no number is specified, the default distance is 8 words.  <br/> | `Mid NEAR(5)` Office finds Mid and Back Office and Mid-Office and Mid, Back, and Front Office.  <br/> |
   
## Using Wildcards
<a name="__top"> </a>

Wildcards can help you expand your keywords to include terms that contain part of a keyword or terms that have alternative spellings.
  
|**Use**|**To**|**Example**|
|:-----|:-----|:-----|
|\* at the end of word  <br/> |Find terms that contain the root word and any additional letters.  <br/> |risk\* finds risk, risks, risked, risking, and risky  <br/> |
   
## Basic rules for using keywords in filters and queries
<a name="__top"> </a>

- A content filter or query can include words, quoted phrases, and terms that use keywords and properties. Separate terms with spaces. 
    
- Commonly used words such as  *the*  ,  *it*  , and  *by*  , and single-digit numbers, are ignored. 
    
- When you enclose a phrase in quotation marks, your search returns content within the chosen scope that contains the exact phrase that you typed. If there is any variance between the phrase in quotations and the actual content, the content will not be found.
    
- Operators (for example, Boolean operators) - such as **OR** and **AND** — should be written as all uppercase. 
    
- If a property of SharePoint content is not listed in the **Specify Property** dropdown menu, you can search for it with keywords. Enclose a property value in quotation marks to find an exact match, or leave the value unquoted to find partial matches that begin with the letters typed. For example, if you look for filename:"Budget" (with quotation marks), your search will return a file named "Budget.xlsx." A search for filename:budget (without quotation marks) will also return the files "Budget_Current.xlsx" and "Budget_Next.xlsx." 
    
-     > [!NOTE]
    >  A query must include a term to find. Queries that consist only of terms to exclude will produce an error message. 
  
## Examples for applying rules
<a name="__top"> </a>

|****Keywords****|****Example Results****|
|:-----|:-----|
| `Executive Briefing` <br/> |Any content that contains both Executive and Briefing, anywhere in the document, page, message, or metadata.  <br/> |
| ` "Executive Briefing" ` <br/> |Any content that contains the exact phrase "Executive Briefing" anywhere in the document, page, or message.  <br/> |
| `"Executive Briefing" AND "Executive Summary"` <br/> |Any content that contains the exact phrases "Executive Briefing" and "Executive Summary" anywhere in the document, page, message, or metadata.  <br/> |
| `filename:budget` <br/> |Any file with budget in its filename, such as 2014 budget projections.docx, 2015 budget priorities.pptx, 2014 budget planning.xlsx, 2014 budget review.xlsx, and so on  <br/> |
| `filename:2014 budget filetype:xlsx` <br/> |Excel worksheets that contain the phrase 2014 budget, such as "2014 budget planning.xlsx" and "2014 budget review.xlsx"  <br/> |
   
## Query Scope
<a name="__top"> </a>

A query can apply to all the content in a case, to specific eDiscovery Sets, or a specific content source (such as Web content or a fileshare) within an eDiscovery Set. Narrowing the scope may help you identify the right content, especially if the case is large, and the search returns in other sources or eDiscovery Sets aren't relevant.
  
> [!IMPORTANT]
>  When the **Select sources** options is selected, any filters that may have been added as part of the Discovery set are not included. 
  
To set the scope of a query, click **Modify Query Scope**, and then select **All case content**, **Select eDiscovery Sets**, or **Select sources**.
  
The **All case content** option includes all content from the list of sources, with any eDiscovery Set filters applied. You can also include additional content locations when setting query scope. 
  
## Viewing and troubleshooting queries
<a name="__top"> </a>

After you run a query, you can view the SharePoint results by relevance to the query, or by the oldest or newest date. You can see a preview of the document by hovering over its title.
  
To narrow down which items are exported, you can further refine the results by file extension and by property, such as Author or Title. 
  
In the query dialog, click the **Advanced Query Options** link. You can see your underlying query syntax for SharePoint, the content sources included in your query, any filters for your query, and any refinements. 
  
## Find more information about eDiscovery
<a name="__top"> </a>

For more information about eDiscovery cases, see the following articles:
  
[Scenario: eDiscovery in SharePoint Server 2013 and Exchange Server 2013](/sharepoint/)
  
[Plan and manage cases in the eDiscovery Center](/sharepoint/governance/plan-and-manage-cases-in-the-ediscovery-center)
  
[Add content to a case and place sources on hold in the eDiscovery Center](add-content-to-a-case-and-place-sources-on-hold-in-the-ediscovery-center.md)
  
[Default crawled file name extensions and parsed file types in SharePoint Server 2013](/SharePoint/technical-reference/default-crawled-file-name-extensions-and-parsed-file-types)
  
[Overview of crawled and managed properties in SharePoint Server 2013](/SharePoint/technical-reference/crawled-and-managed-properties-overview)
  
[Create and run queries in the eDiscovery Center](create-and-run-queries-in-the-ediscovery-center.md)
  
[Export content and create reports in the eDiscovery Center](export-content-and-create-reports-in-the-ediscovery-center.md)
  

