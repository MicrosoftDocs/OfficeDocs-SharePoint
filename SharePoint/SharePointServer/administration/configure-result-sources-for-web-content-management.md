---
title: "Configure result sources for web content management in SharePoint Server"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 9/5/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 3e5c9a22-816a-4eaf-90ba-3f208185e683

description: "Result sources limit searches to certain content or to a subset of search results. SharePoint Server provides 16 pre-defined result sources. The pre-configured default result source is Local SharePoint Results. You can specify a different result source as the default. In addition to the pre-configured result sources, SharePoint Server automatically creates a result source when you connect a publishing site to a catalog, and adds it to the result sources in the publishing site. This result source limits search results to the URL of the catalog. For more information about result sources, seePlan result sources and query rulesin Plan search for cross-site publishing sites in SharePoint Server 2016."
---

# Configure result sources for web content management in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

Result sources limit searches to certain content or to a subset of search results. SharePoint Server provides 16 pre-defined result sources. The pre-configured default result source is **Local SharePoint Results**. You can specify a different result source as the default. In addition to the pre-configured result sources, SharePoint Server automatically creates a result source when you connect a publishing site to a catalog, and adds it to the result sources in the publishing site. This result source limits search results to the URL of the catalog. For more information about result sources, see "Plan result sources and query rules" in [Plan search for cross-site publishing sites in SharePoint Server 2016](plan-search-for-sharepoint-cross-site-publishing-sites.md). 
  
    
## Before you begin
<a name="BKMK_Before"> </a>

