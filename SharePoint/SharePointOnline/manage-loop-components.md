---
ms.date: 01/31/2022
title: "Manage Loop experiences (Loop app and Loop components) in SharePoint"
ms.reviewer: dancost, tonchan
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
- Tier3
search.appverid:
- SPO160
- MET150
description: "Learn how to manage Loop experiences (Loop app and Loop components) by using PowerShell and Cloud Policy."
---

# Manage Loop experiences (Loop app and Loop components) in SharePoint

Loop experiences on Microsoft 365 OneDrive or SharePoint are backed by .fluid or .loop files. IT admins need to manage access to Loop experiences from **BOTH**:
1. Cloud Policy
2. SharePoint PowerShell command

## Available policy settings

There are several IT Admin settings provided to enable the Loop app and Loop experiences across Microsoft 365:

|Configure|Setting Type|Specific Policy|Notes
|---|---|---|---|
|Loop app|Cloud Policy, Primary|**Create and view Loop files in Loop**|*Loop app only checks the setting in this row|
|Loop experiences across Microsoft 365*|Cloud Policy, Primary|**Create and view Loop files in Microsoft apps that support Loop**|Applies to:<br/>- Outlook integration<br/>- Word for the web integration<br/>- Whiteboard integration<br/>Does NOT apply to:<br/>- Loop app<br/>- Teams integration|
|Outlook integration of Loop experiences|Cloud Policy, Secondary|**Create and view Loop files in Outlook**|First checks **Create and view Loop files in Microsoft apps that support Loop**, then applies **Create and view Loop files in Outlook** if applicable|
|Teams integration|SharePoint property, Primary|See [Settings management for Loop components in Teams](#settings-management-for-loop-functionality-in-teams)|*Teams only checks the setting in this row|

## Settings management in Cloud Policy

The Loop experiences (except for Microsoft Teams) check the following Cloud Policy settings. See [Available policy settings](#available-policy-settings) to understand how each app checks these settings:

- **Create and view Loop files in Microsoft apps that support Loop**
- **Create and view Loop files in Outlook**
- **Create and view Loop files in Loop**

See the [Cloud Policy](/deployoffice/admincenter/overview-cloud-policy) setting templates for more information on the settings above.

To configure these Cloud Policy settings:
1. Sign in to https://config.office.com/ with your Microsoft 365 admin credentials.
2. Select **Customization** from the left pane.
3. Select **Policy Management**.
4. Create a new policy configuration or edit an existing one.
5. In **Choose the scope**, choose the security group for which you want to apply the policy.
    - **Note**: you MUST FIRST create a security group that defines which users in your organization this policy will apply to. You can [learn more about creating groups in the Microsoft 365 admin center](/microsoft-365/admin/email/create-edit-or-delete-a-security-group) or creating dynamic groups in AzureAD [here](/azure/active-directory/external-identities/use-dynamic-groups). If you do not create a group, the settings you configure will not apply to your users.
6. In **Configure Settings**, choose one of the settings listed at the top of this section.
7. In configuration setting, choose one of the following:
    - For **Create and view Loop files in Microsoft apps that support Loop**
        - **Enabled**: Loop experience is available to users.
        - **Disabled**: Loop experience is NOT available to users.
        - **Not configured**: Loop experience is available to users.
    - For **Create and view Loop files in Outlook**
        - **Enabled**: Loop experience is available to users.
        - **Disabled**: Loop experience is NOT available to users.
        - **Not configured**: Loop experience is available to users.
    - For **Create and view Loop files in Loop**
        - **Enabled**: Loop app is available to users.
        - **Disabled**: Loop app is NOT available to users.
        - **Not configured**: Loop app is NOT available to users. (Loop during Public Preview is Opt-in by default)
8. Save the policy configuration.
9. Reassign priority for any security group if required. (If two or more policy configurations are applicable to the same set of users, the one with the higher priority is applied.)
10. In case you create a new policy configuration or change the configuration for an existing policy, there will be a delay in the change being reflected as follows:
    - If there were existing policy configurations prior to the change, then it will take 90 mins for the change to be reflected.
    - If there were no policy configurations prior to the change then it will take 24 hours for the change to be reflected.

## Settings management for Loop functionality in Teams

You'll need the latest version of SharePoint PowerShell module to enable or disable Loop experiences in Teams. Loop components default to ON for all organizations. Because Loop components are designed for collaboration, the components are always shared as editable by others, even if your organization is set to default to view-only for other file types. See the Learn more link next to the setting for more details.

|Experience|SharePoint organization properties|Notes|
|---|----|---|
|Loop components in Teams|`IsLoopEnabled` (boolean)|This property controls Loop experiences in Microsoft Teams. |
|Collaborative meeting notes|`IsCollabMeetingNotesFluidEnabled` (boolean)|This property controls the collaborative meeting notes integration in Microsoft Teams.|

To check your tenant's default file permissions

1. Go to the [Microsoft 365 admin center](https://admin.microsoft.com).
2. Under Admin centers, select **SharePoint**.
3. Select **Policies** > **Sharing**, and under **File and folder links**, view your organization's default file permissions.

To check if Loop components are enabled, run `Get-SPOTenant` without any arguments. Verify the value of IsLoopEnabled is true.

To enable Loop components in Teams, run `Set-SPOTenant -IsLoopEnabled $true`. The change will take a short time to apply across your organization.

The feature will be available on Teams Windows Desktop, Mac, iOS, Android, and web. When enabled, users will see a new option for inserting Loop components in the message compose experience for these clients.

To disable Loop components in Teams, run `Set-SPOTenant -IsLoopEnabled $false`. The change will take a short time to apply across your organization. If your organization has multiple regions (that is, organization URLs), you need to disable loop components for all the regions to have consistent results across the organization.

## Loop service requirements

Loop's near real-time communications are enabled by the core services that run a WebSocket server. Coauthors in the same session need to establish secured WebSocket connections to this service to send and receive collaborative data such as changes made by others, live cursors, presence, etc. These experiences are crucial to Loop, and all the scenarios powered by Fluid framework. So, at the minimum, WebSocket will need to be unblocked from the user's endpoint.

Just like other Microsoft 365 experiences, Loop also leverages core services across SharePoint and Microsoft 365. To effectively enable Loop experiences or OneDrive and SharePoint files-backed experiences powered by Fluid Framework, follow the instructions in [Office 365 URLs and IP address ranges](/microsoft-365/enterprise/urls-and-ip-address-ranges) to ensure connections to Loop services.

## eDiscovery

Loop components created in Teams or Outlook are discoverable and have eDiscovery workflow support using the Microsoft Purview tool. Currently, these files are stored in the creator’s OneDrive for Business and are available for search and collection, and render in review for both eDiscovery (Standard) and eDiscovery (Premium). The HTML offline export format is supported on eDiscovery (Premium). You can also download and re-upload the files to any OneDrive for Business to view them in their native format.

Microsoft is currently working on a third-party export API solution for Loop components.

The Loop app does not yet support eDiscovery workflows.

## Related topics

- [Overview of Loop components in Teams](/microsoftteams/live-components-in-teams)
- [Use Loop components in Outlook](https://support.microsoft.com/office/9b47c279-011d-4042-bd7f-8bbfca0cb136)
