---
title: "Migration Assessment Scan Customized Profile Pages"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 5/17/2017
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
ms.custom:
ms.assetid: b4f41860-3db9-4e30-8b5d-9748aa7d95a8
description: "Learn how to mitigate issues with Customized Profile pages during migration."
---

# Migration Assessment Scan: Customized Profile Pages

Learn how to mitigate issues with Customized Profile pages during migration.
  
## Overview

In the source environment, viewing a user's profile is managed by a page hosted in the My Site Host named Person.aspx. For example, clicking on a colleague's name in a document library or from their OneDrive for Business will take you to the person.aspx page to view the user's profile.
  
Post migration to the target environment, the profile experience is managed by the Delve service. There is currently a limitation in that the Delve profile page cannot be modified. This scan report will show you any customizations that have been made to the Person.aspx page in the source environment. This data can be used to understand any impact with the move to the target environment with regards to the profile experience.
  
To learn more, see: [How can I find people and information in Office Delve?](https://support.office.com/article/How-can-I-find-people-and-information-in-Office-Delve-5b8bffdd-a50a-430a-8570-09b39481887c)
  
## Preparing for Migration

Understand any customizations made to the Person.aspx page in the source environment, and investigate whether there is any impact with the move to the new Delve profile experience. The new experience solves most of the scenarios that resulted in customization on the previous platform.
  
## Post Migration

Validate the profile experience on the new platform.
  
## Scan Result Reports

 **CustomizedProfilePages_\<Date\>_\<Time\>.csv** This scan report shows whether the Person.aspx profile page has been modified in SharePoint Designer, or if any of the web parts have been added, deleted, or moved on the page. 
  
|**Column**|**Description**|
|:-----|:-----|
|DisplayTitle  <br/> |Display title of the web part. If the page was modified, there will be a row with DisplayTitle of "Profile Page".  <br/> |
|WebPart  <br/> |Type of web part.  <br/> |
|Scope  <br/> |One of the following: • Page - The page was modified in SharePoint Designer • SharedWebPart - A Shared Web Part was added, deleted, or moved • UserWebPart - A User Web Part was added, deleted, or moved  <br/> |
|Difference  <br/> | The piece of information that was flagged as a change. This could be a combination of the following:  <br/>  Added Web Part  <br/>  Web Part Zone  <br/>  Web Part Order  <br/>  Web Part Missing  <br/>  Page modified in SharePoint Designer  <br/> |
   

