---
title: "Configure properties of the Refinement Web Part in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/11/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 9f039270-d426-4e79-b608-8db792de74ed
description: "Learn how to configure properties of the Refinement Web Part, how to display refiner counts, and how to change the refiner display name."
---

# Configure properties of the Refinement Web Part in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
By default, the Refinement Web Part is used on all search vertical pages (results.aspx, peopleresults.aspx, conversationresults.aspx, videoresults.aspx). The Web Part filters search results from a Search Results Web Part into categories to help users narrow search results to help them find what they are looking for. By changing properties in the Refinement Web Part you can you can do the following:
  
- Specify a different Search Results Web Part from which to filter search results.
    
- Specify which refiners to show in the Web Part.
    
- Change the display template that is applied to each refiner.
    
Before you begin these procedures, verify the following:
  
- The managed properties that you want to use as refiners are set to refinable and queryable in the search schema. You can verify or change this by viewing or editing the **Main characteristics** of the managed property as described in [To add a managed property](manage-the-search-schema.md#proc2).
    
- You have done a full crawl of the content source that contains the managed properties that are enabled as refiners as described in [Start, pause, resume, or stop a crawl in SharePoint Server](start-pause-resume-or-stop-a-crawl.md).
    
    
## Configure properties of the Refinement Web Part
<a name="BKMK_Configure"> </a>

 **To configure the properties of a Refinement Web Part**
  
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the Enterprise Search Center site.
    
2. Browse to the page that contains the Refinement Web Part that you want to configure.
    
3. Click the **Settings** menu, and then click **Edit Page**.
    
4. In the Web Part, click the **Refinement Web Part Menu** arrow, and then click **Edit Web Part**. 
    
5. In the Web Part tool pane, in the **Refinement Target** section, select the Web Part from which from which to filter search results. By default, the Search Results Web Part is selected. 
    
6. In the Web Part tool pane, verify that the **Choose Refiners in this Web Part** is selected. 
    
7. Click **Choose Refiners**.
    
8. On the **Refinement configuration** page, from the **Available refiners** section, use the buttons to select which refiners should be shown in the Web Part, and also in what order that they should be shown. If you have specified an **Alias** for a refinable managed property, this alias is shown in the **Configuration for** section. 
    
9. In the **Configuration for** section, configure how you want each refiner to appear. 
    
    > [!NOTE]
    > If you have a single language site, you can change the refiner display name in the **Display name** section. For multilingual sites, you have to change the refiner display language as described in [Change the refiner display name](configure-properties-of-the-refinement-web-part.md#BKMK_DisplayName). 
  
## Change the refiner display name
<a name="BKMK_DisplayName"> </a>

By default, the name of the managed property that is enabled as a refiner will be used as display name for the refiner. In many cases, the managed property name is not user-friendly — for example, RefinableString00 or ColorOWSTEXT. You can change the display name of the refiner by changing a java script file in the master page gallery.
  
 **To change the refiner display name**
  
1.  Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the Enterprise Search Center site. 
    
2. On the **Settings** menu, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Web Designer Galleries** section, click **Master pages and page layouts**. 
    
4. On the **Master Page Gallery** page, click **Display Templates**.
    
5. On the **Display Templates** page, click **Language Files**.
    
6. On the **Language Files** page, click the folder that contains the language for which you want to change the refiner display name. 
    
7. Open the **CustomStrings.js** file. 
    
8. Add one line to the file for each managed property that is enabled as a refiner for which you want to change the display name by using the following syntax: 
    
     `"rf_RefinementTitle_ManagedPropertyName": "Sample Refinement Title for ManagedPropertyName"`
    
    For example, you can add the following line to change the display name for the managed property RefinableInt00 to Price: 
    
     `"rf_RefinementTitle_RefinableInt00": "Price"`.
    
## Add refiner counts to the Refinement Web Part
<a name="BKMK_AddRefinerCounts"> </a>

By default, the Refiner Web Part will not show refiner counts — that is, the number of items for each refiner value. For example, if you have enabled the managed property Color as a refiner, the refiner values will only show colors such as Red, Green, and Blue. You can add refiner counts by changing a value in an HTML file so that the refiner values are shown as Red (10), Green (12), and Blue (8).
  
 **To add refiner counts to the Refinement Web Part**
  
1.  Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the Enterprise Search Center site. 
    
2. On the **Settings** menu, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Web Designer Galleries** section, click **Master pages and page layouts**. 
    
4. On the **Master Page Gallery** page, click **Display Templates**.
    
5. On the **Display Templates** page, click **Filters**.
    
6. Open the **Filter_Default.html** file. 
    
7. Change the value for **ShowCounts** to **true**.
    
8. Save the file.
    

