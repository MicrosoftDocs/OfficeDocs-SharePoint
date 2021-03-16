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
ms.topic: article
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

## Limitations

### Notes

OneDrive

|Limitation  |Action required  |
|---------|---------|
|Only the domain name portion in URLs is renamed. The relative path that's based on the User Principle Name (UPN) isn't renamed.     | None       |

OneDrive sync app (OneDrive.exe)

|Limitation  |Action required  |
|---------|---------|
|Requires version 17.3.6943.0625 or later for all users.      | Make sure all computers in your organization are able to reach "oneclient.sfx.ms" and "g.live.com." to apply updates. Do not block these URLs.   |
|The organization name displayed in Office apps isn't changed (For example, the app displays the old folder name C:\Users\Sophia\OneDrive – Contoso)      | Users can disconnect and reconnect their account in the Office app. *HOW? I don't see a "disconnect" command*   |

OneNote

|Limitation  |Action required  |
|---------|---------|
|Requires a recent version of OneNote     | Make sure all users have the following versions installed: <br> OneNote desktop app: Version 16.0.8326.2096 or later <br> OneNote for Windows 10: Version 16.0.8431.1006 or later<br> OneNote mobile app: Version 16.0.8431.1011 or later|
|While the domain name is being changed, users might encounter a notebook sync error     | None       |

SharePoint mobile apps

|Limitation  |Action required  |
|---------|---------|
|Requires a recent version of the mobile app     | Make sure all users have the following versions installed:<br>iOS: 4.20.0 or later<br> Android: 3.21.0 or later |
|While the domain name is being changed, users might encounter a notebook sync error     | None       |

### Alerts

Search and Delve

|Limitation  |Action required  |
|---------|---------|
|The search index might take a while to reflect new URL changes. <br>
Search results might not be complete or might return results for the original URLs until the search index is updated.| None |

Office "Recent" and "Pinned" lists

|Limitation  |Action required  |
|---------|---------|
|The Recent and Pinned lists are updated immediately for the first 100 users for each URL that was changed. The remaining are updated when the search index is updated.| None |

Office.com

|Limitation  |Action required  |
|---------|---------|
|The URLs at https://www.office.com can take 24 hours to be updated.| None |

### Warnings

Teams on the web and Teams desktop app

|Limitation  |Action required  |
|---------|---------|
|Meeting notes for previous meetings are lost *THIS SAID "WILL NOT BE FUNCTIONAL" BUT IT SOUNDS LIKE ACTUAL DATA LOSS??*| Before changing your domain name, save the meeting notes to a different location. After the rename, delete and recreate the meeting, and then restore the notes from the saved location. |
|On the Files tab, any folders added with the "Add cloud storage" (which point to another SharePoint site) won't work.| Remove and readd the folders. |
|Document libraries added as a tab won't work| Remove and readd the tab |

Power Apps

|Limitation  |Action required  |
|---------|---------|
|SharePoint forms modified with Power Apps won't work.| Delete any forms you don't need anymore or reset them to enable the default SharePoint form. You might need to delete some forms by using PowerShell. You might also need to recreate SharePoint forms in Power Apps. |
|Apps that use a SharePoint connection as a data source won't work.| Reconnect the apps to SharePoint |


Known issues

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




