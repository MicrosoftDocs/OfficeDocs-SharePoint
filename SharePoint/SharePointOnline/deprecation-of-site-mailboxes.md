---
title: "deprecation of site mailboxes"
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
description: "In this article, you'll learn how to identify and remove site mailboxes."
---

# Retirement of site mailboxes

The site mailboxes are being retired and will be out of service and/or removed . Please use the instructions below to identify, backup and delete site mailboxes.

## To view a list of site mailboxes

Run the following command in Exchange PowerShell:

```Powershell
Get-SiteMailbox -BypassOwnerCheck -ResultSize Unlimited | ft Name, WhenCreated, ClosedTime, SharePointUrl -AutoSize
```

The 'create' date shows the recently created site mailboxes. 
The 'ClosedTime' in the output of 'Get-SiteMailbox' refers to the status of the associated SharePoint site. The companies set a SharePoint policy to close sites after a period of time or provide users permission to close the sites. Closing the site generally means it is out of service. Closed site mailboxes are removed from view in the Outlook desktop client, but they are available in the Outlook Web Access.

For more information see, [Use policies for site closure and deletion](https://support.office.com/article/use-policies-for-site-closure-and-deletion-a8280d82-27fd-48c5-9adf-8a5431208ba5).

## To identify active site mailboxes

Run the following command in Exchange PowerShell:

```powershell
# If you run this more than once, delete/rename the output file first because this command appends to it.
# This is a single, long command line. It could take minutes or hours depending on the number of site mailboxes; thus, the countdown.
$sms = Get-SiteMailbox -BypassOwnerCheck -ResultSize unlimited ; 
$count = $sms.Count ; 
$sms | %{ $count-- ; echo "$count" ; 
Get-MailboxFolderStatistics $_.Identity -FolderScope Inbox | sort LastModifiedTime -Descending | ft Identity,LastModifiedTime >> c:\temp\sitemailboxes.txt 
```

There are no commands to show if the site mailboxes are still active. The above example lists the number of site mailboxes that were recently updated. The details of the site mailboxes are stored in a file. 

>[!NOTE]
> The processing time varies based on the number of site mailboxes.

## To Identify the owners of site mailboxes

Run the following command in Exchange PowerShell:

```powershell
Get-SiteMailbox -BypassOwnerCheck | fl Name, Owners
```

## Export site mailboxes through PST (Manually)

You must have [Microsoft 365 admin permissions](https://docs.microsoft.com/microsoft-365/admin/add-users/assign-admin-roles?view=o365-worldwide) to access the [Microsoft 365 compliance center](https://docs.microsoft.com/microsoft-365/compliance/microsoft-365-compliance-center?view=o365-worldwide). 

For more information, see [Permissions and sharing](https://docs.microsoft.com/sharepoint/modern-experience-sharing-permissions).

1. Go to [https://compliance.microsoft.com/](https://compliance.microsoft.com/) and sign in with an account that has [admin permissions](https://docs.microsoft.com/sharepoint/sharepoint-admin-role) for your organization.

2. In the Microsoft 365 compliance center Home page, navigate to **Show all** > **eDiscovery** > **Core**.

   The **Core eDiscovery** page is displayed.

3. Click **Create a case**.

4. In **New case** details pane, enter the following details:
   - Enter the **Case name** (mandatory).
   - Enter the **Case description** (optional).

5. Click **Save**.

6. Select the case that you saved from the list view and click ![icon-ac](media/icon-for-im3.PNG) to open the case.

   The case opens in a new window.

7. Click **Search** > **+Guided search**.

   The **New Search** details pane is displayed.

8. In the **New search** details pane, under the following tabs:

   a. In **Name your search** tab, do the following:
      - Enter the **Name** (mandatory).
      - Enter **Description** (optional).
      - Click **Next**.
      
   b. In **Choose Locations** tab, do the following:
      - Select **Specific locations**.
      - In **Location**, click **Choose users, groups, or team**.
      
        The **Edit locations** window is displayed.
      - In **Edit locations** window, under **Exchange email**, click **Choose users, groups, or team**.
      - Enter the name of the site mailbox to be exported.
      - Check the confirmation box to ensure the site mailbox is added.
      - Click **Choose** and then click **Done**.
      - Under **SharePoint sites** option, click **Choose sites** to add the SharePoint site associated with the site mailbox.
      - To find the SharePoint URL for the site mailbox, run the following command in Powershell:

        ```Powershell

        PS D:\tools\PSSession> Get-SiteMailbox

        Name        ClosedTime SharePointUrl
        ----        ---------- -------------
        SMO-jknibb1            https://hmopco.sharepoint.com/jknibb1


        PS D:\tools\PSSession>
        ```

        Use ‘Get-SiteMailbox -BypassOwnerCheck’ option to list all the site mailboxes.
      - Enter the URL and check the confirmation box to ensure the URL is added.
      - Click **Choose** and then click **Done**.
      - Click **Next**.
      
   c. In **Create query** tab, click **Finish**.
   
      >[!NOTE]
      > Leave the Condition card blank to ensure the entire mailbox content is searched. The search will take a while based on the amount of content.


9. Once the search is complete, click **More** > **Export results**.

   The **Export results** window is displayed.
    
10. Select the appropriate options and click **Export**.
      
    >[!NOTE]
    > The export wizard takes a few minutes to launch the Export window.

11. In the **Export** window, under the **Export key** section, click **Copy to clipboard**.

12. Click **Download results**.

13. In the dialog box, click **Open**.
    
    >[!NOTE]
    > This will launch the Microsoft Office 365 eDiscovery Export Tool to export the mailbox to PST.
    
14. Click **Install** to install the **Export Tool** to export the mailbox to PST.

15. Paste the **Export key**, provide the location to save the PST file locally and then click **Start**.
    
    >[!NOTE]
    > The export will take a while based on the size of the PST file.

16. Click **Close**.

    The PST can be now attached in Outlook.
    
  >[!NOTE]
  > - Folder with no email items inside them will not be exported.
  > - The site mailboxes contain special folder named, "Documents", of type IPF.ShortcutFolder. This contains "links" to files that are on SP site. The actual SP files must be       exported using eDiscovery for SP sites.
  > - Outlook shows the items inside the Documents folder as unsafe, this is an expected behaviour.
  > - The document attachments in the emails of Documents folder are just place holder, the actual documents are stored in SharePoint.
  
## Export site mailboxes to PST (using script)

1. Copy the [ProcessSiteMailboxes.PS1](https://microsoft-my.sharepoint-df.com/personal/vijagan_microsoft_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fvijagan%5Fmicrosoft%5Fcom%2FDocuments%2FProcessSiteMailboxes%2Eps1%2Etxt&parent=%2Fpersonal%2Fvijagan%5Fmicrosoft%5Fcom%2FDocuments&originalPath=aHR0cHM6Ly9taWNyb3NvZnQtbXkuc2hhcmVwb2ludC1kZi5jb20vOnQ6L3AvdmlqYWdhbi9FZEctUUhjcjJERkJtRGJ4Ni0zMTY3Y0JXWm9IRkdlbHJja3RrVUNZTTJNSjBBP3J0aW1lPVRZOUdCejlXMkVn) to a working directory.

2. Start Windows PowerShell in administrator mode.

   For more information see, [Microsoft 365 admin permissions](https://docs.microsoft.com/microsoft-365/admin/add-users/assign-admin-roles?view=o365-worldwide).
   
   >[!NOTE]
   > Ensure you have admin permissions for the following roles:
   > - Compliance Administrator
   > - eDiscovery Manager
   > - Organization Management

3. Run the script 'ProcessSiteMailboxes.PS1' in PowerShell.

4. Enter the admin username and password when prompted.

5. You can review the list of site mailboxes by opening ‘SiteMailboxesList.csv’ file on a working directory, when it prompts you to review the file.

6. Remove any site mailbox(es) from the list which you would not like to backup.

7. Save 'SiteMailboxesList.csv', after reviewing it.

8. Press 'y' when prompted "Do you like to proceed further? (Y/N)" to continue.

9. Once you get "Mailboxes content search are complete" message on your screen, access the export results created for each mailbox by going to the compliance center in Microsoft 365 Administrator dashboard.

   >[!NOTE]
   > Use Compliance center dashboard to download PST messages on your screen.

 >[!NOTE]
  > - Folder with no email items inside them will not be exported.
  > - The site mailboxes contain special folder named, "Documents", of type IPF.ShortcutFolder. This contains "links" to files that are on SP site. The actual SP files must be       exported using eDiscovery for SP sites.
  > - Outlook shows the items inside the Documents folder as unsafe, this is an expected behaviour.
  > - The document attachments in the emails of Documents folder are just place holder, the actual documents are stored in SharePoint.

## Import site mailboxes

For the site mailboxes to be accessible again for site owners, import the PST files to a mailbox. See one of the following topics for detailed, step-by-step instructions for bulk-importing your organization's PST files to Office 365.

- [Use network upload to import PST files to Office 365](https://docs.microsoft.com/microsoft-365/compliance/use-network-upload-to-import-pst-files?view=o365-worldwide)

- [Use drive shipping to import PST files](https://docs.microsoft.com/microsoft-365/compliance/use-drive-shipping-to-import-pst-files-to-office-365?view=o365-worldwide)

## Use Exchange Web Services (EWS) APIs to extract mailbox content

You can also export and import site mailboxes using EWS APIs like any other mailbox. Exporting and importing of appointments, emails, contacts, tasks, and other mailbox items can be done by using the EWS-Managed API or EWS in Exchange.

For more information see, [Exporting and importing items by using EWS in Exchange](https://docs.microsoft.com/exchange/client-developer/exchange-web-services/exporting-and-importing-items-by-using-ews-in-exchange).

See one of the following topics for exporting and importing of mailbox content:

- [Export items by using EWS in Exchange](https://docs.microsoft.com/exchange/client-developer/exchange-web-services/how-to-export-items-by-using-ews-in-exchange)    
- [Import items by using EWS in Exchange](https://docs.microsoft.com/exchange/client-developer/exchange-web-services/how-to-import-items-by-using-ews-in-exchange)

## To remove the site mailboxes

Use one of the following options:

**Option 1**: Hiding the mailbox from a SharePoint site

You can hide the site mailbox by removing it from the SharePoint site but it will still exist in Exchange. You can access the mailbox through Outlook Web Access if the browser is bookmarked.

1. Navigate to the SharePoint site from which you want to hide the mailbox.

2. Click **Settings** > **Site contents**.

3. Under **Lists, Libraries, and other APPs**, point to **Site Mailbox**, and then click **…** for more information.

4. Click **Remove** and then click **OK** to remove the site mailbox app.

   >[!NOTE]
   > If you remove a mailbox from a site, it won’t be displayed on the site, but it will still be visible in Outlook (if you’re using Exchange).

#### What else do I need to know?
There are a couple of things worth noting about removing a site mailbox:
- The only way to fully delete a site mailbox is to [delete the entire site itself](https://support.microsoft.com/office/delete-a-sharepoint-site-or-subsite-bc37b743-0cef-475e-9a8c-8fc4d40179fb). When a site is closed or deleted (either manually, or by following [site closure policies](https://support.microsoft.com/office/use-policies-for-site-closure-and-deletion-a8280d82-27fd-48c5-9adf-8a5431208ba5)), the site mailbox is also closed or deleted.

- After removing the site mailbox app from a site, mail sent to the mailbox will still be stored. If you [add the mailbox back to the site](https://support.microsoft.com/office/add-a-site-mailbox-to-keep-email-in-context-cccaa235-c611-48e3-9653-0b9e161840e7) later, any mail sent to the site mailbox since it was originally created will still be there.

**Option 2**: Delete the SharePoint site

If the SharePoint site is deleted, Exchange is notified to also delete the site mailbox.

1.	Navigate to the SharePoint site you want to delete.

2.	Select **Settings** at the top of the site and then click **Site information**.

    >[!NOTE]
    > If you do not see **Site information** in the **Settings** panel, work with your SharePoint administrator to get access.

3.	At the bottom of the **Site Information** panel, select **Delete site**.

4.	Check the confirmation box, and then click **Delete**.

**Option 3**: Delete the site mailbox manually

For example, run the following command in Exchange PowerShell:

```powershell
Get-Mailbox MDEL:* | ?{$_.RecipientTypeDetails -eq "TeamMailbox"} | Remove-Mailbox -Confirm:$false
```
Use 'Remove-Mailbox' to delete a site mailbox. The system removes the site mailbox link from the SharePoint site when a site mailbox is deleted. In the example, change the 'MDEL' to the name of the site mailbox you want to delete.

