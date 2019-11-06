---
title: "Create query rules for web content management in SharePoint Server"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 7/21/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 838d2f49-554b-4918-b3db-ba376be9d236
description: "Learn how to improve search results by creating and managing query rules."
---

# Create query rules for web content management in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Without using any custom code, Search service application administrators, site collection administrators, and site owners can help searches respond to the intent of users by creating query rules. In a query rule, you specify conditions and correlated actions. When a query meets the conditions in a query rule, the search system performs the actions specified in the rule to improve the relevance of the search results, such as by narrowing results or changing the order in which results are displayed. For example, a query rule condition could be that a term in a query matches a particular term in a SharePoint Server term set, or that a query is frequently performed on a particular result source in a search system, such as videos. When the query rule condition is satisfied, a correlated action could be to show a specific item at the top of the search results. Say you have an intranet site where all company events are maintained in a library that you have shared as a catalog, and you want to promote a first-aid seminar. To do this, you create a query rule that boosts the first-aid seminar to the top of the search results when someone searches for "seminar" or "event."
  
You can configure query rules for one or more result sources, and you can specify the time period during which the query rule is active. 
  
For more information about query rules, see [Plan result sources and query rules](plan-search-for-sharepoint-cross-site-publishing-sites.md#BKMK_PlanResultSourcesAndQueryRules) in [Plan search for cross-site publishing sites in SharePoint Server 2016](plan-search-for-sharepoint-cross-site-publishing-sites.md).
  
    
## Before you begin
<a name="BKMK_Before"> </a>

> [!NOTE]
>  Because SharePoint Server runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server supports the accessibility features of supported browsers. For more information, see the following resources: > [Plan browser support](https://docs.microsoft.com/sharepoint/install/browser-support-planning-0)> [Accessibility guidelines in SharePoint](https://docs.microsoft.com/sharepoint/accessibility-guidelines)> [Accessibility in SharePoint](https://docs.microsoft.com/sharepoint/dev/general-development/accessibility-in-sharepoint)> [Keyboard shortcuts](https://support.office.com/article/keyboard-shortcuts-in-sharepoint-online-466e33ee-613b-4f47-96bb-1c20f20b1015)> [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506).
  
We recommend that you set up your site, integrate a catalog, and set up your category pages and catalog item pages before you begin to create query rules. This is because you can then more easily test and verify how the different query rules apply to the different Search Web Parts you have on your site.
  
## Creating query rules at different levels in a SharePoint Server farm
<a name="BKMK_CreateRuleLevels"> </a>

You can create a query rule for a Search service application, a site collection, or a site. The following table shows the permissions that are required to create a query rule in each case, and where the query rule can be used.
  
**Levels and permissions for query rules**

|**When you create a query rule at this level**|**You must have this permission**|**The query rule can be used in**|
|:-----|:-----|:-----|
|Search service application  <br/> |Search service application administrator  <br/> |All site collections in web applications that consume the Search service application  <br/> |
|Site collection  <br/> |Site collection administrator  <br/> |All sites in the site collection  <br/> |
|Site  <br/> |Site owner  <br/> |The site  <br/> |
   
To add or edit a query rule, you must go to the **Manage query rules** page. Depending on the level at which you are creating the query rule, use one of the following procedures to go to the **Manage query rules** page. 
  
 **To go to the Manage query rules page for a Search service application**
  
1. Verify that the user account that performs this procedure is an administrator for the Search service application.
    
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
3. Click the Search service application to which you want to add query rules.
    
4. On the Search Administration page for the Search service application, in the Quick Launch, in the **Queries and Results** section, click **Query Rules**.
    
 **To go to the Manage query rules page for a publishing site collection**
  
1. Verify that the user account that performs this procedure is a site collection administrator for the publishing site collection.
    
2. On the publishing site collection, on the **Settings** menu, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Site Collection Administration** section, click **Search Query Rules**.
    
 **To go to the Manage query rules page for a site**
  
1. Verify that the user account that performs this procedure is a member of the Owners group for the site.
    
2. On the **Settings** menu for the site, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Site Administration** section, click **Query Rules**.
    
## Create a query rule
<a name="BKMK_AddQueryRule"> </a>

 **To create a query rule**
  
1. On the **Manage Query Rules** page, in the **Select a Result Source** menu, select a result source for the new query rule. 
    
2. Click **New Query Rule**.
    
3. On the **Add Query Rule** page, in the **General Information** section, in the **Rule name** field, type the name for the query rule. 
    
4. Click to expand the **Context** section. 
    
5. In the **Context** section, select one of the following: 
    
  - To apply the query rule to all result sources, select **All sources**.
    
  - To apply the query rule to one or more specific result sources, select **One of these sources**. By default, the result source that you specified in step 1 is selected. To add a result source for the query rule, do the following: 
    
    Click **Add Source**. In the **Add Source** dialog box, select a result source, and then click **Save**.
    
6. To restrict the query rule to categories —for example, that a query rule should fire only when a term from your managed navigation term set is included in the query — click **Show more conditions**, and then specify the following: 
    
  - To restrict the query rule to a category, click **Add category**. In the **Import from Taxonomy** dialog box, select a term that when you include it in a query will cause the query rule to fire, and then click **Save**.
    
  - To restrict the query rule to a user segment, do the following:
    
1. Click **Add User Segment**.
    
2. In the **Add User Segment** dialog box, in the **Title** field, type the title for this rule. 
    
3. In the **Import from taxonomy** dialog box, select a term that represents a user segment that will cause the query rule to fire when it appears in a query. 
    
4. Click **Save**
    
7. In the **Query Conditions** section, select one of the conditions listed in the following table. 
    
    > [!NOTE]
    > When you create query rules for catalog pages that have Web Parts that use search technology (described in this article as Search Web Parts), and you want the query that is configured in the Web Parts to act as the query condition, click **Remove Condition**, and then go to step 8. You should also do this if you want a query rule to fire every time that a user types anything in a search box. 
  
|**Query condition**|**Description**|**Configuration**|**Example**|
|:-----|:-----|:-----|:-----|
|**Query Matches Keyword Exactly** <br/> |Select this option if you want the query rule to fire when a query exactly matches a word or phrase that you specify.  <br/> |In the **Query exactly matches one of these phrases** text box, type one or more phrases separated by semicolons.  <br/> |You type "picture; pic" in the **Query contains one of these phrases** box. The query rule will fire when a user types "picture" or "pic" in a search box. The rule will not fire if a user types "pictures" or "sunny picture."  <br/> |
|**Query Contains Action Term** <br/> |Select this option if you want the query rule to fire when a query contains a term that indicates something that the user wants to do. The term must be at the beginning or end of the query.  <br/> | Specify the action term that will cause the query rule to fire by doing one of the following:  <br/>  Select **Action term is one of these phrases**, and type one or more phrases.  <br/>  Select **Action term is an entry in this dictionary**, and then click **Import from taxonomy**. In the **Import from taxonomy** dialog box, select a term from a term set, and then click **Save**.  <br/> |You type the word "download" in the **Action term is one of these phrases** text box. When a user types "download Contoso Electronics datasheet" in a search box, the user is probably not searching for a document that contains the words "download," "Contoso," "Electronics," and "datasheet." Instead, the user is probably trying to download a Contoso Electronics datasheet. When a user types "download Contoso Electronics datasheet" in a search box, the query rule fires, and only the words "Contoso," "Electronics," and "datasheet" are passed to the search index.  <br/> |
|**Query Matches Dictionary Exactly** <br/> |Select this option if you want the query rule to fire when the query exactly matches a dictionary entry.  <br/> |From the ** Query contains an entry in this dictionary ** menu, select a dictionary. To specify a different dictionary, click **Import from taxonomy**, and then from the **Import from taxonomy** dialog box, select a term from a term set, and then click **Save**.  <br/> |In an Internet business scenario, you have a term set named Brands that contains all brand names within your catalog. The query rule will fire when a user types a name that matches a term from the Brands term set.  <br/> |
|**Query More Common in Source** <br/> |Select this option if you want the query rule to fire if the query was frequently issued by users on a different result source that you specify.  <br/> |In the **Query is more likely to be used in this source** menu, select a result source.  <br/> |In the **Query is more likely to be used in this source** menu, you select **Local Video Results**. The query rule will fire if a user types the word "training" in a search box and that word was frequently typed in a search box in the Videos vertical.  <br/> |
|**Result Type Commonly Clicked** <br/> |Select this option if you want the query rule to fire if other users frequently clicked a particular result type after they typed the same query.  <br/> |In the **Commonly clicked results match result type** menu, select a result type.  <br/> |In an Internet business scenario, you have a catalog of electronic products. Each product has a PDF datasheet. So when users query for a specific product, the search results will return two result types: one that links to the page that has the product details, and one that links to the PDF datasheet. You can create a query rule that will fire if the system over time recognizes that users frequently click the search result for the PDF datasheet. When you know the type of content the user is looking for, you can specify an action for this query rule.  <br/> |
|**Advanced Query Text Match** <br/> |Select this option if you want to use a regular expression, a phrase, or a dictionary entry that will cause the query rule to fire.  <br/> |To match all phone numbers that are in a certain format, you specify a regular expression in the **Query matches this regular expression** box.  <br/> |To match all phone numbers that are in the format nnn-nnn-nnnn, you specify the regular expression "\(?(\d{3})\)?-?(\d{3})-(\d{4})".  <br/> |
   
    To add conditions, click **Add Alternate Conditions**. 
    
    > [!NOTE]
    > The rule will fire when any condition is true. 
  
8. In the **Actions** section, specify the action to take when the query rule fires. Specify one of the following: 
    
  - To promote individual results so that they appear towards the top of search results, click **Add Promoted Result** (in SharePoint 2010 Products this was called Best Bets). In the **Add Promoted Result** dialog box, in the **Title** field, type the name that you want to give this promoted result. In the **URL** field, type the URL of the result that should be promoted. Render the URL as a banner instead of as a hyperlink. Click **Save**.
    
    You can add several individual promoted results. When there is more than one promoted result, you can specify the relative ranking. 
    
  - To promote a group of search results, click **Add Result Block**. For more information, see [Create and display a result block](create-query-rules-for-web-content-management.md#BKMK_CreateAndDisplayResultBlock) later in this article. 
    
  - To change ranked search results, click **Change ranked results by changing the query**. For more information, see [Change ranked search results](create-query-rules-for-web-content-management.md#BKMK_ChangeRankedSearchResults) later in this article. 
    
9. To make the query rule active during a particular time period, click **Publishing**, and then specify the period.
    
## Create and display a result block
<a name="BKMK_CreateAndDisplayResultBlock"> </a>

A result block is several search results that are displayed as a group. In the same manner as you can promote a specific result, you can promote a result block when a specified query condition applies. For example, you can create a result block named  *Yellow items*  for all catalog items that have the color yellow. In an Internet business scenario where you have a catalog of electronic products and you want to promote yellow mp3 players, you can create a query rule that fires for all items that are tagged with the term  *mp3 players*  , where the action is to display the result block  *Yellow items*  . 
  
Result blocks are automatically displayed in the Search Results Web Part. To display results from a result block in a Content Search Web Part, you have to configure it to display the result block. 
  
When you configure the query condition for a result block, you can use query variables. Query variables are placeholders for values that you don't know when you specify the query. However, when the query is run, this information is known and can be used when the system sends the query to the index. Examples are {User.Name}, which represents the display name of the user who typed the query, or {searchBoxQuery}, which represents the query that a user typed in a search box. When you use Query Builder to configure the query, a list of query variables is shown. (See step 3 in the following procedure.)
  
 <a name="BKMK_ToCreateAResultBlock"></a>**To create a result block**
  
1. In step 8 of the previous procedure, on the **Add Query Rule** page, in the **Actions** section, click **Add Result Block**.
    
2. In the **Block Title** section, in the **Title** field, type a name for the result block. 
    
3. In the **Query** section, to specify the query, click **Launch Query Builder**. In Query Builder, specify the following: 
    
  - On the **BASIC** tab, select options from the following lists to define the query for the result block: 
    
|||
|:-----|:-----|
|**Select a query** <br/> |Select a result source to specify which content should be searched.  <br/> |
|**Keyword filter** <br/> |You can use keyword filters to add query variables to your query. See [Query variables in SharePoint Server](../technical-reference/query-variables.md) for a list of available query variables.  <br/> You can select pre-defined query variables from the drop-down list, and then add them to the query by clicking **Add keyword filter**.  <br/> |
|**Property filter** <br/> |You can use property filters to query the content of managed properties that are set to queryable in the search schema.  <br/> You can select managed properties from the **Property filter** drop-down list. Click **Add property filter** to add the filter to the query.  <br/> |
   
  - On the **SORTING** tab, you can specify how search results within your result block should be sorted. In the **Sort by** drop-down list: 
    
  - To sort by managed properties that are set as sortable in the search schema, select a managed property from the list, and then select **Descending** or **Ascending**. To add more sorting levels, click **Add sort level**.
    
    > [!NOTE]
    > Sorting of search results is case sensitive. 
  
  - To sort by relevance rank, select **Rank**, and then do the following:
    
  - In the **Ranking Model** list, select which ranking model to use for sorting search results (this selection is optional). 
    
  - In the **Dynamic ordering** section, to specify additional ranking by adding rules that will change the order of search results when certain conditions apply, click **Add dynamic ordering rule**, and then specify conditional rules.
    
  - On the **TEST** tab, you can preview the query that is sent. 
    
|||
|:-----|:-----|
|**Query text** <br/> |Shows the final query that will be run by the Content Search Web Part. It is based on the original query template where dynamic variables are substituted with current values. Other changes to the query may have to be made as part of query rules.  <br/> |
   
    Click **Show more** to display additional information. 
    
|||
|:-----|:-----|
|**Query template** <br/> |Shows the content of the query template that is applied to the query.  <br/> |
|**Query template variables** <br/> |Shows the query variables that will be applied to the query, and the values of the variables that apply to the current page. You can type other values to test the effect they will have on the query. Click the **Test Query** button to preview the search results.  <br/> |
   
4. In the **Query** section, in the **Configure Query** box, in the **Search this Source** drop-down list, select the result source to which this result block should be applied. 
    
5. In the **Query** section, in the **Items** drop-down list, select how many results to show in the result block. 
    
6. Click to expand the **Settings** section. 
    
    The result block will only display the number of search results that you specified in the previous step. However, you can add a **SHOW MORE** link at the bottom of the result block that will show all search results for the result block. To add a **SHOW MORE** link, select **"More" link goes to the following URL**, and then type a URL. You can use query variables in this URL — for example,  *http://www.\<site\>/search/results.aspx?k={subjectTerms}*  . 
    
7. In the **Routing** section, in the field under **Label for routing to a Content Search Web Part**, type a label for routing the result block to a Content Search Web Part, or select an existing label. You will use this label in the following procedure.
    
8. Click **OK**.
    
 **To configure a Content Search Web Part to display a result block**
  
1. Add a Content Search Web Part to a page as described in "Add a Content Search Web Part to a page" in [Configure Search Web Parts in SharePoint Server](configure-search-web-parts.md).
    
2. In the Web Part, click the **Content Search Web Part Menu** arrow, and then click **Edit Web Part**.
    
3. In the Web Part tool pane, in the **Properties** section, expand the **Settings** section. 
    
4. In the **Settings** section, from the **Result Table** list, select the label of the result block that you want to display. The label is what you specified in step 7 in the previous procedure, [To create a result block](create-query-rules-for-web-content-management.md#BKMK_ToCreateAResultBlock).
    
5. To use the query results that are returned from another Web Part on the page as input when displaying the result block, from the **Query results provided by** list, select a Web Part. 
    
> [!NOTE]
> When displaying a result block in a Content Search Web Part, paging of search results is not supported through the Control Display Template. 
  
## Display promoted results in a Content Search Web Part
<a name="BKMK_DisplayPromotedResults"> </a>

 **To display promoted results in a Content Search Web Part**
  
1. Add a Content Search Web Part to a page as described in "Add a Content Search Web Part to a page" in [Configure Search Web Parts in SharePoint Server](configure-search-web-parts.md).
    
2. In the Web Part, click the **Content Search Web Part Menu** arrow, and then click **Edit Web Part**.
    
3. In the Web Part tool pane, in the **Properties** section, expand the **Settings** section. 
    
4. In the **Settings** section, in the **Result Table** list, select **SpecialTermResults**.
    
## Change ranked search results
<a name="BKMK_ChangeRankedSearchResults"> </a>

The ranking model calculates a ranking order of search results. You can change this ranking by promoting or demoting items within the search results. For example, for a query that contains "download toolbox," you can create a query rule that recognizes the word "download" as an action term, and change the ranked search results to promote a URL of a particular download site on your intranet. You can also change the sorting order of the search results dynamically, based on several variables such as file name extension or specific keywords. Changing ranked search results by changing the query has the advantage that the results are security trimmed and refinable. Moreover, the search results will not appear if the document is no longer available. 
  
 **To change ranked search results by changing the query**
  
1. From step 8 of the procedure [Create a query rule](create-query-rules-for-web-content-management.md#BKMK_AddQueryRule), on the **Add Query Rule** page, in the **Actions** section, click **Change ranked results by changing the query**.
    
2. In the **Build Your Query** dialog box, specify the following: 
    
  - On the **BASIC** tab, select options from the following lists to change ranked search results: 
    
|||
|:-----|:-----|
|**Select a query** <br/> |Select a result source to specify which content should be searched.  <br/> |
|**Keyword filter** <br/> |You can use keyword filters to add query variables to your query. See [Query variables in SharePoint Server](../technical-reference/query-variables.md) for a list of available query variables.  <br/> You can select pre-defined query variables from the drop-down list, and then add them to the query by clicking **Add keyword filter**.  <br/> |
|**Property filter** <br/> |You can use property filters to query the content of managed properties that are set to queryable in the search schema.  <br/> You can select managed properties from the **Property filter** drop-down list. Click **Add property filter** to add the filter to the query.  <br/> |
   
  - On the **SORTING** tab, you can specify how search results should be sorted by doing the following: 
    
  - In the **Sort by** drop-down list: 
    
  - To sort by managed properties that are set as sortable in the search schema, select a managed property from the list, and then select **Descending** or **Ascending**. To add more sorting levels, click **Add sort level**.
    
    > [!NOTE]
    > Sorting of search results is case sensitive. 
  
  - To sort by relevance rank, select **Rank**, and then do the following:
    
  - In the **Ranking Model** list, select which ranking model to use for sorting search results (this selection is optional). 
    
  - In the **Dynamic ordering** section, to specify additional ranking by adding rules that will change the order of search results when certain conditions apply, click **Add dynamic ordering rule**, and then specify conditional rules.
    
  - On the **TEST** tab, you can preview the query. 
    
|||
|:-----|:-----|
|**Query text** <br/> |Shows the final query that will be run by the Content Search Web Part. It is based on the original query template where dynamic variables are substituted with current values. Other changes to the query may have to be made as part of query rules.  <br/> |
   
    Click **Show more** to display additional information. 
    
|||
|:-----|:-----|
|**Query template** <br/> |Shows the content of the query template that is applied to the query.  <br/> |
|**Query template variables** <br/> |Shows the query variables that will be applied to the query, and the values of the variables that apply to the current page. You can type other values to test the effect they will have on the query. Click the **Test Query** button to preview the search results.  <br/> |
   
## Make a query rule inactive
<a name="BKMK_MakeInactive"> </a>

Query rules that are created at the Search service application level are inherited by site collections and sites that are in web applications that consume the Search service application. Similarly, query rules that are created at the site collection level are inherited by sites in the site collection. If you don't want a query rule to apply to a site that inherits it, you can set the query rule as inactive for the site. 
  
 **To make a query rule inactive on a site**
  
1. Verify that the user account that performs this procedure is a member of the Owners group on the publishing site.
    
2. On the publishing site collection, on the **Settings** menu, click **Site Settings**. 
    
3. In the site collection, in the **Settings** menu, click **Site Settings**. 
    
4. On the **Site Settings** page, in the **Search** section, click **Query Rules**.
    
5. On the **Manage Query Rules** page, on the **Select a Result Source** menu, select the result source that contains the query rule that you want to make inactive. 
    
6. In the **Name** column, point to the query rule that you want to make inactive, click the arrow that appears, and then click **Make Inactive**.
    
## Rank query rules
<a name="BKMK_Rank"> </a>

When multiple query rules are active for a Search service application, a site collection, or a site, more than one rule can fire for a query that is performed at that level. By default, the rules do not fire in a prescribed order. You can control the order in which the rules fire by adding the query rules that you create to query groups. To do this, you select rules to add to a group, and then you specify the order in which the rules in the group will fire if they are triggered. You can also prevent query rules that rank lowest in a group from firing even if they are triggered.
  
 **To rank query rules for a site collection**
  
1. Verify that the user account that performs this procedure is a site collection administrator for the publishing site collection.
    
2. On the publishing site collection, on the **Settings** menu, click **Site Settings**. 
    
3. On the **Site Settings** page, in the **Site Collection Administration** section, click **Search Query Rules**.
    
4. On the **Manage Query Rules** page, on the **Select a Result Source** menu, select the result source that contains the query rules that you want to group. 
    
5.  For each query rule that you created that you want to add to a group, point to the rule and select the check box. 
    
    > [!NOTE]
    > Query rules that you created for this site collection are listed in the **Defined for this site collection** section. 
  
6. Click **Order Selected Rules**.
    
7. In the **Order Selected Rules** dialog box, do either of the following, and then click **OK**:
    
  - Select **Move rules to new group with this name**, and then type a name for the group.
    
  - Select **Move rules to existing group** and select a group in the drop-down list. 
    
8. On the **Manage Query Rules** page, do the following: 
    
1. To change the order in which a rule in a group will fire if it is triggered, change the numeric order of the rule.
    
2. To prevent query rules that are ranked lowest in the group from firing, in the row for the group's query rule that should fire last, in the **Actions** column, in the **Continue/Stop** drop-down list, select **Stop**.
    
## See also
<a name="BKMK_Rank"> </a>

#### Concepts

[Plan to transform queries and order results in SharePoint Server](../search/plan-to-transform-queries-and-order-results.md)
  
[Query variables in SharePoint Server](../technical-reference/query-variables.md)

