---
title: "Manage Loop components in SharePoint"
ms.reviewer: tonchan
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.topic: article
ms.collection:
- Strat_SP_admin
- Microsoft 365-collaboration
search.appverid:
- SPO160
- MET150
description: "Learn how to manage Loop components by using PowerShell."
---

# Manage Loop components in SharePoint

Loop experiences on Microsoft 365 OneDrive or SharePoint are backed by .fluid files and powered by Microsoft Fluid Framework. Administrators need to manage access to Loop experiences from SharePoint and not from the Microsoft Teams admin center.

## Loop service requirements

Loop's near real-time communications are enabled by the core services that run a WebSocket server. Coauthors in the same session need to establish secured WebSocket connections to this service to send and receive collaborative data such as changes made by others, live cursors, presence, etc. These experiences are crucial to Loop, and all the scenarios powered by Fluid framework. So, at the minimum, WebSocket will need to be unblocked from the user's endpoint.

Just like other Microsoft 365 experiences, Loop also leverages core services across SharePoint and Microsoft 365. To effectively enable Loop experiences or OneDrive and SharePoint files-backed experiences powered by Fluid Framework, follow the instructions in [Office 365 URLs and IP address ranges](/microsoft-365/enterprise/urls-and-ip-address-ranges) to ensure connections to Loop services.

## Settings management

You'll need the latest version of SharePoint PowerShell module to enable or disable all Loop (powered by the Fluid Framework) experiences across your Microsoft 365 organization. Microsoft Fluid Framework defaults to ON for all organizations. Because Loop components are designed for collaboration, the components are always shared as editable by others, even if your organization is set to default to view-only for other file types. See the Learn more link next to the setting for more details.

|Experience|SharePoint organization properties|Notes|
|---|----|---|
|Loop components in Teams and Outlook|`IsLoopEnabled` (boolean)|This property controls Loop experiences across the Microsoft 365 experience.|
|Microsoft Whiteboard on OneDrive|`IsWBFluidEnabled` (boolean)|This property controls Microsoft Whiteboard on OneDrive.|
|Microsoft OneNote collaborative Meeting notes|`IsCollabMeetingNotesFluidEnabled` (boolean)|This property controls Microsoft OneNote collaborative Meeting notes.|
|**All Microsoft 365 experiences** powered by Fluid Framework.|`IsFluidEnabled` (boolean)|This core property controls all other experiences powered by Fluid Framework. Setting it to `False` will effectively disable all experiences (everything in this table) in the organization powered by Fluid Framework. **Do not use after May - this setting will be deprecated later this year.**|

To check your tenant's default file permissions

1. Go to the [Microsoft 365 admin center](https://admin.microsoft.com).
2. Under Admin centers, select **SharePoint**.
3. Select **Policies** > **Sharing**, and under **File and folder links**, view your organization's default file permissions.

To check if Loop components are enabled, run `Get-SPOTenant` without any arguments. Verify the value of IsLoopEnabled is true.

To enable Loop components, run `Set-SPOTenant -IsLoopEnabled $true`. The change will take a short time to apply across your organization.

The feature will be available on Teams Windows Desktop, Mac, iOS, Android, and web. When enabled, users will see a new option for inserting Loop components in the message compose experience for these clients.

To disable Loop components, run `Set-SPOTenant -IsLoopEnabled $false`. The change will take a short time to apply across your organization.

## Settings management for Outlook

Microsoft is migrating to Cloud Policy as the mechanism to control Loop experiences. This will be phased over time, so both the above SharePoint setting and these Cloud Policy settings should be used to control existing and new integrations. Specifically, Outlook integration will begin checking only the Cloud Policy setting in late 2022.

* Create and view Loop files in Microsoft apps that support Loop
* Create and view Loop files in Outlook

Check the [Cloud Policy](/deployoffice/admincenter/overview-cloud-policy) setting templates for the settings above for more information.

## eDiscovery

Loop components, Whiteboard on OneDrive, and OneNote collaborative Meeting Notes are discoverable but have limited eDiscovery workflow support. Currently, these files are stored in the creator's OneDrive for Business and are available for search and collection in both eDiscovery (Standard) and eDiscovery (Premium). However, they do not render in preview and the export format for review is not consumable by existing tools. To view the exported content, upload them to any OneDrive for Business.

Microsoft is working on an offline consumable export format. In the meantime, if this workaround for review flows is not sufficient for your organization's needs, you can temporarily disable these experiences as outlined in the [Settings management](#settings-management) section.

## Related topics

[Overview of Loop components in Teams](/microsoftteams/live-components-in-teams)
