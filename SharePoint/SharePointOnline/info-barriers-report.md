---
title: "Create an information barriers policy compliance report"
ms.reviewer: nibandyo
ms.author: kaarins
author: kaarins
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
description: "Learn how to find noncompliant sites after information barriers policies change."
---

# Create an information barriers policy compliance report

If a compliance administrator changes an information barriers policy, the change might affect the compatibility of segments already associated with a site. 
For example, a policy might allow communication and collaboration between the Sales and Research segments. Later, the policy might not allow communication and collaboration between these segments. The segments are incompatible and shouldn't be associated with the same site. 

The SharePoint information barriers policy compliance report lets SharePoint admins view the list of sites that are noncompliant with the updated policy. The report covers these sites:

- Microsoft 365 group-connected team sites that aren't connected to Microsoft Teams
- Communication sites
- Modern team sites that aren't connected to Microsoft 365 groups
- OneDrive

The report displays the list of sites that are noncompliant. For each noncompliant site, it shows compatible segments, incompatible segments, and invalid segments (those that no longer exist)

If a OneDrive is noncompliant, the report lets you remove other segments so that only the user's segment is associated with the OneDrive.

> [!NOTE]
> You only need to run this report if information barriers policies are changed. Depending on the number of sites in your organization, it can take a long time for this report to run.

## Run the report

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." <br>On the Download Center page, select your language and then click the Download button. You'll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you're running the 64-bit version of Windows or the x86 file if you're running the 32-bit version. If you don't know, see [Which version of Windows operating system am I running?](https://support.microsoft.com/help/13443/windows-which-operating-system). After the file downloads, run it and follow the steps in the Setup Wizard. 

2. Connect to SharePoint Online as a [global admin or SharePoint admin](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run the following command to build the report:

      ```PowerShell
      Start-SPOInformationBarriersPolicyComplianceReport
      ```
    
    Or, to automatically update any noncompliant OneDrive accounts when you build the report, run:

      ```PowerShell
      Start-SPOInformationBarriersPolicyComplianceReport -UpdateOneDriveSegments
      ```

4. Run the following command to view the status of the task:

      ```PowerShell
      Get-SPOInformationBarriersPolicyComplianceReport
      ```

    The command returns the following set of information:

    `State: Completed`<br>
    `Id: 9e2bd8d8-64a4-4e68-af63-81f0565c3c00`<br>
    `StartTimeInUtc: 12/6/2020 10:56:12 PM`<br>
    `CompleteTimeInUtc: 12/6/2020 10:56:17 PM`<br>
    `QueuedTimeInUtc: 12/6/2020 10:51:06 PM`<br>
    `UpdateOneDriveSegments: False`

5. Run the following command to view the report:

      ```PowerShell
      Get-SPOInformationBarriersPolicyComplianceReport -reportid <ID>
      ```

    (Where *ID* is the report's Id from the previous step.)

    The command returns the following set of information:

    `Content: {3ef21e8a-69d9-4bf0-a70f-0328e5a18087, 76cd794c-b5f1-4f3d-ad48-075e805fca17, 93d93533-783a-4274-b9c9-b79a3b9beb99}`<br>
    `HasNonCompliantSites: True`<br>
    `State: Completed`<br>
    `Id: 9e2bd8d8-64a4-4e68-af63-81f0565c3c00`<br>
    `StartTimeInUtc: 9/22/2020 11:36:50 PM`<br>
    `CompleteTimeInUtc: 9/22/2020 11:37:00 PM`<br>
    `QueuedTimeInUtc: 9/22/2020 11:31:57 PM`<br>
    `UpdateOneDriveSegments: False`

    The Content row lists the sites that are noncompliant. If all sites are compliant, the Content row is empty and HasNonCompliantSites is "False."

6. Run the following command to view details about the noncompliant segments associated with each site:

      ```PowerShell
      $report = Get-SPOInformationBarriersPolicyComplianceReport -reportid <ID> $report.Content
      ```

    (Where *ID* is the report's Id from the previous step.)

    The command returns the following set of information for each site:

    `SiteId: 3ef21e8a-69d9-4bf0-a70f-0328e5a18087`<br>
    `SiteUrl: https://contoso.sharepoint.com/sites/Research`<br>
    `SiteType: Group`<br>
    `ComplianceState: NonCompliant`<br>
    `CurrentSegments: Sales, Research`<br>
    `OriginalSegments: Sales, Research`<br>
    `InvalidIBSegments:` <br>
    `IncompatibleSegmentsPairs: <Sales, Research>`<br>
    `FailedToBeProcessed: False`<br>

> [!NOTE]
> For info about removing incompatible segments, see [Use information barriers with SharePoint](information-barriers.md#use-powershell-to-associate-segments-with-a-site). When you're done with a report, you can delete it by using `Remove-SPOInformationBarriersPolicyComplianceReport -reportid <>`
