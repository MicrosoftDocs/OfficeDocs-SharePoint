---
title: "Customize search result types in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/7/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: cf19810b-5548-447c-a94d-026ad6e9d096
description: "Create and configure custom search result types in SharePoint Server so that users can readily distinguish and preview different kinds of items in a list of search results."
---

# Customize search result types in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

Create and configure custom search result types in SharePoint Server so that users can readily distinguish and preview different kinds of items in a list of search results in the classic search experience.
  
A search result type is a rule that causes distinct kinds of search results to be displayed in different ways. It consists of the following: 
  
- One or more characteristics or conditions to compare each search result against, such as the result source or content type of the search result
    
- A display template to use for search results that meet the conditions. The display template controls the way in which all results that meet the conditions appear and behave on a search results page. 
    
The search system has preconfigured result types that it uses by default. You can view them on the Manage Result Types page. For example, a preconfigured result type named **Person** specifies that if a search result comes from the result source **Local People Results**, then use the **People Item** display template to display the result. The **People Item** display template shows certain user-profile information in the search result and provides links in the hover panel for documents that the person has authored. 
  
As a site collection administrator or site owner, you can use the default result types as starting points for creating custom result types. For example, the pre-configured **Microsoft Excel** result type specifies the condition that the file extension of the search result is XLS or XLSX. You could copy this result type and customize it so that it also includes the condition that the value of the **ContentType** managed property is Sales Report. That way, users will readily be able to identify certain Excel search results as sales reports.
  
You could also customize the default **Excel Item** display template for this purpose. A display template specifies how to display managed properties of a search result, such as item title, file extension, path, and summary. This helps users to distinguish results easily. The display template also controls how a document or site will appear in the preview pane (also called the hover panel) to the right of the search result. This helps users to know whether a search result will be useful to them before they click the result to open it. For example, the **Excel Item** display template can display relevant charts, worksheets, and tables from an Excel document in the hover panel and enable users to go directly to those sections in the document. For more information about display templates for search result types, see: 
  
- [Result types and display templates that are used to display search results in SharePoint Server](../technical-reference/result-types-and-display-templates-that-are-used-to-display-search-results.md)
    
- [Display template reference in SharePoint Server](../technical-reference/display-template-reference-in-sharepoint-server.md)
    

    
 **Create and configure a custom search result type**
  
1. Go to the Manage Result Types page by doing one of the following:
    
  - If you want to create a result type for a site collection:
    
    - Ensure that you are an administrator for the site collection. 
    
    - In the site collection, go to **Settings** > **Site settings**, and then in the **Site Collection Administration** section, click **Search Result Types**.
    
  - If you want to create a result type for a site:
    
    - Ensure that you are a site owner for the site. 
    
    - On the site, go to **Settings** > **Site settings**, and then in the **Search** section, click **Result Types**.
    
2. To create a result type, do one of the following on the Manage Result Types page:
    
  - Click **New Result Type**.
    
  - In the list of existing result types, click the name of a result type, such as **Person**, and then click **Copy** so that you can modify the copy to create a new result type. 
    
    > [!TIP]
    > When you create a result type, we recommend that you use the copy method, so that the settings in an existing result type can help guide you through the configuration process. 
  
3. On the Add Result Type page, in the **General Information** section, in the **Give it a name** text box, type a name for the new result type. 
    
4. On the Add Result Type page, in the **Conditions** section, do the following: 
    
  - In the **Which source should results match?** drop-down list, select a result source such as **All Sources** or **Documents**.
    
    For any given search result, this condition will be met if the search result is from the result source that you selected from this drop-down list.
    
  - (Optional) In the **What types of content should match?** drop-down list, do the following: 
    
  - Select a type of content, such as **Microsoft Word**.
    
    > [!NOTE]
    > If you do not select a type of content, all results from the result source that you specified (in the **Which source should results match?** section) will match this result type. 
  
  - As many times as appropriate, click **Add Value** and select another type of content. 
    
5. (Optional) On the Add Result Type page, expand the **Show more conditions** section, and then do the following: 
    
  - In the **Which custom properties should match?** section, the items in the **Select a property** drop-down list are retrievable managed properties. Select a property that you want the search system to perform a match on, such as **Author**.
    
  - In the second drop-down list, specify the operator, such as **Equals any of**.
    
  - In the text box, specify the value against which the search system should search for a match.
    
    Separate multiple values with semicolons. Alternatively, as many times as appropriate, click **Add Value** and type another value in the new text box that appears. 
    
    For example, if you select the **Author** property and you select the operator **Equals any of**, then if you specify multiple values such as Kara and Silas, the condition will be "author equals Kara or Silas".
    
  - To add another property to match, click **Add Property**.
    
6. On the Add Result Type page, in the **Actions** section, do the following: 
    
  - In the **What should these results look like?** drop-down list, click a display template such as **Office Document Item** or **PDF Item**.
    
    Display templates for search results are in the **Search** folder in the master page gallery for the site collection. The **Display template URL** box automatically displays the URL of the display template that corresponds to the display template that you selected. 
    
  - Select the **Optimize for frequent use** check box if you expect this result type to appear frequently in search results. 
    
## See also

#### Concepts

[Result types and display templates that are used to display search results in SharePoint Server](../technical-reference/result-types-and-display-templates-that-are-used-to-display-search-results.md)
  
[Display template reference in SharePoint Server](../technical-reference/display-template-reference-in-sharepoint-server.md)

