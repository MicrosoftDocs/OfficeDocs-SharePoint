---
title: "Manage search dictionaries"
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
ms.assetid: 2d0ee673-02f1-4b52-9159-f743b5123460
description: "Learn how to manage search dictionaries. You can use search dictionaries to include or exclude company names to be extracted from the contents of your indexed documents, or you can include or exclude words for query spelling correction."
---

# Manage search dictionaries

Learn how to manage search dictionaries. You can use search dictionaries to include or exclude company names to be extracted from the contents of your indexed documents, or you can include or exclude words for query spelling correction.
  
## Manage company name extraction
<a name="__toc342653321"> </a>

> [!NOTE]
> Beginning on November 15th, 2019, we'll be removing Company Name Extraction from SharePoint Online. This will only impact you if you have configured company name extraction to be surfaced in the classic Enterprise Search Center as a refiner. Learn more about the specifics and other options by reading [Changes to company name extraction in SharePoint Online](changes-to-company-name-extraction-in-sharepoint-online.md).

For company name extraction to work, that is, for a company name to be pulled from your content and for it to be mapped to the managed property **companies**, you have to make sure that:
  
- The managed property setting **Company name extraction** is enabled on the managed property that you want to extract company names from. This setting is available for the managed properties **Title**, **Body** and **Notes**. See also [Manage the search schema in SharePoint](manage-search-schema.md).
    
- The name of the company that you want to extract is in the prepopulated company name dictionary or in the **Company Inclusions** list. 
    
Once you have done this, you can then use the managed property **companies** to create refiners based on the extracted company name in the **Refinement Web** **Part**, on the search results page. 
  
## Include company names
<a name="__toc342653322"> </a>

1. Go to the [More features page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true) and sign in with an account that has admin permissions for your organization.

>[!NOTE]
>If you have Office 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the More features page. <br>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**, and then select **Manage Search Dictionaries** to open the term store. 
    
3. On the **Site Settings: Term Store Management Tool** page, click the arrow to expand the **Search Dictionaries** menu. 
    
4. Click **Company Inclusions**, click the arrow and then click **Create Term**.
    
5. Type the name of the company that you want to include in the box that appears.
    
6. Click anywhere on the page to add the term to the **Company Inclusions** list. 
    
## Exclude company names
<a name="__toc342653323"> </a>

1. Go to the [More features page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true) and sign in with an account that has admin permissions for your organization.

>[!NOTE]
>If you have Office 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the More features page. <br>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**. 
 
3. Select **Manage Search Dictionaries** to open the term store.
   
4. On the **Taxonomy Term Store** page, click the arrow to expand the **Search Dictionaries** menu. 
    
5. Click **Company Exclusions**, click the arrow and then click **Create Term**.
    
6. Type the name of the company that you want to exclude in the box that appears.
    
7. Click anywhere on the page to add the term to the **Company Exclusions** list. 
    
## Manage query spelling correction
<a name="__toc342653324"> </a>

If you or another user enters a word in a search query that appears to be misspelled, the search results page helps you out by displaying query spelling corrections. These are important words in your indexed documents. This is also known as "Did you mean?".
  
For example, if you enter a query that contains the word "ampitheater", the query spelling correction would show "amphitheater" if this term is available in many places in your indexed documents. You can add terms such as the one just shown to the **Query Spelling Inclusions** list, or to the **Query Spelling Exclusions** list to influence how you want query spelling corrections to be applied or not. It takes up to 10 minutes for any changes to the **Query Spelling Inclusions** or the **Query Spelling Exclusions** list to take effect. 
  
## Include a term in query spelling corrections
<a name="__toc342653325"> </a>

1. Go to the [More features page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true) and sign in with an account that has admin permissions for your organization.

>[!NOTE]
>If you have Office 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the More features page. <br>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**. 
 
3. Select **Manage Search Dictionaries** to open the term store.

4. On the **Site Settings: Term Store Management Tool** page, click the arrow to expand the **Search Dictionaries** menu. 
    
5. Click **Query Spelling Inclusions**, click the arrow and then click **Create Term**.
    
6. Type the query spelling that you want to include in the box that appears.
    
7. Click anywhere on the page to add the term to the **Query Spelling Inclusions.**
    
## Exclude a term from query spelling corrections
<a name="__toc342653326"> </a>

1. Go to the [More features page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true) and sign in with an account that has admin permissions for your organization.

>[!NOTE]
>If you have Office 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the More features page. <br>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**. 
 
3. Select **Manage Search Dictionaries** to open the term store.
  
4. On the **Site Settings: Term Store Management Tool** page, click the arrow to expand the **Search Dictionaries** menu.
    
5. Click **Query Spelling Exclusions**, click the arrow and then click **Create Term**.
    
6. Type the query spelling that you want to exclude in the box that appears.
    
7. Click anywhere on the page to add the term to the **Query Spelling Exclusions** list. 
    
## Edit query spelling corrections or company names
<a name="__toc342653327"> </a>

1. Go to the [More features page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true) and sign in with an account that has admin permissions for your organization.

>[!NOTE]
>If you have Office 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the More features page. <br>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**.
 
3. Select **Manage Search Dictionaries** to open the term store.
   
4. On the **Site Settings: Term Store Management Tool** page, click the arrow to expand the **Search Dictionaries** menu.
    
5. Depending on which dictionary the term is in, click **Company Exclusions**, **Company Inclusions**, **Query Spelling Exclusions** or **Query Spelling Inclusions**.
    
6. Double-click the term that you want to edit.
    
7. Type the new name for the term.
    
8. Click anywhere on the page to save the edited term.
