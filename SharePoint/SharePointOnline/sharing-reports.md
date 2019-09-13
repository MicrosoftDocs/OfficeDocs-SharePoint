---
title: "Report on guest sharing"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection:  
- Strat_OD_share
- M365-collaboration
search.appverid:
- SPO160
- MET150
description: "Learn how to report on guest sharing in SharePoint."
---

# Report on guest sharing in SharePoint

•	Where to find?
o	The report is available in the SharePoint Site Usage page as a button (titled “Run Report”) underneath the headline for “Shared With External Users”
•	What does the report do?
o	It generates a CSV file of every unique file, user, permission and link on this site.
•	How do you run the report?
o	Are you click “Run Report”, you will be asked to pick a location to save the report. Note that you may want to customize the permissions of the folder where you create the report if you don’t want people in the site to know what has been shared and with whom
o	Once you select a location, the report will begin running
o	When the report is finished running you will receive an e-mail
•	Other notes & gotchas
o	Only one report can be run per site collection. If someone else has started running the report or you try and run it again, click “Run report” will tell you that fact & give you a link to the save location
o	The report may take some time to run depending on the size of the site.
•	What is in the report (Columns)


|Column|Description|
|:---|:---|
|Resource Path|This is the relative URL of an item|
|Item Type|Tells you what kind of item this is (could be a Web, Folder or File, etc)|
|Permission|Tells you what permission level the user has on this item|
|User Name|Friendly name of the user or group that has access to this item. Note that when a sharing link is created on an item, you will see a user name of “SharingLink”|
|User E-mail|Tells you the email address of the user who has access to this item. This is left blank for groups|
|User or Group Type|Tells you if the “user name” is a Member (internal), Guest (External), SharePOint Group, Security Group or Office 365 Group|
|Link ID|If user name is “Sharing Link”, this will be a unique GUID of the sharing link on this item|
|Link Type|If user name is “Sharing Link”, this will be the type of link (Anonymous, Company, Specific People)|
|AccessViaLinkID|If a user’s permission to an item is via a link (e.g. they clicked on a CSL to get access to the item), you will see one row for the link and another row for each user who has used that link. AccessViaLinkID lets you link a user who used a link to the link they used (i.e. the GUID in Link ID)|





## See also


