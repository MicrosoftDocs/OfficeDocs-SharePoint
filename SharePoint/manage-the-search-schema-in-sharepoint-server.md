---
title: Manage the search schema in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 81890ff0-e2f9-4752-8e8e-2e8502c76311
---


# Manage the search schema in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-24* **Summary:** Learn how to view, add, edit, map, and delete crawled properties, crawled property categories and managed properties in the search schema.The search schema in SharePoint Server determines how content is collected in and retrieved from the search index in SharePoint Server.Crawled properties are metadata that is extracted from content during crawls. Metadata can be structured content (such as the title or the author from a Word document), or unstructured content (such as a detected language or extracted keywords).You decide which crawled metadata to index by mapping the crawled property to a managed property. Users can only search on managed properties. You can map multiple crawled properties to a single managed property or map a single crawled property to multiple managed properties.
> [!IMPORTANT:]

  
    
    

In this article:
-  [Before you begin](#begin)
    
  
-  [To view crawled properties and managed properties](#proc1)
    
  
-  [To add a managed property](#proc2)
    
  
-  [To edit a managed property](#proc3)
    
  
-  [To delete a managed property](#proc4)
    
  
-  [To map a crawled property to a managed property](#proc5)
    
  
-  [To view or edit crawled property categories](#proc6)
    
  
-  [Add a managed property using tenant administration or site collection administration](#proc7)
    
  
-  [Search schema changes that require content to be reindexed](#Schema_Reindex_Table)
    
  

## Before you begin
<a name="begin"> </a>


> [!NOTE:]
>  [Plan browser support in SharePoint Server 2016](html/plan-browser-support-in-sharepoint-server-2016.md)> **Accessibility for SharePoint 2013**>  [Accessibility features in SharePoint Products](https://go.microsoft.com/fwlink/p/?LinkId=246501) (https://go.microsoft.com/fwlink/p/?LinkId=246501)>  [Keyboard shortcuts](https://go.microsoft.com/fwlink/p/?LinkID=246504) (https://go.microsoft.com/fwlink/p/?LinkID=246504)>  [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506) (https://go.microsoft.com/fwlink/p/?LinkId=246506)
  
    
    

Before you begin this operation, review the following information about prerequisites:
- Create a Search service application.
    
  
- Add one or more content sources and run a full crawl.
    
  

## To view crawled properties and managed properties
<a name="proc1"> </a>


1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
  
3. Click the Search service application.
    
  
4. On the Search Administration page, in the Quick Launch, under **Queries and Results**, click **Search Schema**.
    
  
5. On the Managed Properties page, you see an overview of all the managed properties, the settings on the managed properties and the crawled properties they are mapped to. To view crawled properties, click **Crawled Properties**. To view crawled property categories, click **Categories**.
    
  

## To add a managed property
<a name="proc2"> </a>


1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
  
3. Click the Search service application.
    
  
4. On the Search Administration page, in the Quick Launch, under **Queries and Results**, click **Search Schema**.
    
  
5. On the Managed Properties page, click **New Managed Property**.
    
  
6. On the New Managed Property page, in the **Property name** box in the **Name and description** section, enter the name of the new managed property. You can also enter a description.
    
  
7. In the **Type** section, select one of the following options for the property:
    
  - Text
    
  
  - Integer
    
  
  - Decimal
    
  
  - Date and Time
    
  
  - Yes/No
    
  
  - Double precision float
    
  
  - Binary
    
  
8. In the **Main characteristics** section, select one or several of the following:
    
  - Searchable
    
  
  - Advanced Searchable Settings (optional, if Searchable is selected)
    
  
  - Queryable
    
  
  - Retrievable
    
  
  - Allow multiple values
    
  
  - Refinable
    
  
  - Sortable
    
  
  - Alias
    
  
  - Token Normalization
    
  
  - Complete Matching
    
  

    > [!IMPORTANT:]
      
9. In the **Mappings to crawled properties** section, click **Add a mapping**.
    
  
10. On the Crawled property selection page, select a crawled property to map to the managed property and then click **OK**. Repeat this step to map more crawled properties.
    
  
11. On the New Managed Property page, in the **Mappings to crawled properties** section, specify if you want to include:
    
  - All content from all crawled properties mapped to this managed property
    
  
  - Content from the first crawled property that contains a value and, optionally, in which order.
    
  
12. In the **Company name extraction** section, you can optionally select the check box to enable company name extraction.
    
  
13. In the **Custom entity extraction** section, you can optionally select the check box to enable custom entity extraction. See [Create and deploy custom entity extractors in SharePoint Server](html/create-and-deploy-custom-entity-extractors-in-sharepoint-server.md) for the procedures.
    
  
14. Click **OK**.
    
  
You have to perform a full crawl of the content source or sources that contain this new managed property to include it in the search index. If the new managed property is in a SharePoint Server library or list, you have to reindex that library or list.For more information see, Overview of the search schema in SharePoint Server 2016.
## To edit a managed property
<a name="proc3"> </a>


1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
  
3. Click the Search service application.
    
  
4. On the Search Administration page, in the Quick Launch, under **Queries and Results**, click **Search Schema**.
    
  
5. On the Managed Properties page, find the managed property that you want to edit, or enter its name in the **Filter** box.
    
  
6. Point to the managed property that you want to edit, click the arrow, and then click **Edit/Map property**.
    
  
7. On the Edit Managed Property page, edit the settings and then click **OK**.
    
  
Some changes on managed property settings require a full crawl to take effect. See the table Search schema changes that require content to be reindexed for an overview of which changes require you to reindex the content.
## To delete a managed property
<a name="proc4"> </a>


1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
  
3. Click the Search service application.
    
  
4. On the Search Administration page, in the Quick Launch, under **Queries and Results**, click **Search Schema**.
    
  
5. On the Managed Properties page, find the managed property that you want to delete, or enter its name in the **Filter** box.
    
  
6. Point to the managed property that you want to delete, click the arrow, and then click **Delete**.
    
  
7. Click **OK**.
    
  
If you delete a managed property:Users can no longer run queries using this property.A query rule that uses this property no longer works.A custom search application or web part that uses this property no longer works.To delete this property from the search index, you'll have to perform a full crawl. If the deleted property was in a SharePoint Server library or list, you'll have to reindex that library or list.
## To map a crawled property to a managed property
<a name="proc5"> </a>


1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
  
3. Click the Search service application.
    
  
4. On the Search Administration page, in the Quick Launch, under **Queries and Results**, click **Search Schema**.
    
  
5. On the **Crawled Properties** page, find the crawled property that you want to map to a managed property, or enter its name in the **Filters** box.
    
  
6. Point to the crawled property that you want to map, click the arrow, and then click **Edit/Map property**.
    
  
7. On the Edit Crawled Property page, in the Mappings to managed properties section, click **Add a Mapping**.
    
  
8. On the Managed property selection page, select one managed property to map to the crawled property and then click **OK**. Repeat this step to map more managed properties to this crawled property.
    
  
9. In the Include in full-text index section, check the box if you want to include the content of this crawled property in the full-text index.
    
  
10. On the Edit Crawled Property page, click **OK**.
    
  
You have to perform a full crawl of the content source that includes the crawled property that you’ve mapped to a managed property for the new mapping to take effect. If the new mapping is for a SharePoint Server library or list, you have to reindex that library or list.
## To view or edit crawled property categories
<a name="proc6"> </a>


1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. In Central Administration, in **Application Management** section, click **Manage service applications**.
    
  
3. Click the Search service application.
    
  
4. On the Search Administration page, in the Quick Launch, under **Queries and Results**, click **Search Schema**.
    
  
5. On the Categories page, find the crawled property category that you want to view or edit.
    
1. To view which crawled properties belong to a category, and which managed properties they are mapped to, click the crawled property category in the Categories page.
    
  
2. To edit a category, point to the crawled property category that you want to edit, click the arrow, and then click **Edit category**.
    
    > [!WARNING:]
      

## Add a managed property using tenant administration or site collection administration
<a name="proc7"> </a>

Tenant administrators and site collection administrators can create a search schema that is specific for their tenant or site collection. For more information how to manage the search schema for tenants and site collections, see  [Manage the search schema in SharePoint Online](https://office.microsoft.com/redir/HA103628856.aspx).You can create new managed properties for a tenant or a site collection and map crawled properties to them. Alternatively, you can reuse existing, unused managed properties that do not have crawled properties mapped to them, and rename them using an **Alias**. Then, you must map crawled properties to the renamed managed property with the defined alias.When you create a new managed property in the tenant or site collection administration, there are some limitations. For example, the property can only be of type **Text** or **Yes/No**, and it can't be refinable or sortable. If you need a property of a different type, or one that has different characteristics than what is available, follow the steps under [To create a managed property by renaming an existing one](#Schema_Tenant_SiteColl_Alias).When you have added a new property to a list or to a library on a SharePoint Server site, or when you have changed properties that are used in a list or library, the content must be re-crawled before your changes will be reflected in the search index. Because your changes are made in the search schema, and not to the actual site, the crawler will not automatically reindex the list or the library. To make sure that your changes are crawled and reindexed, you can specifically request a reindexing of the list or library. When you do this, the list or library content will be recrawled and reindexed so that you can start using your new managed properties in queries, query rules and display templates.See the table  [Search schema changes that require content to be reindexed](#Schema_Reindex_Table) for an overview of which managed property setting changes require you to reindex the content. **To create a managed property for a tenant or a site collection**
1. Verify that the user account that is performing this procedure is an administrator for the tenant or for the site collection.
    
  
2. Go to the **Search Schema** page for the tenant or for a site collection.
    
  - For the tenant:
    
1. Sign in to the Office 365 Admin Center.
    
  
2. Choose **Admin > SharePoint**. You're now in the SharePoint admin center.
    
  
3. Click **search**, and then on the search administration page, click **Manage Search Schema**.
    
  
  - For the site collection:
    
1. On your site, go to **Settings**, click **Site settings** and then under **Site Collection Administration**, click **Search Schema**.
    
  
3. On the Managed Properties page, click **New Managed Property**.
    
  
4. On the New Managed Property page, in the **Property name** box in the **Name and description** section, enter the name of the new managed property. You can also enter a description.
    
  
5. In the **Type** section, select one of the following options for the property:
    
  - Text
    
  
  - Yes/No
    
  
6. In the **Main characteristics** section, select one or several of the available options.
    
  
7. In the **Mappings to crawled properties** section, click **Add a mapping**.
    
  
8. On the Crawled property selection page, select a crawled property to map to the managed property and then click **OK**. Repeat this step to map more crawled properties.
    
  
9. On the New Managed Property page, in the **Mappings to crawled properties** section, specify if you want to include:
    
  - All content from all crawled properties mapped to this managed property
    
  
  - Content from the first crawled property that contains a value and, optionally, in which order.
    
  
10. Click **OK**.
    
  
 **To create a managed property by renaming an existing one**
1. Verify that the user account that is performing this procedure is an administrator for the tenant or for the site collection.
    
  
2. Go to the **Search Schema** page for the tenant or for a site collection.
    
  - For the tenant:
    
1. Sign in to the Office 365 Admin Center.
    
  
2. Choose **Admin > SharePoint**. You're now in the SharePoint admin center.
    
  
3. Click **search**, and then on the search administration page, click **Manage Search Schema**.
    
  
  - For the site collection:
    
1. On your site, go to **Settings**, click **Site settings** and then under **Site Collection Administration**, click **Search Schema**.
    
  
3. On the Managed Properties page, find an unused managed property. By unused, we mean that the property is not mapped to a crawled property: the **Mapped Crawled Properties** column is empty. See the [Default unused managed properties](#DefaultUnusedMPs) table for more details. Point to the managed property, click the arrow, and then click **Edit/Map property**.
    
  
4. On the Edit Managed Property page, in the Main characteristics section, under **Alias**, enter a name in the field.
    
  
5. In the Mappings to crawled properties section, click **Add a mapping**.
    
  
6. On the Crawled property selection page, select a crawled property to map to the managed property and then click **OK**. Repeat this step to map more crawled properties to this managed property.
    
  
7. Click **OK**.
    
  
 **To reindex a list or library**
1. Verify that the user account that is performing this procedure is an administrator for the tenant or for the site collection.
    
  
2. Browse to the list or library that you want to recrawl, and then do one of the following:
    
  - If you want to perform a full crawl of a library, click the **LIBRARY** tab, and then, on the ribbon, in the **Settings** group, click **Library Settings**.
    
  
  - If you want to perform a full crawl of a list, click the **LIST** tab, and then, on the ribbon, in the **Settings** group, click **List Settings**.
    
  
3. On the Settings page, in the **General Settings** section, click **Advanced settings**.
    
  
4. On the Advanced Settings page:
    
  - If you want to reindex a library: in the **Reindex Library** section, click **Reindex Document Library**.
    
  
  - If you want to reindex a list: in the **Reindex List** section, click **Reindex List**.
    
  
5. Click **OK**.
    
  
The full reindex of the list or library will be performed during the next scheduled crawl.
## Default unused managed properties
<a name="DefaultUnusedMPs"> </a>

The following table provides an overview of the default unused managed properties that you can reuse and rename using an Alias.
### 

Managed property type Count Managed property characteristics Managed property name range Date  <br/> 10  <br/> Queryable  <br/> Date00 to Date09  <br/>  <br/> Date  <br/>  <br/> 20  <br/>  <br/> Multivalued, Queryable, Refinable, Sortable, Retrievable  <br/>  <br/> RefinableDate00 to RefinableDate19  <br/>  <br/> Decimal  <br/>  <br/> 10  <br/>  <br/> Queryable  <br/>  <br/> Decimal00 to Decimal09  <br/>  <br/> Decimal  <br/>  <br/> 10  <br/>  <br/> Multivalued, Queryable, Refinable, Sortable, Retrievable  <br/>  <br/> RefinableDecimal00 to RefinableDecimal09  <br/>  <br/> Double  <br/>  <br/> 10  <br/>  <br/> Queryable  <br/>  <br/> Double00 to Double09  <br/>  <br/> Double  <br/>  <br/> 10  <br/>  <br/> Multivalued, Queryable, Refinable, Sortable, Retrievable  <br/>  <br/> RefinableDouble00 to RefinableDouble09  <br/>  <br/> Integer  <br/>  <br/> 50  <br/>  <br/> Queryable  <br/>  <br/> Int00 to Int49  <br/>  <br/> Integer  <br/>  <br/> 50  <br/>  <br/> Multivalued, Queryable, Refinable, Sortable, Retrievable  <br/>  <br/> RefinableInt00 to RefinableInt49  <br/>  <br/> String  <br/>  <br/> 100  <br/>  <br/> Multivalued, Queryable, Refinable, Sortable, Retrievable  <br/>  <br/> RefinableString00 to RefinableString99  <br/> **How to use an Alias: an example**Say that you want to create a managed property that contains employee numbers, and you want users to be able to search for these by typing " **EmployeeID:12345** ", where " **12345** " is an example employee number. As this managed property is not of the type **Text** or **Yes/No**, you’ll follow the steps in [To create a managed property by renaming an existing one](#Schema_Tenant_SiteColl_Alias) with this input:
- Choose an unused managed property of the type **integer**, see the table [Default unused managed properties](#DefaultUnusedMPs). Use any unused property from **Int00** to **Int49** if you only want users to be able to query on the employee number, or from **RefinableInt00** to **RefinableInt49** if you want users to be able to query, refine, sort etc. on employee number.
    
  
- Give the property an Alias, in this example **EmployeeID**.
    
  
- Map the **EmployeeID** property to the crawled property that contains the employee numbers.
    
  

## Search schema changes that require content to be reindexed
<a name="Schema_Reindex_Table"> </a>


### 

Managed property setting Action Requires a full crawl to reindex  <br/> Mapping a crawled to a managed property  <br/>  <br/> Add/Delete mapping  <br/>  <br/> Yes  <br/>  <br/> Token normalization  <br/>  <br/> Enable/Disable  <br/>  <br/> Yes  <br/>  <br/> Complete matching  <br/>  <br/> Enable/Disable  <br/>  <br/> Yes  <br/>  <br/> Company name extraction  <br/>  <br/> Enable/Disable  <br/>  <br/> Yes  <br/>  <br/> Custom entity extraction  <br/>  <br/> Enable/Disable  <br/>  <br/> Yes  <br/>  <br/> Searchable  <br/>  <br/> Enable/Disable  <br/>  <br/> Yes  <br/>  <br/> Queryable  <br/>  <br/> Enable  <br/>  <br/> Yes  <br/>  <br/> Queryable  <br/>  <br/> Disable  <br/>  <br/> No  <br/>  <br/> Retrievable  <br/>  <br/> Enable  <br/>  <br/> Yes  <br/>  <br/> Retrievable  <br/>  <br/> Disable  <br/>  <br/> No  <br/>  <br/> Refinable  <br/>  <br/> Enable (if not already Sortable)  <br/>  <br/> Yes  <br/>  <br/> Refinable  <br/>  <br/> Disable  <br/>  <br/> No  <br/>  <br/> Sortable  <br/>  <br/> Enable (if not already Refinable)  <br/>  <br/> Yes  <br/>  <br/> Sortable  <br/>  <br/> Disable  <br/>  <br/> No  <br/>  <br/> Alias  <br/>  <br/> Add/Delete  <br/>  <br/> No  <br/> 
