---
title: "Configure Search Web Parts in SharePoint Server"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 7/26/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 76ca8205-2508-42b0-9c8e-36e1081a7fd4

description: "Learn how to configure the different Web Parts that use search technology in a publishing environment."
---

# Configure Search Web Parts in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Web Parts that use search technology to show content in a publishing environment (referred to in this article as Search Web Parts) show content that was crawled and added to the search index, as described in "Understanding how content is added to and managed in the search index" in [Overview of cross-site publishing in SharePoint Server](overview-of-cross-site-publishing.md). These Web Parts have queries defined in them, and when users browse to a page that contains a Web Part that uses search technology, the Web Part issues the query automatically. The query result is then displayed in the Web Part. You can modify the query in the search Web Part to fit your content needs. 
  
    
## Before you begin
<a name="BKMK_AvailableOOTRefiners"> </a>

> [!NOTE]
>  Because SharePoint Server runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server supports the accessibility features of supported browsers. For more information, see the following resources: > [Plan browser support](https://docs.microsoft.com/sharepoint/install/browser-support-planning-0)> [Accessibility guidelines in SharePoint](https://docs.microsoft.com/sharepoint/accessibility-guidelines)> [Accessibility in SharePoint](https://docs.microsoft.com/sharepoint/dev/general-development/accessibility-in-sharepoint)> [Keyboard shortcuts](https://support.office.com/article/keyboard-shortcuts-in-sharepoint-online-466e33ee-613b-4f47-96bb-1c20f20b1015)> [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506).
  
There are many Search Web Parts available in SharePoint Server. These Web Parts have predefined queries, such as what type of content to search for, where to search for content, and how to show content. For information about different Search Web Parts, see "Plan to add search Web Parts to pages" in [Plan publishing sites for cross-site publishing in SharePoint Server](plan-sharepoint-publishing-sites-for-cross-site-publishing.md). Many of the Search Web Parts use result sources and have query rules that are applied to them. Result sources narrow the scope of search results that are retrieved. A query rule is a set of conditions that will cause the query to be changed in a specific way. For more information about result sources and query rules, see [Plan result sources and query rules](plan-search-for-sharepoint-cross-site-publishing-sites.md#BKMK_PlanResultSourcesAndQueryRules).
  
To customize how search results appear in Search Web Parts — for example, to show an image followed by a title in bold to the right of the image — you modify display templates. The two types of display templates that are most relevant to Search Web Parts are control display templates and item display templates. For more information about the default display templates, see [Display template reference in SharePoint Server](../technical-reference/display-template-reference-in-sharepoint-server.md).
  
## Add a Content Search Web Part to a page
<a name="BKMK_AddContentWP"> </a>

 **To add a Content Search Web Part to a page**
  
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the publishing site collection.
    
2. Browse to the page where you want to add the Web Part.
    
3. Click the **Settings** menu, and then click **Edit page**. 
    
4. In the Web Part Zone where you want to add the Web Part, click **Add a Web Part**.
    
5. In the **Categories** list, click **Content Rollup**.
    
6. In the **Parts** list, click **Content Search**, and then click **Add**.
    
## Configure the query for a Content Search Web Part
<a name="BKMK_ConfigureWP"> </a>

You can use the Content Search Web Part in Quick Mode and create a query by selecting options from a list of existing result sources, or you can switch to Advanced Mode to create your own custom query by using Keyword Query Language (KQL). Use the Advanced Mode only if you know KQL and the functionality that is enabled for the managed properties.
  
 **To configure the query for a Content Search Web Part**
  
1.  Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the publishing site collection. 
    
2. Browse to the page that contains the Content Search Web Part that you want to configure.
    
3. Click the **Settings** menu, and then click **Edit Page**.
    
4. In the Web Part, click the **Content Search Web Part Menu** arrow, and then click **Edit Web Part**.
    
5. In the Web Part tool pane, in the **Properties** section, in the **Search Criteria** section, click **Change query**.
    
6. On the **BASICS** tab, do one of the following: 
    
  - To define your query by using Quick Mode, select options as described in the following table:
    
   **Quick Mode (default)**

|||
|:-----|:-----|
|Select a query  <br/> |Select a result source to specify which content should be searched. If you have shared a document library or list as catalog, the catalog result source will be displayed in this drop-down list. By default, this is set to **Recently changed items (System).** <br/> |
|Restrict results by app  <br/> |Select an option from the list to restrict results to a specific site, library, list, or URL. By default, this is set to **Current site**.  <br/> |
|Restrict by tag  <br/> |You can limit results to content that is tagged with a term from a term set.  <br/> Select one of the following options:  <br/> |||
|:-----|:-----|
|Don't restrict by any tag  <br/> |Search results will not be limited based on tags (default).  <br/> |
|Restrict by navigation term of current page  <br/> |Search results will be limited to content that is tagged with the term of the current page. The current tag is displayed as the last part of the friendly URL. This option is only meaningful for sites that use managed navigation.  <br/> |
|Restrict by current and child navigation  <br/> |Search results will be limited to content that is tagged with the term of the current page (displayed as the last part of the friendly URL), and content that is tagged with sub-terms of the current page. This option is only meaningful for sites that use managed navigation.  <br/> > [!NOTE]> In a cross-site publishing scenario, this selection will only work when the result source selected in the **Select a query** section is the catalog result source that is created when a publishing site is connected to a catalog.           |
|Restrict on this tag  <br/> |Search results will be limited to content that is tagged with the tag that you type inside the box.  <br/> |
   
|
   
  - To create your own query by using Keyword Query Language (KQL), click **Switch to Advanced Mode**. For information about KQL, see [Keyword Query Language (KQL) syntax reference](https://msdn.microsoft.com/en-us/library/ee558911%28v=office.15%29.aspx). When you configure the query in Advanced Mode, you can also use query variables. Query variables are placeholders for values that change dynamically depending on the context of the page when the page that contains the Content Search Web Part is being displayed. The correct information is inserted dynamically from the context the query is sent to the index. Examples of query variables are {User.Name}, which represents the name of the user who is viewing the page, or {searchBoxQuery}, which represents the query that a user typed in a search box. Select options as described in the following table: 
    
    > [!NOTE]
    > When you switch to Advanced Mode, the result source that you selected from **Select a query** is replaced by a different result source. This result source could affect the search results. Therefore, make sure that you check the search results that are displayed in the **SEARCH RESULT PREVIEW** section, and add query configuration in the **Query text** field if you need to. 
  
   **Advanced Mode**

|||
|:-----|:-----|
|Select a query  <br/> |Select a result source to specify which content should be searched.  <br/> Default result source is Local SharePoint Results (System).  <br/> |
|Keyword filter  <br/> |You can use keyword filters to add query variables to your query. See [Query variables in SharePoint Server](../technical-reference/query-variables.md) for a list of available query variables.  <br/> You can select pre-defined query variables from the drop-down list, and then add them to the query by clicking **Add keyword filter**.  <br/> |
|Property filter  <br/> |You can use property filters to query the content of managed properties that are set to queryable in the search schema.  <br/> You can select managed properties from the **Property filter** drop-down list. Click **Add property filter** to add the filter to the query.  <br/> |
|Query text  <br/> |Type your query by using Keyword Query Language (KQL), or use the **Keyword filter** and **Property filter** lists to build the query.  <br/> The keyword query can consist of free-text keywords, property filters, or operators. Use braces to enclose query variables. The query variables will be replaced with an actual value when the query is run.  <br/> Keyword queries have a maximum length of 2,048 characters.  <br/> |
   
7. The **REFINERS** tab lists the managed properties that are enabled as refiners in the search schema. You can specify that the search results returned in the Content Search Web Part should be limited to one or more values from the refiners. Click a refiner in the list, and then click **Apply** to add it to the query. 
    
    Click **Show more** if you want to define grouping of results. Under **Group results**, you can specify that the results should be grouped based on one or more managed properties. This is useful when you are displaying several variants for a given item, and want to group them under a single result.
    
8. On the **SORTING** tab, you can specify how search results should be sorted. 
    
    This tab is available only if you use **Advanced Mode**. If you use **Quick Mode**, you can define sorting options in the result source.
    
    In the **Sort by** drop-down list, select a managed property from the list of managed properties that are set as sortable in the search schema, and then select **Descending** or **Ascending**. For example, to sort by relevance (that is, to use a ranking model) select **Rank**. 
    
    To add more sorting levels, click **Add sort level**.
    
    > [!NOTE]
    > Sorting of search results is case sensitive. 
  
    > [!IMPORTANT]
    > If your result source contains sorting, you should not specify sorting in the Content Search Web Part. This is because the sorting in the result source overrides the sorting that you specify in the Content Search Web Part. 
  
    If you selected **Rank** from the **Sort by** list, you can select which ranking model to use for sorting in the **Ranking Model** list. 
    
    Under **Dynamic ordering**, you can specify additional ranking by adding rules that will change the order of results when certain conditions apply. Click **Add dynamic ordering rule**, and then specify conditional rules. 
    
9. On the **SETTINGS** tab, specify the settings that are listed in the following table. 
    
|||
|:-----|:-----|
|Query Rules  <br/> |Select whether to use Query Rules or not.  <br/> |
|URL Rewriting  <br/> |Select if the URL rewrite to the item details page should continue to be relative for each catalog item as defined when you set up the catalog connection. If you select **Don't rewrite URLs**, the URLs for catalog items are pointed directly to the library item of the connected catalog.  <br/> |
|Loading Behavior  <br/> |Select when the search results returned by the Content Search Web Part appear on the web page. The default option is **Sync option: Issue query from the server**. By using this loading behavior, queries are issued from the server, and the search results are included in the page response that is sent back from SharePoint Server. If you select **Async option: Issue query from the browser**, the queries will be issued from the end-users browser after the complete page is received. This option may be considered for secondary content on a page — for example Recommendations or Popular Items.  <br/> |
|Priority  <br/> |Select the level that best describes the relative importance of content that is displayed by this Web Part in relation to other Search Web Parts. If SharePoint Server is running under heavy load, the queries will be run according to their priority.  <br/> |
|Caching  <br/> |Select one Active Directory security group if you want search results to be cached for users in the group. By caching search results for a security group, you can reduce page reload time.  <br/> > [!NOTE]> You should only select a security group where search results are identical for all users in the group. For more information, see [this article](https://blogs.technet.com/b/helgesolheim/archive/2014/03/19/new-group-cache-for-the-content-search-web-part.aspx).           |
   
10. On the **TEST** tab, you can preview the query that is sent by the Content Search Web Part. 
    
|||
|:-----|:-----|
|**Query text** <br/> | Shows the final query that will be run by the Content Search Web Part. It is based on the original query template where dynamic variables are substituted with current values. Other changes to the query may have to be made as part of query rules.  <br/> |
   
    Click **Show more** to display additional information. 
    
|||
|:-----|:-----|
|Query template  <br/> |Shows the content of the query template that is applied to the query.  <br/> |
|Refined by  <br/> |Shows the refiners applied to the query as defined on the **REFINERS** tab.  <br/> |
|Grouped by  <br/> |Shows the managed property on which search results should be grouped as defined on the **REFINERS** tab.  <br/> |
|Applied query rules  <br/> |Shows which query rules are applied to the query.  <br/> |
   
    The **Query template variables** section shows the query variables that will be applied to the query, and the values of the variables that apply to the current page. You can type other values to test the effect they will have on the query. Click the **Test Query** button to preview the search results. 
    
    You can also test how the query works for different user segment terms. Click **Add user segment term** to add terms to be added to the query. Click the **Test query** button to preview the search results. 
    
|||
|:-----|:-----|
|Query text  <br/> |Shows the final query that will be run by the Content Search Web Part. It is based on the original query template where dynamic variables are substituted with current values. Other changes to the query may have to be made as part of query rules.  <br/> |
   
## Configure the display templates for the Content Search Web Part
<a name="BKMK_ConfigureDisplayTemplates"> </a>

When you connect a publishing site to a catalog, the default control display template for the Content Search Web Part on your category page is List with Paging (named Control_ListWithPaging in the Master Page Gallery).
  
The default item display template for the Content Search Web Part is Picture on top, 3 lines on bottom (named Item_Picture3Lines in the Master Page Gallery). If you want to use other display templates on your category page, you can change them by changing the settings for the Content Search Web Part.
  
For information on how to customize and create your own display templates, see [SharePoint 2013 Design Manager display templates](https://msdn.microsoft.com/library/jj945138.aspx). For information about JavaScript methods that you can use when you customize your display templates, see [Srch.U object (DisplayTemplatesSrch)](https://msdn.microsoft.com/library/dn768292%28v=office.15%29.aspx).
  
## Add a Refinement Web Part to a page
<a name="BKMK_AddRefinementPanel"> </a>

You can add refiners to a page to narrow the items that are shown in a Content Search Web Part, and help users quickly browse to specific content. Refiners are based on managed properties from the search index. To display refiners on a page, you must first enable the managed property that you want to use as a refiner, and then add a Refinement Web Part to the page where you want the refiners to appear. You can configure the Refinement Web Part for two types of refiners: **Stand-alone refiners** and **Refiners for faceted navigation**. For more information about the different refiner types, see [Plan refiners and faceted navigation](plan-search-for-sharepoint-cross-site-publishing-sites.md#BKMK_PlanRefinersAndFacetedNavigation) in [Plan search for cross-site publishing sites in SharePoint Server 2016](plan-search-for-sharepoint-cross-site-publishing-sites.md).
  
Before you begin this procedure, verify the following:
  
- The managed properties that you want to use as refiners are enabled as refinable managed properties as described in "Map a crawled property to a refinable managed property in SharePoint site collection administration" or "Enable automatically created managed properties as refiners in SharePoint Central Administration " in [Configure refiners and faceted navigation in SharePoint Server](configure-refiners-and-faceted-navigation.md).
    
- You have done a full crawl of the content source that contains the managed properties that are enabled as refiners, or indicated that your catalog should be fully reindexed during the next scheduled crawl of the catalog as described in "Configure search for cross-site publishing" in [Configure cross-site publishing in SharePoint Server](configure-cross-site-publishing.md).
    
- If you are using refiners for faceted navigation, you have configured the refiners as described in "Add refiners to a term set" in [Configure refiners and faceted navigation in SharePoint Server](configure-refiners-and-faceted-navigation.md).
    
 **To add a Refinement Web Part to a page**
  
1.  Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the publishing site collection. 
    
2. Browse to the page where you want to add the Web Part.
    
3. Click the **Settings** menu, and then click **Edit Page**. 
    
4. In the Web Part Zone where you want to add the Web Part, click **Add a Web Part**.
    
5. In the **Categories** list, select **Search**.
    
6. In the **Parts** list, select **Refinement**, and then click **Add**.
    
## Configure the Refinement Web Part
<a name="BKMK_ConfigureRPWP"> </a>

 **To configure the Refinement Part**
  
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the publishing site collection.
    
2. Browse to the page that contains the Refinement Web Part that you want to configure.
    
3. Click the **Settings** menu, and then click **Edit Page**.
    
4. In the Web Part, click the **Refinement Web Part Menu** arrow, and then click **Edit Web Part**. 
    
5. You can configure the Web Part for stand-alone refiners or for refiners for faceted navigation by using the following procedures,
    
  - To configure the Web Part for stand-alone refiners:
    
1. In the Web Part tool pane, in the **Properties for Search Refinement** section, verify that the **Choose Refiners in this Web Part** is selected. 
    
2. Click **Choose Refiners…**
    
3. On the **Refinement configuration** page, from the **Available refiners** section, use the buttons to select which refiners should be added to the term set, and also in which order that they should be displayed. If you have specified an alias for a refinable managed property, this alias is displayed in the **Configuration for** section. 
    
4. In the **Configuration for** section, set the configuration for how every refiner appears. 
    
    > [!NOTE]
    > If you have a single language site, you can change the refiner display name in the **Display name** section. For multilingual sites, you have to change the refiner display language as described in [Change the refiner display name](configure-search-web-parts.md#BKMK_ChangeDisplayName). 
  
  - To configure the Web Part for refiners for faceted navigation:
    
1. In the Web Part tool pane, in the **Properties for Search Refinement** section, select the option **Use the refinement configuration defined in the Managed Navigation term set**.
    
## Change the refiner display name
<a name="BKMK_ChangeDisplayName"> </a>

When you add a Refinement Web Part, the name of the managed property that is enabled as a refiner will be used as display name for the refiner. In many cases, the managed property name is not user-friendly — for example, RefinableString00 or ColorOWSTEXT. You can change the display name of the refiner by changing a java script file in the master page gallery.
  
 **To change the refiner display name**
  
1.  Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the publishing site collection. 
    
2. On the **Settings** menu, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Web Designer Galleries** section, click **Master pages and page layouts**. 
    
4. On the **Master Page Gallery** page, click **Display Templates**.
    
5. On the **Display Templates** page, click **Language Files**.
    
6. On the **Language Files** page, click the folder that contains the language that you want to change the refiner display name for. 
    
7. Open the **CustomStrings.js** file. 
    
8. Add one line to the file for each managed property that is enabled as a refiner for which you want to change the display name byusing the following syntax: 
    
     `"rf_RefinementTitle_ManagedPropertyName": "Sample Refinement Title for ManagedPropertyName"`
    
    For example, you can add the following line to change the display name for the managed property RefinableInt00 to Price: 
    
     `"rf_RefinementTitle_RefinableInt00": "Price"`.
    
## Display refiner counts in a Refinement Web Part
<a name="BKMK_DisplayRefinerCounts"> </a>

When you add a Refinement Web Part to a page, by default, the Web Part will not show refiner counts — that is, the number of items for each refiner value. For example, if you have enabled the managed property Color as a refiner, the refiner values will only show colors such as Red, Green, and Blue. You can add refiner counts by changing a value in an HTML file so that the refiner values are shown as Red (10), Green (12), and Blue (8). 
  
 **To add refiner counts to the Refinement Web Part**
  
1.  Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the publishing site collection. 
    
2. On the **Settings** menu, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Web Designer Galleries** section, click **Master pages and page layouts**. 
    
4. On the **Master Page Gallery** page, click **Display Templates**.
    
5. On the **Display Templates** page, click **Filters**.
    
6. Open the **Filter_Default.html** file. 
    
7. Change the value for **ShowCounts** to **true**.
    
## Configure the display templates for the Refinement Web Part
<a name="BKMK_ConfigureRefinementDisplayTemplates"> </a>

The display templates for the Refinement Web Part can be found in the Master Page Gallery.
  
 **To view display templates for the Refinement Web Part**
  
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the publishing site collection.
    
2. On the **Settings** menu, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Web Designer Galleries** section, click **Master pages and page layouts**. 
    
4. On the **Master Page Gallery** page, click **Display Templates**.
    
5. On the **Display Templates** page, click **Filters**.
    
For information on how to customize and create your own display templates, see [SharePoint 2013 Design Manager display templates](https://msdn.microsoft.com/library/jj945138.aspx).
  
## Add a Taxonomy Refinement Panel Web Part to a page
<a name="BKMK_AddTaxonomyRefinementPanel"> </a>

Before you begin this procedure, verify the following: 
  
- The managed properties that you want to use as refiners are refiner-enabled as described in "Map a crawled property to a refinable managed property in SharePoint site collection administration" or "Enable automatically created managed properties as refiners in SharePoint Central Administration " in [Configure refiners and faceted navigation in SharePoint Server](configure-refiners-and-faceted-navigation.md).
    
- You have done a full crawl of the content source that contains the managed properties that are enabled as refiners as described in "Configure search for cross-site publishing" in [Configure cross-site publishing in SharePoint Server](configure-cross-site-publishing.md).
    
- If you are using refiners for faceted navigation, you have configured the refiners as described in [Configure refiners and faceted navigation in SharePoint Server](configure-refiners-and-faceted-navigation.md).
    
 **To add a Taxonomy Refinement Panel Web Part to a page**
  
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the publishing site collection.
    
2. Browse to the page where you want to add the Web Part.
    
3. Click the **Settings** menu, and then click **Edit Page**. 
    
4. In the Web Part Zone where you want to add the Web Part, click **Add a Web Part**.
    
5. In the **Categories** list, select **Search**.
    
6. In the **Parts**, select **Taxonomy Refinement Panel**, and then click **Add**.
    
## Configure the Taxonomy Refinement Panel Web Part
<a name="BKMK_ConfigureTaxonomyRefinementPanelWP"> </a>

 **To configure the Taxonomy Refinement Panel Web Part**
  
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the publishing site collection.
    
2. Browse to the page where you have the Taxonomy Refinement Panel Web Part that you want to configure.
    
3. On the **Settings** menu, click **Edit Page**.
    
4. In the Web Part, click the **Taxonomy Refinement Panel Web Part Menu** arrow, and then click **Edit Web Part**. 
    
5. In the Web Part tool pane, in the **Properties** section, in the **Query** section, on the **Refinement Target** menu, select the Web Part you want to associate with the Taxonomy Refinement Panel Web Part. 
    
6. In the Web Part tool pane, in the **Properties** section, in the **Query** section, on the **Refiner** menu, select the managed property that you have specified for Managed Navigation. 
    
## Add a Recommended Items Web Part to a page
<a name="BKMK_AddRecs"> </a>

You can use the Recommended Items Web Part to show content recommendations based how users have previously interacted with the site. For example, you can add this Web Part to a Catalog Item page. If a user views a specific item, this Web Part will display other items that users have previously viewed, such as "Users who viewed this item also viewed these items." For more information about recommendations, see [Plan usage analytics, usage events and recommendations](plan-search-for-sharepoint-cross-site-publishing-sites.md#BKMK_PlanAnalytics) in [Plan search for cross-site publishing sites in SharePoint Server 2016](plan-search-for-sharepoint-cross-site-publishing-sites.md). 
  
 **To add a Recommended Items Web Part to a page**
  
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the publishing site collection.
    
2. Browse to the page where you want to add the Web Part.
    
3. Click the Settings menu, and then click **Edit Page**.
    
4. In the Web Part Zone where you want to add the Web Part, click **Add a Web Part**.
    
5. In the **Categories** list, click **Search-Driven Content**.
    
6. In the **Parts** list, click **Recommended Items**, and then click **Add**.
    
## Configure the Recommended Items Web Part
<a name="BKMK_ConfigureRecs"> </a>

 **To configure the query for a Recommended Items Web Part**
  
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the publishing site collection.
    
2. Browse to the page where you have the Recommended Items Web Part that you want to configure.
    
3. On the **Settings** menu, click **Edit Page**.
    
4. In the Web Part, click the **Recommended Items Web Part Menu** arrow, and then click **Edit Web Part**. 
    
5. In the Web Part tool pane, in the **Properties** section, in the **Search Criteria** section, click **Change query**.
    
6. On the **BASICS** tab, define your query by selecting options described in the following table. 
    
|||
|:-----|:-----|
|Get recommended items for  <br/> |From the drop-down list, select from which value recommendations should be displayed. In a catalog scenario, this will often be **A token from a URL**. If you select this option, you will also have to select which URL token you want to obtain recommendations for.  <br/> For example, let's say that you want to obtain recommendations for items in your catalog. You have a catalog item page where you display your catalog items, and the item number is part of your friendly URL — for example, www.contoso/audio/mp3/4010101. (4010101 represents the item number.) When you want to obtain recommendations for a token from the URL, you should select {URLToken.1} (4010101) from the second drop-down list.  <br/> |
|Restrict results by app  <br/> |Use this drop-down list to specify a scope for the search results.  <br/> |
|Restrict results by content type  <br/> |Use this drop-down list to limit the search results to a specific content type.  <br/> |
|If there are too few recommended items  <br/> |If you don't have much usage data — for example, if your site is fairly new, or if the items do not have recommendations to display — this Web Part will not display any search results. In order for the Web Part to display recommendations even though not enough user data has cumulated, you can select the option to **Select a query to fill in with additional results**.  <br/> |
   
7. The **REFINERS** tab lists the managed properties that are set as refiner-enabled in the search schema. You can specify that the search results returned in the Recommended Items Search Web Part should be limited to one or more values from the refiners. Click a refiner in the list, and then click **Apply** to add it to the query. 
    
    Click **Show more** if you want to define grouping of results. Under **Group results**, you can specify that the results should be grouped based on one or more managed properties.
    
8. On the **SETTINGS** tab, specify the following: 
    
|||
|:-----|:-----|
|Query Rules| Select whether to use Query Rules or not. |
|URL Rewriting|Select if the URL rewrite to the item details page should continue to be relative for each catalog item as defined when you set up the catalog connection. If you select **Don't rewrite URLs**, the URLs for your catalog items are pointed directly to the library item of the connected catalog.|
|Loading Behavior|Select when the search results returned by the Recommended Items Web Part should be displayed on the web page. The default option is **Display the page and web party simultaneously**. By using this loading behavior, queries are issued from the server, and the search results are included in the page response that is sent back from SharePoint Server. If you select **Display the page and web part independently**, the queries will be issued from the end-users browser after the complete page is received. This option may be considered for secondary content on a page — for example, Recommendations or Popular Items|
|Priority|Select the level that best describes the relative importance of content that is displayed by this Web Part in relation to other Search Web Parts. If SharePoint Server is running under heavy load, the queries will be run according to their priority.|
|Caching|Select one Active Directory security group if you want search results to be cached for users in the group. By caching search results for a security group, you can reduce page reload time.> [!NOTE]> You should only select a security group where search results are identical for all users in the group. For more information, see [this article](https://blogs.technet.com/b/helgesolheim/archive/2014/03/19/new-group-cache-for-the-content-search-web-part.aspx).           |
   
9. On the **TEST** tab, you can preview the query that is sent by the Recommended Items Web Part. 
    
|||
|:-----|:-----|
|Query text  <br/> |Shows the content of the query template that is applied to the query.  <br/> |
   
    Click **Show more** to display additional information. 
    
|||
|:-----|:-----|
|Refined by  <br/> |Shows the refiners applied to the query as defined in the **REFINERS** tab.  <br/> |
|Grouped by  <br/> |Shows the managed property on which search results should be grouped as defined in the **REFINERS** tab.  <br/> |
|Applied query rules  <br/> |Shows which query rules are applied to the query.  <br/> |
   
    In the **Query template variables** section, the selections that you made on the BASIC tab are displayed. In addition, you can type additional values for testing as outlined in the following table. Click the **Test query** button to preview the search results. 
    
|||
|:-----|:-----|
|{RecsURL}\*  <br/> |Shows the token you selected when specifying for which value recommendations should be displayed.  <br/> |
|{Scope}\*  <br/> |Shows the scope that you selected for the search results.  <br/> |
|{ContentTypeID}\*  <br/> |Shows the content type that you selected for the search results.  <br/> |
   
    You can also test how the query works for different user segment terms. Click **Add user segment term for testing** to add terms to be added to the query. Click the **Test query** button to preview the search results. 
    
|||
|:-----|:-----|
|Query text  <br/> |Shows the final query that will be run by the Recommended Items Web Part. It is based on the original query template where dynamic variables are substituted with current values. Other changes to the query may have be made as part of query rules.  <br/> |
   
## Configure the display templates for the Recommended Items Web Part
<a name="BKMK_ConfigureRecsDisplayTemplates"> </a>

The default control display template for the Recommended Items Search Web Part is List (known as Control_List in the Master Page Gallery).
  
The default item display template for the Recommended Items Web Part is Recommended Items: Picture on top, 3 lines (known as Item_RecommendationsClickLogging in the Master Page Gallery). When a user clicks a link that is displayed in the Recommended Items Web Part, the default display template logs a Recommendations Clicked usage event.
  
For information on how to customize and create your own display templates, see [SharePoint 2013 Design Manager display templates](https://msdn.microsoft.com/library/jj945138.aspx). For information about JavaScript methods that you can use when you customize your display templates, see [Srch.U object (DisplayTemplatesSrch)](https://msdn.microsoft.com/library/dn768292%28v=office.15%29.aspx).
  
## See also
<a name="BKMK_ConfigureRecsDisplayTemplates"> </a>

#### Concepts

[Query variables in SharePoint Server](../technical-reference/query-variables.md)
#### Other Resources

[Blog series: How to set up a product-centric website in SharePoint Server 2013](https://blogs.technet.com/b/tothesharepoint/archive/2013/02/14/how-to-set-up-a-product-centric-web-site-in-sharepoint-2013.aspx)

