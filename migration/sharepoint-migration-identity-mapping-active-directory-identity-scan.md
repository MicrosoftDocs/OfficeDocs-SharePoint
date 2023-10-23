---
title: "SharePoint Migration Identity Mapping: Microsoft Entra Identity Scan"
description: "Learn about the SharePoint Migration Identity Mapping: Microsoft Entra Identity Scan."
ms.author: mactra
author: MachelleTranMSFT
manager: serdars
recommendations: true
ms.date: 01/5/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: medium
ms.collection:
- SPmigration
- M365-collaboration
- m365initiative-migratetom365
---

# SharePoint Migration Identity Mapping: Active Directory Identity Scan

## Overview

The Active Directory scan looks up any Windows identities that were found in the source SharePoint environment in the customer's Active Directory.
  
If there are no Windows identities, this scan won't perform any work.
  
There are two distinct steps to this assessment scan:
  
-  Discover the Active Directory Forests that are available. 
    
- Look up the identities in Active Directory.
    
## Discover the Active Directory Forests

We find the forest the SharePoint server is connected to. We then enumerate trusts to locate all the trusted Forests. Once we've found the trusted forests, we enumerate all the domains in the forests.
  
This process may prompt for credentials if the currently logged on user doesn't have the ability to read the requested forest. We'll retry connections three times, so if you enter invalid credentials there will be multiple attempts. The tool caches the credentials entered for the current execution.
  
## Look up identities in Active Directory

After we have discovered the forests, we'll use the cached credentials to look up users/groups in Active Directory using the Security Identifier [SID]. This information isn't 100% needed for identity mapping. However, if you have identities flagged as NoMatch or PartialMatch, this information is useful to track down additional information for the identity. For example, you have a user that is showing as Active in SharePoint, but is showing as Disabled in Active Directory. Seeing this user with NoMatch is expected as the user isn't likely to be sync'ed to Microsoft Entra ID.
  
## Scenarios

Two-way trust between the forest SharePoint is joined to and the user forests. Users logs into the SharePoint machine using a domain account. In this scenario, the operator is unlikely to be prompted as their domain credentials should be able to read the associated domains.
  
One-way trust between the forest SharePoint is joined to and the user forests. All the user forests trust each other. In this scenario, the user logs into SharePoint as an account in the SharePoint forest. When querying for Forests, we'll prompt for credentials to read the first user Forest. We'll cache those credentials and use them for the remaining forests. In this scenario, the operator sees one sign in prompt.
  
One-way trust between the forest SharePoint is joined to and the user forests. The user forests don't trust each other. In this scenario, the user logs into SharePoint as an account in the SharePoint forest. When querying for Forests, we'll prompt for each forest. If there are 20 user forests that don't trust each other you would expect to see 20 sign in prompts.
  
