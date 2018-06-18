---
title: "Manage query rules"
ms.author: tlarsen
author: tklarsen
manager: arnek
ms.date: 12/30/2016
ms.audience: End User
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
search.appverid: SPO160
ms.assetid: 53556bb4-3625-490b-aa89-1223e3d4ce3f

description: "Improve search results by creating and managing query rules. Query rules help searches respond to the intent of users."
---

# Manage query rules

As a SharePoint Online administrator, you can improve search results by creating and managing query rules. Query rules help searches respond to the intent of users. 
  
In a query rule, you specify conditions and associated actions. When a query meets the conditions in a query rule, the search system performs the actions specified in the rule to improve the relevance of the search results. This could be by narrowing results or changing the order in which results are displayed. For example, a query rule condition could be that a term in a query matches a particular term in a SharePoint term set, or that a query is frequently performed on a particular result source in a search system, such as videos. When the query rule condition is met, an associated action could be to show a specific item at the top of the search results. Say you have an intranet site where all company events are maintained in a library, and you want to promote a first-aid seminar. To do this, you create a query rule that boosts the first-aid seminar to the top of the search results when someone searches for "seminar" or "event."
  
You can configure query rules for one or more result sources, and you can specify a time period for when the query rule is active. 
  
See also: [Understanding query rules](https://support.office.com/article/8ca2588d-9dc7-45aa-90a4-428d4d695d07)
  
## What do you want to do?
<a name="__top"> </a>

> [Create a query rule](manage-query-rules.md#__toc343764778)
    
> [Create and display a result block](manage-query-rules.md#__toc343764779)
    
> [Change ranked search results by changing the query](manage-query-rules.md#__toc343764780)
    
> [Make a query rule inactive on a site](manage-query-rules.md#__toc343764781)
    
> [Rank query rules for a site collection](manage-query-rules.md#__toc343764782)
    
## Create a query rule
<a name="__toc343764778"> </a>

You can create query rules at different levels: for the whole tenant, for a site collection, or for a site. When you create query rules at tenant level, the query rules can be used in all site collections. When you create query rules at site collection level, the rules can be used on all sites in the site collection. When you create query rules at site level, the rules can only be used on that site.
  
1. Go to the **Manage Query Rules** page for the tenant, for a site collection, or a site: 
    
  - For the tenant:
    
1. Sign in to the Office 365 Admin Center.
    
2. Choose **Admin** \> **SharePoint**. You're now in the SharePoint admin center.
    
3. Click **search**, and then on the search administration page, click **Manage Query Rules**.
    
  - For a site collection:
    
  - In your site collection, go to **Settings**, click **Site settings** and then under **Site Collection Administration**, click **Search Query Rules**.
    
  - For a site:
    
  - On your site, go to **Settings**, click **Site settings**, and then under **Search**, click **Query Rules**.
    
2. On the **Manage Query Rules** page, in the **Select a Result Source** list, select a result source for the new query rule. 
    
3. Click **New Query Rule**.
    
4. On the **Add Query Rule** page, in the **General Information** section, in the **Rule name** field, type the name for the query rule. 
    
5. Click to expand the **Context** section. 
    
6. In the **Context** section, do one of the following: 
    
  - To apply the query rule to all result sources, select **All sources**.
    
  - To apply the query rule to one or more specific result sources, select **One of these sources**. By default, the result source that you specified earlier is selected. To add a result source to the query rule, click **Add Source**, select a result source in the dialog box, and then click **Save**.
    
7. To restrict the query rule to categories —for example, that a query rule should fire only when a term from your managed navigation term set is included in the query, do as follows: 
    
  - To restrict the query rule to a category, click **Add category**. In the **Import from term store** dialog box, select a term which, when you include it in a query, will cause the query rule to fire, and then click **Save**.
    
  - To restrict the query rule to a user segment, do the following:
    
1. Click **Add User Segment**.
    
2. In the dialog box, in the **Title** field, type the name for this rule, and then click **Add user segment term**.
    
3. In the **Import from term store** dialog box, select a term that represents a user segment that will cause the query rule to fire when it appears in a query. 
    
4. Click **Save**.
    
8. In the **Query Conditions** section, do one of the following: 
    
  - Select one of the conditions listed in the following table.
    
  - Click **Remove Condition** to configure this query rule to fire for every query that users type at the level at which you are creating the rule, and then go to the next step. For example, if you are creating this rule for a site collection, click **Remove Condition** if you want this rule to fire for every query that users type inside any search box in the site collection. 
    
|**Query condition**|**Description**|**Configuration**|**Example**|
|:-----|:-----|:-----|:-----|
|**Query Matches Keyword Exactly** <br/> |The query rule fires when a query exactly matches a word or phrase that you specify.  <br/> |If the **Query exactly matches one of these phrases** text box, type one or more phrases separated by semicolons.  <br/> |Type "picture; pic" in the box. The query rule fires when a user types "picture" or "pic" in a search box. The rule doesn't fire if a user types "pictures" or "sunny picture."  <br/> |
|Query Contains Action Term  <br/> |The query rule fires when a query contains a term for something that the user wants to do. The term must be at the beginning or end of the query.  <br/> | Enter the action term that causes the query rule to fire by doing one of the following:  <br/>  Select **Action term is one of these phrases**, and type one or more phrases.  <br/>  Select **Action term is an entry in this dictionary**, and then click **Import from term store**. In the dialog box, select a term from a term set, and then click **Save**.  <br/> |Type the word "download" in the **Action term is one of these phrases** box. When a user types "download Contoso Electronics datasheet" in a search box, there are chances the user isn't searching for a document that contains the words "download," "Contoso," "Electronics," and "datasheet." Instead, the user most likely wants to download a Contoso Electronics datasheet. The query rule fires, and only the words "Contoso," "Electronics," and "datasheet" are sent to the search index.  <br/> |
|Query Matches Dictionary Exactly  <br/> |The query rule fires when the query is an exact match of a dictionary entry.  <br/> |From the **Query exactly matches an entry in this dictionary** list, select a dictionary. To specify a different dictionary, click **Import from term store**, select a term from a term set in the dialog box, and then click **Save**.  <br/> |A word that a user types in a search box perfectly matches an entry in the preconfigured **People Names** dictionary.  <br/> |
|Query More Common in Source  <br/> |The query rule fires if users frequently sent this query from another source that you have already specified.  <br/> |In the **Query is more likely to be used in this source** list, select a result source.  <br/> |You selected **Local Video Results** in the list. The query rule fires if a user types the word "training" in a search box and if that word had already been frequently typed in a search box in the Videos vertical.  <br/> |
|Result Type Commonly Clicked  <br/> |The query rule fires if other users frequently clicked a particular result type after typing the same query.  <br/> |In the **Commonly clicked results match result type** list, select a result type.  <br/> |You selected **SharePoint MicroBlog Post** in the list. If users frequently click a microblog post in search results, consider configuring the most recent microblog post as the first promoted result, and the next most recent microblog post as the second promoted result (in the **Actions** section).  <br/> |
|Advanced Query Text Match  <br/> |You want to use a phrase or a dictionary entry that causes the query rule to fire, and then define more detailed conditions for when the query rule fires.  <br/> | Enter the phrase or term that causes the query rule to fire by doing one of the following:  <br/>  Select **Query contains one of these phrases**, and type one or more phrases.  <br/>  Select **Query contains an entry in this dictionary**, and then click **Import from term store**. In the dialog box, select a term from a term set, and then click **Save**.  <br/>  Then, add more conditions by checking off options in the lists.  <br/> |You selected **Query contains one of these phrases**, and then chose **Start of query matches, but not entire query**. The query rule fires only if the phrase is at the beginning of a query, not if it's at the end.  <br/> |
   
To add more conditions, click **Add Alternate Condition**.
  
> [!NOTE]
>  The rule fires when any condition is true. 
  
1. In the **Actions** section, specify the action to take when the query rule fires. Specify one of the following: 
    
  - To promote individual results so that they appear towards the top of search results, click **Add Promoted Result** (in SharePoint 2010 Products this was called Best Bets). 
    
1. In the dialog box, in the **Title** field, type the name that you want to give this promoted result. 
    
2. In the **URL** field, type the URL of the result that should be promoted. Choose **Render the URL as a banner instead of as a hyperlink**. 
    
3. Click **Save**.
    
    You can add several individual promoted results. When there's more than one promoted result, specify the relative ranking. 
    
  - To promote a group of search results, click **Add Result Block**. For more information, see [Create and display a result block](manage-query-rules.md#__toc343764779) a bit further down. 
    
  - To change ranked search results, click **Change ranked results by changing the query**. For more information, see [Change ranked search results by changing the query](manage-query-rules.md#__toc343764780) a bit further down. 
    
2. To make the query rule active during a particular time period, click **Publishing**, and then specify the period.
    
3. Click **Save**.
    
[As a SharePoint Online administrator, you can improve search results by creating and managing query rules. Query rules help searches respond to the intent of users. In a query rule, you specify conditions and associated actions. When a query meets the conditions in a query rule, the search system performs the actions specified in the rule to improve the relevance of the search results. This could be by narrowing results or changing the order in which results are displayed. For example, a query rule condition could be that a term in a query matches a particular term in a SharePoint term set, or that a query is frequently performed on a particular result source in a search system, such as videos. When the query rule condition is met, an associated action could be to show a specific item at the top of the search results. Say you have an intranet site where all company events are maintained in a library, and you want to promote a first-aid seminar. To do this, you create a query rule that boosts the first-aid seminar to the top of the search results when someone searches for "seminar" or "event."You can configure query rules for one or more result sources, and you can specify a time period for when the query rule is active. See also: Understanding query ruleshttps://support.office.com/article/8ca2588d-9dc7-45aa-90a4-428d4d695d07](manage-query-rules.md#__top)
  
## Create and display a result block
<a name="__toc343764779"> </a>

A result block is several search results that are displayed as a group. Just as you do to promote a specific result, you can promote a result block when a specified query condition applies. 
  
When you configure a query condition for a result block, you use  *query variables*  . Query variables are like placeholders for values that you don't yet know, when you specify the query. However, when the query's run, this information is available and the system uses it to send the query to the index. For example, {User.Name} stands for the display name of the user who typed in the query. Another one's {searchBoxQuery}, which stands for the query a user typed in a search box. When you use the Query Builder to configure the query, a list of query variables is shown. (See step 3 in the procedure right below.) 
  
1. In step 9 of the procedure [Create a query rule](manage-query-rules.md#__toc343764778), on the **Add Query Rule** page, in the **Actions** section, click **Add Result Block**.
    
2. In the **Block Title** section, in the **Title** field, type a name for the result block. 
    
3. In the **Query** section, click **Launch Query Builder** to specify the query. 
    
4. In the **build your query** dialog box: 
    
  - On the **BASICS** tab, select options to define the query for the result block: 
    
|**List**|**Options**|
|:-----|:-----|
|Select a query  <br/> |Select a result source to specify which content should be searched.  <br/> |
|Keyword filter  <br/> |Use keyword filters to add query variables to your query. See [Query variables in SharePoint Server 2013](https://technet.microsoft.com/en-us/library/jj683123) for a list of available query variables.  <br/> Select predefined query variables from the list, and then add them to the query by clicking **Add keyword filter**.  <br/> |
|Property filter  <br/> |Use property filters to query the content of managed properties that are set to queryable in the search schema.  <br/> Select managed properties from the **Property filter** list. Click **Add property filter** to add the filter to the query.  <br/> > [!NOTE]> Custom managed properties are not shown in the **Property filter** list. To add a custom managed property to your query, in the ** Query text ** box, enter the name of your custom managed property followed by the query condition, for example  *MyCustomColorProperty:Green*           |
   
- On the **SORTING** tab, specify how you want your search results within your result block to be sorted. 
    
    In the **Sort results** section, in the **Sort by** list: 
    
  - To sort by managed properties that are set as sortable in the search schema, select a managed property from the list, and then select **Descending** or **Ascending**. To add more sorting levels, click **Add sort level**.
    
  - To sort by relevance rank, select **Rank**, and then:
    
  - In the **Ranking Model** list, select which ranking model to use for sorting search results (this selection is optional). 
    
  - In the **Dynamic ordering** section, to specify more ranking by adding rules that'll change the order of search results when certain conditions apply, click **Add dynamic ordering rule**, and then specify conditional rules.
    
- On the **TEST** tab, you can preview the query that's sent. 
    
|**Option**|**Description**|
|:-----|:-----|
|**Query text**:  <br/> |Shows the final query that'll be run by the Content Search Web Part. It's based on the original query template where dynamic variables are replaced with current values. You might end up making other changes to the query as part of query rules.  <br/> |
|Show more  <br/> |Click to display more options.  <br/> |
|**Query template** <br/> |Shows the content of the query template that's applied to the query.  <br/> |
|**Query template variables** <br/> |Shows the query variables that'll be applied to the query, and the values of the variables that apply to the current page. You can type other values to test the effect they'll have on the query. Click the **Test Query** button to preview the search results.  <br/> |
   
1. Click **OK** to close the **build your query** dialog box. 
    
2. In the **Query** section, in the **Search this Source** list, select the result source that you want the result block to be applied to. 
    
3. In the **Items** drop-down list, select how many results to show in the result block. 
    
4. Click to expand the **Settings** section. 
    
The result block only displays the number of search results that you specified in the previous step. However, you can add a **Show more** link at the bottom of the result block that'll show all search results for the result block. To add a **Show more** link, select **"More" link goes to the following URL**, and then type a URL. You can use query variables in this URL — for example, http://www.\<site\>/search/results.aspx?k={subjectTerms}.
  
1. Click **OK**.
    
[As a SharePoint Online administrator, you can improve search results by creating and managing query rules. Query rules help searches respond to the intent of users. In a query rule, you specify conditions and associated actions. When a query meets the conditions in a query rule, the search system performs the actions specified in the rule to improve the relevance of the search results. This could be by narrowing results or changing the order in which results are displayed. For example, a query rule condition could be that a term in a query matches a particular term in a SharePoint term set, or that a query is frequently performed on a particular result source in a search system, such as videos. When the query rule condition is met, an associated action could be to show a specific item at the top of the search results. Say you have an intranet site where all company events are maintained in a library, and you want to promote a first-aid seminar. To do this, you create a query rule that boosts the first-aid seminar to the top of the search results when someone searches for "seminar" or "event."You can configure query rules for one or more result sources, and you can specify a time period for when the query rule is active. See also: Understanding query ruleshttps://support.office.com/article/8ca2588d-9dc7-45aa-90a4-428d4d695d07](manage-query-rules.md#__top)
  
## Change ranked search results by changing the query
<a name="__toc343764780"> </a>

The ranking model calculates a ranking order of search results. You can change this ranking by promoting or demoting items within the search results. For example, for a query that contains "download toolbox," you can create a query rule that recognizes the word "download" as an action term. Once you've done this, you can change the ranked search results and this will promote the URL of a specific download site on your intranet. You can also dynamically change the sorting order of the search results, based on several variables such as file name extension or specific keywords. When you change ranked search results by changing the query, you'll see that your results are security trimmed and refinable. Moreover, the search results don't show up if the document's no longer there.
  
1. In step 9 of the procedure [Create a query rule](manage-query-rules.md#__toc343764778), on the **Add Query Rule** page, in the **Actions** section, click **Change ranked results by changing the query**.
    
2. In the **build your query** dialog box: 
    
  - On the **BASICS** tab, select options to change ranked search results: 
    
|**List**|**Options**|
|:-----|:-----|
|Select a query  <br/> |Select a result source to specify which content should be searched.  <br/> |
|Keyword filter  <br/> |Use keyword filters to add query variables to your query. See [Query variables in SharePoint Server 2013](https://technet.microsoft.com/en-us/library/jj683123) for a list of available query variables.  <br/> Select predefined query variables from the list, and then add them to the query by clicking **Add keyword filter**.  <br/> |
|Property filter  <br/> |Use property filters to query the content of managed properties that are set to queryable in the search schema.  <br/> Select managed properties from the **Property filter** drop-down list. Click **Add property filter** to add the filter to the query.  <br/> |
   
- On the **SORTING** tab, specify how you want your search results to be sorted: 
  
In the **Sort by** drop-down list: 
    
  - To sort by managed properties that are set as sortable in the search schema, select a managed property from the list, and then select **Descending** or **Ascending**. To add more sorting levels, click **Add sort level**.
    
  - To sort by relevance rank, select **Rank**, and then:
    
  - In the **Ranking Model** list, select which ranking model to use for sorting search results (this selection is optional). 
    
  - In the **Dynamic ordering** section, to specify additional ranking by adding rules that'll change the order of search results when certain conditions apply, click **Add dynamic ordering rule**, and then specify conditional rules.
    
- On the **TEST** tab, you can preview the query that's sent. 
    
|**Option**|**Description**|
|:-----|:-----|
|**Query text**:  <br/> |Shows the final query that'll be run by the Content Search Web Part. It's based on the original query template where dynamic variables are substituted with current values. You might end up making other changes to the query as part of query rules.  <br/> |
|Show more  <br/> |Click to display more information.  <br/> |
|**Query template** <br/> |Shows the content of the query template that's applied to the query.  <br/> |
|**Query template variables** <br/> |Shows the query variables that'll be applied to the query, and the values of the variables that apply to the current page. You can type other values to test the effect they'll have on the query. Click the **Test Query** button to preview the search results.  <br/> |
   
1. Click **OK** to close the **Build Your Query** dialog box. 
    
2. Click **Save**.
    
[As a SharePoint Online administrator, you can improve search results by creating and managing query rules. Query rules help searches respond to the intent of users. In a query rule, you specify conditions and associated actions. When a query meets the conditions in a query rule, the search system performs the actions specified in the rule to improve the relevance of the search results. This could be by narrowing results or changing the order in which results are displayed. For example, a query rule condition could be that a term in a query matches a particular term in a SharePoint term set, or that a query is frequently performed on a particular result source in a search system, such as videos. When the query rule condition is met, an associated action could be to show a specific item at the top of the search results. Say you have an intranet site where all company events are maintained in a library, and you want to promote a first-aid seminar. To do this, you create a query rule that boosts the first-aid seminar to the top of the search results when someone searches for "seminar" or "event."You can configure query rules for one or more result sources, and you can specify a time period for when the query rule is active. See also: Understanding query ruleshttps://support.office.com/article/8ca2588d-9dc7-45aa-90a4-428d4d695d07](manage-query-rules.md#__top)
  
## Make a query rule inactive on a site
<a name="__toc343764781"> </a>

Query rules that are created at the tenant level are inherited by site collections and sites. Similarly, query rules that are created at the site collection level are inherited by sites in the site collection. If you don't want a query rule to apply to a site that inherits it, you can make the query rule inactive for the site.
  
1. On your site, in the **Settings** menu, click **Site Settings**. 
    
2. On the **Site Settings** page, in the **Search** section, click **Query Rules**.
    
3. On the **Manage Query Rules** page, on the **Select a Result Source** menu, select the result source that contains the query rule that you want to make inactive. 
    
4. In the **Name** column, point to the query rule that you want to make inactive, click the arrow that appears, and then click **Make Inactive**.
    
[As a SharePoint Online administrator, you can improve search results by creating and managing query rules. Query rules help searches respond to the intent of users. In a query rule, you specify conditions and associated actions. When a query meets the conditions in a query rule, the search system performs the actions specified in the rule to improve the relevance of the search results. This could be by narrowing results or changing the order in which results are displayed. For example, a query rule condition could be that a term in a query matches a particular term in a SharePoint term set, or that a query is frequently performed on a particular result source in a search system, such as videos. When the query rule condition is met, an associated action could be to show a specific item at the top of the search results. Say you have an intranet site where all company events are maintained in a library, and you want to promote a first-aid seminar. To do this, you create a query rule that boosts the first-aid seminar to the top of the search results when someone searches for "seminar" or "event."You can configure query rules for one or more result sources, and you can specify a time period for when the query rule is active. See also: Understanding query ruleshttps://support.office.com/article/8ca2588d-9dc7-45aa-90a4-428d4d695d07](manage-query-rules.md#__top)
  
## Rank query rules for a site collection
<a name="__toc343764782"> </a>

When multiple query rules are active for a tenant, a site collection, or a site, more than one rule can fire for a query that is performed at that level. By default, the rules don't fire in a given order. However, if you want to control the order in which the rules fire, you have to add the query rules that you create to query groups. To do this, you select rules to add to a group, and then you specify the order in which the rules in the group will fire if they're triggered. You can also prevent query rules that rank lowest in a group from firing even if they do get triggered.
  
1. In the site collection, on the **Settings** menu, click **Site Settings**. 
    
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
    
1. To change the order in which a rule in a group will fire if it's triggered, change the number ordering of the rule.
    
2. To prevent query rules that are ranked lowest in the group from firing, go to the row for the group's query rule that should fire last, and then in the **Actions** column, in the **Continue/Stop** list, select **Stop**.
    
[As a SharePoint Online administrator, you can improve search results by creating and managing query rules. Query rules help searches respond to the intent of users. In a query rule, you specify conditions and associated actions. When a query meets the conditions in a query rule, the search system performs the actions specified in the rule to improve the relevance of the search results. This could be by narrowing results or changing the order in which results are displayed. For example, a query rule condition could be that a term in a query matches a particular term in a SharePoint term set, or that a query is frequently performed on a particular result source in a search system, such as videos. When the query rule condition is met, an associated action could be to show a specific item at the top of the search results. Say you have an intranet site where all company events are maintained in a library, and you want to promote a first-aid seminar. To do this, you create a query rule that boosts the first-aid seminar to the top of the search results when someone searches for "seminar" or "event."You can configure query rules for one or more result sources, and you can specify a time period for when the query rule is active. See also: Understanding query ruleshttps://support.office.com/article/8ca2588d-9dc7-45aa-90a4-428d4d695d07](manage-query-rules.md#__top)
  

