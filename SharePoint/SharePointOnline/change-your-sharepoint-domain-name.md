---
title: "Change your SharePoint domain name"
ms.reviewer: waynewin
ms.author: kaarins
author: kaarins
manager: serdars
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
> This preview is rolling out. Some features are available only to organizations that have selected the [Targeted release option](/microsoft-365/admin/manage/release-options-in-office-365). You might not yet see this feature or it might look different than what is described.

It's now possible to change the SharePoint domain name for your organization in Microsoft 365. For example, if the name of your organization changes from "Contoso" to "Fourth Coffee," you can change  *contoso.sharepoint.com*  to  *fourthcoffee.sharepoint.com*.
  
> [!NOTE]
> This change affects only SharePoint and OneDrive URLs. It doesn't impact email addresses. To change the address of a site, for example, from *https://contoso.sharepoint.com/sites/sample1* to  *https://contoso.sharepoint.com/sites/sample2*, you can use the new SharePoint admin center. For info, see [Change a site address](change-site-address.md).

## Step 1: Add the new domain name

1. Check the availability of the new domain that you want by entering the full SharePoint URL in your browser (for example, https://fourthcoffee.sharepoint.com). If you get a “not found” (404) error, it indicates the domain is most likely available. If the domain is already registered by another customer, we can't provide any information or contact the customer. 

-or-

If you own the domain for another subscription, contact *NEED SPECIFIC INFO* for instructions on how to delete it. It typically takes 4-8 weeks to make the domain available. 

2. Sign in to the Microsoft 365 admin center at https://admin.microsoft.com 

Do not attempt to test this procedure in a test environment first because it could prevent renaming the desired tenant.

3.	In the same browser tab, navigate to https://aka.ms/SPORenameAddDomain which should look similar to this Custom domain names page: 

3.	Click “Add custom domain” (highlighted above) to open the Add domain pane.
4.	In the Custom domain name textbox add the full new MOERA including “.onmicrosoft.com”:
NOTE: Do NOT include any hyphens (“-“) in the new MOERA domain. Although these can be entered, they are not supported in SPO.
 
5.	Ensure you get a confirmation message. You must try a new domain if it is not available. 
 
6.	After getting a confirmation that the domain was added successfully, you may see a message that the properties could not be found. Click the blue retry arrow to refresh.
 
7.	Close the pane and return to the domain list which should now include your new domain in the full list:
 
8.	Do NOT add additional domains as this may impact the SPO Tenant Rename Private Preview Program. 
9.	Do NOT configure the new domain as the initial domain as this is currently not supported.
10.	Confirm that your domain has been added, with your SPO Tenant Rename Preview Program Point of Contact (POC), to schedule the SPO Tenant Rename. 




