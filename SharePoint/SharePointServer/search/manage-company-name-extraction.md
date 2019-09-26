---
title: "Manage company name extraction in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/8/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 89c08a8b-74ee-4a97-8885-16c4c5a1288d
description: "Learn how to include company names to be extracted from content for classic search results, or how to exclude company names from being extracted."
---

# Manage company name extraction in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
The search system can extract company names from content. The following conditions must be met before company names can be extracted: 
  
- The managed property setting **Company name extraction** must be enabled on the managed property that you want to extract company names from. Typically, this is a managed property that you expect to contain these entities, such as the managed properties **Title** or **Body**. Company names are extracted from the full contents of the managed property they are associated with, even if sections in those contents are tagged as **\<no index\>**. 
    
- The name of the company that you want to extract should either already exist in the prepopulated company name dictionary or it should be included in the **Company Inclusions** list. 
    
- A full crawl must be completed. 
    
For example, if a company name is found in the body of a document, **company name extraction** is enabled on the managed property **Body** and a full crawl has been run, the company name is extracted and mapped to the managed property **companies**. You can then use the **companies** managed property to create refiners based on the extracted company name in the Refinement Web Part on the search results page. 
  
There is a prepopulated dictionary for company name extraction which includes a large number of company names. You can add additional company names to be extracted or prevent particular company names from being extracted using the Company Inclusions or Company Exclusions lists. 
  
This article explains how to maintain these lists. It does not cover how to enable a managed property to use company extraction. For more information on how to enable company extraction on a managed property, see [Manage the search schema in SharePoint Server](manage-the-search-schema.md). 
  
  
    
## Open the Term Store Management Tool
<a name="CE_Open_TS"> </a>

The company name exclusion and inclusion lists are managed in the Term Store. Use the Term Store Management Tool to edit the lists.
  
 **To get to the Term Store Management Tool**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application. 
    
2. On the home page of the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Service Applications page, click the Search service application.
    
4. On the Search Administration Page, in the **Queries and Results** section, click **Search Dictionaries**. The Term Store Management Tool opens.
    
## Exclude company names
<a name="CE_Exclude"> </a>

To exclude company names from being extracted as entities from content, add the company name to the Company Exclusions list.
  
 **To add a company name to the Company Exclusions list**
  
1. On the Site Settings: Term Store Management Tool page, click the arrow to expand the **Search Dictionaries** menu. 
    
2. Click Company Exclusions, click the arrow and then click **Create Term**. 
    
3. Type the name of the company that you want to exclude in the box that appears. 
    
4. Click anywhere on the page to add the term to the Company Exclusions list.
    
## Include company names
<a name="CE_Include"> </a>

To include company names to be extracted as entities from content, add the company name to the Company Inclusions list.
  
 **To add a company name to the Company Inclusions list**
  
1. On the Site Settings: Term Store Management Tool page, click the arrow to expand the **Search Dictionaries** menu. 
    
2. Click Company Inclusions, click the arrow and then click **Create Term**. 
    
3. Type the name of the company that you want to include in the box that appears. 
    
4. Click anywhere on the page to add the term to the Company Inclusions list.
    
## Edit terms
<a name="CE_Edit"> </a>

You can edit the names of terms in the Company Exclusions and Company Inclusions lists. 
  
 **To edit terms**
  
1. On the Site Settings: Term Store Management Tool page, click the arrow to expand the **Search Dictionaries** menu. 
    
2. Depending on which list the term is in, click either **Company Exclusions** or **Company Inclusions**.
    
3. Double-click the term that you want to edit. 
    
4. Type the new name for the term. 
    
5. Click anywhere on the page to save the edited term.
    

