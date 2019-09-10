---
title: "Manage query rules"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 53556bb4-3625-490b-aa89-1223e3d4ce3f
ms.collection: M365-collaboration
description: "Improve search results by creating and managing query rules. Query rules help searches respond to the intent of users."
---

# Manage query rules

As a global or SharePoint admin in Office 365, you can improve search results by creating and managing query rules. Query rules help searches respond to the intent of users. 
  
In a query rule, you specify conditions and associated actions. When a query meets the conditions in a query rule, the search system performs the actions specified in the rule to improve the relevance of the search results. This could be by narrowing results or changing the order in which results are displayed. For example, a query rule condition could be that a term in a query matches a particular term in a SharePoint term set, or that a query is frequently performed on a particular result source in a search system, such as videos. When the query rule condition is met, an associated action could be to show a specific item at the top of the search results. Say you have an intranet site where all company events are maintained in a library, and you want to promote a first-aid seminar. To do this, you create a query rule that boosts the first-aid seminar to the top of the search results when someone searches for "seminar" or "event."

A query rule can specify the following three types of actions:
- Promote a search result to appear above ranked results. For example, for the query "sick leave", a query rule could specify a particular result, such as a link to a site that has a statement of company policy regarding time off work.
- Add one or more groups of search results, called result blocks. For example, for a query that contains “Fabrikam sales report”, a query rule might use a taxonomy dictionary to recognize “Fabrikam” as a customer, and then display a result block with pertinent results about Fabrikam from your customer relationship management (CRM) system.
- Change the ranking of search results. For example, for a query that contains “download toolbox”, a query rule could recognize the word “download” as an action term and boost search results that point to a particular download site on your intranet.
  
You can create query rules at different levels: for the whole tenant, for a site collection, or for a site. When you create query rules at tenant level, the query rules can be used in all site collections. When you create query rules at site collection level, the rules can be used on all sites in the site collection. When you create query rules at site level, the rules can only be used on that site.

You can configure query rules for one or more result sources, and you can specify a time period for when the query rule is active.

SharePoint Online has both a classic and a modern search experience. In the modern search experience, only query rules that promote an individual result towards the top of search results and that are defined for the default result source have effect. Users can see such promoted results on the All tab on the search results page when they search across all of SharePoint. [Learn more about the differences between the classic and modern search experiences in SharePoint Online](differences-classic-modern-search.md).
  
 
  
## Promote a search result
<a name="__toc343764778"> </a>

You can add several individual promoted results. When there is more than one promoted result, you can specify the relative ranking. 

  
1. Go to the **Manage Query Rules** page for the tenant, for a site collection, or a site: 
    
  - For a tenant, in the new SharePoint admin center, select **Classic features**. Under **Search**, select **Open**, and then on the search administration page, select **Manage Query Rules**.
    
  - For a site collection, in your site collection, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**. Under **Site Collection Administration**, select **Search Query Rules**.

  - For a site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**. Under **Search**, select **Query Rules**.
    
2. On the **Manage Query Rules** page, in the **Select a Result Source** list, select a result source for the new query rule. 
    
3. Select **New Query Rule**.
    
4. On the **Add Query Rule** page, in the **General Information** section, in the **Rule name** field, type the name for the query rule. 
    
5. Select to expand the **Context** section. 
    
6. In the **Context** section, do one of the following: 
    
  - To apply the query rule to all result sources, select **All sources**.
    
  - To apply the query rule to one or more specific result sources, select **One of these sources**. By default, the result source that you specified earlier is selected. To add a result source to the query rule, select **Add Source**, select a result source in the dialog box, and then select **Save**.
    
7. To restrict the query rule to categories—for example, that a query rule should fire only when a term from your managed navigation term set is included in the query, do as follows: 
    
  - To restrict the query rule to a category, select **Add category**. In the **Import from term store** dialog box, select a term which, when you include it in a query, will cause the query rule to fire, and then select **Save**.
    
  - To restrict the query rule to a user segment, select **Add User Segment**. In the dialog box, in the **Title** field, type the name for this rule, and then select **Add user segment term**. In the **Import from term store** dialog box, select a term that represents a user segment that will cause the query rule to fire when it appears in a query. Select **Save**
    
