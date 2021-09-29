---
title: "Use information barriers with SharePoint"
description: "Learn about associating segments with a site, and what happens when segments are associated with a site."
ms.author: robmazz
author: robmazz
manager: laurawi
recommendations: true
ms.reviewer: nibandyo
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
---

# Use information barriers with SharePoint

[Information barriers](/microsoft-365/compliance/information-barriers) are policies in Microsoft 365 that a compliance admin can configure to prevent users from communicating and collaborating with each other. This solution is useful if, for example, one division is handling information that shouldn't be shared with specific other divisions, or a division needs to be prevented, or isolated, from collaborating with all users outside of the division. Information barriers are often used in highly regulated industries and those organizations with compliance requirements, such as finance, legal, and government.

For SharePoint, information barriers can determine and prevent the following kinds of unauthorized collaborations:

- Adding a user to a site
- User access to a site or site content 
- Sharing a site or site content with other users

## Information barriers modes and SharePoint sites

[Information barriers modes](/microsoft-365/compliance/information-barriers-policies.md#step-6-information-barriers-modes-preview) help strengthen access, sharing, and membership of a site based on its IB mode and segments associated with the site.

When using information barriers with SharePoint, the following IB modes are supported:

| **Mode** | **Description** | **Examples** |
|:-------  |:----------------|:-------------|
| **Open** | When a SharePoint site does not have segments, the site's IB mode is automatically set as *Open*. See [this section](#view-and-manage-IB-mode-as-an-administrator-with-SharePoint-PowerShell) for details on managing segments with the *Open* mode configuration. | A Team site created for picnic event for your organization.  |
| **Owner Moderated** | When a SharePoint site is created for collaboration between incompatible segments moderated by the site owner, the site's IB mode should be set as *Owner Moderated*. This mode is currently supported only for sites that are not connected to Microsoft365 group. See [this section](#owner-moderated-mode-scenario) for details on managing *Owner Moderated* site. | A site is created for collaboration between VP of Sales and Research in the presence of VP of HR (site owner).  |
| **Implicit** | When a site is provisioned by Microsoft Teams, the site's IB mode is set as *Implicit* by default. A SharePoint admin or global admin cannot manage segments with the *Implicit* mode configuration. | A Team is created for all Sales segment users to collaborate with each other. |
| **Explicit** | When segment is added to a SharePoint site either via end-user site creation experience or by a SharePoint admin adding segment to a site, the site's IB mode is set as *Explicit*. See [this section](#view-and-manage-IB-mode-as-an-administrator-with-SharePoint-PowerShell) for details on managing segments with the *Explicit* mode configuration. | A research site is created for Research segment users. |

## Sharing sites for IB modes

### Open

When a site has no segments and site's information barriers mode is set to *Open*:

- The site and its contents can be shared based on the information barrier policy applied to the user. For example, if a user in HR is allowed to communicate with users in Research, the user will be able to share the site with those users.

### Owner Moderated

When a site has information barriers mode is set to *Owner Moderated*:

- The option to share with *Anyone with the link* is disabled.
- The option to share with *Company-wide link* is disabled.
- The site and its content can be shared with existing members.
- The site and its content can be shared only by the site owner per their IB policy.

### Implicit

When a site is associated with a segment and site's information barriers mode is set to *Implicit*:

- The option to share with *Anyone with the link* is disabled.
- The option to share with *Company-wide link* is disabled.
- The site and its content can be shared only with users whose segment matches that of the site. For example, if a site is associated with only HR, the site can be shared with other HR users only (even though HR is compatible with both Sales and Research).
- New users can be added to the site via the Teams add member experience.

### Explicit

When a site is associated with a segment and site's information barriers mode is set to *Explicit*:

- The option to share with *Anyone with the link* is disabled.
- The option to share with *Company-wide link* is disabled.
- The site and its content can be shared only with users whose segment matches that of the site. For example, if a site is associated with only HR, the site can be shared with other HR users only (even though HR is compatible with both Sales and Research).
- New users can be added to the site as site members only if their segment matches that of the site.

## Access control for IB modes

### Open mode

For a user to access a SharePoint site that has no segment and site's information barriers  mode is set to *Open*:

- The user has site access permissions.

### Owner Moderated mode

For a user to access a SharePoint site with site's information barriers mode is set to *Owner Moderated*:

- The user has site access permissions.

### Implicit and Explicit modes

For a user to access SharePoint sites that have segments and site's information barriers mode is *Explicit* or *Implicit*:

- The user's segment must match a segment that is associated with the site.

    AND

- The user must have access permission to the site.  

Non-segment users can't access a site that is associated with segments. They will see an error message.

## Example scenario

The following example illustrates three segments in an organization: HR, Sales, and Research. An information barrier policy has been defined that blocks communication and collaboration between the Sales and Research segments. These segments are incompatible.

![Example of segments in an organization.](media/info-barriers-segments-example.png)

With SharePoint information barriers, a SharePoint or global admin can associate segments to a site to prevent the site from being shared with or accessed by users outside the segments. Up to 100 compatible segments can be associated with a site. The segments are associated at the site level (previously called site collection level). The Microsoft 365 group connected to the site is also associated with the site's segment.

In the above example, the HR segment is compatible with both Sales and Research. However, because the Sales and Research segments are incompatible, they can't be associated with the same site.

## Prerequisites

1. Make sure you meet the [licensing requirements for information barriers](/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#information-barriers).
2. [Create information barrier policies](/office365/securitycompliance/information-barriers-policies) that allow or block communication between the segments, and then set them to active. Create segments and define the users in each.
3. After you've configured and activated your information barrier policies, wait 24 hours for the changes to propagate through your organization.
4. Complete the steps in the following sections to enable and manage SharePoint and OneDrive information barriers in your organization.

## Enable SharePoint and OneDrive information barriers in your organization

SharePoint Administrators or Global Administrators can enable information barriers in SharePoint and OneDrive in your organization. Complete the following steps to enable information barriers for your organization:

1. [Download](https://go.microsoft.com/fwlink/p/?LinkId=255251) and install the latest version of SharePoint Online Management Shell.
2. Connect to SharePoint Online as a global admin or [SharePoint admin](sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
3. To enable information barriers in SharePoint and OneDrive, run the following command:

    ```PowerShell
    Set-SPOTenant -InformationBarriersSuspension $false 
    ```

4. After you've enabled information barriers for SharePoint and OneDrive in your organization, wait for approximately 1 hour for the changes to take effect. 

>[!NOTE]
>If you have Microsoft 365 Multi-Geo, you must run this command for each of your geo-locations.

If you installed a previous version of the SharePoint Online Management Shell, complete the following steps:

1. Go to **Add or remove programs** and uninstall *SharePoint Online Management Shell*.
2. Navigate to the Microsoft Download Center for the [SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251)), select your language, and then select **Download**.
3. You may be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you're running the 64-bit version of Windows or the x86 file if you're running the 32-bit version of Windows. If you don't know which version you're running on your computer, see [Which version of Windows operating system am I running?](https://support.microsoft.com/help/13443/windows-which-operating-system).
4. After the download is complete, run the installer file and follow the configuration steps in the setup wizard.
5. Connect to SharePoint Online as a global admin or [SharePoint admin](sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
6. To enable information barriers in SharePoint and OneDrive, run the following command:

    ```PowerShell
    Set-SPOTenant -InformationBarriersSuspension $false 
    ```

7.After you've configured information barriers in SharePoint and OneDrive in your organization, wait for approximately 1 hour for the changes to take effect.

>[!NOTE]
>If you have Microsoft 365 Multi-Geo, you must run this command for each of your geo-locations.

## View and manage segments as an administrator

SharePoint or Global Administrators can view and manage segments on a SharePoint site as follows:

### 1. Use the SharePoint admin center to view and manage information segments

To view, edit, or remove information segments for a site, use the [Active sites page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=siteManagement&modern=true).  

The Segments column lists the first segment associated with the site and shows whether the site has other segments associated. [Learn how to show or move this column](manage-sites-in-new-admin-center.md#customize-columns)

![Segments column on the Active sites page.](media/info-barriers-segments-column.png)

To view the complete list of segments associated with a site, select the site, and then select the **Policies** tab.

![Policies tab of the details panel listing all associated segments.](media/info-barriers-segments-details.png)

To edit the segments associated with the site, select **Edit**, add or remove segments, and then select **Save**.

![Edit information segments panel.](media/info-barriers-edit-info-segments.png)

### 2. Use SharePoint PowerShell to view and manage information segments on a site

1. Connect to the [Security & Compliance Center PowerShell](/powershell/exchange/office-365-scc/connect-to-scc-powershell/connect-to-scc-powershell) as a global admin.

2. Run the following command to get the list of segments and their GUIDs.

    ```PowerShell
    Get-OrganizationSegment | ft Name, EXOSegmentID
    ```

3. Save the list of segments.

    |**Name**|**EXOSegmentId**|
    |:-------|:---------------|
    | Sales | a9592060-c856-4301-b60f-bf9a04990d4d |
    | Research | 27d20a85-1c1b-4af2-bf45-a41093b5d111 |
    | HR | a17efb47-e3c9-4d85-a188-1cd59c83de32 |

4. If not previously completed, [download](https://go.microsoft.com/fwlink/p/?LinkId=255251) and install the latest SharePoint Online Management Shell. If you installed a previous version of the SharePoint Online Management Shell, follow the instructions in the **Enable SharePoint and OneDrive information barriers in your organization** section in this article.

5. Connect to SharePoint Online as a [global admin or SharePoint admin](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

6. Run the following command:

      ```PowerShell
      Set-SPOSite -Identity <site URL> -AddInformationSegment <segment GUID>
      ```

    For example:

    ```powershell
    Set-SPOSite -Identity https://contoso.sharepoint.com/sites/ResearchTeamSite -AddInformationSegment 27d20a85-1c1b-4af2-bf45-a41093b5d111
    ```

You'll see an error message if you attempt to associate a segment that isn't compatible with the site's existing segments.

>[!NOTE]
>When you add a segment to a site, the site's IB mode is automatically updated as *Explicit*.

To remove segment from a site, run the following command:  

```PowerShell
Set-SPOSite -Identity <site URL> -RemoveInformationSegment <segment GUID>
 ```

For example:

```powershell
Set-SPOSite -Identity https://contoso.sharepoint.com/sites/ResearchTeamSite -RemoveInformationSegment 27d20a85-1c1b-4af2-bf45-a41093b5d111
```

To view the segments of a site, run the following command to return the GUIDs of any segments associated with the site.

>[!NOTE]
>When all segments are removed from a site, the site's IB mode is automatically updated to *Open*.

```PowerShell
Get-SPOSite -Identity <site URL> | Select InformationSegment
```

### 3. Use the SharePoint REST API to view and manage information segments on a site

SharePoint includes a Representational State Transfer (REST) service that you can use to manage segments on a site. To access SharePoint resources and manage site segments using REST, you'll construct a RESTful HTTP request by using the OData standard, which corresponds to the desired client object model application programming interface (API).

For more information about the SharePoint REST service, see [Get to know the SharePoint REST service](/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service).

## View and manage IB mode as an administrator with SharePoint PowerShell

To view the IB mode of a site, run the following command:

```powershell
Get-SPOSite -Identity <site URL> | Select InformationBarriersMode
```

### Owner Moderated mode scenario

You want to allow Sales and Research user to collaborate on a SharePoint site in the presence of HR user.

*Owner Moderated* is a new mode applicable to site (not connected to Microsoft 365 group) which allows incompatible segment users access to site. Only the site owner has the capability to invite incompatible segment users on this same site.

To update a site's mode to *Owner Moderated*, run the following PowerShell command:

```powershell
Set-SPOSite -Identity <siteurl> InformationBarriersMode OwnerModerated
```

Owner Moderated IB mode cannot be set on a site with segments. Remove the segments first before setting IB mode as Owner Moderated. Access to an Owner Moderated site is allowed to users who have site access permissions. Sharing of an Owner Moderated site and its contents is only allowed by the site owner per their IB policy.

## Auditing

Audit events are available in the Microsoft 365 compliance center to help you monitor information barrier activities. Audit events are logged for the following activities:

- Enabled information barriers for SharePoint and OneDrive
- Applied segment to site
- Changed segment of site
- Removed segment of site
- Applied information barriers mode to site
- Changed information barriers mode of site
- Disabled information barriers for SharePoint and OneDrive

For more information about SharePoint segment auditing in Office 365, see [Search the audit log in the compliance center](/microsoft-365/compliance/search-the-audit-log-in-security-and-compliance#information-barriers-activities).

## Site creation and management by site owners

When a segmented user creates a SharePoint site, the site is associated with the user's segment and site's information barriers mode is automatically set to *Explicit*.

In addition, the site owners have the capability to add more segments to a SharePoint site that already has segments with site's mode set as *Explicit*. Site owners cannot remove added segments from sites. SharePoint admins will have to remove added segments in your organization if needed.

When a non-segmented user creates a SharePoint site, the site is not associated with any segment and site's information barriers mode is automatically set to *Open*.

When an SPO admin creates a SharePoint site from SharePoint Admin Center, the site is not associated with any segment and site's IB mode is set to *Open*.

To help site owners add a segment to a site, share the [Associate information segments with SharePoint sites](https://support.microsoft.com/office/associate-information-segments-with-sharepoint-sites-2b03db07-6d3f-4297-a388-b943317a26a7) article with your SharePoint site owners.

## Segments associated with Microsoft Teams sites

When a team is created in Microsoft Teams, a SharePoint site is automatically created for the team's files. Within 24 hours, the segments associated with the team's members are automatically associated with the site and site's information barriers mode is automatically set as *Implicit*. SharePoint admins can't change the segments associated with a site when the site is connected to a team and mode as *Implicit*. For more information, see [Learn more about information barriers in Teams](/microsoftteams/information-barriers-in-teams).

If the global administrator updates IB mode of an existing Microsoft 365 group connected to Microsoft Teams to *Implicit*, make sure to update the IB mode of the Teams connected site to *Implicit*. For more information, see [the section](#view-and-manage-segments-as-an-administrator) on how to manage IB mode of a site.  

> [!NOTE]
> When you create a new team or private channel in Microsoft Teams, a team site in SharePoint gets automatically created. To edit the site description or classification for this team site, go to the corresponding channel's [settings in Microsoft Teams](https://support.microsoft.com/office/change-a-team-s-data-security-classification-in-teams-bf39798f-90d2-44fb-a750-55fa05a56f1d).
>
> Learn more about managing [Microsoft Teams connected teams sites](https://docs.microsoft.com/SharePoint/teams-connected-sites).

## Search

Users will see search results from:

- Sites that have an associated segment that matches the user's segment and the user has access permission to the site.
- Sites that don't have associated segments if they have access to the site.

## Effects of changes to user segments or information barrier policies

If a SharePoint site owner's segment changes, the user won't be able to access the site if their segment doesn't match any of the segments associated with the site. To allow the user to access the site, a SharePoint admin must associate the user's new segment with the site.

If a compliance administrator changes an existing policy, the change may impact the compatibility of the segments associated with a site. For example, segments that were once compatible may no longer be compatible. A SharePoint admin must change the segments associated with an affected site accordingly. [Learn how to create an information barriers policy compliance report in PowerShell](info-barriers-report.md)

Any sharing links will only work if a user's new segment or the new information barrier policy still allows the user to access the site.

## How to suspend SharePoint and OneDrive information barriers in your tenant

If your organization would like to temporarily suspend information barriers on SharePoint, you must use SharePoint Online Management Shell and the [Set-Spotenant](/powershell/module/sharepoint-online/set-spotenant) cmdlet.

To suspend information barriers, run the following command:

```PowerShell
Set-SPOTenant -InformationBarriersSuspension $true 
```

>[!NOTE]
>If you have Microsoft 365 Multi-Geo, you must run this command for each of your geo-locations.

## Resources

- [Information barriers in Microsoft Teams](/microsoftteams/information-barriers-in-teams)
- [Information barriers in OneDrive](/onedrive/information-barriers)