---
ms.date: 08/04/2023
title: Allow only members in specific security groups to share SharePoint and OneDrive files and folders externally
ms.reviewer: srice
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
f1.keywords: CSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_OD_share
- M365-collaboration
ms.custom: admindeeplinkSPO
search.appverid:
- SPO160
- MET150
description: "Learn how to manage security groups for sharing files and folders in SharePoint and OneDrive."
---

# Allow only members in specific security groups to share SharePoint and OneDrive files and folders externally

As a [SharePoint Administrator](/sharepoint/sharepoint-admin-role) and [above](/microsoft-365/admin/add-users/about-admin-roles) in Microsoft 365, you can restrict external sharing of SharePoint and OneDrive content so that only users in specific security groups can share externally. Note that the people in these security groups must be allowed to invite guests in the [Microsoft Entra guest invite settings](/azure/active-directory/external-identities/external-collaboration-settings-configure).
  
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185222" target="_blank">**Sharing** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

2. Under **External sharing**, expand **More external sharing settings**.

3. Select **Allow only users in specific security groups to share externally**, and then select **Manage security groups**.

    :::image type="content" alt-text="Manage security groups" source="media/manage-security-groups.png":::

4. In the **Add a security group** box, search for and select the security groups you want to use (up to 12).

5. Next to the security group name, from the **Can share with** dropdown, select either:

    - **Authenticated guests only** (default)
    - **Anyone**

6. Select **Save**.

By selecting **Anyone**, users in that security group can share links to files and folders externally that don't require users to authenticate using the **Anyone link** in the **Share** dialog box. Forwarded **Anyone links** will work internally or externally, but you can't track who has access to shared items or who has accessed shared items. Users in this group can also share to authenticated guests. This option is best for friction-free sharing, provided files and folders in SharePoint and OneDrive aren't considered sensitive.

By selecting **Authenticated guests only**, sharing externally is limited to those guests who authenticate. This option is best for sharing sensitive or proprietary information because it requires guests to verify their identity before they can access the file or folder.
