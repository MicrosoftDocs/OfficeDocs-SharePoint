---
title: "Manage query rules in SharePoint Server"
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
ms.assetid: 0b6e5490-ea92-4e6d-b2fe-743d06a4c3e6
description: "Learn how to improve search results by creating and managing query rules."
---

# Manage query rules in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Without using any custom code, a Search service application administrator, site collection administrator, or site owner can improve classic search results by creating and managing query rules. Query rules help searches respond to the intent of users. 

 In a query rule, you specify conditions and correlated actions. When a query meets the conditions in a query rule, the search system performs the actions specified in the rule to improve the relevance of the search results, such as by narrowing results or changing the order in which results are displayed. For example, a query rule condition could be that a term in a query matches a particular term in a SharePoint Server term set, or that a query is frequently performed on a particular result source in a search system, such as videos. When the query rule condition is satisfied, a correlated action could be to show a specific item at the top of the search results. 
  
You can configure query rules for one or more result sources, and you can specify the time period during which the query rule is active. 

> [!NOTE]
> A query rule also affects the **modern** search experience in SharePoint Server 2019 when:
> - The action in the rule is to promote an individual result towards the top of search results.
> - The rule is defined for the default result source.
> - The rule is defined at the Search service application level.
>
> Users only see such a promoted result in the modern search experience when:
> - They’ve searched for results across all of SharePoint.
> - The search results page is filtered to **All result types** (default view).
  
    
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
    
 **To go to the Manage query rules page for a site collection**
  
1. Verify that the user account that performs this procedure is a site collection administrator.
    
2. On the **Settings** menu for the site collection, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Site Collection Administration** section, click **Search Query Rules**.
    
 **To go to the Manage query rules page for a site**
  
1. Verify that the user account that performs this procedure is a member of the Owners group for the site.
    
2. On the **Settings** menu for the site, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Site Administration** section, click **Query Rules**.
    
## Create a query rule
<a name="BKMK_AddQueryRule"> </a>

1. Specify a result source for this query rule. Use the **Select a Result Source** menu, on the **Manage Query Rules** page. 
    
2. Click **New Query Rule**.
    
3. Give the query rule a name. Use the **Rule name** field on the **Add Query Rule** page. 
    
4. If relevant, restrict this rule to queries performed on a particular result source. Click to expand the **Context** section, and under **Query is performed on these sources**select one of the following:
    
  - To apply the query rule to all result sources, select **All sources**.
    
  - To restrict the query rule to one or more specific result sources, select **One of these sources**. By default, the result source that you specified in step 1 is selected. 
    
5. If relevant, restrict the rule to be performed from a particular category —for example, that a query rule should fire only when a term from your managed navigation term set is included in the query. In the **Context** section, under **Query is performed from these categories** select one of the following: 
    
  - To restrict the query rule to a particular category, click **One of these categories** and then add the category. In the **Import from Taxonomy** dialog box, select a term that when you include it in a query will cause the query rule to fire, and then click **Save**.
    
  - To remove any restrictions, click **All categories**.
    
6. If relevant, restrict the rule to be performed by a particular user segment. In the **Context** section, under **Query is performed by these user segments** select one of the following:: 
    
  - To restrict the query rule to a particular user segment, click **One of these user segments** and then add the user segment. Enter a title for the user segment and then click **Add user segment term**. In the **Import from Taxonomy** dialog box, select a term that when you include it in a query will cause the query rule to fire, and then click **Save**.
    
  - To remove any restrictions, click **All user segments**.
    
