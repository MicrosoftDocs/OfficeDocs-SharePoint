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
---

# Deploy OneDrive for enterprises

Enterprise deployment guide: Part 3 of 4

Before you read this Part, be sure you’ve read Part 2, [Plan for OneDrive](plan-onedrive-enterprise.md) and taken note of the key decisions needed for deployment. This article walks you through how to deploy OneDrive based on the decisions that you’ve made for your organization.

## Deployment options

For mobile devices running iOS or Android, you can install the OneDrive app manually or deploy by using a mobile device management application such as Intune.

For Windows devices, you can configure syncing manually by walking through OneDrive Setup, or you can centrally deploy the sync client by using scripts or System Center Configuration Manager.

Also, for Windows devices, the OneDrive sync client is included as part of Windows 10 and Office 2016. You do not need to deploy the sync client to devices running these, though you may need to update the sync client to the latest version.

## Deploy and configure OneDrive through Windows AutoPilot

Windows AutoPilot provides a simple way to deliver PCs to users. It is an alternative to the traditional system imaging you typically perform when provisioning a new computer or repurposing an existing computer for a user. Rather than using deployment tools such as System Center Configuration Manager, you can register your hardware information in Azure and use a deployment profile to control the out-of-box experience and register the device in Azure Active Directory (Azure AD).

