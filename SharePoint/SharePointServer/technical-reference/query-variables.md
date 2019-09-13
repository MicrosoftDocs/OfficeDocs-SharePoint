---
title: "Query variables in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/25/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 2d8373ff-0808-40b7-8a21-5534720719f4
description: "Learn about the query variables that you can use when you configure a query."
---

# Query variables in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
## Query variables

The following tables show the query variables for SharePoint Server, and examples on how they can be used.
  
**Site and site collection properties**

|**Query variable**|**Definition**|
|:-----|:-----|
|{Site} or {Site.URL}  <br/> |URL of the site from where the query was issued. For example, this value can be used to query content of the managed property Path.  <br/> |
|{Site.ID}  <br/> |GUID of site from where the query was issued. This value corresponds to the value of the managed property WebId.  <br/> |
|{Site.LCID}  <br/> |Numeric value of the locale as specified by the Regional Settings in the Site Settings on the Site from where the query was issued.  <br/> |
|{Site.Locale}  <br/> |Language of the Site from where the query was issued in ll-cc format — for example, en-us.  <br/> |
|{Site.\<property\>}  <br/> |Any property from the property bag of the site (SPWeb) from where the query was issued, including custom properties.  <br/> |
|{SiteCollection} or {SiteCollection.URL}  <br/> |URL of site collection from where the query was issued. For example, this value can be used to query content of the managed property Path.  <br/> |
|{SiteCollection.ID}  <br/> |GUID of site collection from where the query was issued. This value corresponds to the value of the managed property SiteID.  <br/> |
|{SiteCollection.LCID}  <br/> |Numeric value of the locale as specified by the Regional Settings in the Site Settings on the Site Collection from where the query was issued.  <br/> |
|{SiteCollection.Locale}  <br/> |Language of the Site Collection from where the query was issued in ll-cc format — for example, en-us.  <br/> |
|{SiteCollection.\<property\>}  <br/> |Any property from the property bag of the root site (SPWeb) in the site collection (SPSite) from where the query was issued, including custom properties.  <br/> |
   
**Page, URL token, query string and request properties**

|**Query variable**|**Definition**|
|:-----|:-----|
|{Page} or {Page.URL}  <br/> |URL of the page from where the query was issued. For example, this value can be used to query content of the managed property Path.  <br/> |
|{Page.UsageAnalyticsId}  <br/> |Item ID for Usage Analytics  <br/> |
|{Page.\<FieldName\>}  <br/> |The value of a field on the page from where the query was issued. For example, if the page from where the query was issued contained a site column named "ContentOwner," specifying {Page.ContentOwner} would allow you to query for the value of "ContentOwner."  <br/> |
|{URLToken.\<integer\>}  <br/> |A value from the URL of a page. The integer represents the position of the value in the URL as counted from right to left. For example, for the page http://www.contoso/audio/mp3/1010101, the query variable {URLToken.1} will query for the last value in the URL, 1010101. The query variable {URLToken.3} will query for the third last property in the URL, audio. You can query for values up to the ninth last position in a ULR.  <br/> |
|{QueryString.\<ParameterName\>}  <br/> |A value from a query string in the URL of the current page. For example, if the URL of the current page contains a query string such as ItemNumber=567, you could obtain the value 567 by specifying {QueryString.ItemNumber}.  <br/> |
|{Request.\<PropertyName\>}  <br/> |A value from the current http request - for example, {Request.Url}.  <br/> |
   
**User properties**

|**Query variable**|**Definition**|
|:-----|:-----|
|{User} or {User.Name}  <br/> |Display name of the user who issued the query. For example, this value can be used to query content of the managed property Author.  <br/> |
|{User.Email}  <br/> |Email address of the user who issued the query. For example, this value can be used to query content of the managed property WorkEmail.  <br/> |
|{User.SID}  <br/> |SID of the user who issued the query.  <br/> |
|{User.LCID}  <br/> |Numeric value of locale as defined in the profile of the user who issued the query.  <br/> |
|{User.PreferredContentLanguage}  <br/> |Language as specified as Preferred Content Language in the profile of the user who issued the query.  <br/> |
|{User.PreferredDisplayLanguage}  <br/> |Language as specified as Preferred Display Language in the profile of the user who issued the query.  <br/> |
|{User.\<property\>}  <br/> |Any property from the user profile of the user who issued the query — for example, SPS-Interests, including custom properties.  <br/> |
   