7. Specify when a query makes this rule fire. You can have more than one condition, and the rule will fire when any condition is true. In the **Query Conditions** section do one of the following: 
    
  - Select one of the conditions listed in [Overview of conditions that make a query rule fire](manage-query-rules.md#BKMK_Conditions_that_fire_query_rule).
    
  - Add an alternate condition.
    
  - Click **Remove Condition** to configure this query rule to fire for every query that users type at the level at which you are creating the rule. For example, if you are creating this rule for a site collection, click **Remove Condition** if you want this rule to fire for every query that users type inside any search box in the site collection. 
    
8. Specify the action to take when the query rule fires. In the **Actions** section you can: 
    
  - Promote individual results so that they appear towards the top of search results. You can add several individual promoted results. When there is more than one promoted result, you can specify the relative ranking. To promote, click **Add Promoted Result** (in SharePoint 2010 Products this was called Best Bets). In the **Add Promoted Result** dialog box give the promoted result a name and enter the URL of the result to promote. You can define that the URL is rendered as a banner instead of as a hyperlink. 
    
  - Promote a group of search results, click **Add Result Block**. For more information, see [Create and display a result block](manage-query-rules.md#BKMK_CreateAndDisplayResultBlock) later in this article. 
    
  - Change ranked search results, click **Change ranked results by changing the query**. For more information, see [Change ranked search results](manage-query-rules.md#BKMK_ChangeRankedSearchResults) later in this article. 
    
9. To make the query rule active during a particular time period, click **Publishing**, and then specify the period.
    
### Overview of conditions that make a query rule fire
<a name="BKMK_Conditions_that_fire_query_rule"> </a>

|**Query condition**|**Description**|**Configuration**|**Example**|
|:-----|:-----|:-----|:-----|
|**Query Matches Keyword Exactly** <br/> |Select this option if you want the query rule to fire when a query exactly matches a word or phrase that you specify.  <br/> |In the **Query exactly matches one of these phrases** text box, type one or more phrases separated by semicolons.  <br/> |You type "picture; pic" in the **Query contains one of these phrases** box. The query rule will fire when a user types "picture" or "pic" in a search box. The rule will not fire if a user types "pictures" or "sunny picture."  <br/> |
|**Query Contains Action Term** <br/> |Select this option if you want the query rule to fire when a query contains a term that indicates something that the user wants to do. The term must be at the beginning or end of the query.  <br/> |The action term can be one of several phrases that you enter. Alternatively the action term can be an entry in a dictionary, where you import the term.  <br/> |You type the word "download" in the **Action term is one of these phrases** text box. When a user types "download Contoso Electronics datasheet" in a search box, the user is probably not searching for a document that contains the words "download," "Contoso," "Electronics," and "datasheet." Instead, the user is probably trying to download a Contoso Electronics datasheet. When a user types "download Contoso Electronics datasheet" in a search box, the query rule fires, and only the words "Contoso," "Electronics," and "datasheet" are passed to the search index.  <br/> |
|**Query Matches Dictionary Exactly** <br/> |Select this option if you want the query rule to fire when the query exactly matches a dictionary entry.  <br/> |From the ** Query contains an entry in this dictionary ** menu, select a dictionary. To specify a different dictionary, click **Import from taxonomy**, and then from the **Import from taxonomy** dialog box, select a term from a term set, and then click **Save**.  <br/> |A word that a user types in a search box matches an entry in the pre-configured People Names dictionary.  <br/> |
|**Query More Common in Source** <br/> |Select this option if you want the query rule to fire if the query was frequently issued by users on a different result source that you specify.  <br/> |In the **Query is more likely to be used in this source** menu, select a result source.  <br/> |In the **Query is more likely to be used in this source** menu, you select **Local Video Results**. The query rule will fire if a user types the word "training" in a search box and that word was frequently typed in a search box in the Videos vertical.  <br/> |
|**Result Type Commonly Clicked** <br/> |Select this option if you want the query rule to fire if other users frequently clicked a particular result type after they typed the same query.  <br/> |In the **Commonly clicked results match result type** menu, select a result type.  <br/> |In the **Commonly clicked results match result type** box, you select **SharePoint MicroBlog post**. If users frequently click a microblog post in search results, then in the **Actions** section, you might want to configure the most recent microblog post as the first promoted result, and the next most recent microblog post as the second promoted result.  <br/> |
|**Advanced Query Text Match** <br/> |Select this option if you want to use a regular expression, a phrase, or a dictionary entry that will cause the query rule to fire.  <br/> |To match all phone numbers that are in a certain format, you specify a regular expression in the **Query matches this regular expression** box.  <br/> |To match all phone numbers that are in the format nnn-nnn-nnnn, you specify the regular expression "\(?(\d{3})\)?-?(\d{3})-(\d{4})".  <br/> |
   
## Create and display a result block
<a name="BKMK_CreateAndDisplayResultBlock"> </a>

A result block is several search results that are displayed as a group. For example, for a query that contains "Fabrikam sales report", a query rule might use a taxonomy dictionary to recognize "Fabrikam" as a customer, and then display a result block with pertinent results about Fabrikam from your customer relationship management (CRM) system.
  
In the same manner as you can promote a specific result, you can promote a result block when a specified query condition applies. 
  
When you configure the query to run for a result block, you can use query variables. Query variables are placeholders for values that you don't know when you specify the query. However, when the query is run, this information is known and can be used when the system sends the query to the index. Examples are {User.Name}, which represents the display name of the user who typed the query, or {searchBoxQuery}, which represents the query that a user typed in a search box. See [Query variables in SharePoint Server](../technical-reference/query-variables.md) for a list of available query variables. 
  
If you're not familiar with query variables, you can use the Query Builder to configure the query (see step 3 in the following procedure).
  
 **To create a result block**
  
1. In step 8 of the previous procedure, on the **Add Query Rule** page, in the **Actions** section, click **Add Result Block**.
    
2. Enter the title that shall appear in the result block in the **Title** field in the **Block Title** section. Enter a title for each language that's relevant. 
    
3. Configure the query that gives results for the block. In the **Query** section, click **Launch Query Builder**, and on the **BASIC** tab do the following:. 
    
  - Select which content to search by selecting a result source from the drop-down list in the **Select a query** section. 
    
  - Specify your query in the **Query text** box. You can select pre-defined query variables from the **Keyword filter** drop-down list, and then add them to the **Query text** box by clicking **Add keyword filter**.
    
  - If relevant, use property filters to query the content of managed properties that are set to queryable in the search schema. You can select managed properties from the **Property filter** drop-down list. Click **Add property filter** to add the filter to the query. 
    
  - Test the query by clicking **Test query**.
    
4. Specify how the search results within your result block should be sorted. Sorting of search results is **case sensitive**. On the **SORTING** tab, in the **Sort by** drop-down list, select a managed property, and then select **Descending** or **Ascending**. The list only contains managed properties that are set as sortable in the search schema. You can also sort by rank. To add more sorting levels, click **Add sort level**:
    
5. If you chose to sort by rank, you can optionally:
    
  - Select which model to use for ranking search results (this selection is optional). Use the **Ranking Model** drop-down list. 
    
  - Define rules for dynamically changing the ordering of results. In the **Dynamic ordering** section, define when to change ranking by selecting a condition from the drop-down list and then specifying whether to **promote** or **demote** the result. To add more rules, click **Add dynamic ordering rules**
    
6. Preview the final query that will be run by the Content Search Web Part, on the **TEST** tab. The preview is based on the original query template where dynamic variables are substituted with current values. Other changes to the query may have to be made as part of query rules. Click **Show more** to display additional information. 
    
  - The **Query template** box shows the content of the query template that is applied to the query. 
    
  - The **Query template variables** section shows the query variables that will be applied to the query, and the values of the variables that apply to the current page. You can type other values to test the effect they will have on the query. Click the **Test Query** button to preview the search results. 
    
7. Define which result source this result block should be applied to. Use the **Search this Source** drop-down list in the **Query** section. 
    
8. Define how many results ro show in the result block. Use the In the **Items** drop-down list, in the **Query** section. 
    
9. The result block will only display the number of search results that you specified in the previous step. However, you can add a **SHOW MORE** link at the bottom of the result block that will show all search results for the result block. To add a **SHOW MORE** link, expand the **Settings** section, select **"More" link goes to the following URL**, and then type a URL. You can use query variables in this URL — for example,  *http://www.\<site\>/search/results.aspx?k={subjectTerms}*  . 
    
10. Skip the **Routing** section. 
    
11. Click **OK**.
    
## Change ranked search results
<a name="BKMK_ChangeRankedSearchResults"> </a>

The ranking model calculates a ranking order of search results. You can change this ranking by promoting or demoting items within the search results. For example, for a query that contains "download toolbox," you can create a query rule that recognizes the word "download" as an action term, and change the ranked search results to promote a URL of a particular download site on your intranet. You can also change the sorting order of the search results dynamically, based on several variables such as file name extension or specific keywords. Changing ranked search results by changing the query has the advantage that the results are security trimmed and refinable. Moreover, the search results will not appear if the document is no longer available. 
  
 **To change ranked search results by changing the query**
  
1. From step 8 of the procedure [Create a query rule](manage-query-rules.md#BKMK_AddQueryRule), on the **Add Query Rule** page, in the **Actions** section, click **Change ranked results by changing the query**. The **Build Your Query** dialog box appears. 
    
2. On the **BASIC** tab do the following:. 
    
  - Select which content to search by selecting a result source from the drop-down list in the **Select a query** section. 
    
  - Specify your query in the **Query text** box. You can select pre-defined query variables from the **Keyword filter** drop-down list, and then add them to the **Query text** box by clicking **Add keyword filter**.
    
  - If relevant, use property filters to query the content of managed properties that are set to queryable in the search schema. You can select managed properties from the **Property filter** drop-down list. Click **Add property filter** to add the filter to the query. 
    
  - Test the query by clicking **Test query**.
    
3. Specify how the search results within your result block should be sorted. Sorting of search results is **case sensitive**. On the **SORTING** tab, in the **Sort by** drop-down list, select a managed property, and then select **Descending** or **Ascending**. The list only contains managed properties that are set as sortable in the search schema. You can also sort by rank. To add more sorting levels, click **Add sort level**:
    
4. If you chose to sort by rank, you can optionally:
    
  - Select which model to use for ranking search results (this selection is optional). Use the **Ranking Model** drop-down list. 
    
  - Define rules for dynamically changing the ordering of results. In the **Dynamic ordering** section, define when to change ranking by selecting a condition from the drop-down list and then specifying whether to **promote** or **demote** the result. To add more rules, click **Add dynamic ordering rules**
    
5. Preview the final query that will be run by the Content Search Web Part, on the **TEST** tab. The preview is based on the original query template where dynamic variables are substituted with current values. Other changes to the query may have to be made as part of query rules. Click **Show more** to display additional information. 
    
  - The **Query template** box shows the content of the query template that is applied to the query. 
    
  - The **Query template variables** section shows the query variables that will be applied to the query, and the values of the variables that apply to the current page. You can type other values to test the effect they will have on the query. Click the **Test Query** button to preview the search results. 
    
## Make a query rule inactive
<a name="BKMK_MakeInactive"> </a>

Query rules that are created at the Search service application level are inherited by site collections and sites that are in web applications that consume the Search service application. Similarly, query rules that are created at the site collection level are inherited by sites in the site collection. If you don't want a query rule to apply to a site that inherits it, you can set the query rule as inactive for the site. 
  
 **To make a query rule inactive on a site**
  
1. Verify that the user account that performs this procedure is a member of the Owners group for the site.
    
2. In the site collection, in the **Settings** menu, click **Site Settings**. 
    
3. On the **Site Settings** page, in the **Search** section, click **Query Rules**.
    
4. On the **Manage Query Rules** page, on the **Select a Result Source** menu, select the result source that contains the query rule that you want to make inactive. 
    
5. In the **Name** column, point to the query rule that you want to make inactive, click the arrow that appears, and then click **Make Inactive**.
    
## Rank query rules
<a name="BKMK_Rank"> </a>

When multiple query rules are active for a Search service application, a site collection, or a site, more than one rule can fire for a query that is performed at that level. By default, the rules do not fire in a prescribed order. You can control the order in which the rules fire by adding the query rules that you create to query groups. To do this, you select rules to add to a group, and then you specify the order in which the rules in the group will fire if they are triggered. You can also prevent query rules that rank lowest in a group from firing even if they are triggered.
  
 **To rank query rules for a site collection**
  
1. Verify that the user account that performs this procedure is a site collection administrator.
    
2. In the site collection, on the **Settings** menu, click **Site Settings**. 
    
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

[Plan to transform queries and order results in SharePoint Server](plan-to-transform-queries-and-order-results.md)
  
[Overview of search result ranking in SharePoint Server](overview-of-search-result-ranking.md)
  
[Query variables in SharePoint Server](../technical-reference/query-variables.md)

