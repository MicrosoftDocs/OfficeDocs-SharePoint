---
title: "Deploy OneDrive apps using Intune"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: get-started-article
ms.service: one-drive
localization_priority: Priority
ms.collection: Strat_OD_admin
search.appverid:
- MET150
- ODB160
- MOE150
- MED150
- MBS150
- ODB150
ms.assetid: 3f3a511c-30c6-404a-98bf-76f95c519668
description: "Learn how to deploy OneDrive apps by using Intune."
---

# Deploy OneDrive apps by using Intune

You can use Intune to deploy the mobile apps for iOS and Android and to deploy the new OneDrive sync client (OneDrive.exe). Before you begin deploying, make sure you have reviewed the planning information and deployment options in the [OneDrive guide for enterprises](plan-onedrive-enterprise.md).

### Deploy OneDrive to iOS devices by using Intune

1. Create a group of devices or users to target the deployment in Azure AD.
2. Select **Mobile apps** and **Apps**.
3. Under **App type**, select **iOS**.
4. Select **Search the App Store**.
5. In the search box, enter **Microsoft OneDrive** to find the OneDrive app, as shown below.

![](media/deploy-onedrive-enterprise_image1.png)


6. Under **Assignments**, choose the group you created. For info about this, see [How to assign apps to groups with Microsoft Intune](/intune/apps-deploy/).

For more info about using Intune to deploy apps to iOS devices, see [How to add iOS store apps to Microsoft Intune](/intune/store-apps-ios/). 

### Deploy OneDrive to Android devices by using Intune

1. Create a group of devices or users to target the deployment in Azure AD.
2. Select **Mobile apps** and **Apps**.
3. Under **App type**, select **Android**.
4. Enter the required info, including **https://play.google.com/store/apps/details?id=com.microsoft.skydrive** for the app store URL and **Android 4.0 (Ice Cream Sandwich)** for the minimum operating system. 

![](media/deploy-onedrive-enterprise_image2.png)

5. Assign the app to the group you created. For info about this, see [How to assign apps to groups with Microsoft Intune](/intune/apps-deploy/).


For more info about using Intune to deploy OneDrive to Android devices, see [How to add Android store apps to Microsoft Intune](/intune/store-apps-android). 



### Deploy OneDrive to Windows devices by using Intune

To use Intune to deploy OneDrive to Windows devices, follow these steps:

1. Create a group of devices or users to target the deployment in Azure AD.
2. Select **Mobile apps**, and **Apps**. 
3. Under **Office 365 Suite**, select **Add**.
4. In the **App type** list, select **Windows 10**. 
5. Select **OneDrive Desktop**.

![](media/deploy-onedrive-enterprise_image3.png)

> [!NOTE]
> You aren’t required to deploy the entire Office 365 suite at once. If you need the OneDrive sync client only, you can select that one item.

6. Specify a name, description, and installation options. 
7. Select assignments, select **Included groups**, and choose the group you created.
8. If you want to use silent account configuration, add a PowerShell script to do this and assign it to the group. For info about this, see [Silently configure user accounts](use-silent-account-configuration.md).

For more info about deploying Office 365 apps to Windows 10 devices using Intune, see [How to assign Office 365 apps to Windows 10 devices with Microsoft Intune](/intune/apps-add-office365/). 




