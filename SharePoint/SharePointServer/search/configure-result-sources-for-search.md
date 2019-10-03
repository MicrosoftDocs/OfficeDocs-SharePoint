---
title: "Configure result sources for search in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/8/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: d6845f9b-7c1e-4220-a24d-1e5cade8f0d8
description: "Learn how to create and manage result sources in SharePoint Server."
---

# Configure result sources for search in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Result sources limit searches to certain content or to a subset of search results. SharePoint Server provides 16 pre-defined result sources for the classic search experience. The pre-configured default result source is **Local SharePoint Results**. You can specify a different result source as the default. The modern search experience uses the default results source, so if you change the default result source for classic search, you also change it for modern search. For more information, see [Understanding result sources for search in SharePoint Server](understanding-result-sources-for-search.md).

 
    
## Create a result source
<a name="BKMK_CreateResutlSource"> </a>

You can create a result source for a Search service application, a site collection, or a site. The following table shows the permissions that are required to create a result source at each level, and where the result source can be used.
  
**Levels and permissions for result sources**

| **When you create a result source at this level** |    **You must have this permission**     |                         **The result source can be used in**                         |
| :------------------------------------------------ | :--------------------------------------- | :----------------------------------------------------------------------------------- |
| Search service application                        | Search service application administrator | All site collections in web applications that consume the Search service application |
| Site collection                                   | Site collection administrator            | All sites in the site collection                                                     |
| Site                                              | Site owner                               | The site                                                                             |
   
 **To create a result source**
  
Depending on the level at which you want to create the result source, first do one of the following: 
  
- To create a result source for a Search service application: 
    
  - Verify that the user account that performs this procedure is an administrator on the Search service application. 
    
  - In Central Administration, in the **Application Management** section, click **Manage service application**.
    
  - Click the Search service application for which you want to create a result source.
    
  - On the **Search Administration** page for the Search service application, on the Quick Launch, in the **Queries and Results** section, click **Result Sources**.
    
- To create a result source for a site collection: 
    
  - Verify that the user account that performs this procedure is an administrator for the site collection. 
    
  - On the **Settings** menu for the site collection, click **Site Settings**.
    
  - On the **Site Settings** page, in the **Site Collection Administration** section, click **Search Result Sources**.
    
- To create a result source for a site:
    
  - Verify that the user account that performs this procedure is a member of the Owners group for the site.
    
  - On the **Settings** menu for the site, click **Site Settings**.
    
  - On the **Site Settings** page, in the **Search** section, click **Result Sources**.
    
Next:
  
1. On the **Manage Result Sources** page, click **New Result Source**.
    
2. On the **Add Result Source** page, in the **General Information** section, do the following: 
    
  - In the **Name** box, type a name for the result source. 
    
  - In the **Description** box, type a description of the result source. 
    
