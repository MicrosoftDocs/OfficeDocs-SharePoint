---
title: Deploy OneDrive
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: one-drive
localization_priority: Normal
description: "Learn how to deploy OneDrive in an an enterprise."
...

# Deploy OneDrive for enterprises

Before you read this article, be sure you’ve read Plan for OneDrive and taken note of the key decisions needed for deployment. This article walks you through how to deploy OneDrive based on the decisions that you’ve made for your organization.

## Configure your infrastructure

Before you configure OneDrive, configure your infrastructure:

-   Read *Network utilization* to measure your OneDrive network utilization and create policies to control throughput.

-   If you’ve decided to deploy OneDrive Multi-Geo or hybrid, read the related sections below to learn how to configure these options.

### Network utilization

Before you roll out OneDrive to your organization, it’s important to assess your network bandwidth needs to support it. The basic recommended steps are:

1.  Assess the number of users and computers per user to which you'll deploy the sync client.

2.  Assess the available bandwidth and network conditions.

3.  Measure the network utilization of the sync client for a pilot group during each sync state.

4.  Create policies to control sync throughput as necessary.

The article [Network utilization planning for the OneDrive sync client](https://docs.microsoft.com/onedrive/network-utilization-planning) includes the details around how to carry out these steps.

### Multi-geo

If you plan to configure OneDrive Multi-Geo prior to deploying OneDrive for your users, read [Plan for OneDrive for Business Multi-Geo](https://docs.microsoft.com/office365/enterprise/plan-for-multi-geo) and follow the steps in [OneDrive for Business Multi-Geo tenant configuration](https://docs.microsoft.com/office365/enterprise/multi-geo-tenant-configuration). Once you’ve configured your allowed data locations and set the appropriate preferred data location for each of your users, they can begin using OneDrive and their OneDrive will be deployed in the correct geo-location.

If you plan to start using OneDrive before you configure OneDrive Multi-Geo, keep in mind that each user’s OneDrive will be deployed to the central location for your Office 365 subscription. If in the future you need to move a user’s OneDrive to a different geo location, follow the steps in [Move a OneDrive site to a different geo-location](https://docs.microsoft.com/office365/enterprise/move-onedrive-between-geo-locations).

### Hybrid

If you plan to deploy hybrid OneDrive, read [Plan hybrid OneDrive for Business](https://docs.microsoft.com/sharepoint/hybrid/plan-hybrid-onedrive-for-business), and then follow the [Configure hybrid OneDrive for Business roadmap](https://docs.microsoft.com/sharepoint/hybrid/configure-hybrid-onedrive-for-businessroadmap).

If your users have files in OneDrive in SharePoint Server on-premises, be sure that you have a migration plan for this data before you configure hybrid OneDrive. See Migrate data later in this article for migration options.

Keep in mind that once you configure hybrid OneDrive, the OneDrive navigation links in SharePoint Server on-premises will point to OneDrive in Office 365. We recommend that you have your users bookmark the URL to their on-premises OneDrive in case they need to return to it after hybrid OneDrive has been configured.

Once you’ve migrated your users’ files from on-premises OneDrive and configured hybrid OneDrive, you can reduce the quota for your on-premises OneDrive top-level site collection to a minimal value to save disk space.

### Configure data governance and security

Once you have your infrastructure configured, the next step is to configure any data governance and security policies that you decided on in the planning phase.

### Information rights management–protected file synchronization

If you currently use or plan to use IRM-protected files, see [SharePoint Online and OneDrive for Business: IRM Configuration](https://docs.microsoft.com/information-protection/deploy-use/configure-office365#sharepoint-online-and-onedrive-for-business-irm-configuration) for the configuration steps needed.

You must also deploy the latest [Rights Management Services (RMS) client](https://www.microsoft.com/en-us/download/details.aspx?id=38396) to your users’ computers.

### Windows Information Protection

If you’ve decided to use Windows Information Protection with OneDrive, see the following resources to set up your Windows Information Protection policies:

-   [Create a Windows Information Protection (WIP) policy using Microsoft Intune](https://docs.microsoft.com/windows/security/information-protection/windows-information-protection/overview-create-wip-policy)

-   [Create a Windows Information Protection (WIP) policy using System Center Configuration Manager](https://docs.microsoft.com/windows/security/information-protection/windows-information-protection/overview-create-wip-policy-sccm)

### Azure Information Protection

If you have decided to use Azure Information Protection, see [Office 365: Configuration for clients and online services to use the Azure Rights Management service](https://docs.microsoft.com/azure/information-protection/deploy-use/configure-office365#sharepoint-online-and-onedrive-for-business-irm-configuration)[](https://docs.microsoft.com/information-protection/deploy-use/configure-office365#sharepoint-online-and-onedrive-for-business-irm-configuration) to configure the necessary settings for it to work with OneDrive.

### Sharing options

Based on the sharing decisions you made during the planning phase, go to the [OneDrive admin center](https://admin.onedrive.com) and configure your sharing options.

In the **External sharing** section, choose one of the following settings:

-   **Anyone** – if you want users to be able to create sharable links to files and folders that can be used by anyone without authentication.

-   **New and existing external users** – if you want to require authentication from external users when files and folders are shared with them.

-   **Existing external users** – if you only want to allow sharing with external users who have been added to your directory.

-   **Only people in your organization** – if you don’t want to allow external sharing at all.

Remember that the sharing permissions for SharePoint Online must be at least as permissive as the settings for OneDrive.

After you have selected your external sharing setting, in the **Links** section, choose a default link type. (Options will vary depending on your sharing settings.) This is the default option that users will see when they share, though they can change it at the time of sharing if they want.

### Data retention

Set the data retention policy that you decided on in the planning phase:

In the [OneDrive admin center](https://admin.onedrive.com/), and click the **Storage** tab and set a value between 0 days and 3650 days (ten years) for the days to retain files in OneDrive after an account is marked for deletion.

## Migrate data

Once you’ve finished setting up your governance policies, it’s time to migrate your user’s data. Follow the sections below based on the migration decisions that you made in the planning phase.

### Migrating with FastTrack

If you have decided to take advantage of Microsoft FastTrack, visit [FastTrack](https://fasttrack.microsoft.com/) to review resources and submit a Request for Assistance.

### Hybrid

If you’re migrating from OneDrive in SharePoint Server on-premises and configuring hybrid OneDrive, be sure to read the hybrid section in this article and also in Plan for OneDrive for important considerations around the migration phase.

### Migrating data from on-premises SharePoint Server

If you're migrating data from on-premises SharePoint, then you should use the SharePoint Migration Tool. See [How to use the SharePoint Migration Tool](https://docs.microsoft.com/sharepointmigration/how-to-use-the-sharepoint-migration-tool) to get started.

If your users have not yet started using OneDrive in Office 365, then they likely do not yet have a OneDrive site that you can migrate to. In this case, you must pre-provision each user's OneDrive. See [Pre-provision OneDrive for users in your organization](https://support.office.com/article/ceef6623-f54f-404d-8ee3-3ce1e338db07) to get started.

### Migrating data in Known Folders

If your users have thier files stored in Known Folders (deskotp, Documents, etc.) and you want to redirect Known Folders to OneDrive, you can do so by configuring this in Group Policy. Go get started, see [Redirect and move Windows known folders to OneDrive](redirect-known-folders.md)

If your users have already installed the OneDrive sync client and they're using OneDrive, they can set up Known Folders Move themselves by following the instructions in [Protect your files by saving them to OneDrive](https://support.office.com/article/d61a7930-a6fb-4b95-b28a-6552e77c3057)

### Migrating data in unknown folders

If you’ve chosen to have your users migrate their own files by copying them to OneDrive through the web interface or a synced folder on their local disk, we recommend including basic instructions around how to do this and how to get assistance when you communicate your migration plan.

## Deploy the OneDrive sync client

The procedures in this section guide you through how to deploy the OneDrive sync client based on the decisions that you made in the planning phase.

### Sync client update process

If you’re planning to use the Production ring for updating the OneDrive sync client, then no action is needed – that’s the default ring.

If you want to use the Enterprise ring, you must configure this by enabling the **Delay updating OneDrive.exe until the second release wave** group policy. For information about configuring the OneDrive sync client by using group policy, see [Use Group Policy to control OneDrive sync client settings](https://support.office.com/article/0ecb2cf5-8882-42b3-a6e9-be6bda30899c).

For details about the update process, see [The OneDrive sync client update process](https://support.office.com/article/the-onedrive-sync-client-update-process-2f748bc6-6f01-4406-a791-ec047f066d6d).

### Upgrade from the Groove sync client to the OneDrive sync client

If you currently have the old OneDrive sync client (Groove.exe), then you’ll need to follow a slightly different process to upgrade to the new sync client. If you had more than 250 licensed users before June 2016, you may need to run a takeover command to continue syncing existing libraries using the new client. For detailed information about this process (and caveats), see [Transition from the previous OneDrive for business sync client](https://support.office.com/article/transition-from-the-previous-onedrive-for-business-sync-client-4100df3a-0c96-464f-b0a8-c20de34da6fa).

### Deploy the OneDrive sync client by using Intune

If you’ve decided to deploy the OneDrive sync client by using Intune, follow the procedures in this section.

### Deploy OneDrive to iOS devices by using Intune

To use Intune to deploy OneDrive to iOS devices, complete the steps in [How to add iOS store apps to Microsoft Intune](https://docs.microsoft.com/intune/store-apps-ios). When searching for the app in the app store, in the search box, type **Microsoft OneDrive** to find the OneDrive app, as shown below.

![](media/deploy-onedrive-enterprise_image1.png)

When you’ve added the iOS app to Intune, assign it to the group or individuals who should receive it. To do that, complete the steps in [How to assign apps to groups with Microsoft Intune](https://docs.microsoft.com/intune/apps-deploy).

### Deploy OneDrive to Android devices by using Intune

To use Intune to deploy OneDrive to Android devices, complete the steps in [How to add Android store apps to Microsoft Intune](https://docs.microsoft.com/intune/store-apps-android). When configuring the app store URL, type **https://play.google.com/store/apps/details?id=com.microsoft.skydrive**, and then set the minimum operating system to **Android 4.0 (Ice Cream Sandwich)**, as shown below.

![](media/deploy-onedrive-enterprise_image2.png)

After you’ve added the Android app to Intune, assign it to the group or individuals who should receive it. To do that, complete the steps in [How to assign apps to groups with Microsoft Intune](https://docs.microsoft.com/intune/apps-deploy).

### Deploy OneDrive to Windows devices by using Intune

To use Intune to deploy OneDrive to Windows devices, complete the steps in [How to assign Office 365 apps to Windows 10 devices with Microsoft Intune](https://docs.microsoft.com/intune/apps-add-office365). When configuring the app suite, be sure to select **OneDrive for Business (Next Gen Sync Client)**, as shown below.

![](media/deploy-onedrive-enterprise_image3.png)

> [!NOTE]
> You aren’t required to deploy the entire Office 365 suite at once. If you need the OneDrive sync client only, you can select that one item.

### Deploy OneDrive by using System Center Configuration Manager
<span id="_Hlk509358526" class="anchor"></span>

If you’ve decided to deploy the OneDrive sync client by using System Center Configuration Manager, follow the procedures in this section.

### Mobile devices running iOS or Android

You can use System Center Configuration Manager to deploy apps to mobile devices. Before you do, however, you need to complete a few prerequisite steps because integration with Intune is required to manage mobile devices in System Center Configuration Manager. For information about managing mobile devices with System Center Configuration Manager and Intune, see [Manage Mobile Devices with Configuration Manager and Microsoft Intune](https://technet.microsoft.com/library/jj884158.aspx).

To deploy OneDrive to an iOS device, see [Create iOS applications with System Center Configuration Manager](https://docs.microsoft.com/en-us/sccm/mdm/deploy-use/creating-ios-applications), and use https://itunes.apple.com/us/app/onedrive/id823766827?mt=12 as the app location, as shown in Figure 14.

![](media/deploy-onedrive-enterprise_image4.png)

To deploy OneDrive to an Android device, see [Create Android applications with System Center Configuration Manager](https://docs.microsoft.com/sccm/mdm/deploy-use/creating-android-applications), and use https://play.google.com/store/apps/details?id=com.microsoft.skydrive&hl=en as the app location, as shown in Figure 15.

![](media/deploy-onedrive-enterprise_image5.png)

### Windows devices

Windows 10 devices come with the OneDrive sync client installed. Office 2016 and later installations also have the sync client installed. If you’re deploying OneDrive to devices running an earlier version of Windows or on which you haven’t installed Office 2016, see [Deploy the new OneDrive sync client in Windows](https://support.office.com/article/deploy-the-new-onedrive-sync-client-in-an-enterprise-environment-3f3a511c-30c6-404a-98bf-76f95c519668) for a sample System Center Configuration Manager package that contains the OneDrive sync client. You can use this sample application as a starting point for your deployment.

The sample .zip file contains the script installer deployment type that you’ll use to deploy the OneDrive client to Windows devices. Import the .zip file by going to Software Library\\Application Management, right-clicking **Applications**, and then selecting **Import Application**, as shown in Figure 16. The only thing left to do after importing the .zip file is deploy it to the target computers.

![](media/deploy-onedrive-enterprise_image6.png)

> [!NOTE]
> The script installer deployment type already has a detection method script and will correctly assess the installation. Also, there is an uninstall switch, which means that you can easily remove the OneDrive client, if necessary.

For more information about packages and programs in System Center Configuration Manager, see [Packages and programs in System Center Configuration Manager](https://docs.microsoft.com/sccm/apps/deploy-use/packages-and-programs).

### Computers running macOS

Before you can deploy applications to computers running macOS, you need to complete some prerequisite tasks on the System Center Configuration Manager site. For detailed information about these prerequisites and how to prepare a System Center Configuration Manager environment for Mac management, see [Prepare to deploy client software to Macs](https://docs.microsoft.com/sccm/core/clients/deploy/prepare-to-deploy-mac-clients). When you’ve completed the prerequisites, you can deploy applications to Macs by completing the steps described in [How to Create and Deploy Applications for Mac Computers in Configuration Manager](https://technet.microsoft.com/en-us/library/jj687950.aspx).

### Install OneDrive on Windows devices by using scripting methods

OneDrive is already available in Windows 10 and Office 2016, so if these products are deployed, you probably don’t need to install OneDrive, although you may have to update it. For older versions of Windows that aren’t running Office 2016, start by downloading the new OneDrive sync client for Windows from [https://onedrive.live.com/about/download](https://onedrive.live.com/about/download/).

With the silent account configuration feature, you can configure the OneDrive client by using Group Policy or through scripted registry modification on behalf of a user so that no additional setup is required.

To silently install the OneDrive sync client on an individual computer, run the following command:

\<pathToExecutable\>\\OneDriveSetup.exe /silent

To silently update the OneDrive sync client, run the following command:

\<pathToExecutable\>\\OneDriveSetup.exe /update

For more information about silently installing the OneDrive sync client on computers across your organization, see [Silently deploy and configure the OneDrive sync client in your enterprise](https://support.office.com/article/64aa1f56-d7f6-4500-a408-1fde8fe6db36).

### Install the OneDrive sync client manually

Although not particularly scalable, you always have the option of Installing OneDrive manually on a device. For some devices, this process may be as simple as installing an app. For others, you may need to delete older versions of OneDrive first. This section walks you through the manual installation and configuration of OneDrive on iOS and Android mobile devices, Windows devices, and computers running macOS.

### <span id="_Manually_install_and" class="anchor"><span id="_Hlk511511158" class="anchor"></span></span>Manually install and configure OneDrive on a mobile device

Have your users install manually

Installing the OneDrive app on a mobile device is simple: users can download the app from the app store on any Android, iOS, or Windows mobile device. To simplify the manual installation process even further, users can go to [https://onedrive.live.com/about/download](https://onedrive.live.com/about/download/) and enter the mobile phone number of their device. Microsoft will send a text message to the mobile device with a link to the app in the device’s app store. Once installed, users can start the configuration process by opening the app and responding to the prompts.

Send your users the following links to set up OneDrive on their mobile devices:

-   [Use OneDrive on iOS](https://support.office.com/article/use-onedrive-on-ios-08d5c5b2-ccc6-40eb-a244-fe3597a3c247)

-   [Use OneDrive for Android](https://support.office.com/article/Use-OneDrive-for-Android-eee1d31c-792d-41d4-8132-f9621b39eb36)

### <span id="_Manually_install_OneDrive" class="anchor"><span id="_Hlk511394696" class="anchor"></span></span>Manually install and configure OneDrive on a Windows device

Manually installing OneDrive on a Windows device may or may not be necessary: many devices may already have it, either because the user installed Microsoft Office 2016 or simply because the device runs Windows 10, both of which include the OneDrive client by default. For devices running older versions of Windows or on which Office 2016 is not installed, you can download the new OneDrive sync client for Windows from [https://onedrive.live.com/about/download](https://onedrive.live.com/about/download/).

> [!NOTE]
> You may be required to uninstall an old version of the OneDrive sync client before you can install the new one. If so, you will receive a notification stating that you must uninstall the previous version before you can proceed.

To manually configure OneDrive on a Windows device, see [Sync files with the OneDrive sync client in Windows](https://support.office.com/article/sync-files-with-the-onedrive-sync-client-in-windows-615391c4-2bd3-4aae-a42a-858262e42a49).

### Manually install and configure OneDrive on a macOS device

For information about installing the OneDrive app on a computer running macOS or adding a work account to an existing installation, see [Sync files with the OneDrive sync client on Mac OS X](https://support.office.com/article/sync-files-with-the-onedrive-sync-client-on-mac-os-x-d11b9f29-00bb-4172-be39-997da46f913f?ui=en-US&rs=en-US&ad=US).