> [!NOTE]
>  Because SharePoint Server runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server supports the accessibility features of supported browsers. For more information, see the following resources: > [Plan browser support](https://docs.microsoft.com/en-us/sharepoint/install/browser-support-planning-0)> [Accessibility guidelines in SharePoint](https://docs.microsoft.com/sharepoint/accessibility-guidelines)> [Accessibility in SharePoint](https://docs.microsoft.com/en-us/sharepoint/dev/general-development/accessibility-in-sharepoint)> [Keyboard shortcuts](https://support.office.com/article/keyboard-shortcuts-in-sharepoint-online-466e33ee-613b-4f47-96bb-1c20f20b1015)> [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506).
  
We recommend that you set up the publishing site, integrate a catalog, and configure category and catalog item pages before you begin to create result sources. This is because you can then more easily test and verify how the different result sources apply to the different Search Web Parts that you have on the site.
  
## Create a result source
<a name="BKMK_CreateResutlSource"> </a>

You can create a result source for a Search service application, a site collection, or a site. The following table shows the permissions that are required to create a result source at each level, and where the result source can be used.
  
**Levels and permissions for result sources**

|**When you create a result source at this level**|**You must have this permission**|**The result source can be used in**|
|:-----|:-----|:-----|
|Search service application  <br/> |Search service application administrator  <br/> |All site collections in web applications that consume the Search service application  <br/> |
|Site collection  <br/> |Site collection administrator  <br/> |All sites in the site collection  <br/> |
|Site  <br/> |Site owner  <br/> |The site  <br/> |
   
 **To create a result source**
  
1. Depending on the level at which you want to create the result source, do one of the following: 
    
  - To create a result source for a Search service application: 
    
1. Verify that the user account that performs this procedure is an administrator on the Search service application. 
    
2. In Central Administration, in the **Application Management** section, click **Manage service application**.
    
3. Click the Search service application for which you want to create a result source.
    
4. On the **Search Administration** page for the Search service application, on the Quick Launch, in the **Queries and Results** section, click **Result Sources**.
    
  - To create a result source for a site collection: 
    
1. Verify that the user account that performs this procedure is a site collection administrator on the publishing site collection.
    
2. On the publishing site collection, on the **Settings** menu, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Site Collection Administration** section, click **Search Result Sources**.
    
  - To create a result source for a site:
    
1. Verify that the user account that performs this procedure is a member of the Owners group on the publishing site.
    
2. On the publishing site, on the **Settings** menu, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Search** section, click **Result Sources**.
    
2. On the **Manage Result Sources** page, click **New Result Source**.
    
3. On the **Add Result Source** page, in the **General Information** section, do the following: 
    
1. In the **Name** box, type a name for the result source. 
    
2. In the **Description** box, type a description of the result source. 
    
4. In the ** Protocol ** section, select one of the following protocols for retrieving search results: 
    
  - **Local SharePoint**, the default protocol, provides results from the search index for this Search service application.
    
  - **Remote SharePoint** provides results from the index of a search service in another farm. 
    
    > [!IMPORTANT]
    > To use the Remote SharePoint protocol to get search results in one SharePoint Server on-premises farm from the index of another SharePoint Server on-premises farm, you must configure the farm that receives the queries to trust the farm that sends the queries. For information about how to do this, see [Configure trust for search between two SharePoint Server farms](../search/configure-trust-for-search-between-two-sharepoint-server-farms.md). 
  
  - **OpenSearch** provides results from a search engine that uses the OpenSearch 1.0/1.1 protocol. 
    
  - **The Exchange protocol only enables you to discover Exchange Server 2013 content**vides results from Microsoft Exchange Server 2013 through a SharePoint Server 2016 eDiscovery Center. Click **Use AutoDiscover** to have the search system find an Exchange Server 2013 endpoint automatically, or type the URL of the Exchange web service to retrieve results from — for example, https://contoso.com/ews/exchange.asmx.
    
    > [!NOTE]
    >  The Exchange protocol only enables you to discover Exchange Server content, and only from a SharePoint Server eDiscovery Center. For more information, see [Configure communication between SharePoint Server and Exchange Server](/SharePoint/governance/configure-ediscovery-0). >  The Exchange Web Services Managed API must be installed on the computer on which the search service is running. For more information, see [Optional software supported in SharePoint Server 2016](../install/hardware-and-software-requirements.md#OptionalSoftware) in [Hardware and software requirements for SharePoint Server 2016](../install/hardware-and-software-requirements.md). 
  
5. In the **Type** section, select **SharePoint Search Results** to search the whole index, or **People Search Results** to enable query processing that is specific to people search. 
    
6. In the **Query Transform** field, do one of the following: 
    
  - Leave the default query transform ( **searchTerms**) as is. In this case, the query will be unchanged since the previous transform.
    
  - Type a different query transform in the text box.
    
  - Use the Query Builder to configure a query transform by doing the following: 
    
1. Click **Launch Query Builder**.
    
2. In the **Build Your Query** dialog box, optionally build the query by specifying filters, sorting, and testing on the tabs as shown in the following tables. 
    
  - 
   **On the BASICS tab**

|||
|:-----|:-----|
|**Keyword filter** <br/> |You can use keyword filters to add pre-defined query variables to the query transform. You can select pre-defined query variables from the drop-down list, and then add them to the query by clicking **Add keyword filter**.  <br/> For an overview of query variables, see [Query variables in SharePoint Server](../technical-reference/query-variables.md).  <br/> |
|**Property filter** <br/> |You can use property filters to query the content of managed properties that are set to  *queryable*  in the search schema.  <br/> You can select managed properties from the **Property filter** drop-down list. Click **Add property filter** to add the filter to the query.  <br/> |
   
  - 
   **On the SORTING tab**

|||
|:-----|:-----|
|**Sort results** <br/> |In the **Sort by** menu, you can select a managed property from the list of managed properties that are set as sortable in the search schema, and then select **Descending** or **Ascending**. To sort by relevance, that is, to use a ranking model, select **Rank**. You can click **Add sort level** to specify a property for a secondary level of sorting for search results.  <br/> > [!NOTE]> Sorting of search results is case sensitive.           |
|**Ranking Model** <br/> |If you selected  *Rank*  from the **Sort by** list, you can select the ranking model to use for sorting.  <br/> |
|**Dynamic ordering** <br/> |You can click **Add dynamic ordering rule** to specify additional ranking by adding rules that change the order of results within the result block when certain conditions are satisfied.  <br/> |
   
  - 
   **On the TEST tab**

|||
|:-----|:-----|
|**Query text** <br/> |You can view the final query text, which is based on the original query template, the applicable query rules, and the variable values.  <br/> |
|Click **Show more** to display the options in the following rows of this table.  <br/> ||
|**Query template** <br/> |You can view the query as it is defined in the **BASICS** tab or in the text box in the **Query transform** section on the Add Result Source page.  <br/> |
|**Query template variables** <br/> |You can test the query template by specifying values for the query variables.  <br/> |
   
7. On the **Add Result Source** page, in the **Credentials Information** section, select the authentication type that you want for users to connect to the result source. 
    
## Set a result source as default
<a name="BKMK_Default"> </a>

 You can set any result source as the default result source. Specifying a result source as default can make it easier to edit the query in Search Web Parts. For example, when you add a Content Search Web Part to a page, the Web Part automatically uses the default result source. For more information, see [Configure Search Web Parts in SharePoint Server](configure-search-web-parts.md). 
  
 **To set a result source as default**
  
1. Perform the appropriate procedures in the following list depending on the level at which the result source was configured.
    
  - If the result source was created at the Search service application level, do the following:
    
1. Verify that the user account that performs this procedure is an administrator for the Search service application.
    
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
3. Click the Search service application for which you want to set the result source as default.
    
4. On the **Search Administration** page, in the **Queries and Results** section, click **Result Sources**.
    
  - If the result source is at the site collection level, do the following: 
    
1. Verify that the user account that performs this procedure is a site collection administrator on the publishing site collection.
    
2. On the publishing site collection, on the **Settings** menu, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Site Collection Administration** section, click **Search Result Sources**.
    
  - If the result source is at the site level, do the following: 
    
1. Verify that the user account that performs this procedure is a member of the Owners group on the publishing site.
    
2. On the publishing site, on the **Settings** menu, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Search** section, click **Result Sources**.
    
2. On the **Manage Result Sources** page, point to the result source that you want to set as default, click the arrow that appears, and then click **Set as Default**.
    
## See also
<a name="BKMK_Default"> </a>

#### Concepts

[Query variables in SharePoint Server](../technical-reference/query-variables.md)
  
[Configure Search Web Parts in SharePoint Server](configure-search-web-parts.md)

