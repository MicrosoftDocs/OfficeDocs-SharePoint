---
title: "Migration Assessment Scan Locked Sites"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
ms.date: 7/5/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
ms.custom:
ms.assetid: 57e13cc6-cec7-4b81-8fe9-7b2646fd5532
description: "Learn how to mitigate issues with locked sites during migration."
---

# Migration Assessment Scan: Locked Sites

Learn how to mitigate issues with locked sites during migration.
  
## Overview

When a site is configured as "No Access" in SharePoint, the site is inaccessible by both users and the system. As a result, the various pre-migration scans are configured to ignore any site that is configured as "No Access". It is **locked**. 
  
## Data Migration

Locked sites cannot be migrated to the target environment, as the migration tooling is unable to read the site contents.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Ensure the list of locked sites is correct. If you have sites that are incorrectly marked as "No Access", update the lock status to "Not Locked".
  
## Post Migration

To manage the lock status on sites on the target environment, leverage the SharePoint Online Management Shell.
  
 **How to unlock a site collection on vNext**
  
1. Use the Set-SPSite cmdlet from the PowerShell cmdlets to unlock sites.
    
2. Download the cmdlets from the [SharePoint Online Management Shell download.](https://www.microsoft.com/download/details.aspx?id=35588) https://www.microsoft.com/download/details.aspx?id=35588 
    
3. Launch SharePoint Online Management Shell
    
4. Run:  `Set-SPSite -LockStatus Unlock`
    
 **How to set a site to "No Access"**
  
1. Use Set-SPSite from the PowerShell cmdlets to lock sites. This is similar to "No Access" in that users can't get to the site.
    
2. Download the cmdlets from the [SharePoint Online Management Shell download.](https://www.microsoft.com/download/details.aspx?id=35588) https://www.microsoft.com/download/details.aspx?id=35588 
    
3. Launch SharePoint Online Management Shell
    
4. Run:  `Set-SPSite -LockStatus NoAccess`
    
 **How to set a site to "Read only"**
  
1. Set-SPSite does not support setting a site to "Read Only". An alternative method is to use Site Collection Policies on a site collection.
    
2. Browse the site you want to be "Read Only".
    
3. In the top right, select the gear icon, and then select **Site Settings**.
    
4. Select **Site Policies**.
    
5. Select **Create**.
    
  - a. Enter a **Name** and **Description**.
    
  - Select **Do not close or delete site automatically**.
    
  - Check **The site collection will be read only when it is closed**.
    
  - Select **OK**.
    
6. On **Site Settings**, select **Site Closure and Deletion**.
    
1. For **Site Policy**, select the "Read Only" policy from Step 4.
    
2. Select **OK**.
    
3. Go back to **Site Closure and Deletion**, and select **Close this site now**. The site is now "Read Only".
    
4. Only a site collection admin can access and select **Open this site**.
    
## Scan Result Reports

 **LockedSites-detail.csv** This scan report contains a list of URLs that are configured as "No Access" in SharePoint. 
  
|**Column**|**Description**|
|:-----|:-----|
|URL  <br/> |URL of the site collection that is configured as "No Access".  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