3. In the **Protocol** section, select one of the following protocols for retrieving search results: 
    
  - **Local SharePoint**, the default protocol, provides results from the search index for this Search service application.
    
  - **Remote SharePoint** provides results from the index of a search service in another farm. 
    
    > [!IMPORTANT]
    > To use the Remote SharePoint protocol to get search results in one SharePoint Server on-premises farm from the index of another SharePoint Server on-premises farm, you must configure the farm that receives the queries to trust the farm that sends the queries. For information about how to do this, see [Configure trust for search between two SharePoint Server farms](configure-trust-for-search-between-two-sharepoint-server-farms.md). 
  
  - **OpenSearch** provides results from a search engine that uses the OpenSearch 1.0/1.1 protocol. 
    
  - **Exchange** provides results from Exchange Server through a SharePoint Server eDiscovery Center. Click **Use AutoDiscover** to have the search system find an Exchange Server endpoint automatically, or type the URL of the Exchange web service to retrieve results from — for example, https://contoso.com/ews/exchange.asmx.
    
    > [!NOTE]
    >  The Exchange protocol only enables you to discover Exchange Server content, and only from a SharePoint Server eDiscovery Center. For more information, see [Configure communication between SharePoint Server and Exchange Server](/SharePoint/governance/configure-ediscovery-0) . >  The Exchange Web Services Managed API must be installed on the computer on which the search service is running. For more information, see [Optional software supported in SharePoint Server 2016](../install/hardware-and-software-requirements.md#OptionalSoftware) in [Hardware and software requirements for SharePoint Server 2016](../install/hardware-and-software-requirements.md). 
  
4. In the previous step, if you selected either **Local SharePoint** or **Remote SharePoint** for the protocol, then in the **Type** section, select **SharePoint Search Results** to search the whole index, or select **People Search Results** to enable query processing that is specific to people search. 
    
5. If you selected **Remote SharePoint** for the protocol, then in the **Remote Service URL** section, type the address of the root site collection of the remote SharePoint farm. 
    
6. If you selected **OpenSearch 1.0/1.1** for the protocol, then in the **Source URL** section, type the URL of the OpenSearch source. 
    
7. If you selected **Exchange** for the protocol, then in the **Exchange Source URL** section, type the URL of the Exchange web service — for example, https://contoso.com/ews/exchange.asmx.
    
8. In the **Query Transform** section, do one of the following: 
    
  - Leave the default query transform ( **searchTerms**) as is. In this case, the query will be unchanged since the previous transform.
    
  - Type a different query transform in the text box. For more information, see [Understanding query transforms](https://office.microsoft.com/en-us/sharepoint-server-help/understanding-query-transforms-HA102848843.aspx).
    
  - Use the Query Builder to configure a query transform by doing the following: 
    
    - Click **Launch Query Builder**.
    
    - In the **Build Your Query** dialog box, optionally build the query by specifying filters, sorting, and testing on the tabs as shown in the following tables. 
    
**On the BASICS tab**

|                     |                                                                                                                                                                                                                                                                                                                                                            |
| :------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Keyword filter**  | You can use keyword filters to add pre-defined query variables to the query transform. You can select pre-defined query variables from the drop-down list, and then add them to the query by clicking **Add keyword filter**.  <br/><br/> For an overview of query variables, see [Query variables in SharePoint Server](../technical-reference/query-variables.md). |
| **Property filter** | You can use property filters to query the content of managed properties that are set to  *queryable*  in the search schema.   <br/><br/> You can select managed properties from the **Property filter** drop-down list. Click **Add property filter** to add the filter to the query.                                                                                 |
   
**On the SORTING tab**

|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Sort results**     | In the **Sort by** menu, you can select a managed property from the list of managed properties that are set as sortable in the search schema, and then select **Descending** or **Ascending**. To sort by relevance, that is, to use a ranking model, select **Rank**. You can click **Add sort level** to specify a property for a secondary level of sorting for search results.   Note that sorting of search results is case sensitive. |
| **Ranking Model**    | If you selected  *Rank*  from the **Sort by** list, you can select the ranking model to use for sorting.                                                                                                                                                                                                                                                                                                                                    |
| **Dynamic ordering** | You can click **Add dynamic ordering rule** to specify additional ranking by adding rules that change the order of results within the result block when certain conditions are satisfied.                                                                                                                                                                                                                                                   |
   
**On the TEST tab**

|                                                                                 |                                                                                                                                                    |
| :------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Query text**                                                                  | You can view the final query text, which is based on the original query template, the applicable query rules, and the variable values.             |
| Click **Show more** to display the options in the following rows of this table. |                                                                                                                                                    |
| **Query template**                                                              | You can view the query as it is defined in the **BASICS** tab or in the text box in the **Query transform** section on the Add Result Source page. |
| **Query template variables**                                                    | You can test the query template by specifying values for the query variables.                                                                      |
   
Finally, on the **Add Result Source** page, in the **Credentials Information** section, select the authentication type that you want for users to connect to the result source. 
  
## Set a result source as default
<a name="BKMK_Default"> </a>

 You can set any result source as the default result source. Specifying a result source as default can make it easier to edit the query in Search Web Parts. For example, when you add a Content Search Web Part to a page, the Web Part automatically uses the default result source. For more information, see [Configure Search Web Parts in SharePoint Server](../administration/configure-search-web-parts.md).

> [!NOTE]
> The modern search experience in SharePoint Server 2019 gets results from the default result source. If you change the default result source it impacts both the classic and modern search experiences.
  
 **To set a result source as default**
  
Perform the appropriate procedures in the following list depending on the level at which the result source was configured.
  
- If the result source was created at the Search service application level, do the following:
    
  1. Verify that the user account that performs this procedure is an administrator for the Search service application.
    
  2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
  3. Click the Search service application for which you want to set the result source as default.
    
  4. On the **Search Administration** page, in the **Queries and Results** section, click **Result Sources**.
    
- If the result source is at the site collection level, do the following: 
    
  1. Verify that the user account that performs this procedure is an administrator for the site collection administrator. 
    
  2. On the **Settings** menu for the site collection, click **Site Settings**.
    
  3. On the **Site Settings** page, in the **Site Collection Administration** section, click **Search Result Sources**.
    
- If the result source is at the site level, do the following: 
    
  1. Verify that the user account that performs this procedure is a member of the Owners group for the site.
    
  2. On the **Settings** menu for the site, click **Site Settings**.
    
  3. On the **Site Settings** page, in the **Search** section, click **Result Sources**.
    
- On the **Manage Result Sources** page, point to the result source that you want to set as default, click the arrow that appears, and then click **Set as Default**.
    
## See also
<a name="BKMK_Default"> </a>


[Query variables in SharePoint Server](../technical-reference/query-variables.md)