**Term and term set properties**

|**Query variable**|**Definition**|
|:-----|:-----|
|{Term} or {Term.ID} or {Term.IDNoChildren}  <br/> |GUID of current site navigation node with a prefix of #0 — for example, #083e99dcb-7907-4dc9-abc8-b5614a284f1c. For example, this value can be used to query content of the managed property owstaxIdMetadataAllTagsInfo or owstaxIdProductCatalogItemCategory in a Product Catalog Site Collection.  <br/> |
|{Term.IDWithChildren}  <br/> |GUID of current site navigation node with a prefix of # — for example, #83e99dcb-7907-4dc9-abc8-b5614a284f1c. This will return all items tagged with the current site navigation term, or children of the current site navigation term. For example, this value can be used to query content of the managed property owstaxIdProductCatalogItemCategory in a Product Catalog Site Collection. This value cannot be used to query the content of the managed property owstaxidmetadataalltagsinfo.  <br/> |
|{Term.Name}  <br/> |Label of the site navigation node — for example, Audio.  <br/> |
|{Term.\<property\>}  <br/> |Any property from the property bag of the term, including custom properties.  <br/> |
|{TermSet} or {TermSet.ID}  <br/> |GUID of the term set used for current site navigation.  <br/> |
|{TermSet.Name}  <br/> |Label of the term set used for current site navigation.  <br/> |
   
**List and list item properties**

|**Query variable**|**Definition**|
|:-----|:-----|
|{List}  <br/> |URL of the current list.  <br/> |
|{List.\<property\>}  <br/> |Any property of the current list.  <br/> |
|{ListItem}  <br/> |URL of the current list item.  <br/> |
|{ListItem.\<property\>}  <br/> |Any property of the current list item.  <br/> |
   
**Other properties**

|**Query variable**|**Definition**|
|:-----|:-----|
|{Today+/- \<integer value for number of days\>}  <br/> |A date calculated by adding/subtracting the specified number of days to/from the date when the query is issued. Date format is YYYY-MM-DD. For example, this value can be used to query content of the managed property LastModifiedTime.  <br/> |
|{SearchBoxQuery}  <br/> |The query value entered into a search box on a page.  <br/> |
|{CurrentDisplayLanguage}  <br/> |The current display language based on MUI in ll-cc format.  <br/> |
|{CurrentDisplayLCID}  <br/> |Numeric value of the current display language based on MUI in ll-cc format.  <br/> |
   
### Dealing with spaces in values

Search queries use the space character to tokenize query values issued by users. When a query variable is expanded to a value that contains a space, the complete value is enclosed in double quotations. For example, for the query author:{User}, the expanded value becomes author:"John Smith". 
  
If you don't want the value to be enclosed with double quotations — for example, when concatenating multiple values — you can use the escape character in the query variable. For example: customProperty:"{\User.Name};{\User.ZipCode}" would become customProperty:"John Smith;98109".
  
### Query variables with multiple values

Some query variables may return multiple values. For query variables that return multiple values, the following syntax must be used: {|ManagedProperty:{QueryVariable}}. All the query variable values will be combined by using the bitwise OR operation. For example, say that you have a term set that is used to categorized interest of users. All users are configured to have one or more interests using the multi-value property SPS-Interests in the User Profile Service Application. To issue a query for any of the interests of the current user, the following syntax could be used: {|owstaxIdMetadataAllTagsInfo:{User.SPS-Interests}}. If the current user is configured to have two interests — football (#0f95d1fdf-781f-42f4-99f9-c656c1341b2e) and basketball (#0c2cff933-9377-4692-aa98-ce59768aa38b) — the query will be transformed to  *(owstaxIdMetadataAllTagsInfo:#0f95d1fdf-781f-42f4-99f9-c656c1341b2e) OR (owstaxIdMetadataAllTagsInfo:#0c2cff933-9377-4692-aa98-ce59768aa38b)*  . 
  
There are some restrictions with using multiple values. Only the OR operator ({|) is supported for multiple values. The AND operator is not supported. Also, only columns of type Managed Metadata work correctly for multiple value cases. Other types of columns that may use multiple values, such as columns of type Person or Group or Choice, the items will be expanded into a delimited string. 
  

