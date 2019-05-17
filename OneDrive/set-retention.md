---
title: "Set the OneDrive retention for deleted users"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
f1_keywords:
- 'O365E_ODACStorage'
ms.service: one-drive
localization_priority: Normal
ms.collection: 
- Strat_OD_admin
- M365-collaboration
search.appverid:
- ODB160
- ODB150
- MET150
ms.assetid: fa1641ea-9f03-4f34-a826-dbd8697e76fe
description: "Learn how to specify how long the files of deleted users are preserved using the OneDrive admin center. "
---

# Set the OneDrive retention for deleted users

If a user's Office 365 account is deleted, their OneDrive for Business files are preserved for a period of time that you can specify.
  
 **To set the retention time for OneDrive accounts**
  
1. Open the [OneDrive admin center](https://admin.onedrive.com/?v=StorageSettings), and select **Storage** in the left pane. 
    
    ![The Storage page of the OneDrive admin center](media/15942b88-2f71-4c85-87ec-eb14b88f8f93.png)
  
2. Enter the number of days you want to retain OneDrive files in the **Days to retain files in OneDrive after a user account is marked for deletion** box. 
    
    The setting takes effect for the next user that is deleted. The count begins as soon as the user account is deleted in the Microsoft 365 admin center, even though the deletion process takes time. The minimum value is 30 days and the maximum value is 3650 days (ten years).
    
3. Click **Save**.
    
## See also

[Delete a user from your organization](/office365/admin/add-users/delete-a-user)
  
[Set up OneDrive to alert managers and delegate access automatically when users leave your organization](http://go.microsoft.com/fwlink/p/?LinkId=798417&amp;clcid=0x409)
  
[Overview of retention policies](/office365/securitycompliance/retention-policies)