From there, Intune can deploy apps such as OneDrive to the device automatically. To deliver OneDrive during this process, complete the configuration steps in [Deploy OneDrive by using Intune](#deploy-onedrive-by-using-intune).

For an overview of Windows AutoPilot, see [Overview of Windows AutoPilot](/windows/deployment/windows-autopilot/windows-10-autopilot/).

## Install OneDrive apps and sync clients manually

Although not particularly scalable, you always have the option of installing OneDrive manually on a device. For some devices, this process may be as simple as installing an app. For others, you may need to delete older versions of OneDrive first. This section walks you through the manual installation and configuration of OneDrive on iOS and Android mobile devices, Windows devices, and computers running macOS.

### Manually install and configure OneDrive on a mobile device

Installing the OneDrive app on a mobile device is simple: users can download the app from the app store on any Android, iOS, or Windows mobile device. To simplify the manual installation process even further, users can go to [https://onedrive.live.com/about/download](https://onedrive.live.com/about/download/) and enter the mobile phone number of their device. Microsoft will send a text message to the mobile device with a link to the app in the device’s app store. Once installed, users can start the configuration process by opening the app and responding to the prompts.

Send your users the following links to set up OneDrive on their mobile devices:

-   [Use OneDrive on iOS](https://support.office.com/article/08d5c5b2-ccc6-40eb-a244-fe3597a3c247)

-   [Use OneDrive for Android](https://support.office.com/article/eee1d31c-792d-41d4-8132-f9621b39eb36)

### Manually install and configure OneDrive on a Windows device

Manually installing OneDrive on a Windows device may or may not be necessary: many devices may already have it, either because the user installed Microsoft Office 2016 or simply because the device runs Windows 10, both of which include the OneDrive client by default. For devices running older versions of Windows or on which Office 2016 is not installed, you can download the new OneDrive sync client for Windows from [https://onedrive.live.com/about/download](https://onedrive.live.com/about/download/).

> [!NOTE]
> You may be required to uninstall an old version of the OneDrive sync client before you can install the new one. If so, you will receive a notification stating that you must uninstall the previous version before you can proceed.

To manually configure OneDrive on a Windows device, see [Sync files with the OneDrive sync client in Windows](https://support.office.com/article/615391c4-2bd3-4aae-a42a-858262e42a49).

### Manually install and configure OneDrive on a macOS device

For information about installing the OneDrive app on a computer running macOS or adding a work account to an existing installation, see [Sync files with the OneDrive sync client on Mac OS X](https://support.office.com/article/d11b9f29-00bb-4172-be39-997da46f913f).

## Install OneDrive on Windows devices by using scripting methods

OneDrive is already available in Windows 10 and Office 2016, so if these products are deployed, you probably don’t need to install OneDrive, although you may have to update it. For older versions of Windows that aren’t running Office 2016, start by downloading the new OneDrive sync client for Windows from [https://onedrive.live.com/about/download](https://onedrive.live.com/about/download/).

With the silent account configuration feature, you can configure the OneDrive client by using Group Policy or through scripted registry modification on behalf of a user so that no additional setup is required.

To silently install the OneDrive sync client on an individual computer, run the following command:

\<pathToExecutable\>\\OneDriveSetup.exe /silent

To silently update the OneDrive sync client, run the following command:

\<pathToExecutable\>\\OneDriveSetup.exe /update

For information about enabling silent account configuration, see [Silently configure user accounts](use-silent-account-configuration.md).


## Deploy OneDrive by using Intune

If you’ve decided to deploy the OneDrive sync client by using Intune, follow the procedures in this section.

### Deploy OneDrive to iOS devices by using Intune

To use Intune to deploy OneDrive to iOS devices, follow the steps in [How to add iOS store apps to Microsoft Intune](/intune/store-apps-ios/). When searching for the app in the app store, in the search box, type **Microsoft OneDrive** to find the OneDrive app, as shown below.

![](media/deploy-onedrive-enterprise_image1.png)

When you’ve added the iOS app to Intune, assign it to the group or individuals who should receive it. To do that, follow the steps in [How to assign apps to groups with Microsoft Intune](/intune/apps-deploy/).

### Deploy OneDrive to Android devices by using Intune

To use Intune to deploy OneDrive to Android devices, follow the steps in [How to add Android store apps to Microsoft Intune](/intune/store-apps-android). When configuring the app store URL, type **https://play.google.com/store/apps/details?id=com.microsoft.skydrive**, and then set the minimum operating system to **Android 4.0 (Ice Cream Sandwich)**, as shown below.

![](media/deploy-onedrive-enterprise_image2.png)

After you’ve added the Android app to Intune, assign it to the group or individuals who should receive it. To do that, follow the steps in [How to assign apps to groups with Microsoft Intune](/intune/apps-deploy/).

### Deploy OneDrive to Windows devices by using Intune

To use Intune to deploy OneDrive to Windows devices, complete the steps in [How to assign Office 365 apps to Windows 10 devices with Microsoft Intune](/intune/apps-add-office365/). When configuring the app suite, be sure to select **OneDrive for Business (Next Gen Sync Client)**, as shown below.

![](media/deploy-onedrive-enterprise_image3.png)

> [!NOTE]
> You aren’t required to deploy the entire Office 365 suite at once. If you need the OneDrive sync client only, you can select that one item.

## Deploy OneDrive by using System Center Configuration Manager


If you’ve decided to deploy the OneDrive sync client by using System Center Configuration Manager, follow the procedures in this section.

### Mobile devices running iOS or Android

You can use System Center Configuration Manager to deploy apps to mobile devices. Before you do, however, you need to complete a few prerequisite steps because integration with Intune is required to manage mobile devices in System Center Configuration Manager. For information about managing mobile devices with System Center Configuration Manager and Intune, see [Manage Mobile Devices with Configuration Manager and Microsoft Intune](https://technet.microsoft.com/library/jj884158.aspx).

To deploy OneDrive to an iOS device, see [Create iOS applications with System Center Configuration Manager](/sccm/mdm/deploy-use/creating-ios-applications/), and use https://itunes.apple.com/us/app/onedrive/id823766827?mt=12 as the app location, as shown below.

![](media/deploy-onedrive-enterprise_image4.png)

To deploy OneDrive to an Android device, see [Create Android applications with System Center Configuration Manager](/sccm/mdm/deploy-use/creating-android-applications/), and use https://play.google.com/store/apps/details?id=com.microsoft.skydrive&hl=en as the app location, as shown below.

![](media/deploy-onedrive-enterprise_image5.png)

### Windows devices

Windows 10 devices come with the OneDrive sync client installed. Office 2016 and later installations also have the sync client installed. If you’re deploying OneDrive to devices running an earlier version of Windows or on which you haven’t installed Office 2016, see [Deploy the new OneDrive sync client in Windows](deploy-on-windows.md) for a sample System Center Configuration Manager package that contains the OneDrive sync client. You can use this sample application as a starting point for your deployment.

The sample .zip file contains the script installer deployment type that you’ll use to deploy the OneDrive client to Windows devices. Import the .zip file by going to Software Library\\Application Management, right-clicking **Applications**, and then selecting **Import Application**, as shown below. The only thing left to do after importing the .zip file is deploy it to the target computers.

![](media/deploy-onedrive-enterprise_image6.png)

> [!NOTE]
> The script installer deployment type already has a detection method script and will correctly assess the installation. Also, there is an uninstall switch, which means that you can easily remove the OneDrive client, if necessary.

For more information about packages and programs in System Center Configuration Manager, see [Packages and programs in System Center Configuration Manager](/sccm/apps/deploy-use/packages-and-programs/).

### Computers running macOS

Before you can deploy applications to computers running macOS, you need to complete some prerequisite tasks on the System Center Configuration Manager site. For detailed information about these prerequisites and how to prepare a System Center Configuration Manager environment for Mac management, see [Prepare to deploy client software to Macs](/sccm/core/clients/deploy/prepare-to-deploy-mac-clients/). When you’ve completed the prerequisites, you can deploy applications to Macs by completing the steps described in [How to Create and Deploy Applications for Mac Computers in Configuration Manager](/previous-versions/system-center/system-center-2012-R2/jj884158(v%3dtechnet.10)/).

To learn about managing OneDrive, see Part 4 in the Enterprise deployment guide, [Manage OneDrive](manage-onedrive.md).



