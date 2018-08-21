---
title: Manage OneDrive
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: one-drive
localization_priority: Normal
description: "Learn how to manage OneDrive in an an enterprise."
---

# Manage OneDrive

Enterprise deployment guide: Part 4 of 4

The tools and technologies you use to manage OneDrive are based on the individual management task you want to perform. The following table shows the three primary categories to consider when managing OneDrive and the technologies and methods available for that category.


|**Category**|**Tasks**|**Technology or method**|
|:-----|:-----|:-----|
|OneDrive organization-wide settings|Manage settings such as storage limits and sharing capabilities.|OneDrive admin center<br>Microsoft PowerShell|
|App updates|Update the OneDrive sync client or mobile apps|MDM (for example, Intune)<br>System Center Configuration Manager<br>Group Policy<br>OneDrive admin center<br>Manually|
|Sync client settings|Configure the sync client update ring, DLP policies, and other device or app restrictions.|MDM (for example, Intune)<br>System Center Configuration Manager<br>Group Policy<br>Manually|

## Manage OneDrive by using the OneDrive admin center

The OneDrive admin center [https://admin.onedrive.com](https://admin.onedrive.com) in Office 365 enables you to manage OneDrive settings and device access from one central location. Some settings in the OneDrive admin center you’ll use regardless of any other technologies you use to manage OneDrive (for example, to configure storage space settings). Others may overlap management apps in use (for example, the MDM section). Most organizations will use the OneDrive admin center for some of their settings, but only those organizations without an MDM application would likely use the device access functionality in the OneDrive admin center.

For more info about the admin center, see [OneDrive for Business for admins](onedrive.md)

Settings in the OneDrive admin center are grouped into six categories:

-   **Sharing** - On the **Sharing** tab, you can configure the default sharing link users send out to colleagues to share a file as well as external sharing settings. These settings are organization-wide and applicable to all organizations, regardless of the device management tool in use. Use this page to configure the sharing option based on the sharing decisions you made in Part 2, [Plan for OneDrive for enterprises](plan-onedrive-enterprise.md).

-   **Sync** - On the **Sync** tab, you can configure sync restrictions based on file types, require that synced devices be domain joined, or restrict synchronization from computers running macOS. Depending on your device management tool, the PC device restrictions in this section may overlap other management settings.

-   **Storage** - On the **Storage** tab, you specify the default OneDrive storage limit for users within your Office 365 organization. You can also configure data retention settings for users whose accounts have been deleted (the maximum value is 10 years). These organization-wide configuration settings are applicable to all organizations, regardless of the device management tool they use. Use this page to configure the data retention value based on the decisions you made in Part 2, [Plan for OneDrive for enterprises](plan-onedrive-enterprise.md).

-   **Device Access** - On the **Device Access** tab, you can restrict device access to OneDrive based on network location and apps that don’t use modern authentication among other application management options. Depending on your device management tool, the restrictions configurable on this tab may overlap with other management settings. If a conflict occurs with an Intune policy, for example, the Intune policy will take precedence for the users that policy targets.

-   **Compliance** - The **Compliance** tab provides a centralized list of links to auditing, DLP, retention, ediscovery, and alerting capabilities within Office 365 that are applicable to OneDrive. Selecting an item’s link redirects you to the Office 365 Security & Compliance Center, where you can configure that item. You can create DLP policies from templates that protect certain types of data, such as Social Security numbers, banking information, and other financial and medical content. Some capabilities won’t be available if you’re using Intune (for example, device management). For a walkthrough of how to create DLP policies in Office 365 and apply them to OneDrive, see [Create a DLP policy from a template](https://support.office.com/article/59414438-99f5-488b-975c-5023f2254369).

-   **Notifications** - On the **Notifications** tab, you define when OneDrive owners should receive notifications about sharing or accessing their data. For information about enabling these options, see [Turn on external sharing notifications for OneDrive for Business](turn-on-external-sharing-notifications.md).


## Manage OneDrive by using an MDM application

You can use MDM solutions such as Intune to manage OneDrive settings. 

### Manage OneDrive settings by using Intune

Unlike Windows, OneDrive doesn’t have a configuration service provider. Therefore, to use Intune to configure OneDrive settings, you must deploy the setting’s corresponding registry key and value by using a PowerShell cmdlet. Read [Use Group Policy to control OneDrive sync client settings](https://support.office.com/article/use-group-policy-to-control-onedrive-sync-client-settings-0ecb2cf5-8882-42b3-a6e9-be6bda30899c) for a list of settings and their corresponding registry values; then, construct a PowerShell script using the following cmdlet syntax:

```PowerShell
New-ItemProperty -Path \$Path -Name \$Name -Value \$Value -PropertyType DWORD -Force | Out-Null
```

where \$Path is the full path to the subkey to which you want to add a value to (for example, **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\OneDrive**), \$Name is the name of the value you’re adding (for example, **AutomaticUploadBandwidthPercentage**), \$Value is the data within the new value (for example, **32**), and the value following the PropertyType switch is the type of value you’re adding.

Save the PowerShell script as a .ps1 file. Then, see [Manage PowerShell scripts in Intune for Windows 10 devices](https://docs.microsoft.com/intune/intune-management-extension) for instructions on how to deploy the PowerShell script in your environment.

### Manage OneDrive updates by using Intune

OneDrive is updated through Windows Update in two waves. Out of the box, OneDrive sync clients are in the first wave, which means that they receive updates as soon as they’re published. The second wave receives those same updates several weeks later. To configure Windows devices to be in the second wave, you must configure the **EnableEnterpriseUpdate** entry by using the following command:

```PowerShell
New-ItemProperty -Path 'HKCU:\\SOFTWARE\\Microsoft\\OneDrive' -Name 'EnableEnterpriseUpdate' -Value '1' -PropertyType DWORD -Force | Out-Null
```

Save the script as a .ps1 file. Then, see [Manage PowerShell scripts in Intune for Windows 10 devices](https://docs.microsoft.com/intune/intune-management-extension) for instructions on how to deploy the PowerShell script in your environment.

### Manage OneDrive by using third-party MDM tools

Intune isn’t the only MDM option you can use to manage OneDrive apps and settings. For information about managing OneDrive for Windows 10 by using VMware AirWatch, see [Modern Management for Windows 10](https://www.air-watch.com/solutions/windows-10-management/). For information about managing OneDrive for Windows 10 by using MobileIron, see [Windows 10 in the Enterprise](https://www.mobileiron.com/solutions/multi-os-management/windows-10).

## Manage OneDrive by using Group Policy

You can use Group Policy to manage OneDrive settings for domain-joined machines in your environment. For information, see [Use Group Policy to control OneDrive sync client settings](use-group-policy.md). Using Group Policy, you can [redirect and move Windows known folders to OneDrive](redirect-known-folders.md), [enable silent account configuration](use-silent-account-configuration.md),  [configure the maximum size that will be downloaded automatically](use-group-policy.md#configure-the-maximum-onedrive-size-for-downloading-all-files-automatically), and much more. 


## Manage OneDrive by using System Center Configuration Manager

Because Windows devices that you use System Center Configuration Manager to manage are either domain joined (and therefore managed in Active Directory) or administered through Intune, the role of System Center Configuration Manager in managing OneDrive settings is limited. When using System Center Configuration Manager to manage OneDrive, Microsoft recommends using either Group Policy or Intune, depending on whether the device is domain joined. For information about how to use Group Policy to manage OneDrive settings, see [Manage OneDrive settings by using GPOs](#_Manage_OneDrive_settings).

System Center Configuration Manager can manage OneDrive updates and configuration alongside other updates in your environment, such as for Windows and Office applications. 

#### Manage OneDrive updates by using System Center Configuration Manager

Depending on where the OneDrive client originated—as part of an Office package, Windows 10, or as a stand-alone installation—there are two primary methods for using System Center Configuration Manager to manage OneDrive updates:

-   **Traditional updates managed through Windows Service Update Services (WSUS).** OneDrive product updates are downloaded to WSUS, and you can manage them alongside your Windows and Office updates. For information about how to configure System Center Configuration Manager with WSUS, see [Install and configure a software update point](https://docs.microsoft.com/sccm/sum/get-started/install-a-software-update-point).

-   **Single-instance updates.** If you want to perform an ad hoc update of the OneDrive sync client on a Windows device, start by downloading the updated OneDrive sync client from [OneDrive for Windows](https://onedrive.live.com/about/download). This method is typically applicable only for older installations of Office running on devices with a Windows version earlier than Windows 10 that are not updating OneDrive as part of their other updates.

    Once downloaded, you can create a script in System Center Configuration Manager by following the process in [Create and run PowerShell scripts from the Configuration Manager Console](https://docs.microsoft.com/sccm/apps/deploy-use/create-deploy-scripts) or by using a traditional script-based application such as that in [Create applications with System Center Configuration Manager](https://docs.microsoft.com/sccm/apps/deploy-use/create-applications). When using either option, the command to update the OneDrive client using the installer is:

> Execute \<pathToExecutable\>\\OneDriveSetup.exe /update /restart


