---
title: "Add columns to a content type"
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
description: "Learn how to add columns to a content type in the SharePoint admin center."
---

# Add columns to a content type

Content types are a way of grouping information about list items or documents that you want to capture using columns. For example, if you have a purchase order content type, it could include account number, project number, date, and project manager. You can customize content types by adding columns of the types you need. You can add the appropriate content type to your list or library and get a group of columns, rather than creating or adding each column individually. You can have multiple content types in the same list or library, and create views to see different types of items and documents.

When you can create content types on a site level or a list or library level the advantage is that they are shared for all sites and subsites under the top site. This can help standardize columns, and minimize errors. The disadvantage is that they require administrator permissions to create, and have to be planned more carefully. List or library level content types are quick to create, but are unique to the library they're in.

## Add a column to a content type

To add a column to a content type, follow these steps:

> [!WARNING]
> If the content types that appear are not hyperlinks or cannot be selected, it means that the site inherits its content types from a different site. To add a column to the content type, you must change it on the other site.

### Add a column to a site content type

1. Go to the SharePoint admin center.

2. Under **Content services**, select **Content type gallery**.

3. On the **Content type gallery** page, under the **Site content type** column, select the name of the site content type to which you want to add a column.

4. Under **Site columns**, from the **Add site column** dropdown, select **Add from existing site columns**. The **Add from existing site columns** panel appears.

5. In the **Select site columns from existing category** section, select a category, and then select **Add** or **Remove** to add or remove columns from the choices that appear.

6. In the **Update List and Site Content Types** section, decide whether you want to update all site and content types that inherit from this site content type with the settings on this page.

7. Select **Save**.

## Change column order

To change column order for a content type, follow these steps.

### Change column order on a content type

1. Go to the SharePoint admin center.

2. Under **Content services**, select **Content type gallery**.

3. On the **Content type gallery** page, under the **Site content type** column, select the name of the site content type to which you want to change a column's order. That site content type page appears.

4. Under **Site columns**, in the **Name** column, select the column that you want to change its order.

5. Select the vertical ellipsis to the right of the site column name you selected, and from the dropdown, select **Reorder site columns** and then select from the following four choices:

    - **Move to top**

    - **Move up**

    - **Move down**

    - **Move to bottom**

## Make a column required, optional, or hidden

To make a column required, optional or hidden, follow these steps.

### For a site content type

1. Go to the SharePoint admin center.

2. Under **Content services**, select **Content type gallery**.

3. On the **Content type gallery** page, under the **Site content type** column, select the name of the site content type that you want to change a site content type by adding a column. That site content type page appears.

4. Under **Site columns**, in the **Name** column, select the name of the column that you want to make optional, required, or hidden.

5. Select **Edit site column settings**. The **Edit site column settings** panel appears.

6. In the **Show or hide site column** section, do one of the following:

    - To show or hide this column in list, check or uncheck **Show this column in lists**, respectively.

    - To make it optional for users to specify information for a column, select **Optional (may contain information)**.

    - To require users to specify information for a column, select **Required (must contain information)**.
    
7. Under **Update sites and lists**, if you want to update all site and list content types that inherit from this content type with the settings on this page, check the box.

8. Select **Save**.

## Related topics

[Add columns to a content type](https://support.microsoft.com/office/1806e29e-8bcd-4058-b0e7-3aac40a3ae9a)

[Add a content type to a list or library](https://support.microsoft.com/office/917366ae-f7a2-47ad-87a5-9689a1884e60)

[Create, change, or delete a view of a list or library](https://support.microsoft.com/office/27ae65b8-bc5b-4949-b29b-4ee87144a9c9)