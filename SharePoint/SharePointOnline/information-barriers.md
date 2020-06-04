---
title: "Use information barriers with SharePoint"
ms.reviewer: nibandyo
ms.author: kaarins
author: kaarins
manager: pamgreen
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
description: "Learn about associating segments with a site, and what happens when segments are associated with a site."
---

# Use information barriers with SharePoint

Information barriers are policies in Microsoft 365 that a compliance admin can configure to prevent users from communicating and collaborating with each other. This is useful if, for example, one department is handling information that shouldn't be shared with specific other departments or a group needs to be prevented, or isolated, from collaborating with all users outside of that group. Information barriers are often used in highly regulated industries and those with compliance requirements, such as finance, legal, and government. [Learn more about information barriers](/microsoft-365/compliance/information-barriers).

The following image illustrates three segments in an organization: HR, Sales, and Research. An information barriers policy has been defined that blocks communication and collaboration between the Sales and Research segments. These segments are incompatible. 

![Example of segments in an organization](media/info-barriers-segments-example.png)

With SharePoint information barriers, a SharePoint or global admin can associate segments to a site to prevent the site from being shared with or accessed by users outside the segments. Up to 10 compatible segments can be associated with a site. The segments are associated at the site level (previously called site collection level). Segments can't be associated at the subsite level.

In the above example, the HR segment is compatible with both Sales and Research. However, because the Sales and Research segments are incompatible, they can't be associated with the same site. 

## Prerequisites

- [Make sure you meet the licensing requirements for information barriers](/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#information-barriers).
- Complete the form to enable SharePoint and OneDrive information barriers in your organization. 
- Create segments and define the users in each. Create policies that allow or block communication between the segments, and then set them to active. For info, see [Define policies for information barriers](/office365/securitycompliance/information-barriers-policies).

## Use PowerShell to associate segments with a site

1. Connect to the [Security & Compliance Center PowerShell](/powershell/exchange/office-365-scc/connect-to-scc-powershell/connect-to-scc-powershell) as a global admin. 

2. Run the following command to get the list of segments and their GUIDs.

    ```PowerShell
    Get-OrganizationSegment | ft Name, EXOSegmentID
    ```

3.	Save the list of segments.

    |Name  |EXOSegmentId  |
    |---------|---------|
    |Sales     |  a9592060-c856-4301-b60f-bf9a04990d4d       |
    |Research     |     27d20a85-1c1b-4af2-bf45-a41093b5d111    |
    |HR     |      a17efb47-e3c9-4d85-a188-1cd59c83de32   |

4. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." <br>On the Download Center page, select your language and then click the Download button. You'll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you're running the 64-bit version of Windows or the x86 file if you're running the 32-bit version. If you don't know, see https://support.microsoft.com/help/13443/windows-which-operating-system. After the file downloads, run it and follow the steps in the Setup Wizard. 

5. Connect to SharePoint Online as a [global admin or SharePoint admin](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
6. Run the following command:

      ```PowerShell
      Set-Sposite -Identity <site URL> -AddInformationSegment <segment GUID>
      ```

    Example: 
    Set-SPOSite -Identity https:<i></i>//contoso<i></i>.sharepoint<i></i>.com/sites/ResearchTeamSite 
-AddInformationSegment 27d20a85-1c1b-4af2-bf45-a41093b5d111

An error will appear if you attempt to associate a segment that isn't compatible with the site’s existing segments. 

> [!NOTE]
> To remove a segment, use the -RemoveInformationSegment parameter.

## Segments associated with Microsoft Teams sites

When a team is created in Microsoft Teams, a SharePoint site is automatically created for the team's files. Within 24 hours, the segments associated with the team's members are automatically associated with the site. SharePoint admins can't change the segments associated with a site when the site is connected to a team. [Learn more about information barriers in Teams](/microsoftteams/information-barriers-in-teams)

## View the segments associated with a site

Run the following command in the SharePoint Online Management Shell to return the GUIDs of any segments associated with a site.

```PowerShell
Get-SPOSite -Identity <site URL> | Select InformationSegment
```

## Sharing sites that have segments associated

When a segment is associated with a site:

- The option to share with "Anyone with the link" is disabled.
- The site and its content can be shared only with users whose segment matches that of the site. For example, if a site is associated with only HR, only users in the HR segment can access that site (even though HR is compatible with both Sales and Research).
- New users can be added to the site as site members only if their segment matches that of the site. 

When a site has no segments associated: 

- The site and its contents can be shared based on the information barriers policy applied to the user. For example, if a user in HR is allowed to communicate with users in Research, the user will be able to share the site with those users. 

## Access to sites that have segments associated

Access to a SharePoint site is allowed only to users whose segment matches a segment associated with the site AND who have access permission to the site.  

## Search

Users will see search results from:

- Sites that have an associated segment that matches the user's segment and the user has access permission to the site. 
- Sites that don't have associated segments if they have access to the site. 

## Effects of changing information barriers policies and user segments

If a compliance administrator changes an existing policy, the change may impact the compatibility of the segments associated with a site. For example, segments that were once compatible may no longer be compatible. A SharePoint admin must change the segments associated with an affected site accordingly. 

If a SharePoint site owner’s segment changes, the user won't be able to access the site if their segment doesn't match any of the segments associated with the site. To allow the user to access the site, a SharePoint admin must associate the user's new segment with the site.

## Known issues

- For organizations that have [Microsoft 365 Multi-Geo](/office365/enterprise/office-365-multi-geo), moving a site that has associated segments isn't supported. Remove any associated segments, move the site, and then reassociate the segments. 

