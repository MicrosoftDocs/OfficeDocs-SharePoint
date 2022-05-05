---
title: "SharePoint Migration Identity Mapping Tool SharePoint Identity Scan"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
ms.date: 01/5/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: medium
ms.collection:
- SPmigration
- M365-collaboration
---

# SharePoint Migration Identity Mapping Tool: SharePoint Identity Scan

## Overview

The SharePoint Identity scanner is responsible for finding users and groups that are listed as active in the SharePoint farm being scanned. The result of this scan is a set of distinct identities that have permissions in the source SharePoint environment. A distinct set of identities is captured. For example, if contoso\bobsmith is listed in permissions for multiple site collections, there will be one entry for contoso\bobsmith in the resulting output.
  
The tool will read each SharePoint Content Database and if the User Profile Service is available, it will gather the email and My Site information related to the identity.
  
This scan is required for identity mapping as the data located in SharePoint is used for the resultant identity scans. 
  

