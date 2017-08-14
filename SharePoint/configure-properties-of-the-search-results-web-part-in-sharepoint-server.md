---
title: Configure properties of the Search Results Web Part in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: d0e68cf4-80f6-4f1f-af49-a3b9c43408ac
---


# Configure properties of the Search Results Web Part in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-18* **Summary:** Learn how to configure the query and properties of the Search Results Web Part, and how to disable stemming in the Web Part.The Search Results Web Part displays the search results of a query entered in a Search Box Web Part. By default, the Search Results Web Part is used on all search vertical pages (results.aspx, peopleresults.aspx, conversationresults.aspx, videoresults.aspx). The Search Results Web Part displays the actual search results and it also passes the search results to the Refinement Web Part and the Search Navigation Web Part on the same page.The Search Results Web Part uses a query that is specified in the Web Part to display search results. By default, the query defined in this Web Part uses the query variable {searchboxquery}. The query variable is a placeholder for a value. When a query is run, the placeholder is replaced with a value. For example, when a user types the search phrase  *yellow*  in the Search Box Web Part, the {searchboxquery} variable in the Search Results Web Part will resolve to search all items that contain the phrase *yellow*  .By changing the properties and query in the Search Results Web Part you can you can do the following:
- Limit search results to a result source.
    
  
- Add query variables or property filters that customize search results for different users.
    
  
- Promote or demote items or pages within the search results.
    
  
- Change the sorting of the search results.
    
  
- Change the display template.
    
  
In this article:
-  [Before you begin](#begin)
    
  
-  [Configure properties of the Search Results Web Part](#BKMK_ConfigureProperties)
    
  
-  [To disable stemming in a Search Results Web Part](#BKMK_DisableStemming)
    
  

## Before you begin
<a name="begin"> </a>


> [!NOTE:]
>  [Plan browser support](https://go.microsoft.com/fwlink/p/?LinkId=246502)> **Accessibility for SharePoint 2013**>  [Accessibility features in SharePoint 2013 Products](https://go.microsoft.com/fwlink/p/?LinkId=246501)>  [Keyboard shortcuts](https://go.microsoft.com/fwlink/p/?LinkID=246504)>  [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506)
  
    
    


## Configure properties of the Search Results Web Part
<a name="BKMK_ConfigureProperties"> </a>

 **To configure the properties of a Search Results Web Part**
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the Enterprise Search Center site.
    
  
2. On the search results page, click the **Settings** menu, and then click **Edit Page**.
    
  
3. In the Search Results Web Part, click the **Search Results Web Part Menu** arrow, and then click **Edit Web Part**.
    
  
4. In the Web Part tool pane, in the **Search Criteria** section, click **Change query**.
    
  
5. On the **BASICS** tab, do one of the following:
    
  - To define your query by using Keyword Query Language (KQL), select options as described in the following table:
    
### Advanced Mode (default)

 **Select a query** <br/>  Select a result source to specify which content should be searched. <br/>  By default, the following result sources are set for the different search vertical pages: <br/>  Everything (results.aspx): **Local SharePoint Results (System)** <br/>  People (peopleresults.aspx): **Local People Results (System)** <br/>  Conversations (conversationresults.aspx): **Conversations (System)** <br/>  Videos (videoresults.aspx): **Local Video Results (System)** <br/> **Keyword filter** <br/> You can use keyword filters to add query variables to your query. For a list of available query variables,see  [Query variables in SharePoint Server](html/query-variables-in-sharepoint-server.md).  <br/> You can select pre-defined query variables from the drop-down list, and then add them to the query by clicking **Add keyword filter**. <br/> **Property filter** <br/> You can use property filters to query the content of managed properties that are set to  *queryable*  in the search schema. <br/> You can select managed properties from the **Property filter** drop-down list. Click **Add property filter** to add the filter to the query. <br/> **Query text** <br/> By default, the query variable {searchboxquery} is defined for this field. You can change the query text by using KQL. For more information about KQL, see  [Keyword Query Language (KQL) syntax reference](https://msdn.microsoft.com/en-us/library/ee558911%28v=office.15%29.aspx). Alternatively you can use the **Keyword filter** and **Property filter** lists to build the query. <br/> The keyword query can consist of free-text keywords, property filters, or operators. Use braces to enclose query variables. The query variables will be replaced with an actual value when the query is run.  <br/> Keyword queries have a maximum length of 2,048 characters.  <br/>   - To define your query by using pre-defined variables, click **Switch to Quick Mode**. Select options as described in the following table:
    
### Quick Mode

 **Select a query** <br/> Select a result source to specify which content should be searched. If you have shared a document library or list as catalog, the catalog result source will be displayed in this drop-down list.  <br/> **Restrict by app** <br/> Select an option from the list to restrict results to a specific site, library, list, or URL.  <br/> **Restrict by tag** <br/> You can limit results to content that is tagged with a term from a term set.  <br/> Select one of the following options:  <br/> 
### 

 **Don’t restrict by any tag** <br/> Search results will not be limited based on tags (default).  <br/> **Restrict by navigation term of current page** <br/> Search results will be limited to content that is tagged with the term of the current page. The current tag is displayed as the last part of the friendly URL. This option is only meaningful for sites that use managed navigation.  <br/> **Restrict by current and child navigation** <br/> Search results will be limited to content that is tagged with the term of the current page (displayed as the last part of the friendly URL), and content that is tagged with sub-terms of the current page. This option is only meaningful for sites that use managed navigation.  <br/> **Restrict on this tag** <br/> Search results will be limited to content that is tagged with the tag that you type inside the box.  <br/> 
    > [!NOTE:]
      
6. The **REFINERS** tab lists the managed properties that are enabled as refiners in the search schema. You can specify that the search results returned in the Search Results Web Part should be limited to one or more values from the refiners. Select a refiner in the list, and then click **Add** to add it to the query.
    
    Click **Show more** if you want to define grouping of results. Under **Group results**, you can specify that the results should be grouped based on one or more managed properties. This is useful when you are displaying several variants for a given item, and want to group them under a single result.
    
  
7. On the **SORTING** tab, you can specify how search results should be sorted. This tab is available only if you use **Advanced Mode**. If you use **Quick Mode**, you can define sorting options in the result source.
    
    In the **Sort by** drop-down list:
    
1. Select a managed property from the list of managed properties that are set as sortable in the search schema, and then select **Descending** or **Ascending**. To add more sorting levels, click **Add sort level**.
    
    > [!NOTE:]
      

    > [!IMPORTANT:]
      
2. Select **Rank** to sort by relevance rank. You can then specify which ranking model to use or specify dynamic ordering rules.
    
  - (Optional) Select which ranking model to use for sorting in the **Ranking Model** list.
    
  
  - Under **Dynamic ordering**, you can specify additional ranking by adding rules that will change the order of results when certain conditions apply. Click **Add dynamic ordering rule**, and then specify conditional rules.
    
  
8. On the **SETTINGS** tab, specify the settings that are listed in the following table.
    
### 

 **Query Rules** <br/> Select whether to use Query Rules or not.  <br/> **URL Rewriting** <br/> Select if the URL rewrite to the item details page should continue to be relative for each catalog item as defined when you set up the catalog connection. This option is only meaningful for sites that use managed navigation and have connected to a catalog that uses anonymous access for the catalog pages. If you select **Don’t rewrite URLs**, the URLs for catalog items are pointed directly to the library item of the connected catalog. <br/> **Loading Behavior** <br/> Select when the search results returned by the Search Results Web Part appear on the web page. The default option is **Async option: Issue query from the browser**. Queries will be issued from the end-users browser after the complete page is received. This option may be considered for secondary content on a page — for example, Recommendations or Popular Items. If you select **Sync option: Issue query from the server**, queries are issued from the server, and the search results are included in the page response that is sent back from SharePoint Server. <br/> 9. On the **TEST** tab, you can preview the query that is sent by the Search Results Web Part.
    
### 

 **Query text** <br/>  Shows the final query that will be run by the Search Results Web Part. It is based on the original query template where dynamic variables are substituted with current values. Other changes to the query may be made as part of a query rule. <br/> 
    Click **Show more** to display additional information.
    
### 

 **Query template** <br/> Shows the content of the query template that is applied to the query.  <br/> **Refined by** <br/> Shows the refiners applied to the query as defined on the **REFINERS** tab. <br/> **Grouped by** <br/> Shows the managed property on which search results should be grouped as defined on the **REFINERS** tab. <br/> **Applied query rules** <br/> Shows which query rules are applied to the query.  <br/> 
    The **Query template variables** section shows the query variables that will be applied to the query, and the values of the variables that apply to the current page. You can type other values to test the effect they will have on the query. Click the **Test Query** button to preview the search results.
    
    You can also test how the query works for different user segment terms. Click **Add user segment term** to add terms to be added to the query.
    
    Click the **Test query** button to preview the search results.
    
### 

Query text  <br/> Shows the final query that will be run by the Search Results Web Part. It is based on the original query template where dynamic variables are substituted with current values. Other changes to the query may be made as part of a query rule.  <br/> 10. In the Web Part tool pane, in the **Display Templates** section, the default selection is **Use result types to display items**. This selection will apply different display templates according to the result type of the search result. For example, if the result type of a search result is a PDF file, the display template **PDF Item** will be applied. If the result type of a search result is an image, the **Picture Item** display template will be applied. To apply one display template to all result types of the search results, select **Use a single template to display items**, and then select the display template that you want to apply.
    
  
11. In the Web Part tool pane, in the **Settings** section, in the **Results Settings**, to further specify how search results should be shown, change the values in the following fields:
    
  - **Number of results per page** The number of search results to be displayed per page.
    
  
  - **Show ranked results** Clear the check box if you want to show only promoted blocks (such as promoted results or personal favorites) or result controls (such as result counts) instead of the ranked results.
    
  
  - **Show promoted results** Clear the check box if you do not want to show search results that you have promoted by using Query rules.
    
  
  - **Show "Did you mean?"** Clear the check box if you do not want to show query spelling corrections as **Did you mean** suggestions. For more information about query spelling corrections, see [Manage query spelling correction in SharePoint Server](html/manage-query-spelling-correction-in-sharepoint-server.md).
    
  
  - **Show personal favorites** Clear the check box if you do not want to show personal favorites.
    
  
  - **Show View Duplicates link** Select the check box if you want to show a **View Duplicates** link.
    
  
  - **Show link to search center** Select the check box if you want to show a link to the Search Center.
    
  
12. In the Web Part tool pane, in the **Settings** section, in the **Results control settings** section, to specify how search results should be shown, change the values in the following fields:
    
  - **Show advanced link** Clear the check box if you don’t want to show a link to the Advanced Search page in the Web Part.
    
  
  - **Show result count** Clear the check box if you don't want to show the number of results found in the Web Part.
    
  
  - **Show language dropdown** Clear the check box if you don't want to show the language drop-down in the Web Part.
    
  
  - **Show sort dropdown** Select the check box if you want to show the sort drop-down in the Web Part.
    
  
  - **Show paging** Clear the check box if you don't want to show paging in the Web Part.
    
  
  - **Show preferences link** Clear the check box if you don't want to show a link to the preferences page in the Web Part.
    
  
  - **Show AlertMe link** Clear the check box if you don't want to show a link to the **Alert Me** page in the Web Part. For more information about search alerts, see [Enable search alerts in SharePoint Server](html/enable-search-alerts-in-sharepoint-server.md).
    
  

## To disable stemming in a Search Results Web Part
<a name="BKMK_DisableStemming"> </a>

Stemming means that nouns and adjectives in a query are expanded to different possible inflections. For example, if a person enters the English word "foot" in a query, it is automatically expanded to {"feet"}. Similarly, the word "overview" is expanded to {"overviews"}. **To disable stemming in a Search Results Web Part**
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the Enterprise Search Center site.
    
  
2. On the search results page, click the **Settings** menu, and then click **Edit page**.
    
  
3. In the Search Results Web Part, click the **Search Results Web Part Menu** arrow, click **Export…**, and then save the Web Part to your computer.
    
  
4. Open the Web Part in a text editor — for example, Notepad.
    
  
5. Change the value for **EnableStemming** to **false**, and then save the file with a new name — for example, Search_Results_NoStemming.webpart.
    
  
6. On the search results page, in the **Main Zone**, click **Add a Web Part**.
    
  
7. In the **Categories** section, click the **Upload a Web Part** arrow.
    
  
8. In the **Upload a Web Part** section, click **Browse** to find the Web Part file that you have edited, and then click **Upload**.
    
  
9. To add the customized **Search Results Web Part** to the search results page, do the following:
    
  - Browse to the search results page.
    
  
  - Click the **Settings** menu, and then click **Edit Page**.
    
  
  - In the Web Part Zone where you want to add the Web Part, click **Add a Web Part**.
    
  
  - In the **Categories** list, select **Imported Web Parts**.
    
  
  - In the **Parts** list, select the Web Part that you uploaded, and then click **Add**.
    
  
10. To remove the default Search Results Web Part from the search results page, do the following: 
    
  - Browse to the search results page.
    
  
  - Click the **Settings** menu, and then click **Edit Page**.
    
  
  - In the Web Part, click the **Search Results Web Part** menu arrow, and then click **Delete**.
    
  

> [!NOTE:]

  
    
    


# See also

#### 

 [Query variables in SharePoint Server](html/query-variables-in-sharepoint-server.md)
  
    
    
 [Configure result sources for search in SharePoint Server](html/configure-result-sources-for-search-in-sharepoint-server.md)
  
    
    
 [Plan to transform queries and order results in SharePoint Server](html/plan-to-transform-queries-and-order-results-in-sharepoint-server.md)
  
    
    

#### 

 [Blog series: How to change the way search results are displayed in SharePoint Server 2013](https://blogs.technet.com/b/tothesharepoint/archive/2013/09/03/how-to-change-the-way-search-results-are-displayed-in-sharepoint-server-2013.aspx)
  
    
    

  
    
    

