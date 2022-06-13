---
title: "Sign out inactive users"
ms.reviewer: samust
manager: serdars
recommendations: true
ms.author: mikeplum
author: MikePlumleyMSFT
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:
- Strat_SP_admin
- M365-collaboration
- ms.custom: admindeeplinkSPO
search.appverid:
- SPO160
- ODB160
- MET150
ms.assetid: 5d94efb4-ab46-429d-a021-d71eec787522
description: "Learn how to set an idle session sign-out policy for SharePoint and OneDrive browser sessions on unmanaged devices."
---

# Sign out inactive users

This article is for global and SharePoint admins in Microsoft 365 who want to control user access to SharePoint and OneDrive data on unmanaged devices. Idle session sign-out lets you specify a time at which users are warned and are later signed out of Microsoft 365 after a period of browser inactivity in SharePoint and OneDrive.

> [!NOTE]
> Idle session sign-out applies to the entire organization and can't be set for specific sites or users.  To target different settings for different users, use Azure AD Conditional Access policies instead (and see the next important note about the Azure AD Premium requirement).

> [!IMPORTANT]
> This feature relies on Azure AD Conditional Access policies being available. You will need an Azure AD Premium P1 or P2 subscription for this to work. For more info about this, refer to the [announcement in the Azure Active Directory Identity Blog](https://techcommunity.microsoft.com/t5/azure-active-directory-identity/conditional-access-8220-limited-access-8221-policies-for/ba-p/245228).

Idle session sign-out is one of a number of policies you can use with SharePoint and OneDrive to balance security and user productivity and help keep your data safe irrespective of where users access the data from, what device they're working on, and how secure their network connection is. For more ways to control access in SharePoint and OneDrive, see [How SharePoint and OneDrive safeguard your data in the cloud](safeguarding-your-data.md).

## The idle session sign-out experience

When a user is inactive in SharePoint and OneDrive for the time period you specify, the following message appears:

![Inactive Microsoft 365 sign out warning message](media/80c0d10b-df78-4e3c-9df0-b94a923b3871.png)

> [!NOTE]
> Activity is counted as requests sent to SharePoint, such as mouse clicks on a UI element like a button, list entry, or a link. Moving the mouse and scrolling are not counted as activity.

If users don't select **Continue**, they're automatically signed out, and the following message appears.

![Microsoft 365 signed out due to inactivity message](media/acc48304-dacd-41db-a4b6-8702cb6afa04.png)

> [!NOTE]
> If a user is active in another Microsoft 365 service (such as Outlook), but inactive in SharePoint and OneDrive, they're signed out across Microsoft 365. If a user has multiple tabs to OneDrive and SharePoint sites open at the same time, they won't be signed out unless they're inactive on all the sites. Users won't be signed out if they selected to stay signed in when they signed in. For info about hiding this option, see [Add company branding to your sign-in page in Azure AD](/azure/active-directory/fundamentals/customize-branding). Users won't be signed out on a managed device (one that is compliant or joined to a domain), unless they're using inPrivate mode or a browser other than Edge or Internet Explorer. If they use Google Chrome, you need to use an extension to pass the device state claim. For more info about device state claims, see [Azure AD conditional access settings](/azure/active-directory/conditional-access/concept-conditional-access-conditions).

> [!IMPORTANT]
> Microsoft 365 apps and services will not support Internet Explorer 11 starting August 17, 2021 (Microsoft Teams will not support Internet Explorer 11 earlier, starting November 30, 2020). [Learn more](https://aka.ms/AA97tsw). Please note that Internet Explorer 11 will remain a supported browser. Internet Explorer 11 is a component of the Windows operating system and [follows the Lifecycle Policy](/lifecycle/faq/internet-explorer-microsoft-edge) for the product on which it is installed.

## Specify idle session sign-out settings in the new SharePoint admin center

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185071" target="_blank">**Access control** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

   > [!NOTE]
   > If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Access control page.

2. Select **Idle session sign-out**.

    ![The Idle session sign-out panel](media/idle-session-sign-out.png)

3. Turn on **Sign out inactive users automatically**, and then select when you want to sign out users and how much notice you want to give them before signing them out.

4. Select **Save**.

## Specify idle session sign-out settings by using PowerShell

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." <br>On the Download Center page, select your language and then click the Download button. You'll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you're running the 64-bit version of Windows or the x86 file if you're running the 32-bit version. If you don't know, see [Which version of Windows operating system am I running?](https://support.microsoft.com/help/13443/windows-which-operating-system) After the file downloads, run it and follow the steps in the Setup Wizard.

2. Connect to SharePoint as a [global admin or SharePoint admin](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following command:

   ```PowerShell
   Set-SPOBrowserIdleSignOut -Enabled $true -WarnAfter (New-TimeSpan -Seconds 2700) -SignOutAfter (New-TimeSpan -Seconds 3600)
   ```

   Where:

   - **-Enabled** specifies whether idle session sign-out is enabled or disabled by using **$true** or **$false**.

   - **-WarnAfter** specifies the amount of after which a user is notified that they'll be signed out after a period of inactivity as a **New-TimeSpan** which can be configured in seconds, minutes, or hours.

   - **-SignOutAfter** specifies the amount of time after which is a user is signed out of Microsoft 365 if they don't respond to the **-WarnAfter** prompt.

> [!NOTE]
> You must specify values for both **WarnAfter** and **SignOutAfter**. The **SignOutAfter** must be greater than the **WarnAfter** value.
>
> It takes about 15 minutes for the policy to take effect across your organization. The policy doesn't affect existing sessions. To view the idle session sign-out values you've set, use **Get-SPOBrowserIdleSignOut**.
>
> For info about Microsoft 365 session lengths (regardless of activity), see [Session timeouts for Microsoft 365](/office365/enterprise/session-timeouts).
