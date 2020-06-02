---
title: "Stage 7 Upload page layouts and create new pages in a publishing site in SharePoint Server"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 12/29/2016
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 5310987c-4499-4092-ac0c-fc4c1bb1a58d
description: "Learn how to upload page layouts and create new pages in a publishing site in SharePoint Server 2016."
---

# Stage 7: Upload page layouts and create new pages in a publishing site in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
> [!NOTE]
> Many of the features described in this series are also available for most sites in SharePoint for Microsoft 365. 
  
## Quick overview

[Stage 6: Upload and apply a new master page to a publishing site in SharePoint Server](stage-6-upload-and-apply-a-new-master-page-to-a-publishing-site.md) explained how to upload and apply a new master page. The next step in giving our site a "Contoso look" is to create new pages. 
  
In this stage, you'll learn:
  
- [About page layouts](stage-7-upload-page-layouts-and-create-new-pages-in-a-publishing-site.md#BKMK_AboutPageLayouts)
    
- [About pages and rendered pages](stage-7-upload-page-layouts-and-create-new-pages-in-a-publishing-site.md#BKMK_AboutPagesAndRenderedPages)
    
- [How to upload a new page layout](stage-7-upload-page-layouts-and-create-new-pages-in-a-publishing-site.md#BKMK_HowToUploadANewPageLayout)
    
- [How to turn off versioning for the Pages Library](stage-7-upload-page-layouts-and-create-new-pages-in-a-publishing-site.md#BKMK_HowToTurnOffVersioningForThePagesLibrary)
    
- [How to create a page based on a page layout](stage-7-upload-page-layouts-and-create-new-pages-in-a-publishing-site.md#BKMK_HowToCreateAPageBasedOnAPageLayout)
    
> [!NOTE]
> This article doesn't cover how to create a page layout. It explains how to upload already completed page layouts. These files won't be made available for download. 
  
## Start stage 7

### About page layouts
<a name="BKMK_AboutPageLayouts"> </a>

A **page layout** is a template for a page in your site. This is where you define the layout and structure for the body of a page. 
  
Page layouts contain page field controls and Web Part zones. Page field controls and Web Part zones are placeholders that define where content can be added by authors. They are added to a page layout at a specific position, for example on the left side of a column, and with specific style elements, such as bold.
  
![Page Layout](../media/OTCSP_PageLayout.png)
  
[Stage 6: Upload and apply a new master page to a publishing site in SharePoint Server](stage-6-upload-and-apply-a-new-master-page-to-a-publishing-site.md) explained how SharePoint Server 2016 automatically converts an HTML master page into an ASP.NET page. The same rule applies to page layouts. You can create a page layout in HTML format and SharePoint Server 2016 will automatically convert it to an ASP.NET page for you. This means that you can design your page layout using your favorite HTML editor, and focus on HTML, CSS, and JavaScript. You don't have to worry about ASP.NET or SharePoint specific markup. 
  
For more information, see:
  
- [Overview of the SharePoint 2013 page model](https://go.microsoft.com/fwlink/p/?LinkId=400535)
    
- [How to: Create a page layout in SharePoint 2013](https://go.microsoft.com/fwlink/p/?LinkId=400538)
    
### About pages and rendered pages
<a name="BKMK_AboutPagesAndRenderedPages"> </a>

It is important to understand that authors do not add content to a page layout. Content is added to a **page**. 
  
A page is created based on a specific page layout. Once you've created a page, authors can add content that they want to display on their website to the page. Because the page is based on a page layout with page field controls and Web Part zones, authors can't add content outside these areas.
  
When visitors browse a site, they will see a rendered page. In a rendered page, the master page is merged with the page layout, and the content for the page is displayed in the page fields and Web Part zones.
  
![Rendered Page](../media/OTCSP_RenderedPage.png)
  
For more information, see [Overview of the SharePoint 2013 page model](https://go.microsoft.com/fwlink/p/?LinkId=400535).
  
### How to upload a new page layout
<a name="BKMK_HowToUploadANewPageLayout"> </a>

In our Contoso scenario, we have two page layouts: one for the category page, and one for the catalog item page.
  
[Stage 6: Upload and apply a new master page to a publishing site in SharePoint Server](stage-6-upload-and-apply-a-new-master-page-to-a-publishing-site.md) explained how to map a network drive. Because we have mapped our network drive, uploading these page layouts becomes very easy. Simply drag-and-drop the files into your **Master Page Gallery**. 
  
![Drag and Drop](../media/OTCSP_DragAndDrop.png)
  
In SharePoint, refresh the **Master Page Gallery** page to see that the two page layouts are added. Also notice that an associated ASP.NET file was created for the page layouts. 
  
![Pages Added to MPG](../media/OTCSP_PagesAddedToMPG.png)
  
### How to turn off versioning for the Pages Library
<a name="BKMK_HowToTurnOffVersioningForThePagesLibrary"> </a>

In our scenario, we are not using SharePoint workflows for approval. The files have already been approved. Therefore, before we create a new page, we want to turn off versioning for the **Pages** library. 
  
To turn off versioning for the **Pages** library: 
  
1. From the **Site Settings** menu, select **Site contents**. 
    
     ![Create Search Vertical: Site Contents](../media/OTCSP_SiteContents.png)
  
2. On the **Site Contents** page, select **Pages**. 
    
3. In the **Pages** library, on the **LIBRARY** tab, select **Library Settings**. 
    
4. On the **Settings** page, select **Versioning settings**. 
    
5. In the **Require Check Out section**, for **Require documents to be checked out before they can be edited**, select **No**. 
    
     ![Versioning](../media/OTCSP_Versioning.png)
  
We are now ready to create our two new pages.
    
### How to create a page based on a page layout
<a name="BKMK_HowToCreateAPageBasedOnAPageLayout"> </a>

To create a new page:
  
1. On the **Site Contents** page, select **Pages**. 
    
2. In the **Pages** library, select the **FILES** tab, and then select **New Document**. 
    
     ![New Document](../media/OTCSP_NewDocument.png)
  
3. On the **Create Page** page, enter a **Title** and a **URL name**. From the **Page Layout** list, select the page layout that you want to apply to the new page. In our scenario, the page layout is the newly uploaded page layout called *ContosoElectronicsCategoryPageLayout*. 
    
     ![Create Page](../media/OTCSP_CreatePage.png)
  
After you select **OK**, the newly created page is shown in the **Pages** library. 
    
     ![New Category Page](../media/OTCSP_NewCategoryPage.png)
  
4. In our Contoso scenario, we'll also need a catalog item page. To create this page, repeat Steps 3 and 4 from the previous procedure. However for **Page Layout**, select *ContosoElectroniceCatalogItemPageLayout*. 
    
     ![Create Catalog Item Page](../media/OTCSP_CreateCatalogItemPage.png)
  
Our **Pages** library now contains two new pages: *ContosoCategoryPage* and *ContosoCatalogItemPage*. 
    
     ![Two New Pages](../media/OTCSP_TwoNewPages.png)
  
Now that we have created these pages, the next step is to assign them to the terms that drive our site navigation.
  
#### Next article in this series

[Stage 8: Assign a category page and a catalog item page to a term in SharePoint Server](stage-8-assign-a-category-page-and-a-catalog-item-page-to-a-term.md)
  
## See also

#### Other Resources

[How to: Create a page layout in SharePoint Server 2013](https://msdn.microsoft.com/library/jj822368.aspx)
  
[Add snippets to a master page or a page layout in SharePoint Server 2013](https://msdn.microsoft.com/library/office/jj822367.aspx)

