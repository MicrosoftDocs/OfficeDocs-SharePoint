---
title: "Manage result sources"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: End User
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: fd8d6ac6-c5d0-454d-80a9-51580902b25d

description: "Result sources limit searches to certain content or to a subset of search results. You can create your own result sources, or change the predefined result sources."
---

# Manage result sources

Result sources limit searches to certain content or to a subset of search results. You can also use result sources to send queries to external providers such as Bing. 
  
A global or SharePoint admin can manage result sources for all site collections and sites in the tenant. A site collection administrator or a site owner can manage result sources for a site collection or a site, respectively. 

SharePoint Online has both a classic and a modern search experience. The modern search experience gets results from the default result source. If you change the default result source, this impacts both the classic and modern search experiences. [Learn more about the differences between the classic and modern search experiences in SharePoint Online](differences-classic-modern-search.md).
  
For the classic search experience, you can create your own result sources, or use the predefined result sources. After you create a result source, you configure Search Web Parts and query-rule actions to use it.

  
## Create a new result source
<a name="__toc342634787"> </a>

1. Go to the **Manage Result Sources** page for the tenant, for a site collection, or a site: 

  - For a tenant, in the new SharePoint admin center, select **Classic features**. Under **Search**, select **Open**, and then on the search administration page, select **Manage Result Sources**.

  - For a site collection, in your site collection, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**. Under **Site Collection Administration**, select **Search Result Sources**.
    
  - For a site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**. Under **Search**, select **Result Sources**.
    
2. On the **Manage Result Sources** page, select **New Result Source**.
    
3. In the **General Information** section, type a name and a description for the new result source. 
    
4. In the **Protocol** section, select one of the following protocols for retrieving search results: 
    
  - **Local SharePoint**, the default protocol, provides results from the search index of this tenant (Search Service).
    
  - **Remote SharePoint** provides results from the index of a search service in a different farm (external source). In the **Remote Service URL** box, type the address of the root site collection of the remote SharePoint farm. 
    
  - **OpenSearch 1.0/1.1** provides results from a search engine that uses the OpenSearch 1.0/1.1 protocol. 
    
  - **Exchange** provides results from Microsoft Exchange Server. Select **Use AutoDiscover** to have the search system find an Exchange Server endpoint automatically, or type the URL of the Exchange web service to retrieve results from — for example, https://contoso.com/ews/exchange.asmx 
    
    > [!NOTE]
    >  The Exchange Web Services Managed API must be installed on the computer where the search service is running. 
  
5. If you choose **Local SharePoint** or **Remote SharePoint** for protocol, choose a **Type**:
    
  - **SharePoint Search Results** to search the whole index. 
    
  - **People Search Results** to search in people profiles and enable query processing that is specific to people search, such as phonetic name matching or nickname matching. 
    
6. In the **Query Transform** section, you can change incoming queries to use a new query text instead. Choose one of these options: 
    
  - Leave the default query transform ( **searchTerms**) as is. The query will be unchanged since the previous transform.
    
  - Type a different query transform in the box. See [Understanding query transforms](https://support.office.com/article/b31631a5-0c1f-436e-8061-fd807bb96ae1).
    
  - Build your own query. Select **Launch Query Builder** and build your query by specifying filters on the **BASICS**, sorting on the **SORTING** tab, and then testing the query on the **TEST** tab. Each of these tabs are described in the following sections. 
    
7. In the **Credentials Information** section, choose an authentication type for users to connect to the result source. 
    
8. Select **Save**.
    
### The BASICS tab

|**Choose this option**|**To do this**|
|:-----|:-----|
|Keyword filter  <br/> |Use keyword filters to add predefined query variables to the query transform. Select query variables from the list, and add them to the query by clicking **Add keyword filter**.  <br/> |
|Property filter  <br/> |Use property filters to query the content of managed properties that are set to **queryable** in the search schema.  <br/> Select managed properties from the **Property filter** list. Click **Add property filter** to add the filter to the query. </br>**NOTE**: Custom managed properties are not shown in the **Property filter** list. To add a custom managed property to your query, in the **Query text** box, enter the name of your custom managed property followed by the query condition, for example *MyCustomColorProperty:Green*           |
   
### The SORTING tab

|**Choose this option**|**To do this**|
|:-----|:-----|
|Sort results  <br/> |Define sorting for results. The **Sort by** list contains managed properties that are set as sortable in the search schema.  <br/> Select a property to sort by, and then select **Descending** or **Ascending**. To sort by relevance, select **Rank**.  <br/> Click **Add sort level** if you want to specify more levels of sorting.  <br/> |
|Ranking model  <br/> |If you selected **Rank** from the **Sort by** list, choose the ranking model to use for sorting.  <br/> |
|Dynamic ordering  <br/> |Click **Add dynamic ordering rule** to specify additional ranking by adding rules that change the order of results within the result block when certain conditions are met. You can add conditions by choosing from the lists that appears.  <br/> |
   
### The TEST tab

|**Choose this option**|**To do this**|
|:-----|:-----|
|Query text  <br/> |See the final query text, which is based on the original query template, the applicable query rules, and the variable values.  <br/> |
|Show more  <br/> |Click the link to show more options.  <br/> |
|Query template  <br/> |See the query as it is defined in the **BASICS** tab or in the text box in the **Query transform** section on the Add Result Source page.  <br/> |
|Query template variables  <br/> |Test the query template by specifying values for the query variables. Click **Test query** to see the results.  <br/> |
   
## Set a result source as default
<a name="__toc342634788"> </a>

The default result source is **Local SharePoint Results**, but you can choose to set a different one as the default. By doing this, it will be easier to edit the query in Search Web Parts. For example, when you add a Content Search Web Part to a page, the Web Part automatically uses the default result source. 
  
1. Go to the **Manage Result Sources** page for the tenant, for a site collection, or a site: 

    - For a **tenant**, in the new SharePoint admin center, select **Classic features**. Under **Search**, select **Open**, and then on the search administration page, select **Manage Result Sources**.
    
     - For a site collection, in your site collection, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**. Under **Site Collection Administration**, select **Search Result Sources**.
    
      - For a site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**. Under **Search**, select **Result Sources**.


    
2. On the **Manage Result Sources** page, point to the result source that you want to set as the default, select the arrow that appears, and then select **Set as Default**.
    
## See also
<a name="__toc342634788"> </a>

[Understanding result sources](https://support.office.com/article/3fb2c8c4-ecbd-4210-abf7-1f0df59a370b)
  
[Understanding query transforms](https://support.office.com/article/b31631a5-0c1f-436e-8061-fd807bb96ae1)

