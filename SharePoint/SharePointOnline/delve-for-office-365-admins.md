---
title: "Delve for admins"
ms.reviewer: 
ms.author: gretel
author: gretel
manager: pamgreen
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: overview
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.custom: admindeeplinkSPO
search.appverid:
- SPO160
- MOE150
- DEL150
- FRP150
- MET150
ms.assetid: 54f87a42-15a4-44b4-9df0-d36287d9531b
description: "The more you and your colleagues use Microsoft 365 to work together, by viewing, editing, and sharing each other's documents, the more useful Delve will be for all of you. Learn more about how you as an admin can help users get the most out of Delve."
---

# Delve for admins

The more you and your colleagues use Microsoft 365 to work together, by viewing, editing, and sharing each other's documents, the more useful Delve will be for all of you. Learn more about how you as an admin can help users get the most out of Delve.
  
Delve is powered by the Microsoft Graph and shows users the most relevant content based on who they work with and what they're working on. The information in Delve is tailored to each user. Delve doesn't change permissions and users will only see what they already have access to.
  
As an admin, you can make sure that you allow your organization to access Delve, and that you have set up other Microsoft 365 services that Delve uses, such as SharePoint and OneDrive. You can also help people get started with Delve, and address questions that users might have.
  
## What you need to get Delve
<a name="BKMK_PrereqsDelve"> </a>

Delve is available for Office 365 Enterprise (E1, E3, and E5), Office 365 Education (E1, E3, and E5), Office 365 Government (E1, E3, and E5), Microsoft 365 Business Basic, and Microsoft 365 Business Standard.
  
Regardless of which Microsoft 365 or Office 365 subscriptions you have, you need to activate the SharePoint service and assign users a SharePoint license before they can start using Delve. You also have to set up Exchange Online if you want attachments to show up on users' Home pages in Delve. If you set up Microsoft Teams, users can start Microsoft Teams conversations directly from Delve.

