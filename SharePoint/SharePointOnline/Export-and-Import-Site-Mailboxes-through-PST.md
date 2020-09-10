---
title: "Export and Import Site Mailboxes through PST (Manually)"
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
description: "In this article, you'll learn how to export and import site mailboxes through PST "
---
##  Export and Import Site Mailboxes through PST (Manually)

You must have [Microsoft 365 admin permissions](https://docs.microsoft.com/en-us/microsoft-365/admin/add-users/assign-admin-roles?view=o365-worldwide) to access the [Microsoft 365 compliance center](https://docs.microsoft.com/en-us/microsoft-365/compliance/microsoft-365-compliance-center?view=o365-worldwide). 

For more information, see [Permissions and sharing](https://docs.microsoft.com/en-us/sharepoint/modern-experience-sharing-permissions).

1. Go to [https://compliance.microsoft.com/](https://compliance.microsoft.com/) and sign in with an account that has [admin permissions](https://docs.microsoft.com/en-us/sharepoint/sharepoint-admin-role) for your organization.

2. In the Microsoft 365 compliance center, choose **eDiscovery** > **Core**.

3. Select **Create a case**.
   [image]

4. In **New case** details pane, enter a case name and description.
   [image]

5. Click **Save**.

6. Select the case and click on the icon to open the case.
   The case is opened in a new tab.
   [image]

7. Select **Search**.

8. Select **Guided search**[image icon].

9. In the **New search** details pane, under the **Name your search** tab, enter the name and description.

10.	Click **Next**.

11.	In **Choose locations** tab, select **Specific locations**.

12.	In **Locations**, click **Choose users, groups, or team**.

13.	In **Edit locations** window, under **Exchange email**, click **Choose users, groups, or team**.

14.	Enter the name of the site mailbox to be exported.

15.	Check the confirmation box to ensure the site mailbox is added.
    [image]
    
16.	Click **Choose**and then click **Done**.
    [image]
    
17.	Under SharePoint sites option, click **Choose sites** to add the SharePoint site associated with the site mailbox.
    [image]
18.	To find the SharePoint URL for the site mailbox, run the following command in Powershell:

```Powershell

PS D:\tools\PSSession> Get-SiteMailbox

Name        ClosedTime SharePointUrl
----        ---------- -------------
SMO-jknibb1            https://hmopco.sharepoint.com/jknibb1


PS D:\tools\PSSession>
```

Use ‘Get-SiteMailbox -BypassOwnerCheck’ option to list all the site mailboxes.

19.	In **SharePoint sites** details pane, enter the URL and check the confirmation box to ensure the URL is added.
    [image]
    
20. Click **Choose**and then click **Done**.

21.	In the **New search** details pane, click **Next**.

22.	Click **Finish**.

>[!NOTE]
> Leave the Condition card blank to ensure the entire mailbox content is searched. The search will take a while based on the amount of content.

23.	Once search is complete, click **More** and then click **Export results**.

24.	Select the appropriate options and click **Export**.
The export wizard takes a few minutes to launch the Export.

25.	In **Export key** section, click **Copy to clipboard**.

26.	Click **Download results**.

27.	In the dialog box, click **Open**.
    This will launch the Microsoft Office 365 eDiscovery Export Tool to export the mailbox to PST.
    [image]
    
28.	Click **Install**.

29.	Paste the **Export key**, provide the location to save the PST file locally and then click **Start**.
The export will take a while based on the size of the PST file.

30.	Click **Close**.
    The PST can be now attached in Outlook.

