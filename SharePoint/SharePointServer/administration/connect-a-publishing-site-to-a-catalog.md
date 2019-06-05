---
title: "Connect a publishing site to a catalog in SharePoint Server"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 7/18/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: d32c1b21-60c4-465e-82c9-d907d913f8aa
description: "Learn how to connect a publishing site collection to a library or list that is shared as a catalog."
---

# Connect a publishing site to a catalog in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
To show content from a library or list that is shared as a catalog, you must connect the publishing site collection to the catalog. When you connect a publishing site collection to a catalog, the following occurs: 
  
- The catalog content is integrated into the publishing site collection.
    
- The term set used by the catalog is integrated into the term set of the publishing site collection.
    
- A category page and an item details page are created for the catalog pages.
    
- Friendly URL is created for the item details page.
    
- A result source is created for the catalog.
    
    
## Before you begin
<a name="BKMK_Before"> </a>

> [!NOTE]
>  Because SharePoint Server runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server supports the accessibility features of supported browsers. For more information, see the following resources: > [Plan browser support](https://go.microsoft.com/fwlink/p/?LinkId=246502)> [Accessibility for SharePoint 2013](/SharePoint/accessibility-guidelines)> [Accessibility features in SharePoint 2013 Products](https://go.microsoft.com/fwlink/p/?LinkId=246501)> [Keyboard shortcuts](https://go.microsoft.com/fwlink/p/?LinkID=246504)> [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506)
  
Before you connect the publishing site collection to a catalog, review the information in [Plan category pages and catalog item pages](plan-sharepoint-publishing-sites-for-cross-site-publishing.md#BKMK_PlanCategoryPagesAndItemDetailPages). Also verify the following:
  
- The publishing site that you connect to a catalog uses managed navigation. By default, site collections that are created by using the Publishing Portal Site Collection template use managed navigation.
    
- The library or list was shared as a catalog, as described in [Share a library or list as a catalog](configure-cross-site-publishing.md#BKMK_Share_library_list_as_catalog).
    
- A full crawl of the content source that contains the catalog was performed, as described in [Configure search for cross-site publishing](configure-cross-site-publishing.md#BKMK_Configure_search).
    
- The term set that is used by the catalog is available to the publishing site collection, as described in [Make a term set available to other site collections](configure-cross-site-publishing.md#BKMK_Make_term_set_available).
    
> [!NOTE]
> If you want to extend the web application for your publishing site, for example to support different authentication providers, extend the web application  *before*  you do this procedure. If you extend the web application after you've connected to a catalog, the friendly URLs to your catalog items will be broken. 
  
## Connect a publishing site to a catalog
<a name="BKMK_Connect"> </a>

 **To connect a publishing site to a catalog**
  
1. Verify that the user account that completes this procedure is a member of the Owners SharePoint group on the publishing site collection.
    
2. On the publishing site collection, on the **Settings** menu, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Site Administration** section, click **Manage catalog connections**.
    
4. On the **Manage catalog connections** page, click **Connect to a catalog**. A list of available catalogs appears. Note that only catalogs that have been crawled will appear.
    
5. On the line that contains the catalog that you want to connect to, click **Connect**. You can also search for a specific catalog by typing the catalog name in the search field.
    
6. On the **Catalog Source Settings** page, in the **Connection Integration** section, do one of the following: 
    
  - To make catalog content available to the publishing site and integrate the catalog tagging term set into the publishing site navigation term set, select **Integrate the catalog into my site**. When you select this option, use the following steps to specify at which level the term sets should be integrated, specify the URL for the catalog item details page, and select category pages and catalog item pages. 
    
  - To make the catalog content available to the publishing site, select **Connect, but do not integrate the catalog**. You should select this option if you want to use content from the library to create individual catalog item pages. 
    
    Either option creates a result source for the catalog.
    
7. In the **Navigation Hierarchy** section, specify the term from which the catalog tagging term set should be integrated into the publishing site navigation term set. The catalog navigation column that you previously configured in [Share a library or list as a catalog](configure-cross-site-publishing.md#BKMK_Share_library_list_as_catalog) appears by default. The fields in this section are optional. Therefore, if you don't change the fields in this section, the catalog tagging term set will be integrated from the root term. If you want to integrate the catalog tagging term set from a different term, do the following: 
    
  - Next to the **Root term of hierarchy** box, click **Browse for a valid choice**.
    
  - In the **Select: Add Terms** dialog box, click the term that corresponds to the level from which you want to integrate the catalog tagging term set, click **Select**, and then click **OK**.
    
  - To integrate the root term that is the parent of the selected term in the publishing site navigation term set, select the **Include root term in site navigation** check box. 
    
    > [!NOTE]
    > All items in the catalog must be tagged with a term from the specified catalog tagging term set. If this is not done, site navigation will not work as intended for all items. 
  
8. In the **Navigation Position** section, specify the term in the publishing site navigation term set where the catalog tagging term set should be integrated. Do one of the following: 
    
  - To integrate the catalog tagging term set to the root term of the publishing site navigation term set, click **Add to navigation root**.
    
  - To integrate the catalog tagging term set to a term below the root term of the publishing site navigation term set, click **Select an alternate location in site navigation**, and then do the following:
    
  - Click **Browse for a valid choice** to display the publishing site navigation term set. 
    
  - In the **Select: Add Terms** dialog box, click the term that corresponds to the level from which you want to integrate the catalog tagging term set, click **Select**, and then click **OK**.
    
9. If you want changes to the catalog tagging term set to be updated on the publishing site, in the **Navigation Pinning** section, select the **Pin terms to site navigation** check box. By default, this option is selected. If you clear this check box, changes made to the catalog tagging term set are not reflected on the publishing site navigation. 
    
10. In the **Catalog Item URL Behavior** section, specify what you want the URL of the catalog item to do by selecting one of the following options: 
    
  - To point the URL of the catalog item to an item details page, select **Make URLs relative to this site**. When you select this option, you have to specify a catalog item URL format as described in the next step. This also means that the content that you can display on the item details page has to come from the search index. 
    
  - To have the catalog item URL point to the item in the source catalog, select **Make URLs point to source catalog**. When you select this option, you do not have to specify a catalog item URL format. Note that when you select this option, anonymous users are not able to access and view the item in the source catalog.
    
11. In the **Catalog Item URL Format** section, select which properties the URL of the item details page should contain by doing one of the following: 
    
  - To use the field that you specified as Primary Key the when you shared the library or list as a catalog as described in [Share a library or list as a catalog](configure-cross-site-publishing.md#BKMK_Share_library_list_as_catalog), select **Use the default URL format provided by the catalog source**. By default, this option is already selected.
    
    > [!NOTE]
    > All items in the catalog must have values for the specified field. Site navigation will not work as intended for items with missing values. 
  
  - To manually define a format for the URL, select **Manually define a URL format**, and then type in a URL. You should select this option only if you have created an item details page and the items in your catalog are not tagged with a term from a catalog tagging term set. Type the URL in the following format: / _\<Folder of item details page\>_ _/\<Name of item details page\>_.aspx?  _\<Managed property name\>_=[ _Managed property value_] — for example, /Pages/itemdetails.aspx?TitleProperty=[Title]. 
    
  - To construct a custom URL based on catalog properties, select **Construct a URL format from catalog properties**, and then do the following:
    
  - In the **Available Fields** list, select up to five fields, and then click **Add**.
    
    > [!IMPORTANT]
    > Fields of site column type Number will not create a valid URL. All items in the catalog must have values for the specified fields. Site navigation will not work as intended for items with missing values. 
  
12. In the **Category Page** section, do one of the following: 
    
  - To have SharePoint Server automatically create a new Category page for your catalog content, click **Create a new page**, and then select a master page. The page will be added to the Pages library with the name  _Category-\<catalog tagging term set name\>_. The page will not be published automatically.
    
  - To use a Category page that was already created, select **Use an existing page**, and then specify the location of the page. 
    
13. In the **Item Page** section, do one of the following: 
    
  - To have SharePoint Server automatically create a new Item page for your catalog content, click **Create a new page**, and then select a master page. The page will be added to the Pages library with the name  _CatalogItem-\<catalog tagging term set name\>_. The page will not be published automatically. 
    
  - To use an already created Item page, select **Use an existing page**, and specify the location of this page.
    
14. Click **OK**.
    
## Disconnect a publishing site from a catalog
<a name="BKMK_Disconnect"> </a>

If you want to remove the content of a connected catalog from a publishing site, you have to disconnect the publishing site from the catalog.
  
> [!IMPORTANT]
> If you have integrated a catalog tagging term set into the publishing site navigation term set, the tagging terms will not be removed from the navigation when you disconnect from the catalog. To remove the tagging terms from the navigation, you have to delete the terms in Term Store Management. For more information, see [Create and manage terms in a term set](https://docs.microsoft.com/sharepoint/create-and-manage-terms).
  
Also, if you had SharePoint Server automatically create a category page and an item details page for the catalog pages, these will not be deleted from the Pages library when you disconnect from the catalog.
  
 **To disconnect a publishing site from a catalog**
  
1. Verify that the user account that completes this procedure is a member of the Owners SharePoint group on the publishing site collection.
    
2. On the **Site Settings** page, in the **Site Administration** section, click **Manage catalog connections**.
    
3. On the **Manage catalog connections** page, a list of connected catalogs appears. 
    
4. On the line that contains the catalog that you want to disconnect, click **Disconnect**, and then **Disconnect** to verify that you want to disconnect the catalog. 
    
## See also
<a name="BKMK_Disconnect"> </a>

#### Other Resources

[Blog post: Connect your publishing site to a catalog](https://blogs.technet.com/b/tothesharepoint/archive/2013/03/07/stage-5-connect-your-publishing-site-to-a-catalog.aspx)

