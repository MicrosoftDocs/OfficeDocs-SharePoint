---
title: "Add columns to a content type"
ms.reviewer: shrganguly
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
search.appverid:
- SPO160
- MET150
ms.collection:  
- M365-collaboration
ms.custom: admindeeplinkSPO
description: "Learn how to add columns to a content type in the SharePoint admin center."
---

# Add columns to a content type

The columns for a content type represent metadata. To add a metadata element, add a new column.

For example, your organization might want to track specific metadata for purchase orders, such as account number, project number, and project manager. If you add columns for this information to the purchase order content type, SharePoint prompts users to provide the information when they save their work. In addition, if you add the content type to a list or library, you can define a view to display the columns.

You can customize content types by adding columns of the types you need. You can also change the order of columns and specify if they are required fields.

## Add a column to a content type

To add a column to a content type, follow these steps:

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185074" target="_blank">Content type gallery in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization. The Content type gallery page isn't available if you have the global reader role. 

2. Under the **Site content type** column, select the name of the site content type to which you want to add a column.

3. Under **Site columns**, from the **Add site column** dropdown, select **Add from existing site columns**. The **Add from existing site columns** panel appears.

4. In the **Select site columns from existing category** section, select **Add** or **Remove** to add or remove columns from the choices that appear. You can choose a category to narrow the list of available columns.

5. In the **Update List and Site Content Types** section, decide whether you want to update all site and content types that inherit from this content type with the settings on this page.

6. Select **Save**.

## Change column order

To change column order for a content type, follow these steps.

**To change column order on a content type**

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185074" target="_blank">Content type gallery in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization. The Content type gallery page isn't available if you have the global reader role. 

2. Under the **Site content type** column, select the name of the site content type to which you want to change a column's order. That site content type page appears.

3. Under **Site columns**, in the **Name** column, select the column that you want to change its order.

4. Select the vertical ellipsis to the right of the site column name you selected, and from the dropdown, select **Reorder site columns** and then select from the following four choices:

    - **Move to top**

    - **Move up**

    - **Move down**

    - **Move to bottom**

## Make a column required, optional, or hidden

To make a column required, optional, or hidden, follow these steps.

**To make a column required, optional, or hidden**

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185074" target="_blank">Content type gallery in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization. The Content type gallery page isn't available if you have the global reader role. 

2. Under the **Site content type** column, select the name of the site content type that you want to change a site content type by adding a column. That site content type page appears.

3. Under **Site columns**, in the **Name** column, select the name of the column that you want to make optional, required, or hidden.

4. Select **Edit site column settings**. The **Edit site column settings** panel appears.

5. In the **Show or hide site column** section, do one of the following:

    - To show or hide this column in lists, check or clear **Show this column in lists**, respectively.

    - To make it optional for users to specify information for a column, select **Optional (may contain information)**.

    - To require users to specify information for a column, select **Required (must contain information)**.
    
6. Under **Update sites and lists**, if you want to update all site and list content types that inherit from this content type with the settings on this page, check the box.

7. Select **Save**.

> [!NOTE]
>  When you update the column name of an existing site column that is part of a published content type from the content type hub, ensure that the language of the target site and the language of the browser are the same for the latest site column name to appear correctly after the sync completes.

## Related topics

[Remove columns from a content type](remove-columns-content-type.md)

[Add columns to a content type](https://support.microsoft.com/office/1806e29e-8bcd-4058-b0e7-3aac40a3ae9a)

[Add a content type to a list or library](https://support.microsoft.com/office/917366ae-f7a2-47ad-87a5-9689a1884e60)

[Create, change, or delete a view of a list or library](https://support.microsoft.com/office/27ae65b8-bc5b-4949-b29b-4ee87144a9c9)
