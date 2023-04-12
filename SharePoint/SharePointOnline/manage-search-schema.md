---
ms.date: 07/12/2018
title: "Manage the search schema in SharePoint"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
search.appverid:
- SPO160
- MET150
ms.assetid: d4fab46d-ba41-4c03-9d4c-32b5b33198b6
ms.collection: M365-collaboration
ms.custom: admindeeplinkSPO
description: "Learn about the search schema and how you can view, create, or change managed properties, and map crawled properties to managed properties to create a customized search experience."
---

# Manage the search schema in SharePoint

The search schema controls what users can search for, how users can search it, and how you can present the results on your search websites. By changing the search schema, you can customize the search experience in SharePoint in Microsoft 365.

See [Overview of crawled and managed properties in SharePoint Online](crawled-and-managed-properties-overview.md) for a list of crawled and managed properties specific to SharePoint Online.

See [Overview of crawled and managed properties in SharePoint Server](../SharePointServer/technical-reference/crawled-and-managed-properties-overview.md) for a list of existing crawled and managed properties in SharePoint.
  
## About the search schema
<a name="__toc351360836"> </a>

When a user searches for content on SharePoint sites, search only finds what's in the **search index**, and only shows results that the user has permission to see. 
  
Search discovers information by crawling items on your site. The discovered content and metadata are called **properties** of the item. The **search schema** has a list of **crawled properties** that helps the crawler decide what content and metadata to extract. 
  
Not all crawled content or metadata is useful to have in the search index, so the search schema has a list of useful types of content and metadata, called **managed properties**. The index only includes content and metadata from the managed properties. Examples of useful metadata for the index are the author and the title of a document. 
  
Search comes with relevant crawled properties mapped to managed properties. For example, crawled properties related to author map to a managed property related to author. If you add a managed property, you must map it to a crawled property to get content into the index. After the site, library, or list has been crawled, users can search for the content and metadata of new, or changed managed properties. See [Introducing Search Schema for SharePoint](/archive/blogs/tothesharepoint/introducing-search-schema-for-sharepoint-2013) for more info.

> [!NOTE]
> Numeric data in Microsoft Excel files isn't indexed. For example, the number "123456789" isn't indexed, but the string "PO123456789" is indexed. 
  
### Managed properties and search
<a name="__toc351360837"> </a>

Each managed property has settings that determine how users can search for the content of that managed property, and how the content can be shown in the search results.
  
You can create new, **custom** managed properties, but these can only contain text or Yes/No. If you need other content types in your custom managed property, then use one of the unused, **built-in** managed properties that search comes with. These managed properties can contain information in integer, decimal, date and time, double precision float, or binary format. You can "rename" these unused managed properties by using the alias setting. 
  
For the built-in managed properties, you can change their mappings to crawled properties, but the only setting you can change is the alias.
  
 **Define which content that users can search and get results for**
  
If you set a managed property to be **searchable**, the content is added to the index. This means that a simple query for "Smith" returns items that contain the word "Smith" and also items whose "author" property contains "Smith". If you want users to be able to "only search for items that have this specific author", set the author property to be **queryable**. Then, to find only items that have an author named Smith, users can query for "author:Smith". 
  
If you want to prevent the content in a managed property from showing up as search results, you can disable the **retrievable** setting for the managed property. 
  
If you don't want anonymous users to see the information in a managed property, for example who has authored an item, disable the "Safe for Anonymous" setting for the managed property.
  
 **Get better search results when you have multi-lingual content and metadata with special characters**
  
When search indexes content or when it processes queries, it breaks a stream of text into smaller parts such as words, phrases, symbols, or other meaningful elements. These parts are called tokens. When users enter a query, search tries to find tokens in the index that match the tokens of the query.
  
For most languages, search changes text to lower-case, removes diacritics, replaces special characters, such as punctuation, with white space, and then breaks on white spaces.
  
