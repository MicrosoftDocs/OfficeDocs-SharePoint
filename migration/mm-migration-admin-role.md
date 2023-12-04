---
title: "Microsoft 365 Migration Admin role"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- SPMigration
- m365initiative-migratetom365
search.appverid: MET150
description: Learn about the admin role for Migration Manager
---

# Migration Admin role

>[!Note]
>This feature is currently in public preview, with full availability by mid-January 2024.

A new Microsoft 365 Migration Administrator role is now available to provide access to Migration Manager within the Microsoft 365 Admin Center. Currently, you must assign their migration team the SharePoint admin role, giving more access than needed. With this new role, you limit usage to only what is required to migrate your content, reserving SharePoint Admin access to only users who need it.

>[!Important]
>This role doesn't allow access to Migration Manager from the SharePoint admin center. Continue to use the SharePoint Administrator role to migrate from network file shares.

In addition, this role provides all the functionality required to migrate including the ability to:

- Access Migration Manager to migrate from Google Drive, Dropbox, Box and Egnyte
- Select migration sources, create migration inventories (such as Google Drive user lists), schedule and execute migrations, and download reports
- Create new SharePoint sites if the destination sites don't already exist
- Create SharePoint lists under the SharePoint admin sites
- Create and update items in SharePoint lists
- Manage migration project settings and migration lifecycle for tasks
- Manage permission mappings from source to destination

###  How to use

To use this feature, you must create a new user in the Microsoft 365 admin center, then assign them the Migration Administrator role. This role allows access to only to Migration Manager.

>[!Important]
>You can continue to use Migration Manager as you currently do today.  Your projects will continue to work normally.

## FAQs

**Question:**  I'm migrating network file shares. Can I use the Migration Admin role instead of the Sharepoint Admin?
Answer:  No.  Currently, this role isn't supported for File Share migrations. Continue to use the SharePoint Admin role to access Migration Manager for file share migrations. 

**Question:** Can I add this role to existing user account?
Answer:  No. You must create a new user account from the Microsoft 365 admin center and then assign this role.

**Question:**  I created a new user account in the Microsoft Admin Center, and assigned the Migration Admin role. Can I access existing projects?
Answer:  Yes, provided you access Migration Manager from the Microsoft Admin Center, not the Sharepoint Admin Center.

**Question:**  Does this role apply to all migration scenarios supported by Migration Manager?
Answer:  The Migration Admin role can be used only for our supported cloud migrations:  Google Drive, Box, Dropbox, and Egnyte.

**Question:**  I currently have my migration team assigned with the SharePoint Admin role.  Can I just continue using that?
Answer:  Yes, using the Migration Admin role isn't required. However, it helps managing access easier.