> [!IMPORTANT]
> Microsoft 365 apps and services will not support Internet Explorer 11 starting August 17, 2021 (Microsoft Teams will not support Internet Explorer 11 earlier, starting November 30, 2020). [Learn more](https://aka.ms/AA97tsw). Please note that Internet Explorer 11 will remain a supported browser. Internet Explorer 11 is a component of the Windows operating system and [follows the Lifecycle Policy](/lifecycle/faq/internet-explorer-microsoft-edge) for the product on which it is installed. 

The Delve app is also enabled for modern authentication. For more info, see [How modern authentication works](/microsoft-365/enterprise/modern-auth-for-office-2013-and-2016).
  
## Control access to Delve
<a name="BKMK_DelveOnOff"> </a>

You control access to Delve from the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a>. By default, users in your organization have access to Delve. Users can limit their Delve experience to only show profile information by turning off **Show documents in Delve** under **Settings** > **Feature settings** in Delve. As an admin, you can also remove documents from Delve through the item insights privacy settings.

For more info on item insights privacy settings, see [Customizing item insights privacy in Microsoft Graph (preview)](/graph/insights-customize-item-insights-privacy).

For more info on disabling Delve, see [What is the effect of enabling or disabling Delve](/sharepoint/delve-for-office-365-admins#BKMK_EffectOfficegraphOnOff).
  
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185072" target="_blank">**Settings** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

    > [!NOTE]
    > If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the **Settings** page.
 
2. At the bottom of the page, select **classic settings page**.
    
3. Under **Delve**, select one of the following:
    
    - **Enable Delve**
    
    - **Disable Delve**
> [!NOTE]
> Previously, when turning Delve on or off in the SharePoint admin center, it also had an impact on a few other insights-driven experiences in Microsoft 365. Starting July 1, 2021, the Delve setting will be decoupled from the back end and will only impact Delve. Use the item insights privacy settings to control item insights in Microsoft 365.
    
## Introducing Delve in your organization
<a name="BKMK_DelveIntroduce"> </a>

Here are some resources that you can use to get your organization started with Delve. 
  
 **Before you announce Delve**
  
- SharePoint and OneDrive are the primary sources of content in Delve. How you and users manage permissions on documents and sites affects what users see in Delve. For more info, see [Overview: best practices for managing how people use your team site](https://support.office.com/article/95e83c3d-e1b0-4aae-9d08-e94dcaa4942e) and [Plan your permissions strategy](/sharepoint/plan-your-permissions-strategy).
    
 **Using Delve on a day-to-day basis**
  
- You can point users to the Delve help articles. [What is Delve?](https://support.office.com/article/1315665a-c6af-4409-a28d-49f8916878ca) is a great starting point, and users may be particularly interested in the information in the articles [Are my documents safe in Delve?](https://support.office.com/article/f5f409a2-37ed-4452-8f61-681e5e1836f3), [Connect and collaborate in Delve](https://support.office.com/article/46f92806-b52c-4187-b60e-b3bf8d25f73e) and [Store your documents where Delve can get to them](https://support.office.com/article/49a0db49-5e6c-4dda-816e-e11dd77de49d).
    
 **Data and geographic region**
  
- When users go to Delve, for example by entering **delve.office.com** in a browser, they're automatically redirected to the geographic region where your organization's environment is located. After the redirect, a three letter prefix indicating the region is added to the URL, for example **https://nam.delve.office.com** for North America, or **https://eur.delve.office.com** for Europe. 
    
## Help users troubleshoot Delve
<a name="BKMK_DelveTroubleshoot"> </a>

To help troubleshoot issues with Delve, see the following info. 
  
  - [ Users don't see Delve in the Microsoft 365 app launcher ](delve-for-office-365-admins.md#BKMK_DelveGlobalNav)
    
  - [Users see incorrect colleagues in Delve](delve-for-office-365-admins.md#BKMK_DelveIncorrectColleague)
    
  - [Users don't see user pictures in Delve](delve-for-office-365-admins.md#BKMK_DelvePictures)
    
  - [Users see documents from other users who have turned off Documents in Delve](delve-for-office-365-admins.md#BKMK_DelveOff)
    
  - [Users see little or no content in Delve](delve-for-office-365-admins.md#BKMK_DelveNotMuchContent)
    
  - [Users can't find a specific item in Delve](delve-for-office-365-admins.md#BKMK_DelveNoItem)
    
  - [Users are concerned that private or sensitive documents are available in Delve](delve-for-office-365-admins.md#BKMK_DelveHide)
    
### Users don't see Delve in the Microsoft 365 app launcher
<a name="BKMK_DelveGlobalNav"> </a>

There are a few things you should check if one or more users in your organization don't see Delve in the app launcher. All these things need to be in place for your organization before people can start using Delve.
  
 **Solution(s)**
  
- [Check that you allow your organization to access Delve](#BKMK_OfficeGraphAccess).
    
- Check that you're using a subscription that supports Delve.
    
- Check that you've assigned the correct user licenses.
    
 **Check that you allow your organization to access Delve**
<a name="BKMK_OfficeGraphAccess"></a>
  
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185072" target="_blank">**Settings** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

    > [!NOTE]
    > If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Settings page.
 
2. At the bottom of the page, select **classic settings page**.

3. Under **Delve**, make sure that you've selected **Enable Delve**. 
    
    > [!NOTE]
    > If you have a SharePoint standalone service (SharePoint Plan 1 or SharePoint Plan 2) you'll see the Delve setting in the SharePoint admin center. However, users won't be able to use Delve or see Delve in the app launcher, because Delve is not available for standalone services yet.
  
 **Check that you're using an Office 365 or Microsoft 365 plan that supports Delve**
<a name="#BKMK_CheckPlan"></a>
  
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Microsoft 365 admin permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.
    
2. In the left pane, select **Billing** \> **Products &amp; services**.
    
3. Verify that you have one of the following subscriptions:
    
    - Office 365 Enterprise (E1, E3, or E5)
    
    - Office 365 Education
    
    - Office 365 Government (E1, E3, or E5)
    
    - Microsoft 365 Business Basic
    
    - Microsoft 365 Business Standard
    
 **Check that you've assigned the correct user licenses**
<a name="#BKMK_CheckLicense"></a>
  
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Microsoft 365 admin permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.
    
2. Select **Users** \> **Active users**.
    
3. Select the box in front of the name of the user who you want to check the licenses for.
    
4. Verify that the user has one of the following combinations of licenses:
    
   - Office 365 Plan E1 plus SharePoint (Plan 1 or Plan 2)
    
   - Office 365 Plan E3 plus SharePoint (Plan 1 or Plan 2)
    
   - Office 365 Plan E5 plus SharePoint (Plan 1 or Plan 2)
    
   - Microsoft 365 Business Basic plus SharePoint (Plan 1 or Plan 2)
    
   - Microsoft 365 Business Standard plus SharePoint (Plan 1 or Plan 2)
    
    For more info about how to manage licenses, see [Assign licenses to users](/office365/admin/subscriptions-and-billing/assign-licenses-to-users).
    
### Users see incorrect colleagues in Delve
<a name="BKMK_DelveIncorrectColleague"> </a>

If Azure Active Directory has outdated information or hasn't been synced with the SharePoint user profiles, Delve may not show the most relevant colleagues.
  
Delve uses info from user profiles to determine who users in your organization work with most closely. These profiles contain information from Azure Active Directory and from SharePoint user profiles. Every 24 hours, people information from Azure Active Directory is automatically added to SharePoint user profiles.
  
 **Solution(s)**
  
- Check and clean up your Azure Active Directory, and wait for the information to sync to SharePoint user profiles.
    
- If you're an academic organization, the sync between Azure Active Directory and user profiles is not automatic. Your users will need to sign in to SharePoint at least once to create user profiles.
    
- If you have an on-premises Active Directory and if you've set up Active Directory synchronization, make sure it's synced correctly with Azure Active Directory.
    
### Users don't see user pictures in Delve
<a name="BKMK_DelvePictures"> </a>

The user pictures in Delve are from the SharePoint user profiles. If there's no picture for a user in their SharePoint user profile, Delve has no picture to show.
  
 **Solution(s)**
  
- Make sure that users upload their user profile picture to SharePoint. For more info, point users to [View and update your profile in Delve](https://support.office.com/article/4e84343b-eedf-45a1-aeb9-8627ccca14ba). 
    
### Users see documents from other users who have turned off documents in Delve
<a name="BKMK_DelveOff"> </a>

 Users can turn off documents in Delve, which means that they won't see any documents in Delve, and their **activities** and **relationships** won't be included in Microsoft Graph.
  
However, if other users still have *access* to documents from a user who has turned off documents, they can still see those documents in Delve, just as they can search for them in SharePoint.
  
Other info that's available to everyone in the organization will also be visible even if a user has turned off **Documents**, such as info from the Azure Active Directory.
  
 **Solution(s)**
  
- No action needed.
    
### Users see little or no content in Delve
<a name="BKMK_DelveNotMuchContent"> </a>

The content in Delve comes from different content sources such as Exchange Online, SharePoint, and OneDrive.
  
If users don't have any recently modified or viewed content in these content sources, and they don't have access to other users' content, Delve may have little or no content to show. Users also need to have licenses to Microsoft 365 and Office 365 services and they need to have the item insights privacy settings enabled.
  
 **Solution(s)**
  
- Encourage your users to store and share documents in SharePoint and OneDrive. For more info, point users to [Store your documents where Delve can get to them](https://support.office.com/article/49a0db49-5e6c-4dda-816e-e11dd77de49d). 
    
- Check the permission settings on SharePoint sites to make sure that the user has access to the correct sites and their content.
    
- Check that the user is in Active Directory and a member of the correct Active Directory groups. To verify, go to **Microsoft 365 admin center** \> **Users** \> **Active Users**.
    
- Make sure that the user allows Delve to show documents. To verify, have the user go to **App launcher** \> **Delve** \> **Feature settings** and make sure that **Show documents in Delve** isn't turned off.
    
- Make sure that you've assigned users a license to access to the Microsoft 365 services that you've activated.
    
### Users can't find a specific item in Delve
<a name="BKMK_DelveNoItem"> </a>

Delve doesn't change any permissions and users will only see what they already have access to. Not all content types will appear in Delve, and it can take up to 24 hours for new documents to show up. Also, Delve prioritizes content that's been modified or viewed in the last three months.
  
 **Solution(s)**
  
- Check the steps under [Users see little or no content in Delve](delve-for-office-365-admins.md#BKMK_DelveNotMuchContent).
   
- Check when the document was added. It can take up to 24 hours for new documents to show up in Delve.
    
### Users are concerned that private or sensitive documents are available in Delve
<a name="BKMK_DelveHide"> </a>

Any document that a user can view or edit in Microsoft 365, can also appear in Delve. Delve doesn't change any permissions and users will only see documents they already have access to. However, there are times when you may want to prevent a document from appearing in Delve.
  
 **Solution(s)**
  
- Check the permission settings for the documents, sites and libraries and make sure that only the intended users have access to the content.
    
- If you want to prevent specific documents from appearing in Delve, follow the steps in [Hide documents from Delve](manage-search-schema.md#BKMK_HideFromDelveSteps). You can keep storing the documents in Microsoft 365, and people can still find them through search - they just won't show up in Delve.
  
### What is the effect of enabling or disabling Delve?
<a name="BKMK_EffectOfficegraphOnOff"> </a>

Changing the Delve setting in the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a> will enable or disable the full Delve experience for all users in the tenant. If Delve is enabled, users in your organization will have Delve in the app launcher and they can use all the functionality in Delve. Selecting a person in Delve will open that person's page. The person page contains user profile information such as contact information and org chart details, and also documents relating to the person. 

If you choose to disable Delve for your organization, Delve will be removed from the app launcher for all users. When users visit a person's page, for example by clicking on a person in OneDrive, that person's page will contain only user profile information. No documents will be shown. Users can still search for other people, but not for documents or boards. If the Delve setting is disabled, users will not see the frequent sites and suggested sites in the SharePoint start page.

> [!NOTE]
> Disabling Delve does no longer disable *Microsoft Graph* or insights services generated on top of it. This level of control is now available from the item insights privacy settings. For more info about the item insights settings, see [Customizing item insights privacy in Microsoft Graph](/graph/insights-customize-item-insights-privacy). For more info about Microsoft Graph, see [Overview of Microsoft Graph](/graph/overview).

## Additional resources
<a name="BKMK_DelveAdditionalResources"> </a>

End users
  
- [What is Delve?](https://support.office.com/article/1315665a-c6af-4409-a28d-49f8916878ca)

- [What is OneDrive?](https://support.office.com/article/187f90af-056f-47c0-9656-cc0ddca7fdc2)

- [How does Delve know what's relevant to me?](https://support.microsoft.com/office/048d502e-80a7-4f77-ac5c-f9d81733c385)

Admins
  
- [SharePoint Planning Guide for Microsoft 365 Apps for business](introduction.md)

- [Manage SharePoint user profiles from the SharePoint admin center](manage-user-profiles.md)

- [Microsoft 365 integration with on-premises environments](/office365/enterprise/office-365-integration)

- [User Account Management](/office365/servicedescriptions/office-365-platform-service-description/user-account-management)

- [Directory synchronization roadmap](/azure/active-directory/hybrid/whatis-hybrid-identity)

- [Yammer - Admin Help](https://support.office.com/article/e1464355-1f97-49ac-b2aa-dd320b179dbe)

- [Plan Options](/office365/servicedescriptions/office-365-platform-service-description/office-365-plan-options)
  
- [Set up the Standard or Targeted release options in Microsoft 365](/office365/admin/manage/release-options-in-office-365)