8. In the **Query Conditions** section, do one of the following: 
    
  - Select one of the conditions listed in [Overview of conditions that make a query rule fire](manage-query-rules.md#BKMK_Conditions_that_fire_query_rule). 
    
    > [!NOTE]
    >  The rule fires when any condition is true. 
  
    To add more conditions, select **Add Alternate Condition**
    
  - Select **Remove Condition** to configure this query rule to fire for every query that users type at the level at which you are creating the rule, and then go to the next step. For example, if you are creating this rule for a site collection, select **Remove Condition** if you want this rule to fire for every query that users type inside any search box in the site collection. 
    
9. In the **Actions** section, specify the action to take when the query rule fires. Specify one of the following: 
    
  - To promote individual results so that they appear towards the top of search results, select **Add Promoted Result** (in SharePoint 2010 Products this was called Best Bets). In the dialog box, in the **Title** field, type the name that you want to give this promoted result. In the **URL** field, type the URL of the result that should be promoted. Choose **Render the URL as a banner instead of as a hyperlink**. Select **Save**.
    
    You can add several individual promoted results. When there's more than one promoted result, specify the relative ranking. 
    
  - To promote a group of search results, select **Add Result Block**. For more information, see [Create and display a result block](manage-query-rules.md#__toc343764779) a bit further down. 
    
  - To change ranked search results, select **Change ranked results by changing the query**. For more information, see [Change ranked search results by changing the query](manage-query-rules.md#__toc343764780) a bit further down. 
    
10. To make the query rule active during a particular time period, select **Publishing**, and then specify the period.
    
11. Select **Save**.
    
## Create and display a result block
<a name="__toc343764779"> </a>

A result block contains a small subset of results that are related to a query in a particular way. Like individual results, you can promote a result block or rank it with other search results. 
  
When you configure a query condition for a result block, you use  *query variables*. Query variables are like placeholders for values that you don't yet know, when you specify the query. However, when the query's run, this information is available and the system uses it to send the query to the index. For example, {User.Name} stands for the display name of the user who typed in the query. Another one's {searchBoxQuery}, which stands for the query a user typed in a search box. When you use the Query Builder to configure the query, a list of query variables is shown. (See step 3 in the procedure right below.) 
  
1. In step 9 of the procedure [Create a query rule](manage-query-rules.md#__toc343764778), on the **Add Query Rule** page, in the **Actions** section, click **Add Result Block**.
    
2. Enter the title that shall appear in the result block in the **Title** field in the **Block Title** section. 
    
3. Configure the query that gives results for the block. In the **Query** section, click **Launch Query Builder** and on the **BASICS** tab do the following: 
    
  - Select which content to search by selecting a result source from the drop-down list in the **Select a query** section 
    
  - Specify your query. See [Query variables in SharePoint Server 2013](/SharePoint/technical-reference/query-variables) for a list of available query variables. You can select pre-defined query variables from the **Keyword filter** drop-down list, and then add them to the Query text box by clicking **Add keyword filter**
    
  - If relevant, use property filters to query the content of managed properties that are set to queryable in the search schema. You can select managed properties from the **Property filter** drop-down list. Click **Add property filter** to add the filter to the query. 
    
    > [!NOTE]
    > Custom managed properties are not shown in the **Property filter** list. To add a custom managed property to your query, in the **Query text** box, enter the name of your custom managed property followed by the query condition, for example  *MyCustomColorProperty:Green* 
  
4. Specify how the search results within your result block should be sorted. Sorting of search results is case sensitive. On the **SORTING** tab, in the **Sort by drop-down list**, select a managed property, and then select **Descending** or **Ascending**. The list only contains managed properties that are set as sortable in the search schema. You can also sort by rank. To add more sorting levels, click **Add sort level**.
    
5. If you chose to sort by rank, you can optionally:
    
  - Select which model to use for ranking search results (this selection is optional). Use the **Ranking Model** drop-down list. 
    
  - Define rules for dynamically changing the ordering of results. In the **Dynamic ordering** section, define when to change ranking by selecting a condition from the drop-down list and then specifying whether to **promote** or **demote** the result. To add more rules, click **Add dynamic ordering rules**
    
6. Preview the final query that will be run by the Content Search Web Part, on the **TEST** tab. The preview is based on the original query template where dynamic variables are substituted with current values. Other changes to the query may have to be made as part of query rules. Click **Show more** to display additional information. 
    
  - The **Query text** shows the final query that'll be run by the Content Search Web Part. It's based on the original query template where dynamic variables are replaced with current values. You might end up making other changes to the query as part of query rules. 
    
  - The **Query template** box shows the content of the query template that is applied to the query. 
    
  - The **Query template variables** section shows the query variables that will be applied to the query, and the values of the variables that apply to the current page. You can type other values to test the effect they will have on the query. Click the **Test Query** button to preview the search results. 
    
7. Click **OK** to close the **build your query** dialog box. 
    
8. Define which result source this result block should be applied to. Use the **Search this Source** drop-down list in the **Query** section 
    
9. In the **Items** drop-down list, select how many results to show in the result block. 
    
10. Click to expand the **Settings** section. 
    
    The result block only displays the number of search results that you specified in the previous step. However, you can add a **Show more** link at the bottom of the result block that'll show all search results for the result block. To add a **Show more** link, select **"More" link goes to the following URL**, and then type a URL. You can use query variables in this URL—for example, [http://www.\<site\>/search/results.aspx?k={subjectTerms}]( ).
    
11. Click **OK**.
    
## Change ranked search results by changing the query
<a name="__toc343764780"> </a>

The ranking model calculates a ranking order of search results. You can change this ranking by promoting or demoting items within the search results. For example, for a query that contains "download toolbox", you can create a query rule that recognizes the word "download" as an action term. Once you've done this, you can change the ranked search results and this will promote the URL of a specific download site on your intranet. 

You can also dynamically change the sorting order of the search results, based on several variables such as file name extension or specific keywords. When you change ranked search results by changing the query, you'll see that your results are security trimmed and refinable. Moreover, the search results don't show up if the document's no longer there.
  
1. In step 9 of the procedure [Create a query rule](manage-query-rules.md#__toc343764778), on the **Add Query Rule** page, in the **Actions** section, click **Change ranked results by changing the query**. The **build your query** dialog box appears 
    
2. On the **BASICS** tab, do the following: 
    
  - Select which content to search by selecting a result source from the drop-down list in the **Select a query** section 
    
  - Specify your query. See [Query variables in SharePoint Server 2013](/SharePoint/technical-reference/query-variables) for a list of available query variables. You can select pre-defined query variables from the **Keyword filter** drop-down list, and then add them to the Query text box by clicking **Add keyword filter**
    
  - If relevant, use property filters to query the content of managed properties that are set to queryable in the search schema. You can select managed properties from the **Property filter** drop-down list. Click **Add property filter** to add the filter to the query. 
    
3. Specify how the search results within your result block should be sorted. Sorting of search results is case sensitive. On the **SORTING** tab, in the **Sort by drop-down list**, select a managed property, and then select **Descending** or **Ascending**. The list only contains managed properties that are set as sortable in the search schema. You can also sort by rank. To add more sorting levels, click **Add sort level**.
    
4. If you chose to sort by rank, you can optionally:
    
  - Select which model to use for ranking search results (this selection is optional). Use the **Ranking Model** drop-down list. 
    
  - Define rules for dynamically changing the ordering of results. In the **Dynamic ordering** section, define when to change ranking by selecting a condition from the drop-down list and then specifying whether to **promote** or **demote** the result. To add more rules, click **Add dynamic ordering rules**
    
5. Preview the final query that will be run by the Content Search Web Part, on the **TEST** tab. The preview is based on the original query template where dynamic variables are substituted with current values. Other changes to the query may have to be made as part of query rules. Click **Show more** to display additional information. 
    
  - The **Query text** shows the final query that'll be run by the Content Search Web Part. It's based on the original query template where dynamic variables are replaced with current values. You might end up making other changes to the query as part of query rules. 
    
  - The **Query template** box shows the content of the query template that is applied to the query. 
    
  - The **Query template variables** section shows the query variables that will be applied to the query, and the values of the variables that apply to the current page. You can type other values to test the effect they will have on the query. Click the **Test Query** button to preview the search results. 
    
6. Click **OK** to close the **Build Your Query** dialog box. 
    
7. Click **Save**.
    
## Make a query rule inactive on a site
<a name="__toc343764781"> </a>

Query rules that are created at the tenant level are inherited by site collections and sites. Similarly, query rules that are created at the site collection level are inherited by sites in the site collection. If you don't want a query rule to apply to a site that inherits it, you can make the query rule inactive for the site.
  
1. On your site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**. 
    
2. On the **Site Settings** page, in the **Search** section, click **Query Rules**.
    
3. On the **Manage Query Rules** page, on the **Select a Result Source** menu, select the result source that contains the query rule that you want to make inactive. 
    
4. In the **Name** column, point to the query rule that you want to make inactive, click the arrow that appears, and then click **Make Inactive**.
    
## Rank query rules for a site collection
<a name="__toc343764782"> </a>

When multiple query rules are active for a tenant, a site collection, or a site, more than one rule can fire for a query that is performed at that level. By default, the rules don't fire in a given order. However, if you want to control the order in which the rules fire, you have to add the query rules that you create to query groups. To do this, you select rules to add to a group, and then you specify the order in which the rules in the group will fire if they're triggered. You can also prevent query rules that rank lowest in a group from firing even if they do get triggered.
  
1. In the site collection, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. On the **Site Settings** page, in the **Site Collection Administration** section, click **Search Query Rules**.
    
3. On the **Manage Query Rules** page, on the **Select a Result Source** menu, select the result source that contains the query rules that you want to group. 
    
4. For each query rule that you created that you want to add to a group, point to the rule and select the check box.
    
    > [!NOTE]
    >  Query rules that you created for this site collection are listed in the **Defined for this site collection** section. 
  
5. Click **Order Selected Rules**.
    
6. In the **Order Selected Rules** dialog box, do either of the following, and then click **OK**:
    
  - Select **Move rules to new group with this name**, and then type a name for the group.
    
  - Select **Move rules to existing group** and select a group in the list. 
    
7. On the **Manage Query Rules** page: 
    
  - To change the order in which a rule in a group will fire if it's triggered, change the number ordering of the rule.
    
  - To prevent query rules that are ranked lowest in the group from firing, go to the row for the group's query rule that should fire last, and then in the **Actions** column, in the **Continue/Stop** list, select **Stop**.
    
## Overview of conditions that make a query rule fire
<a name="BKMK_Conditions_that_fire_query_rule"> </a>

|**Query condition**|**Description**|**Configuration**|**Example**|
|:-----|:-----|:-----|:-----|
|**Query Matches Keyword Exactly** <br/> |The query rule fires when a query exactly matches a word or phrase that you specify.  <br/> |In the **Query exactly matches one of these phrases** text box, type one or more phrases separated by semicolons.  <br/> |Type "picture; pic" in the box. The query rule fires when a user types "picture" or "pic" in a search box. The rule doesn't fire if a user types "pictures" or "sunny picture."  <br/> |
|Query Contains Action Term  <br/> |The query rule fires when a query contains a term for something that the user wants to do. The term must be at the beginning or end of the query.  <br/> |Enter the action term that causes the query rule to fire by doing one of the following:  <br/> Select **Action term is one of these phrases**, and type one or more phrases.  <br/> Select **Action term is an entry in this dictionary**, and then click **Import from term store**. In the dialog box, select a term from a term set, and then click **Save**.  <br/> |Type the word "download" in the **Action term is one of these phrases** box. When a user types "download Contoso Electronics datasheet" in a search box, there are chances the user isn't searching for a document that contains the words "download," "Contoso," "Electronics," and "datasheet." Instead, the user most likely wants to download a Contoso Electronics datasheet. The query rule fires, and only the words "Contoso," "Electronics," and "datasheet" are sent to the search index.  <br/> |
|Query Matches Dictionary Exactly  <br/> |The query rule fires when the query is an exact match of a dictionary entry.  <br/> |From the **Query exactly matches an entry in this dictionary** list, select a dictionary. To specify a different dictionary, click **Import from term store**, select a term from a term set in the dialog box, and then click **Save**.  <br/> |A word that a user types in a search box perfectly matches an entry in the preconfigured **People Names** dictionary.  <br/> |
|Query More Common in Source  <br/> |The query rule fires if users frequently sent this query from another source that you have already specified.  <br/> |In the **Query is more likely to be used in this source** list, select a result source.  <br/> |You selected **Local Video Results** in the list. The query rule fires if a user types the word "training" in a search box and if that word had already been frequently typed in a search box in the Videos vertical.  <br/> |
|Result Type Commonly Clicked  <br/> |The query rule fires if other users frequently clicked a particular result type after typing the same query.  <br/> |In the **Commonly clicked results match result type** list, select a result type.  <br/> |You selected **SharePoint MicroBlog Post** in the list. If users frequently click a microblog post in search results, consider configuring the most recent microblog post as the first promoted result, and the next most recent microblog post as the second promoted result (in the **Actions** section).  <br/> |
|Advanced Query Text Match  <br/> |You want to use a phrase or a dictionary entry that causes the query rule to fire, and then define more detailed conditions for when the query rule fires.  <br/> |Enter the phrase or term that causes the query rule to fire by doing one of the following:  <br/> Select **Query contains one of these phrases**, and type one or more phrases.  <br/> Select **Query contains an entry in this dictionary**, and then click **Import from term store**. In the dialog box, select a term from a term set, and then click **Save**.  <br/> Then, add more conditions by checking off options in the lists.  <br/> |You selected **Query contains one of these phrases**, and then chose **Start of query matches, but not entire query**. The query rule fires only if the phrase is at the beginning of a query, not if it's at the end.  <br/> |
   