Breaking on white spaces works fine for a language like English, but not so well for East Asian languages. Let's say you have a document library that contains product datasheets both in English and Chinese. Each datasheet has a product identifier with non-alphanumerical characters, such as "11.132-84-115#4". When search processes the datasheet, it **detects** its language, and tokenizes everything in it according to that language. So, the product identifier in a Chinese data sheet is tokenized as if it was Chinese text, and in an English data sheet the product identifier is tokenized as if it was English text. When users search for a product identifier, search tokenizes their query according to the language setting of the SharePoint site they're on. If the site is set to English, and the user searches for a product identifier that was tokenized as Chinese text, the tokens might not match, and the users get no results. 
  
Here's how you can make results better for users: When search crawls the datasheet, it extracts the product identifier. Map the crawled property for the product identifier to a new managed property, "ProductID". Enable **language neutral tokenization** for the "ProductID" managed property, and instruct users to search for product identifiers against the "ProductID" managed property, like this:  *ProductID:"11.132-8"*  . Because you've enabled language neutral tokenization for "ProductID", search uses language neutral tokenization for the query and can find matching results for the query. 
  
 **Get better search results when you have metadata with special characters**
  
To help users get better search results when they search in managed properties that contain metadata with non-alphanumeric characters, you can enable the **finer tokenization** setting for the managed property. 
  
Let's look at the example with a product datasheet library again.
  
Users who prefer to quickly enter a query and then browse the results to find the datasheet they're looking for, typically enter queries like ProductID:"132-884". Because search breaks content for the **search index** into smaller parts than it does for **queries**, search might not find matches for these queries. When the query is tokenized finer, it's more likely that there are matches between the tokens in the search index and in the query. Users can also query for the middle or last part of the product identifier. 
  
Users who search for a datasheet and expect to only get results that match the full product identifier, typically write queries like  *ProductID:"11.132-884-115#4"*  . Finer query tokenization doesn't make a difference for such queries. 
  
 **Determine which title to show in results**
  
A single crawled property can be mapped to multiple managed properties. Or, multiple crawled properties can be mapped to a single managed property, for example both the "Writer" and "Author" crawled properties can be mapped to the "Author" managed property.
  
For example, a document in a library can have a SharePoint title, a title in the file metadata, and the content can have a title formatted with the style "Title". All these are mapped to the "Title" managed property. It's the title from the crawled property that's highest on the mapping list and that has a value that's included in the index.
  
 **Auto-generated managed properties**
  
Some managed properties are generated automatically. One example is when you add a site column to a SharePoint library or list. When search crawls that list it automatically generates a crawled and a managed property for the site column, and a mapping between them. Another example is when crawling finds metadata in a document you've uploaded to SharePoint. If there isn't already a mapping to a managed property for that metadata, such as 'Title', search auto-generates a managed property. The type of crawled property determines the settings of the auto-generated managed property.
  
The search schema displays the name of auto-generated managed properties and their mappings to crawled properties in grey in the search schema. The search schema doesn't hold the settings of the managed auto-generated managed properties. The settings exist, but they're hidden from the search schema. You can add mappings to other managed properties for the crawled properties, but if you change any other setting, you override the other (hidden) settings and the auto-generated managed property is converted to a regular managed property. If you decide to **change** an auto-generated managed property, review **all** the settings carefully, just as you would when you create a new property manually.

>[!IMPORTANT]
>Auto-generated managed properties are case-sensitive. When accessing auto-generated managed properties, such as through a REST query, verify the casing is correct. If the casing is incorrect, no value will be returned.
  
### Refine on managed properties
<a name="__toc351360838"> </a>

