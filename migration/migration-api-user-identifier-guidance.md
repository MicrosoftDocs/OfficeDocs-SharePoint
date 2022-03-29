---
title: "ISV Guidance for user identifier in UserGroup.xml"
ms.reviewer: jhendr
author: JoanneHendrickson
ms.author: jhendr
manager: serdars
audience: ITPro
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
localization_priority: Priority
ms.collection: 
- m365solution-migratefileshares
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
search.appverid: MET150
ROBOTS: NOINDEX
description: "How to correctly generate the UserGroup.xml in the submitted migration package." 
---

# Guidelines for user identifier in UserGroup.XML

When generating the UserGroup.XML in the submitted package, the user identifier requires

- A maximum of one identifier per user in a single package.
- The 'login' attribute of the user identifier requires a UPN. **Do not** enter a non-UPN email address.
 

 
#### Examples

The following show the correct and incorrect ways of entering the user identifier in UserGroup.XML: 

In this case, our user has the following:

- **UPN**: robert@contoso.com
- **Email**: robert.downey@contoso.com. 



**Correct**

<User Id="1" Login="i:0#.f|membership|robert@contoso.com" …/>

 
**Incorrect**

Example 1: This example does not follow either guidelines.


<User Id="1" Login="i:0#.f|membership|robert@contoso.com" …/>
<User Id="2" Login="i:0#.f|membership|robert.downey@contoso.com" …/>

 
Example 2: This example incorrectly uses a non-UPN email address.

<User Id="2" Login="i:0#.f|membership|robert.downey@contoso.com" …/>

 
>[!Important]
> As of March 2, 2022, the Migration API will validate and enforce a maximum of one identifier per user in a single package. 
>
>The 'login' attribute of the user identifier requires a UPN.  While using a non-UPN email won't result in a failed job, it may bring unexpected results in SharePoint Online.


