---
title: "Report on sharing"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ROBOTS: NOINDEX
ms.collection:  
- Strat_OD_share
- M365-collaboration
search.appverid:
- SPO160
- MET150
description: "Learn how to report on file and folder sharing in a SharePoint site."
---

# Report on file and folder sharing in a SharePoint site

You can create a CSV file of every unique file, user, permission and link on a given SharePoint site. This can help you understand how sharing is being used for the site, and if any files or folders are being shared with guests.

When you run the report, the CSV file is saved to a location of your choosing on the site. If you don't want site members to see the report, consider creating a folder with different permissions where only site owners can access the report.

To run the report
1. Open the site where you want to run the report
2. On the **Settings** menu, click **Site usage**.
3. In the **Shared with external users** section, click **Run report**.
4. Choose a location to save the report, and then click **Run report**.

The report may take some time to run depending on the size of the site.

When the report is finished running you will receive an email with a link to the report.

## CSV format

For items shared with direct access, the report contains one row for each user / item combination.

For items shared with a link, the report contains a row for each signed-in user who has used the link or has been sent the link through the sharing dialog box. Links emailed directly that haven't been clicked, and *Anyone* links are not included in the report.

The report contains the following columns:

|Column|Description|
|:---|:---|
|Resource Path|The relative URL of the item|
|Item Type|The type of item (web, folder, file, etc.)|
|Permission|The permission level the user has on this item|
|User Name|Friendly name of the user or group that has access to this item. If this is a sharing link, the user name is *SharingLink*|
|User E-mail|The email address of the user who has access to this item. This is blank for SharePoint groups.|
|User or Group Type|The type of user or group: Member (internal), Guest (external), SharePoint group, Security group or Office 365 group. (Note that *Member* refers to a member in the directory, not a member of the site.)|
|Link ID|The GUID of the sharing link if user name is *Sharing Link*|
|Link Type|The type of link (Anonymous, Company, Specific People) if user name is *Sharing Link*|
|AccessViaLinkID|The **Link ID** used to access the item if a user's permission to an item is via a link.



