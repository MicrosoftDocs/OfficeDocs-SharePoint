---
title: "SharePoint Migration Identity Mapping Tool Azure Active Directory Identity Scan"
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
ms.date: 01/5/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
description: Learn about SharePoint Migration Identity Mapping Tool for Azure AD Identity Scan.
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: medium
ms.collection:
- SPmigration
- M365-collaboration
- m365initiative-migratetom365
---

# SharePoint Migration Identity Mapping Tool: Azure Active Directory Identity Scan

## Overview

The Azure Active Directory scan looks up identities that were found in the source SharePoint environment in the Azure Active Directory that you authenticate to.
  
When the tool is performing look-ups, the pattern used for matching is listed in the table.
  
| Users |&nbsp;  |
|:-----|:-----|
|ExactMatch  <br/> |Source Identity is a Windows user with a Security Identifier [SID]. The target is the OnPremisesSecurityIdentifier in Azure Active Directory.  <br/> Non-Windows accounts will never be able to have an ExactMatch.  <br/> |
|PartialMatch  <br/> |Source identity claim value equals the UserPrincipalName or Mail value in Azure Active Directory.  <br/> or  <br/> Source Identity Display Name equals the Display Name in Azure Active Directory.  <br/> |
|NoMatch  <br/> |Unable to perform neither ExactMatch or PartialMatch.  <br/> |
   
| Groups |&nbsp;  |
|:-----|:-----|
|ExactMatch  <br/> |Source Identity is a Windows group with a Security Identifier [SID]. The target is the OnPremisesSecurityIdentifier in Azure Active Directory.  <br/> Non-Windows accounts will never have an ExactMatch.  <br/> |
|PartialMatch  <br/> |Source Identity Display Name equals the Display Name in Azure Active Directory.  <br/> |
|NoMatch  <br/> |Unable to perform neither ExactMatch or PartialMatch.  <br/> |
   
We use Microsoft Authentication Library to authenticate the operator to Azure Active Directory. This requires consent for the application to read the Azure Active Directory. In order to ensure there's consent prior to running the scans, the tool performs a preflight validation check that involves authenticating to Azure. This enables the operator to avoid running a long scan process if all the prerequisites haven't been met. See [SharePoint Migration Identity Mapping Tool - Preflight validation checks](./sharepoint-migration-identity-mapping-tool.md#pre-flight-validation-checks) for more information.
