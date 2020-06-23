---
title: "Create or customize a content type"
ms.reviewer: anfra
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.collection:  
- M365-collaboration
description: "Learn how to create or customize a content type in the SharePoint admin center."
---

# Create or customize a content type

Site content types help make it easy to provide consistency across a site. As a site owner, you create or customize a content type with the characteristics that you want, such as a certain template, specific metadata, and so on. For example, when a user chooses an item from the **New Item** or **New Document** menu, you can ensure that customized content is used.

![New Document Menu](media/new-document-menu.png)

To learn more about content types, see [Introduction to content types and content type publishing](https://support.microsoft.com/office/introduction-to-content-types-and-content-type-publishing-e1277a2e-a1e8-4473-9126-91a0647766e5).

> [!IMPORTANT]
> To create site content types for a site, you must have Full Control for that site. To create site content types for the top-level site in a site collection, you must be a site collection admin.

To create a site content type that people can use everywhere on a site, follow these steps:

**Create a content type**

1. Go to the SharePoint admin center.

2. Under **Content services**, select **Content type gallery**. The **Content type gallery** page appears showing all the existing site content types, their respective parent and category. The one that you select becomes the parent group of your new content type.

3. Select **Create content type**. The **Create content type** panel appears.

4. On the **Create content type** panel, provide a name and description for the new content type.

    ![Create content type](media/create-content-type.png)

5. In the **Parent content type** section, from the **Category** amd **Content type** dropdowns, select the content type that you want to base this content type on.

6. In the **Category** section, you are provided two choices:

    - To put the new content type in an existing category, select **Use an existing category**, and from the **Category** dropdown, select a category.
    
    - To put the content in a new category, select **Create a new category**, and in the **Category name** box, provide a name. 

7. Select **Create**.

The new content type appears in the **Content type gallery**.

## Change the name of a site content type

1. Go to the SharePoint admin center.

2. Under **Content services**, select **Content type gallery**.

3. On the **Content type gallery** page, under the **Site content type** column, select the name of the site content type that you want to change. That site content type page appears.

4. On this page, on the menu bar, select **Edit**. The **Edit content type** panel appears.

5. In the **Name** text box, change the name of the content type.

6. When done, select **Save**.

## Associate a document template with a site content type

To make sure that documents have consistent content across a site and its subsites, you can associate a Word, Excel, or PowerPoint template with a site content type.

For example, you might want employees to use a standard Excel template when they create a weekly timesheet. If you associate the template with a Timesheet content type, every time someone uses the Timesheet content type, the correct template is automatically loaded in the worksheet.

You can make it even easier for users by adding the Timesheet content type to a library. Then, users can open the correct timesheet just by selecting **Timesheet** on the **New Documents** menu. To learn how to do this, see [Add a content type to a list or library](https://support.microsoft.com/office/add-a-content-type-to-a-list-or-library-917366ae-f7a2-47ad-87a5-9689a1884e60).

To associate a template with a site content type, follow these steps.

1. Go to the SharePoint admin center.

2. Under **Content services**, select **Content type gallery**.

3. On the **Content type gallery** page, under the **Site content type** column, select the name of the site content type that you want to change by associating a Word, Excel, or PowerPoint template. That site content type page appears.

4. In the menu bar, under **Settings**, select **Advanced Settings**. The **Advanced Settings** panel appears.

5. Enter the location of the template:

    - If the template is stored on your site, select **Use an existing template**, and then enter the URL for the template that you want to use. To edit the template, select **Edit template**.

    - If the document template is stored on your local computer, select **Upload a new document template**, and then select **Upload**. From the explorer page, locate the file that you want to use, select it, and then select **Open**.

6. Under **Permissions**, to select whether the content type can be modified, select either **Read** or **Edit**. You can change this setting later from this page by anyone with permissions to edit this content type.

7. Under **Update site and lists**, if you want to update all site and list content types that inherit from this content type with the settings on this page, select **Enable**.

8. Select **Save**.

## Add columns to a site content type

The columns for a content type represent metadata. To add a metadata element, add a new column.

For example, your organization might want to track specific metadata for purchase orders, such as account number, project number, and project manager. If you add columns for this information to the purchase order content type, SharePoint prompts users to provide the information when they save their work. In addition, if you add the content type to a list or library, you can define a view to display the columns.

> [!NOTE]
> To add a column to a content type, you must first select the content type. If you are not able to select the content types that appear, the site inherits its content types from a parent site. To add a column to the content type, you must change it on the parent site.

1. Go to the SharePoint admin center.

2. Under **Content services**, select **Content type gallery**.

3. On the **Content type gallery** page, under the **Site content type** column, select the name of the site content type to which you want to add a column.

4. Under **Site columns**, from the **Add site column** dropdown, select **Add from existing site columns**. The **Add from existing site columns** panel appears.

5. In the **Select site columns from existing category** section, select a category, and then select **Add** or **Remove** to add or remove columns from the choices that appear.

6. In the **Update List and Site Content Types** section, decide whether you want to update all site and content types that inherit from this site content type with the settings on this page.

7. Select **Save**.

## Set up the Document Information Panel for a site content type

The Document Information Panel is available for Word, Excel, and PowerPoint in Microsoft Office 2010 and later. The Document Information Panel displays an InfoPath form on these documents where you can enter metadata information in the panel.

For example, suppose that you want to make sure that salespeople provide the company name and phone number for every sales proposal. You can create a Proposal content type, and include company name and phone number in the Document Information Panel. When they open a Proposal document, users enter or update the required name and phone number. When they save the document, SharePoint automatically updates the metadata stored as columns in the document library.

To learn more about content types and metadata, see [Add metadata columns to a content type](https://support.microsoft.com/office/add-columns-to-a-content-type-1806e29e-8bcd-4058-b0e7-3aac40a3ae9a).

To set up a Document Information Panel for a document content type, follow these steps.

1. Go to the SharePoint admin center.

2. Under **Content services**, select **Content type gallery**.

3. On the **Content type gallery** page, under the **Site content type** column, select the name of the site content type that you want to change. That site content type page appears.

> [!NOTE]
> If names of the content types that appear are not hyperlinks, then this site inherits its site content types from another (parent) site. To update the site content type, go to the parent site.

4. Under **Settings**, select **Advanced settings**.

5. In the **Document template** section, do one of the following:

    - To use a default template that displays the metadata (columns) that you defined for the content type, select **Use an existing template**.

    - To use an existing custom template, select **Use existing custom template**, and then enter the path of the location of the template.

    - To upload an existing custom template (XSN), select **Upload a new document template**, and to locate the template that you want to use, select **Upload**. From the explorer page, locate the file that you want to use, select it, and then select **Open**.

6. Select **Save**.