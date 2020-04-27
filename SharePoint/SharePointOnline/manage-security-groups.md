---
title: "Manage security groups"
ms.reviewer: srice
ms.author: v-jwight
author: jackwi-alt
manager: pamgreen
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_OD_share
- M365-collaboration
ms.custom:
search.appverid:
- SPO160
- MET150
description: "Learn how to manage security groups for sharing files and folders in SharePoint and OneDrive."
---

# Manage security groups

As a SharePoint or global admin in Microsoft 365, you can identify specific security groups within an organization in SharePoint or OneDrive to share links to files and folders externally.
  
1. In the SharePoint admin center, check the **Allow only users in specific groups to share externally** box.

2. Select **Manage security groups**.

3. In the **Add a security group** box, enter a name for a security group. The security group box appears.

4. Next to the security group name, from the **Can share with** dropdown, select either:

- **Authenticated guests only** (default)
- **Anyone**

5. Select **Save**.

By selecting **Anyone**, users in that security group can share links to files and folders externally that don’t require users to authenticate (for example, the **Anyone link** in the **Share** dialog box). Forwarded **Anyone links** will work internally or externally, but you won't be able to track who has access to shared items or who has accessed shared items. Users in this group can also share to authenticated guest users. This option is best for a security group prefering friction-free sharing, provided files and folders in SharePoint and OneDrive aren’t classified as sensitive.

By selecting **Authenticated guests only**, sharing externally is strictly limited to those guests who authenticate. This is the best option for external sharing of sensitive or proprietary information because it requires that the guest verify their identity before they can access the file or folder. Authenticated guests can share with another authenticated guest, but cannot forward these links.

![Manage security groups by sharing panel]](media/manage-security-groups-sharing.png)

