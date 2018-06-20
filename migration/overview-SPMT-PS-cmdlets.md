---
title: "Using Powershell to Migrate to SharePoint Online"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 6/20/2018
ms.audience: ITPro
ms.topic: conceptual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 
description: "Using Powershell to Migrate to SharePoint Online"
---
## Using Powershell to Migrate to SharePoint Online 


New PowerShell cmdlets based on the SharePoint Migration Tool (SPMT) migration engine. They will move files from file shares, SharePoint on-prem 2013 document libraries, or list items from SharePoint on-prem 2013 to Office 365.

The newly defined PowerShell cmdlets provide the same functionalities as SPMT V2 (INSERT LINK) and have  the same recommended and minimum requirements(see appendix). 

There are 8 new cmdlets. They are: 
- Register-SPMTMigration 
- Add-SPMTTask 
- Remove-SPMTTask
- Start-SPMTMigration  
- Get-SPMTMigration 
- Show-SPMTMigration 
- Stop-SPMTMigration  
- Unregister-SPMTMigration 


### Cmdlets Details:
**Register-SPMTMigration**<br>
This cmdlet will create a SPMT migration session and initialization. The initialization includes configuring migration settings at session level and connecting to SPO. If no specific setting parameters are defined, default settings will be used. 
After a session is registered, the Administrator can add a migration task to the SPMT session and start migration.




 
