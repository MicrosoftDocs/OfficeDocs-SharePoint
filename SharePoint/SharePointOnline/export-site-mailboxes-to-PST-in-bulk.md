---
title: "Export site mailboxes to PST in Bulk (using script)"
ms.author: v-bshilpa
author: Benny
manager: Serdars
audience: Admin
f1.keywords:
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
ms.collection:  
ms.custom:
description: "In this article, you'll learn how to export site mailboxes to PST in Bulk (using script)"
---

## Export site mailboxes to PST in Bulk (using script)

1. Copy the [ProcessSiteMailboxes.PS1](https://microsoft-my.sharepoint-df.com/personal/vijagan_microsoft_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fvijagan%5Fmicrosoft%5Fcom%2FDocuments%2FProcessSiteMailboxes%2Eps1%2Etxt&parent=%2Fpersonal%2Fvijagan%5Fmicrosoft%5Fcom%2FDocuments&originalPath=aHR0cHM6Ly9taWNyb3NvZnQtbXkuc2hhcmVwb2ludC1kZi5jb20vOnQ6L3AvdmlqYWdhbi9FZEctUUhjcjJERkJtRGJ4Ni0zMTY3Y0JXWm9IRkdlbHJja3RrVUNZTTJNSjBBP3J0aW1lPVRZOUdCejlXMkVn) to a working directory.

2. Start Windows PowerShell in administrator mode.

   For more information see, [Microsoft 365 admin permissions](https://docs.microsoft.com/en-us/microsoft-365/admin/add-users/assign-admin-roles?view=o365-worldwide).
   
>[!NOTE]
> Ensure you have admin permissions for the following roles:
> -	Compliance Administrator
> -	eDiscovery Manager
> - Organization Management

3. Run the script 'ProcessSiteMailboxes.PS1' in Powershell.

4. Enter the admin username and password when prompted.

5. You can review the list of site mailboxes by opening ‘SiteMailboxesList.csv’ file on a working directory, when it prompts you to review the file.

6. Remove any site mailbox(es) from the list which you would not like to backup.

7. Save 'SiteMailboxesList.csv', after reviewing it.

8. Press 'y' when prompted "Do you like to proceed further? (Y/N)" to continue.

9. Monitor script execution progress and access export created for each mailbox via compliance center in Microsoft 365 Administrator dashboard when you get “Mailboxes content search are complete" message.

>[!NOTE]
> Use Compliance Center dashboard to download PST messages on your screen.

 >[!NOTE]
  > - Folder with no email items inside them will not be exported.
  > - The site mailboxes contain special folder named, "Documents", of type IPF.ShortcutFolder. This contains "links" to files that are on SP site. The actual SP files must be       exported using eDiscovery for SP sites.
  > - Outlook shows the items inside the Documents folder as unsafe, this is an expected behaviour.
  > - The document attachments in the emails of Documents folder are just place holder, the actual documents are stored in SharePoint.

## Import site mailboxes

For the site mailboxes to be accessible again for site owners, import the PST files to a mailbox. See one of the following topics for detailed, step-by-step instructions for bulk-importing your organization's PST files to Office 365.

- [Use network upload to import PST files to Office 365](https://docs.microsoft.com/en-us/microsoft-365/compliance/use-network-upload-to-import-pst-files?view=o365-worldwide)

-	[Use drive shipping to import PST files](https://docs.microsoft.com/en-us/microsoft-365/compliance/use-drive-shipping-to-import-pst-files-to-office-365?view=o365-worldwide)