If you want to use a managed property as a refiner on the search results page, use the setting **refinable**. This setting is only available on the built-in managed properties, and only [affects the classic search experience](differences-classic-modern-search.md). If you need to use a new managed property, or an auto-generated managed property, as a refiner, rename an existing, unused managed property (that's refinable) by using an alias. There are quite a few managed properties available for this purpose. They have names such as "RefinableString00" and "RefinableDate19." 
  
For example, you create a new site column called "NewColors", and you want users to be able to use "NewColors" as an option when they refine on the search results. In the search schema, you choose an unused managed property, for example "RefinableString00", and rename the property to "NewColors" by using the Alias setting. Then, you map this new managed property to the relevant crawled property.
  
### Change the search schema on tenant level or on site collection level
<a name="__toc351360839"> </a>

Usually, you don't have to change the default search schema for the tenant unless you want to create a more advanced or customized search experience.
  
You can change the search schema for the whole tenant or for a specific site collection only. The search schema for the site collection is based on the search schema for the tenant, so typically, you would make changes on the tenant level first, and then on the site collection level. Any changes you make on a site collection, only apply to that site collection.
  
### Crawling and re-indexing
<a name="__toc351360840"> </a>

When you change managed properties or add new ones, the changes take effect only after the content has been re-crawled. In SharePoint in Microsoft 365, crawling happens automatically based on the defined crawl schedule.
  
When you have added a new property to a list or to a library, or when you have changed properties that are used in a list or library, search has to re-crawl the content before your changes will be reflected in the search index. Because your changes are made in the search schema, and not to the actual site, the search will not automatically re-crawl the list or the library. To make sure that your changes are crawled, you can specifically request a re-indexing of the list or library. When you do this, the list or library content will be re-crawled so that you can start using your new managed properties in queries, query rules and display templates.
  
### Managed properties and Delve
<a name="__toc351360840"> </a>

Delve uses managed properties to query the Office graph and to display content cards in Delve. For example, you can see managed properties like Author, Filename, ModifiedBy and LastModifiedTime on the Delve content cards.
  
Any document that a user can view or edit in Microsoft 365, can also appear in Delve. Delve doesn't change any permissions and users will only see documents they already have access to. Sometimes, though, you may want to prevent a document from appearing in Delve.
  
You can use the HideFromDelve managed property to hide a document from Delve. You can keep storing the document in Office 365, and people can still find it through search - it just won't show up in Delve anymore. See [Hide documents from Delve](manage-search-schema.md#BKMK_HideFromDelveSteps).
  
For more info about Delve, see [Office Delve for Office 365 admins](./delve-for-office-365-admins.md)
  
## Create a new managed property
<a name="__toc351360841"> </a>

> [!NOTE]
> Not all options are available in SharePoint in Microsoft 365.  Refinable Managed Properties cannot be created. Instead use the existing Refinable Managed Properties, e.g. RefinableString00 or RefinableInt00. Searching "Refinable" will show all of the usable Refinable Managed Properties available.

In SharePoint in Microsoft 365, when you create a new managed property, it will have some limitations. For example, the property can only be of type **Text** or **Yes/No**, and it can't be refinable or sortable.

> [!IMPORTANT]
> Consider using only letters and digits in managed property names. Although it is possible to create custom managed properties with special characters (such as hyphens, dots, and underscores), many of those characters act as operator characters in the query syntax. For example, a hyphen means negation. Such property names have to be enclosed in double quotation marks when used in queries.  Many tools and applications that create queries don’t handle this correctly, and therefore it is better to use only letters and digits in managed property names.
  
If you need a property of a different type, or one that has different characteristics than what is available, follow the steps under [Create a managed property by renaming an existing one](manage-search-schema.md#__ref341260321).
  
**Go to the Search Schema page for the tenant**
    
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

>[!NOTE]
>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**.
 
3. On the search administration page, select **Manage Search Schema**. 
    
**Go to the Search Schema page for a site collection**
    
1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. Under **Site Collection Administration**, select **Search Schema**.
    
3. Select **Managed Properties**.
    
4. On the **Managed Properties** page, select **New Managed Property**. 
    
5. In the **Name and description** section, in the **Property name** box, enter the name of the new managed property. Optionally, enter a description. 
    
6. In the **Type** section, select one of the available options for the property: 
    
  - Yes/No.
    
  - Text.
    
7. In the **Main characteristics** section, select one or several of the available options. 
    
8. In the **Mappings to crawled properties** section, select **Add a mapping**.
    
9. In the **crawled property selection** dialog, select a crawled property to map to the managed property, and then select **OK**. If you want to map more crawled properties to the same managed property, repeat this step.
    
10. In the **Mappings to crawled properties** section, specify if you want to include: 
    
  - All content from all crawled properties mapped to this managed property.
    
  - Content from the first crawled property that contains a value and, optionally, in which order.
    
11. Select **OK**.
    
## Create a managed property by renaming an existing one
<a name="__ref341260321"> </a>

**Go to the Search Schema page for the tenant**
    
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

>[!NOTE]
>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**.

3. On the search administration page, select **Manage Search Schema**. 
    
**Go to the Search Schema page for a site collection**
    
1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. Under **Site Collection Administration**, select **Search Schema**.
    
3. On the **Managed Properties** page, find an unused managed property. By unused, we mean that the property is not mapped to a crawled property: the **Mapped Crawled Properties** column is empty. See the [Default unused managed properties](manage-search-schema.md#DefaultUnusedMPs) table for more details. 
    
    > [!IMPORTANT]
    > To be able to use the property as a refiner later, choose a managed property that is marked with **Refine**. 
  
4. Point to the managed property, select the arrow, and then select **Edit/Map property**.
    
5. On the **Edit Managed Property** page, under **Main characteristics**, in the **Alias** section, in the **Alias** box, enter the new name for the property. 
    
6. In the **Mappings to crawled properties** section, select **Add a mapping**.
    
7. On the **Crawled property selection** page, select a crawled property to map to the managed property, and then select **OK**. Repeat this step to map more crawled properties to this managed property.
    
8. Select **OK**.
    
    > [!IMPORTANT]
    > When you have created a new managed property this way, the library or list that will use the refiner must be re-crawled and re-indexed before the property will appear as an option in the refinement configuration. See [Request re-indexing of a document library or list](manage-search-schema.md#__ref341258429). 
  
## View crawled properties and managed properties
<a name="__toc351360843"> </a>

**Go to the Search Schema page for the tenant**
    
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

>[!NOTE]
>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**.

3. On the search administration page, select **Manage Search Schema**.

    
**Go to the Search Schema page for a site collection**
    
1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. Under **Site Collection Administration**, select **Search Schema**.
    
3. On the **Managed Properties** tab, you see all the managed properties, the settings on the managed properties, and the crawled properties they are mapped to. 
    
4. To view crawled properties and the managed properties they are mapped to, select **Crawled Properties**.
    
5. To view crawled property categories, select **Categories**.
    
## Edit a managed property
<a name="__toc351360844"> </a>

> [!NOTE]
> Not all options are available in SharePoint. 
  
  
**Go to the Search Schema page for the tenant**
    
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

>[!NOTE]
>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**.

3. On the search administration page, select **Manage Search Schema**.

    
**Go to the Search Schema page for a site collection**
    
1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. Under **Site Collection Administration**, select **Search Schema**.
    
3. On the **Managed Properties** tab, in the **Property Name** column, find the managed property that you want to edit, or in the **Filter** box, enter the name. 
    
4. Point to the managed property in the list, select the arrow, and then select **Edit/Map property**.
    
5. On the **Edit Managed Property** page, edit the settings, and then select **OK**.
    
## Delete a managed property
<a name="__toc351360845"> </a>

**Go to the Search Schema page for the tenant**
    
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

>[!NOTE]
>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**.

3. On the search administration page, select **Manage Search Schema**.

**Go to the Search Schema page for a site collection**
    
1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. Under **Site Collection Administration**, select **Search Schema**.
    
3. On the **Managed Properties** tab, find the managed property that you want to delete, or in the **Filter** box, enter its name. 
    
4. Point to the managed property that you want to delete, select the arrow, and then select **Delete**.
    
5. Select **OK**.
    
    > [!IMPORTANT]
    >  If you delete a managed property: >  Users can't search on the property. >  A query rule that uses the property no longer works. >  A custom web part that uses the property no longer works. 
  
## Map a crawled property to a managed property
<a name="__toc351360846"> </a>

**Go to the Search Schema page for the tenant**
    
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

>[!NOTE]
>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**.

3. On the search administration page, select **Manage Search Schema**.

    
**Go to the Search Schema page for a site collection**
    
1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. Under **Site Collection Administration**, select **Search Schema**.
    
3. Choose **Crawled Properties**.
    
4. On the **Crawled Properties** page, find the crawled property that you want to map to a managed property, or under **Filters**, enter its name in the **Crawled properties** box.
    
5. Point to the crawled property that you want to map, select the arrow, and then select **Edit/Map property**.
    
6. On the **Edit Crawled Property** page, in the **Mappings to managed properties** section, select **Add a Mapping**.
    
7. In the **managed property selection** dialog, select a managed property to map to the crawled property, and then select **OK**. Repeat this step to map more managed properties to this crawled property.
    
8. In the **Include in full-text index** section, if you want to include the content of this crawled property in the full-text index, select the box. 
    
9. Select **OK**.
    
## View or edit crawled property categories
<a name="__toc351360847"> </a>

**Go to the Search Schema page for the tenant**
    
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

>[!NOTE]
>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**.

3. On the search administration page, select **Manage Search Schema**.

    
**Go to the Search Schema page for a site collection**
    
1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. Under **Site Collection Administration**, select **Search Schema**.
    
3. Select **Categories**.
    
4. On the Categories page, find the crawled property category that you want to view or edit.
    
5. Do one of the following:
    
    - To view which crawled properties belong to a category, and which managed properties they are mapped to, click the crawled property category in the Categories page.
    
    - To edit a category, point to the crawled property category that you want to edit, click the arrow, and then click **Edit category**.

## Default unused managed properties
<a name="DefaultUnusedMPs"> </a>

The following table provides an overview of the default unused managed properties that you can reuse and rename using an Alias.

| **Managed property type** | **Count** | **Multi** | **Query** | **Search** | **Retrieve** | **Refine** | **Sort** | **Managed property name range** | **Notes** |
| :------------------------ | :-------- | :-------- | :-------- | :--------- | :----------- | :--------- | :------- |:------------------------------------------------------- | :--------------------------------------- |
| Date                      | 10        |   -   | Query | - |     -    |    -   |   -  | Date00 to Date09                                           | |
| Date                      | 20        | Multi | Query | - | Retrieve | Refine | Sort | RefinableDate00 to RefinableDate19                         | |
| Date                      |  2        |   -   | Query | - | Retrieve | Refine | Sort | RefinableDateInvariant00 to RefinableDateInvariant01       | \* |
| Date                      |  5        |   -   | Query | - | Retrieve | Refine | Sort | RefinableDateSingle00 to RefinableDateSingle04             | |
| Decimal                   | 10        |   -   | Query | - |     -    |    -   |   -  | Decimal00 to Decimal09                                     | |
| Decimal                   | 10        | Multi | Query | - | Retrieve | Refine | Sort | RefinableDecimal00 to RefinableDecimal09                   | |
| Double                    | 10        |   -   | Query | - |     -    |    -   |   -  | Double00 to Double09                                       | |
| Double                    | 10        | Multi | Query | - | Retrieve | Refine | Sort | RefinableDouble00 to RefinableDouble09                     | |
| Integer                   | 50        |   -   | Query | - |     -    |    -   |   -  | Int00 to Int49                                             | |
| Integer                   | 50        | Multi | Query | - | Retrieve | Refine | Sort | RefinableInt00 to RefinableInt49                           | |
| String                    | 200       | Multi | Query | - | Retrieve | Refine | Sort | RefinableString00 to RefinableString199                    | |
| String                    | 40        | Multi | Query | - | Retrieve | Refine | Sort | RefinableStringFirst00 to RefinableStringFirst39           | \* |
| String                    | 10        | Multi | Query | - | Retrieve | Refine | Sort | RefinableStringLn00 to RefinableStringLn09                 | \*\* |
| String                    | 50        |   -   | Query | - | Retrieve | Refine | Sort | RefinableStringWbOff00 to RefinableStringWbOff49           | \*\*\* |
| String                    | 50        | Multi | Query | - | Retrieve | Refine | Sort | RefinableStringWbOffFirst00 to RefinableStringWbOffFirst49 | \*, \*\*\* |

\* Mappings to crawled properties - Include content from the first crawled property that is not empty, based on the specified order.

\*\* Language neutral word breaker

\*\*\* Complete Matching

## Hide documents from Delve

<a name="BKMK_HideFromDelveSteps"> </a>

If you don't want a document to show up in Delve, you can create a HideFromDelve site column of the type **Yes/No**. This site column creates a new crawled property, ows_HideFromDelve, which is automatically mapped to the HideFromDelve managed property.
  
 **Add a site column to the library or list where the document is stored**
  
1. Sign in as a site collection administrator, and go to the site where the document that you want to hide from Delve is stored.
    
2. On the ribbon, select the **List** or **Library** tab. 
    
3. In the **Manage Views** group, select **Create Column**. 
    
4. Under the **Name and Type** section, in the **Column name** box, enter HideFromDelve, and then select **Yes/No** (check box)*
    
    > [!IMPORTANT]
    > In the **Additional Column Settings** section, in the **Default value** dropdown, select **No**. If you select **Yes**, all new documents are hidden from Delve. 
  
5. Do one of the following:
    
  - For SharePoint 2016 or SharePoint in Microsoft 365, clear the **Add to all content types** check box. 
    
  - For SharePoint 2013, clear the **Add to default view** check box. 
    
6. Select **OK**.
    
 **Mark the document you want to hide from Delve**
  
1. Go to the site where the document that you want to hide from Delve is stored.
    
2. Find the document that you want to hide in the library or list, select **edit properties**, and then check **HideFromDelve**. 
    
3. Select **OK**.
    
After the next scheduled crawl, or after you [Request re-indexing of a document library or list](manage-search-schema.md#__ref341258429), the document is hidden from Delve. If you want the document to show up in Delve again, uncheck the **HideFromDelve** column for the hidden document. 
  
## Request re-indexing of a document library or list
<a name="__ref341258429"> </a>

1. On your site, go to the list or library where you have added the new property, and select the title. The **Library** or **List** tabs appear. 
    
2. On the ribbon, select the **Library** tab or the **List** tab. 
    
3. Under the **Settings** section, select **Library settings** or **List settings**. 
    
4. On the **Settings** page, under **General Settings**, select **Advanced settings**.
    
5. Scroll down to **Reindex Document Library** or **Reindex List**, and select the button. All of the content in the document library or list is re-indexed during the next scheduled crawl.
    
    > [!NOTE]
    > This may cause a massive load on the search system, so be sure to re-index only after you've made all the changes you want to be re-indexed. 
  
## Related Topics
<a name="__ref341258429"> </a>

[Overview of crawled and managed properties in SharePoint Online](crawled-and-managed-properties-overview.md)

[Overview of crawled and managed properties in SharePoint Server](../SharePointServer/technical-reference/crawled-and-managed-properties-overview.md)
  
[Overview of the search schema in SharePoint Server](../SharePointServer/search/search-schema-overview.md)
  
[Manually request crawling and re-indexing of a site](crawl-site-content.md)

