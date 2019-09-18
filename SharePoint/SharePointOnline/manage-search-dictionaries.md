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

For company name extraction to work, that is, for a company name to be pulled from your content and for it to be mapped to the managed property **companies**, you have to make sure that:
  
- The managed property setting **Company name extraction** is enabled on the managed property that you want to extract company names from. This setting is available for the managed properties **Title**, **Body** and **Notes**. See also [Manage the search schema in SharePoint Online](manage-search-schema.md).
    
- The name of the company that you want to extract is in the prepopulated company name dictionary or in the **Company Inclusions** list. 
    
Once you have done this, you can then use the managed property **companies** to create refiners based on the extracted company name in the **Refinement Web** **Part**, on the search results page. 
  
## Include company names
<a name="__toc342653322"> </a>

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
    
3. In the left pane, select **Classic features**. 
 
4. Under **Search**, select **Open**, and then select **Manage Search Dictionaries** to open the term store. 
    
5. On the **Site Settings: Term Store Management Tool** page, click the arrow to expand the **Search Dictionaries** menu. 
    
6. Click **Company Inclusions**, click the arrow and then click **Create Term**.
    
7. Type the name of the company that you want to include in the box that appears.
    
8. Click anywhere on the page to add the term to the **Company Inclusions** list. 
    
## Exclude company names
<a name="__toc342653323"> </a>

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  

2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
    
3. In the left pane, select **Classic features**. 
 
4. Under **Search**, select **Open**. 
 
5. Select **Manage Search Dictionaries** to open the term store.
   
6. On the **Taxonomy Term Store** page, click the arrow to expand the **Search Dictionaries** menu. 
    
7. Click **Company Exclusions**, click the arrow and then click **Create Term**.
    
8. Type the name of the company that you want to exclude in the box that appears.
    
9. Click anywhere on the page to add the term to the **Company Exclusions** list. 
    
## Manage query spelling correction
<a name="__toc342653324"> </a>

If you or another user enters a word in a search query that appears to be misspelled, the search results page helps you out by displaying query spelling corrections. These are important words in your indexed documents. This is also known as "Did you mean?".
  
For example, if you enter a query that contains the word "ampitheater", the query spelling correction would show "amphitheater" if this term is available in many places in your indexed documents. You can add terms such as the one just shown to the **Query Spelling Inclusions** list, or to the **Query Spelling Exclusions** list to influence how you want query spelling corrections to be applied or not. It takes up to 10 minutes for any changes to the **Query Spelling Inclusions** or the **Query Spelling Exclusions** list to take effect. 
  
## Include a term in query spelling corrections
<a name="__toc342653325"> </a>

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  

2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
    
3. In the left pane, select **Classic features**. 
 
4. Under **Search**, select **Open**. 
 
5. Select **Manage Search Dictionaries** to open the term store.

5. On the **Site Settings: Term Store Management Tool** page, click the arrow to expand the **Search Dictionaries** menu. 
    
6. Click **Query Spelling Inclusions**, click the arrow and then click **Create Term**.
    
7. Type the query spelling that you want to include in the box that appears.
    
8. Click anywhere on the page to add the term to the **Query Spelling Inclusions.**
    
## Exclude a term from query spelling corrections
<a name="__toc342653326"> </a>

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  


2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
    
3. In the left pane, select **Classic features**. 
 
4. Under **Search**, select **Open**. 
 
5. Select **Manage Search Dictionaries** to open the term store.
  
6. On the **Site Settings: Term Store Management Tool** page, click the arrow to expand the **Search Dictionaries** menu.
    
7. Click **Query Spelling Exclusions**, click the arrow and then click **Create Term**.
    
8. Type the query spelling that you want to exclude in the box that appears.
    
9. Click anywhere on the page to add the term to the **Query Spelling Exclusions** list. 
    
## Edit query spelling corrections or company names
<a name="__toc342653327"> </a>

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    

2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
    
3. In the left pane, select **Classic features**. 
 
4. Under **Search**, select **Open**.
 
5. Select **Manage Search Dictionaries** to open the term store.
   
6. On the **Site Settings: Term Store Management Tool** page, click the arrow to expand the **Search Dictionaries** menu.
    
7. Depending on which dictionary the term is in, click **Company Exclusions**, **Company Inclusions**, **Query Spelling Exclusions** or **Query Spelling Inclusions**.
    
8. Double-click the term that you want to edit.
    
9. Type the new name for the term.
    
8. Click anywhere on the page to save the edited term.
    

