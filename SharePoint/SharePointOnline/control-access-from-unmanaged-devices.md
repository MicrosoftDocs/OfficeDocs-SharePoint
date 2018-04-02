---
title: "Control access from unmanaged devices"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 3/30/2018
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.collection: Strat_SP_admin
ms.assetid: 5ae550c4-bd20-4257-847b-5c20fb053622
description: "Learn how to limit web access to SharePoint and OneDrive, or block all access, on devices that aren't compliant or joined to a domain."
---

# Control access from unmanaged devices

 *Last updated: March 2018* 
  
> [!NOTE]
> Some functionality is introduced gradually to organizations that have set up the [Set up the Standard or Targeted release options in Office 365](https://support.office.com/article/3b3adfa4-1777-4ff0-b606-fb8732101f47). This means that you may not yet see this feature or it may look different than what is described in this article. 
  
As a SharePoint or global admin in Office 365, you can block or limit access to SharePoint and OneDrive content from unmanaged devices (those not joined to a domain or compliant in Intune). You can block or limit access for:
  
- All users in the organization or only some users or security groups.
    
- All sites in the organization or only some site collections.
    
Blocking access helps provide security but comes at the cost of usability and productivity. Limiting access allows users to remain productive while addressing the risk of accidental data loss on unmanaged devices. When you limit access, users on managed devices will have full access (unless they use one of the browser and operating system combinations listed below). Users on unmanaged devices will have browser-only access with no ability to download, print, or sync files. They also won't be able to access content through apps, including the Microsoft Office desktop apps. When you limit access, you can choose to allow or block editing files in the browser.
  
> [!NOTE]
>  Blocking or limiting access on unmanaged devices relies on Azure AD conditional access policies. To learn more about them and the subscriptions they require, see [Conditional access in Azure Active Directory](https://go.microsoft.com/fwlink/?linkid=857717). >  If you limit access on unmanaged devices, users on managed devices who have the following browser and operating system combinations will also have limited access: >  Chrome, Firefox, or any other browser besides Microsoft Edge and Microsoft Internet Explorer on Windows 10 or Windows Server 2016 >  Firefox in Windows 8.1, Windows 7, Windows Server 2012 R2, Windows Server 2012, or Windows Server 2008 R2 
  
## Block access to SharePoint and OneDrive content using the SharePoint admin center

1. [Sign in to Office 365](e9eb7d51-5430-4929-91ab-6157c5a050b4) as a global admin or SharePoint admin. 
    
2. Select the app launcher icon ![The icon that looks like a waffle and represents a button click that will reveal multiple application tiles for selection.](media/3b8a317e-13ba-4bd4-864e-1ccd47af39ee.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** > **SharePoint**.
    
4. In the SharePoint admin center, click **access control**.
    
5. Select **Block Access**.
    
6. Click **OK**.
    
     ![The block access setting on the access control page](media/ea0ee472-6fde-4d2d-bc7b-9d3b9eee0d96.PNG)
  
    > [!NOTE]
    > It can take 5-10 minutes for the policy to take effect. It won't take effect for users who are already signed in from unmanaged devices. 
  
If you go to the Azure AD admin center and click **Conditional access**, you can see that a policy was created by the SharePoint admin center.
  
![Creating a policy in the Azure AD admin center to block access](media/2d892713-3423-4870-b074-4f013b177c3b.png)
  
## Limit access to SharePoint and OneDrive content using the SharePoint admin center

1. [Sign in to Office 365](e9eb7d51-5430-4929-91ab-6157c5a050b4) as a global admin or SharePoint admin. 
    
2. Select the app launcher icon ![The icon that looks like a waffle and represents a button click that will reveal multiple application tiles for selection.](media/3b8a317e-13ba-4bd4-864e-1ccd47af39ee.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** > **SharePoint**.
    
4. In the SharePoint admin center, click **access control**.
    
5. Select **Allow limited, web-only access**.
    
6. Click **OK**.
    
     ![The limited access setting on the access control page](media/1ac2b9f4-32eb-4f21-85f1-e971c50f8b23.png)
  
    > [!NOTE]
    >  It can take 5-10 minutes for the policies to take effect. They won't take effect for users who are already signed in from unmanaged devices. >  By default, the policy allows users to edit files in the browser, copy and paste file contents out of the browser window, and download files that can't be previewed in the browser (like .zip and .exe). To change this, see [Advanced configurations](control-access-from-unmanaged-devices.md#advanced). 
  
If you go to the Azure AD admin center and click **Conditional access**, you can see that two policies were created by the SharePoint admin center. By default, the policy applies to all users. To apply it to only specific security groups, make changes under **Users and groups**. Be careful not to create multiple conditional access polices in the Azure AD admin center that conflict with each other. You can disable the policies created by the SharePoint admin center and then manually create the conditional access policies you need.
  
![Creating two policies in the Azure AD admin center to limit access](media/54c5106a-fd19-49b9-a997-4295e9f788be.png)
  
## Limit access to SharePoint and OneDrive content using PowerShell

1. In the [SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251), connect to the SharePoint admin center with your admin account by running  `Connect-SPOService`. For info about running this cmdlet, see [Connect-SPOService](https://technet.microsoft.com/en-us/library/fp161392.aspx).
    
2. Run  `Set-SPOTenant -ConditionalAccessPolicy AllowLimitedAccess`.
    
> [!NOTE]
>  By default, the policy allows users to edit files in the browser and copy file contents out of the browser window. See [Advanced configurations](control-access-from-unmanaged-devices.md#advanced) to change this. >  Some file types like .zip and .exe can't be previewed in a browser. By default, the policy allows users to download these files. See [Advanced configurations](control-access-from-unmanaged-devices.md#advanced) to change this. >  For more info about managing SharePoint Online using PowerShell, see [Introduction to the SharePoint Online Management Shell](https://technet.microsoft.com/en-us/library/fp161388.aspx). 
  
## Block or limit access to specific SharePoint site collections or OneDrive accounts

To block or limit access to specific sites, you must set the organization-wide policy to "Allow full access from desktop apps, mobile apps, and the web." Then follow these steps to manually create a policy in the Azure AD admin center and run PowerShell cmdlets.
  
1. In the Azure AD admin center, select **Conditional access**, and then click **Add**.
    
2. Under **Users and groups**, select whether you want the policy to apply to all users or only specific security groups.
    
3. Under **Cloud apps**, select **Office 365 SharePoint Online**.
    
4. Under **Conditions**, select both **Mobile apps and desktop clients** and **Browser**.
    
5. Under **Session**, select **Use app enforced restrictions**. This tells Azure to use the settings you'll specify in SharePoint.
    
6. Enable the policy and save it.
    
     ![Creating a policy in the Azure AD admin center to use app-enforced restrictions](media/c6467cd8-612d-4f8e-98bf-4913b35f49f1.png)
  
7. In the [SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251), connect to the SharePoint admin center with your admin account by running  `Connect-SPOService`. For info about running this cmdlet, see [Connect-SPOService](https://technet.microsoft.com/en-us/library/fp161392.aspx).
    
8. To block access, run  `Set-SPOSite -Identity https://<SharePoint online URL>/sites/<name of site collection or OneDrive account> -ConditionalAccessPolicy BlockAccess`.
    
    To limit access, run  `Set-SPOSite -Identity https://<SharePoint online URL>/sites/<name of site collection or OneDrive account> -ConditionalAccessPolicy AllowLimitedAccess`.
    
> [!NOTE]
>  The site collection-level setting must be at least as restrictive as the organization-wide setting. >  By default, the limited access policy allows users to edit files in the browser, and allows users to download files that can't be previewed in a browser (like .zip and .exe). See [Advanced configurations](control-access-from-unmanaged-devices.md#advanced) to change this. 
  
For more info about managing SharePoint Online using PowerShell, see [Introduction to the SharePoint Online Management Shell](https://technet.microsoft.com/en-us/library/fp161388.aspx).
  
## Advanced configurations
<a name="advanced"> </a>

The following parameters can be used with  `-ConditionalAccessPolicy AllowLimitedAccess` for both the organization-wide setting and the site-level setting. 
  
-  `-AllowEditing $false` Prevents users from editing files in the browser and copying and pasting file contents out of the browser window. 
    
-  `-LimitedAccessFileType -OfficeOnlineFilesOnly` Allows users to preview only Office files in the browser. 
    
-  `-LimitedAccessFileType -WebPreviewableFiles` Allows users to preview other file types in the browser, such as PDF files and images. 
    
-  `-LimitedAccessFileType -OtherFiles` Allows users to download files that can't be previewed, such as .zip and .exe. 
    
External users will be affected when you use conditional access policies to block or limit access from unmanaged devices. To exempt all external users from the policies, run the following cmdlet.
  
 `Set-SPOTenant -ApplyAppEnforcedRestrictionsToAdHocRecipients $false`
  
> [!NOTE]
> Anonymous access links (shareable links that don't require sign-in) are not affected by these policies. Anyone who has an anonymous access link to an item will be able to download the item. For all site collections where you enable conditional access policies, you should disable anonymous access links. 
  

