---
title: "Configure cross-site publishing in SharePoint Server"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 7/18/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: b08c20f6-a142-4001-a92a-cee49b1145b2
description: "Learn to create and tag catalog content in authoring sites and configure search settings for cross-site publishing in SharePoint Server."
---

# Configure cross-site publishing in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
Before you configure cross-site publishing, make sure that you understand the concepts and terminology in [Plan for cross-site publishing in SharePoint Server](plan-for-cross-site-publishing.md).
  
    
## Before you begin
<a name="BKMK_Accessibility"> </a>

> [!NOTE]
>  Because SharePoint Server runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server supports the accessibility features of supported browsers. For more information, see the following resources: > [Plan browser support in SharePoint 2013](https://go.microsoft.com/fwlink/p/?LinkId=246502)> [Accessibility guidelines in SharePoint Server 2016](https://docs.microsoft.com/en-us/sharepoint/accessibility-guidelines)> [Accessibility features in SharePoint Online](https://go.microsoft.com/fwlink/p/?LinkId=246501)> [Keyboard shortcuts](https://support.office.com/en-us/article/keyboard-shortcuts-86d68234-7f1a-40fc-a3d6-4c39c7a5ddaf?ocmsassetID=HA010369395&CorrelationId=1313c2d0-6e28-43a4-bc2b-d7be614597f3&ui=en-US&rs=en-US&ad=US)> [Windows Touch Gestures Overview](https://go.microsoft.com/fwlink/p/?LinkId=246506)
  
## Create site collections for cross-site publishing
<a name="BKMK_Create_site_collections"> </a>

In a cross-site collection publishing scenario where content is reused across site collections, you must have at least two site collections, one for authoring content and one for publishing content. Before you create the site collections, review the following information:
  
- "Plan site collections and site structure for SharePoint authoring sites" in [Plan authoring sites for cross-site publishing in SharePoint Server](plan-sharepoint-authoring-sites-for-cross-site-publishing.md).
    
-  "Plan site collections and site structure for SharePoint publishing sites" in [Plan publishing sites for cross-site publishing in SharePoint Server](plan-sharepoint-publishing-sites-for-cross-site-publishing.md).
    
For information about how to create a site collection by using either Central Administration or Microsoft PowerShell, see [Create a site collection in SharePoint Server](../sites/create-a-site-collection.md).
  
## Activate the Cross-Site Collection Publishing feature
<a name="BKMK_Activate"> </a>

Before you can use cross-site collection publishing to reuse content across site collections, you have to activate the Cross-Site Collection Publishing feature on the authoring site collection.
  
> [!NOTE]
> If you used the Product Catalog Site Collection template to create the authoring site collection, you do not have to do this operation. By default, the Cross-Site Collection publishing feature is active when you create a site collection by using the Product Catalog Site Collection template. 
  
 **To activate the Cross-Site Collection Publishing feature**
  
1. Verify that the user account that performs this procedure is a site collection administrator on the authoring site collection. 
    
2. On the top-level site of the authoring site collection, on the **Settings** menu, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Site Collection Administration** section, click **Site collection features**.
    
4. On the **Site Collection Features** page, next to **Cross-Site Collection Publishing**, click **Activate**.
    
> [!NOTE]
> Deactivating the Cross-Site Publishing feature on an authoring site will not remove the contents of a connected catalog from a publishing site. By deactivating this feature, you will no longer be able to modify existing catalog settings, or connect other publishing sites to catalogs within the site collection. To remove contents of a connected catalog from a publishing site, you have to disconnect the publishing site from the catalog. For more information, see [Disconnect a publishing site from a catalog](connect-a-publishing-site-to-a-catalog.md#BKMK_Disconnect). 
  
## Create content for authoring sites
<a name="BKMK_Create_content"> </a>

Before you create content for authoring sites, review "Plan term sets for tagging content on authoring sites" and "Plan catalog content for authoring sites" in [Plan authoring sites for cross-site publishing in SharePoint Server](plan-sharepoint-authoring-sites-for-cross-site-publishing.md).
  
### Create and manage term sets for tagging content on authoring sites
<a name="BKMK_CreateTermSet"> </a>

You create and manage term sets by using the Term Store Management Tool. For information about how to create and manage term sets, see the following articles:
  
- [Set up a new term set](https://docs.microsoft.com/sharepoint/set-up-new-term-set)
    
- [Create and manage terms in a term set](https://docs.microsoft.com/sharepoint/create-and-manage-terms)
    
After you have created a term set, you have to make it available for tagging content. If you used the Product Catalog Site Collection template to create the authoring site collection, and you have created a term set in this site collection, you do not have to do this operation. By default, new term sets created in the Product Catalog site collection are available for tagging content.
  
 **To make a term set available for tagging content**
  
1. Verify that the user account that performs this procedure is a member of the Owners SharePoint group on the authoring site that contains the catalog.
    
2. On the authoring site, on the **Settings** menu, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Site Administration** section, click **Term store management**.
    
4. In the **TAXONOMY TERM STORE** section, click the term set that you want to make available for tagging. 
    
5. Click the **INTEDED USE** tab, and then select **Available for Tagging**.
    
6. Click **Save**.
    
### Create catalog content by using SharePoint lists
<a name="BKMK_Create_catalog_content_lists"> </a>

When you create catalog content by using SharePoint lists, we recommend that you create site columns for the lists in which you want to maintain your catalog content. This is because managed properties are automatically created for site columns, and you can use these managed properties when defining queries for you catalog content on a publishing site. If you have several lists, we recommend that you create a site content type for each list, and then associate the appropriate site columns to this site content type. If you want to use managed navigation to display catalog content on a publishing site, you also have to create at least one term set as described in [Create and manage term sets for tagging content on authoring sites](configure-cross-site-publishing.md#BKMK_CreateTermSet). The tagging term set must be tied to a site column that is a Managed Metadata data type.
  
For information about how to create site content types and site columns, see the following articles:
  
- [Create or customize a content type](https://office.microsoft.com/en-us/sharepoint-server-help/create-or-customize-a-content-type-HA102773269.aspx?CTT=1)
    
- [Create a column in a SharePoint list or library](https://support.office.com/article/2b0361ae-1bd3-41a3-8329-269e5f81cfa2)
    
- [Create a managed metadata column](https://office.microsoft.com/en-us/office365-sharepoint-online-enterprise-help/create-a-managed-metadata-column-HA102832524.aspx?CTT=1)
    
If you have large amounts of data in external business systems — for example, an ERP system — consider importing this data into one or more SharePoint lists. SharePoint Server does not have a solution for importing list content. However, you can develop custom import tools — for example, by using Microsoft PowerShell. For a set of example Microsoft PowerShell scripts that you can use to import list content for cross-site publishing, see [Import list content to Products list for SharePoint 2013 Preview](https://gallery.technet.microsoft.com/Import-list-content-to-f735d7fb). The example scripts import content only to a site collection that was created by using the Product Catalog Site Collection template.
  
### Share a library or list as a catalog
<a name="BKMK_Share_library_list_as_catalog"> </a>

Before you share a library or list as a catalog, verify that the Cross-Site Collection Publishing feature is activated for the site collection. If you used the Product Catalog Site Collection template to create the site collection, the Cross-Site Collection Publishing feature is already active. For all other types of site collections, you must activate the Cross-Site Collection Publishing feature before you can continue with the following steps. For more information, see [Activate the Cross-Site Collection Publishing feature](configure-cross-site-publishing.md#BKMK_Activate) earlier in this article. 
  
By default, anonymous access is enabled when you share a library or list as a catalog. If you have connected a publishing site to the catalog, and you don't want anonymous users to be able to view and search content that was added to the search index from this catalog, you should disable anonymous access.
  
> [!IMPORTANT]
> In addition to enabling anonymous access for a catalog, you must enable anonymous access for the web application and publishing site so that anonymous users can search and view the content. For more information, see [Create claims-based web applications in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee806885(v=office.14)). 
  
 **To share a library or list as a catalog**
  
1. Verify that the user account that performs this procedure is a member of the Owners group on the site that contains the library or list that you want to share. 
    
2. Browse to the library or list that you want to share, and then do one of the following:
    
  - To share a library, click the **LIBRARY** tab, and then, on the ribbon, in the **Settings** group, click **Library Settings**.
    
  - To share a list, click the **LIST** tab, and then, on the ribbon, in the **Settings** group, click **List Settings**.
    
3. On the **Settings** page, in the **General Settings** section, click **Catalog Settings**.
    
4. On the **Catalog Settings** page, in the **Catalog Sharing** section, select the **Enable this library as a catalog** check box. 
    
5. In the **Anonymous Access** section, if you want don't want anonymous users to view and search this content, click **Disable anonymous access**.
    
6. In the **Catalog Item URL Fields** section, in the **Available fields** box, select up to five fields that uniquely identify an item in the library or list, and then click **Add**. 
    
    After you connect a publishing site to this catalog, the fields that you specified as catalog item URL fields appear as part of the friendly URL. (See the example that follows this procedure.) 
    
7. In the **Navigation Hierarchy** section, select the column that is associated with the term set that you want to use as a navigation term set for catalog pages. After you connect a publishing site to this library or list to show catalog content, the value of the column that you selected appears as part of the friendly URL (see the example that follows this procedure). 
    
    > [!NOTE]
    > You only have to make a selection in this section if you want to use managed navigation to display catalog content on a publishing site. 
  
8. Click **OK**.
    
    > [!NOTE]
    > After you share a library or list as a catalog, the content source that contains the catalog must be crawled. You don't have to start a full crawl. This is because an incremental crawl or a continuous crawl also adds the content to the search index. For more information, see [Start, pause, resume, or stop a crawl in SharePoint Server](../search/start-pause-resume-or-stop-a-crawl.md). 
  
In this example, let's say that you have a list that contains data for different electronic products. The following items were specified when the list was shared as catalog:
  
> Electronic products
    
    - Audio
    
  - Car audio
    
  - MP3
    
    - Computers
    
  - Laptops
    
  - Desktops
    
Each item in the shared list is associated with a value from this term set in the Item Category Managed Metadata site column. For more information about Managed Metadata columns, see [Create a Managed Metadata column](https://office.microsoft.com/en-us/sharepoint-server-help/create-a-managed-metadata-column-HA101631602.aspx?CTT=1).
  
The following table describes how site columns and their corresponding values in the previous list are combined to create friendly URLs for catalog content when you connect a publishing site collection to this list.
  
|**Product title**|**Item Category**|**Item Number**|**Friendly URL to an item when the catalog is connected to a publishing site**|
|:-----|:-----|:-----|:-----|
|Proseware 50W Car Radio  <br/> |Car audio  <br/> |1010101  <br/> |\<site\>/audio/car-audio/1010101  <br/> |
|Contoso 4GB Portable MP3 Player M450  <br/> |MP3  <br/> |4020102  <br/> |\<site\>/audio/mp3/4020102  <br/> |
|AdventureWorks Laptop8.9 E0890  <br/> |Laptops  <br/> |7030906  <br/> |\<site\>/computers/laptops/7030906  <br/> |
|WWI Desktop PC2.33 X2330  <br/> |Desktops  <br/> |7030906  <br/> |\<site\>/computers/desktops/3030802  <br/> |
   
### Make a term set available to other site collections
<a name="BKMK_Make_term_set_available"> </a>

After you create a term set on the authoring site collection, you have to make it available to publishing site collections. You can make a term set available to all site collections or to specific site collections.
  
 **To make a term set available to all site collections**
  
1. Verify that the user account that performs this procedure is a member of the Owners SharePoint group on the authoring site that contains the catalog.
    
2. On the authoring site, on the **Settings** menu, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Site Administration** section, click **Term store management**. If the user that performs this procedure is already a member of the Term Store Administrators group, you can skip to step 7.
    
4. In the **Term Store Management Tool**, verify that **Managed Metadata Service** is selected. 
    
5. In the **Term Store Administrator** section, type one or more user names. 
    
6. Click **Save**.
    
7. Right-click **Managed Metadata Service**, and then select **New Group**.
    
8. Type the name of the global term set that you want to create, and then press **Enter**.
    
9. Refresh the page.
    
10. Right-click the term set that you want to make available to all site collections, and then click **Move Term Set**.
    
11. In the **Term Set Move** dialog box, click the global term set that you want to move the term set to, and then click **OK**.
    
12. Refresh the page.
    
 **To make a term set available to specific site collections**
  
1. Verify that the user account that performs this procedure is a member of the Owners SharePoint group on the authoring site that contains the catalog.
    
2. On the authoring site, on the **Settings** menu, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Site Administration** section, click **Term store management**.
    
4. In the **Term Store Management Tool**, click the group that contains all term sets within the site collection. 
    
5. In the **Site Collection Access** section, type the URLs of the site collections to which you want to make the term set available — for example, http://<site>/sites/products. 
    
6. Click **Save**.
    
## Configure search for cross-site publishing
<a name="BKMK_Configure_search"> </a>

Because cross-site publishing depends on search, you have to create a content source and manage crawling for SharePoint Server cross-site publishing sites.
  
A content source specifies what, when, and how content should be crawled. When a Search service application is created, a content source named Local SharePoint sites is created and is automatically configured to crawl all SharePoint Server sites in the local server farm. You can create additional content sources to specify other content to crawl and define how SharePoint Server should crawl that content. You do not have to create a separate content source for catalog content in order to make content available to other site collections. However, it is easier to maintain crawl schedules when you have separate content sources for the different content that you want users to view and search. 
  
The ability to enable continuous crawls is a new crawl schedule option in SharePoint Server. When you enable continuous crawls, any changes that are made to content within the specified content source is picked up automatically by the crawler and added to the search index. A continuous crawl starts at set intervals. The default interval is 15 minutes, but you can set continuous crawls to occur at shorter intervals by using Microsoft PowerShell. 
  
For information about how to create a new content source and manage crawling in Central Administration, see the following articles:
  
- [Add, edit, or delete a content source in SharePoint Server](../search/add-edit-or-delete-a-content-source.md)
    
- [Start, pause, resume, or stop a crawl in SharePoint Server](../search/start-pause-resume-or-stop-a-crawl.md)
    
- [Manage continuous crawls in SharePoint Server](../search/manage-continuous-crawls.md)
    
### Reindex catalog content
<a name="BKMK_Perform_crawl_catalog"> </a>

Some actions — for example, doing search schema management to enable refiners — require a full reindex of the content source that contains the catalog for the changes to be added to the search index. A site collection administrator can independently of the Search service application administrator indicate that a catalog should be fully reindexed during the next scheduled crawl of the catalog.
  
 **To reindex catalog content**
  
1. Verify that the user account that performs this procedure is a member of the Site collection administrators group on the site that contains the catalog.
    
2. Browse to the catalog, and then do one of the following:
    
  - If you want to perform a full crawl of a catalog in a library, click the **LIBRARY** tab, and then, on the ribbon, in the **Settings** group, click **Library Settings**.
    
  - If you want to perform a full crawl of a catalog in a list, click the **LIST** tab, and then, on the ribbon, in the **Settings** group, click **List Settings**.
    
3. On the **Settings** page, in the **General Settings** section, click **Advanced settings**.
    
4. On the **Advanced Settings** page, in the **Reindex List** section, click **Reindex List**, and then click **Reindex List** to confirm that you want the catalog to be reindexed during the next scheduled crawl. 
    
5. Click **OK**.
    
    > [!NOTE]
    > The full reindex of the catalog will be performed during the next scheduled crawl. 
  
## See also
<a name="BKMK_Configure_search"> </a>

#### Concepts

[Automatically created managed properties in SharePoint Server](../technical-reference/automatically-created-managed-properties-in-sharepoint.md)


