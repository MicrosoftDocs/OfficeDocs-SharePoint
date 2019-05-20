---
title: "SharePoint Migration Identity Mapping Active Directory Identity Scan"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 01/5/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 772cd4ed-6ed6-42b5-abe1-01dddcd8b6df

---

# SharePoint Migration Identity Mapping: Active Directory Identity Scan

## Overview

The Active Directory scan will look up any Windows identities that were found in the source SharePoint environment in the customer's Active Directory.
  
If there are no Windows identities, this scan will not perform any work.
  
There are 2 distinct steps to this assessment scan:
  
-  Discover the Active Directory Forests that are available. 
    
- Lookup the identities in Active Directory.
    
## Discover the Active Directory Forests

We find the forest the SharePoint server is connected to. We then enumerate trusts to locate all the trusted Forests. Once we've found the trusted forests, we enumerate all the domains in the forests.
  
This process may prompt for credentials if the currently logged on user does not have the ability to read the requested forest. We will retry connections 3 times, so if you enter invalid credentials there will be multiple attempts. The tool will cache the credentials entered for the current execution.
  
## Lookup identities in Active Directory

After we have discovered the forests, we will use the cached credentials to lookup users/groups in Active Directory using the Security Identifier [SID]. This information is not 100% needed for identity mapping. However, if you have identities flagged as NoMatch or PartialMatch, this information is useful to track down additional information for the identity. For example, you have a user that is showing as Active in SharePoint, but is showing as Disabled in Active Directory. Seeing this user with NoMatch is expected as the user is not likely to be sync'ed to Azure Active Directory.
  
## Scenarios

Two-way trust between the forest SharePoint is joined to and the user forests. Users logs into the SharePoint machine using a domain account. In this scenario, the operator is unlikely to be prompted as their domain credentials should be able to read the associated domains.
  
One-way trust between the forest SharePoint is joined to and the user forests. All the user forests trust each other. In this scenario, the user logs into SharePoint as an account in the SharePoint forest. When querying for Forests, we will prompt for credentials to read the first user Forest. We will cache those credentials and use them for the remaining forests. In this scenario, the operator will see one logon prompt.
  
One-way trust between the forest SharePoint is joined to and the user forests. The user forests do not trust each other. In this scenario, the user logs into SharePoint as an account in the SharePoint forest. When querying for Forests, we will prompt for each forest. If there are 20 user forests that don't trust each other you would expect to see 20 logon prompts.
  

