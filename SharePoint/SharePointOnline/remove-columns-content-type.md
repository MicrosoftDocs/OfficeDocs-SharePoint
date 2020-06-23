---
title: "Remove columns from a content type"
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
description: "Learn how to remove columns from a content type in the SharePoint admin center."
---

# Remove columns from a content type

Content types are a way of grouping information about list items or documents that you want to capture using columns. Columns can be added and removed from content types as necessary. However, they require administrator permissions to create or delete.

To learn more about adding columns to content types at the site, library, or list level, see [Add columns to a content type](https://support.microsoft.com/office/add-columns-to-a-content-type-1806e29e-8bcd-4058-b0e7-3aac40a3ae9a). For more info about adding content types, see [Create or customize a site content type](https://support.microsoft.com/office/create-or-customize-a-site-content-type-27eb6551-9867-4201-a819-620c5658a60f) and [Add a content type to a list or library](https://support.microsoft.com/office/add-a-content-type-to-a-list-or-library-917366ae-f7a2-47ad-87a5-9689a1884e60).

To remove a column from a content type, follow these steps:

> [!WARNING]
> If the content types that appear are not hyperlinks or cannot be selected, it means that the site inherits its content types from a different site. To remove a column to the content type, you must change it on the other site.

## Remove a column from a site content type

1. Go to the SharePoint admin center.

2. Under **Content services**, select **Content type gallery**.

3. On the **Content type gallery** page, under the **Site content type** column, select the name of the site content type to which you want to remove a column.

4. Under **Site columns**, select the column name you want to remove.

5. Select the vertical ellipsis to the right of the site column name you selected, and from the dropdown, select **Delete**. A **Delete site column** dialog box appears prompting you that this action will remove the column from the content type. Existing items in lists will not be affected, but new items will not have this column.

6. Select **Delete**.

## Remove a column from a list or library content type

1. Go to the list or library where you want to change the column order.

2. Do one of the following:

    - If you're working in a list, select the **List** tab, and then select **List Settings**.
    
        ![List settings](media/list-settings.png)

    - If you're working in a library, select the **Library** tab, and then select **Library Settings**.
    
        ![Library settings](media/library-settings.png)

3. On the **Content type gallery** page, under the **Site content type** column, select the name of the site content type to which you want to remove a column.

4. Under **Site columns**, select the column name you want to remove.

5. Select the vertical ellipsis to the right of the site column name you selected, and from the dropdown, select **Delete**. A **Delete site column** dialog box appears prompting you that this action will remove the column from the content type. Existing items in lists will not be affected, but new items will not have this column.

6. Select **Delete**.

## Related topics

[Remove columns from a content type](https://support.microsoft.com/office/f44da9ca-d70e-477a-93bf-6f6b046a1f39)