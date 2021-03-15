---
title: "Change your SharePoint domain name"
ms.reviewer: waynewin
ms.author: kaarins
author: kaarins
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- CSH
ms.topic: troubleshooting
ms.custom:
- 'SPOTADNS'
- 'O365M_DomainsWizAdd_SPOUseMultiServices'
- 'O365M_DomainsProp_SPO'
- 'O365E_DomainsWizAdd_SPOUseMultiServices'
- 'O365E_DomainsProp_SPO'
- 'O365E_DomainsMain_PublicWebsite'
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MOE150
- MED150
- MBS150
- BCS160
- MET150
ms.assetid: 576325ad-8c40-4fe8-8a63-68c3b7d536cf
description: "Learn about changing your organization name in SharePoint URLs"
---

# Change your SharePoint domain name

> [!NOTE]
> This preview is rolling out to organizations with the fewest sites first. It might not be available yet for your organization.

It's now possible to change the SharePoint domain name for your organization in Microsoft 365. For example, if the name of your organization changes from "Contoso" to "Fourth Coffee," you can change  *contoso.sharepoint.com*  to  *fourthcoffee.sharepoint.com*.
  
> [!NOTE]
> This change affects only SharePoint and OneDrive URLs. It doesn't impact email addresses. For info about changing a site address, for example, from *https://contoso.sharepoint.com/sites/sample1* to  *https://contoso.sharepoint.com/sites/sample2*, see [Change a site address](change-site-address.md).

## Step 1: Add the new domain name

1. Check the availability of the new domain you want by entering the full SharePoint URL in your browser (for example, https://fourthcoffee.sharepoint.com). If you get a “not found” (404) error, it indicates the domain is most likely available. If the domain is already registered by another customer, we can't provide any information or contact the customer. 

-or-

If you own the domain for another subscription, contact *NEED SPECIFIC INFO* for instructions on how to delete it. It typically takes 4-8 weeks to make the domain available. 

> [!WARNING]
> Do not use the domain to test this procedure in a test environment first. If you do, you won't be able to use the domain for your production environment.

2. Sign in to the Microsoft 365 admin center at https://admin.microsoft.com.

3. In the same browser tab, navigate to https://aka.ms/SPORenameAddDomain.

4. Select **Add custom domain**.

5. In the **Custom domain name** box, add the full new “.onmicrosoft.com” domain.

> [!IMPORTANT]
> Do NOT include any hyphens (-) in the new domain. They aren't supported in SharePoint.
 
6. Make sure you get a confirmation message. If the domain isn't available, try a different domain. 
 
7. After getting a confirmation that the domain was added successfully, you might see a message that the properties could not be found. Select the message to refresh domain references.
 
8. Close the pane *HOW*? to return to the domain list.

> [!WARNING]
> Do NOT add any other domains. Do NOT configure the new domain as the initial domain.
 
9. Confirm that your domain has been added to the list. 




