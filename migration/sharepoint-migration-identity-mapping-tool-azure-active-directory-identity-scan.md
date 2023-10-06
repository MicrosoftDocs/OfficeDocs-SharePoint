---
title: "SharePoint Migration Identity Mapping Tool: Microsoft Entra Identity Scan"
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
ms.date: 01/5/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
description: Learn about SharePoint Migration Identity Mapping Tool for Microsoft Entra Identity Scan.
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: medium
ms.collection:
- SPmigration
- M365-collaboration
- m365initiative-migratetom365
---

# SharePoint Migration Identity Mapping Tool: Microsoft Entra Identity Scan

## Overview

The Microsoft Entra Identity Scan looks up identities that were found in the source SharePoint environment in the Microsoft Entra ID that you authenticate to.
  
When the tool is performing look-ups, the pattern used for matching is listed in the table.
  
| Users |&nbsp;  |
|:-----|:-----|
|ExactMatch  <br/> |Source Identity is a Windows user with a Security Identifier [SID]. The target is the OnPremisesSecurityIdentifier in Microsoft Entra ID.  <br/> Non-Windows accounts will never be able to have an ExactMatch.  <br/> |
|PartialMatch  <br/> |Source identity claim value equals the UserPrincipalName or Mail value in Microsoft Entra ID.  <br/> or  <br/> Source Identity Display Name equals the Display Name in Microsoft Entra ID.  <br/> |
|NoMatch  <br/> |Unable to perform neither ExactMatch or PartialMatch.  <br/> |
   
| Groups |&nbsp;  |
|:-----|:-----|
|ExactMatch  <br/> |Source Identity is a Windows group with a Security Identifier [SID]. The target is the OnPremisesSecurityIdentifier in Microsoft Entra ID.  <br/> Non-Windows accounts will never have an ExactMatch.  <br/> |
|PartialMatch  <br/> |Source Identity Display Name equals the Display Name in Microsoft Entra ID.  <br/> |
|NoMatch  <br/> |Unable to perform neither ExactMatch or PartialMatch.  <br/> |
   
We use Microsoft Authentication Library to authenticate the operator to Microsoft Entra ID. This requires consent for the application to read the Microsoft Entra ID. In order to ensure there's consent prior to running the scans, the tool performs a preflight validation check that involves authenticating to Azure. This enables the operator to avoid running a long scan process if all the prerequisites haven't been met. See [SharePoint Migration Identity Mapping Tool - Preflight validation checks](./sharepoint-migration-identity-mapping-tool.md#preflight-validation-checks) for more information.
