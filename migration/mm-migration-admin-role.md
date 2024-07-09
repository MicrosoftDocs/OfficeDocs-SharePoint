---
title: "Microsoft 365 Migration Admin role"
ms.reviewer: 
ms.author: jtremper
author: JoanneHendrickson
manager: jtremper
ms.date: 01/25/2024
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
>This feature is currently in public preview, with full availability by June 2024.

A Microsoft 365 Migration Administrator role is now available to provide access to Migration Manager within the Microsoft 365 Admin Center. Currently, your migration team must be assigned the SharePoint admin role, giving more access than needed. With this new role, you limit usage to only what is required to migrate your content, reserving SharePoint Admin access to only users who need it.

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

To use this feature, assign the migration admin role to a new or existing user. This role only allows access to Migration Manager.

>[!Note]
>Tabs may appear on the left navigation pane, including one for Groups, Users, Roles, and Settings. Users assigned the Migration Admin role can select and navigate these tabs, however, they are read-only.

>[!Important]
>You can continue to use Migration Manager as you currently do today.  Your projects will continue to work normally.

## FAQs

**Question:**  I'm migrating network file shares. Can I use the Migration Admin role instead of the Sharepoint Admin?</br>
Answer:  No. The Migration Admin role can be used only for our supported cloud migrations: Google Drive, Box, Dropbox, and Egnyte. This role is currently not supported for file share migrations. Continue to use accounts assigned the SharePoint Admin role.

**Question:** Can I assign this role to an existing user account?</br>
Answer:  Yes.

**Question:**  I created a new user account in the Microsoft Admin Center, and assigned it the Migration Admin role. Does this new account have access existing projects?</br>
Answer:  Yes, provided you access Migration Manager from the Microsoft Admin Center to migrate from Google Drive, Box, Dropbox and Egnyte.
</br>

**Question:**  I currently have my migration team assigned with the SharePoint Admin role.  Can I just continue using that?</br>
Answer:  Yes, using the Migration Admin role isn't required. However, it makes managing access easier.

**Question:** I see a gmail migration entry listed that I wasn't expecting.  
Answer:  This is a known issue, and a fix is pending.
