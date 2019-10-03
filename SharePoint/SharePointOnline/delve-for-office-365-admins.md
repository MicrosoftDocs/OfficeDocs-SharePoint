---
title: "Office Delve for Office 365 admins"
ms.reviewer: 
ms.author: gretel
author: gretel
manager: pamgreen
audience: Admin
ms.topic: overview
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MOE150
- DEL150
- FRP150
- MET150
ms.assetid: 54f87a42-15a4-44b4-9df0-d36287d9531b
description: "The more you and your colleagues use Office 365 to work together, by viewing, editing and sharing each other's documents, the more useful Delve will be for all of you. Learn more about how you as an admin can help users get the most out of Delve."
---

# Office Delve for Office 365 admins

The more you and your colleagues use Office 365 to work together, by viewing, editing and sharing each other's documents, the more useful Delve will be for all of you. Learn more about how you as an admin can help users get the most out of Delve. 
  
Delve is powered by the Office Graph and shows users the most relevant content based on who they work with and what they're working on. The information in Delve is tailored to each user. Delve doesn't change permissions and users will only see what they already have access to. 
  
As an admin, you can make sure that you allow your organization to access Delve, and that you have set up other Office 365 services that Delve uses, for instance SharePoint Online and OneDrive for Business. You can also help people get started with Delve, and address questions that users might have.
  
## What you need to get Delve
<a name="BKMK_PrereqsDelve"> </a>

Delve is available for Office 365 Enterprise (E1, E3, and E5), Office 365 Education (E1, E3 and E5), Office 365 Government (E1, E3 and E5), Office 365 Business Essentials and Office 365 Business Premium. 
  
Regardless of which of these Office 365 plans you have, you need to activate the SharePoint Online service and assign users a SharePoint Online license before they can start using Delve. You also have to set up Exchange Online if you want attachments to show up on users' Home pages in Delve. If you set up Skype for Business Online, users can start Skype for Business Online conversations directly from Delve. And if you set up Yammer Enterprise, users can engage in Yammer conversations about documents directly from Delve. 
  
Delve is designed to work with the current or immediately previous version of Internet Explorer or Firefox, or the latest version of Chrome or Safari.

The Delve O365 app is also enabled for modern authentication. For more information, see [Office 365 Client app Support - Modern Authentication](https://docs.microsoft.com/office365/enterprise/office-365-client-support-modern-authentication).
  
## Get new Delve features quicker
<a name="BKMK_DelveFirstRelease"> </a>

If you want to receive new functionality in Delve before it's made available in standard releases, you can opt in to the  *Targeted release*  program. You'll receive new feature updates a minimum of two weeks before customers in the  *Standard release*  program. To learn more, see [Office 365 release options](/office365/admin/manage/release-options-in-office-365). 
   
   > [!TIP]
   > It takes some time to build personalized Delve views for users in your organization. If you opt in to the targeted release program just before the start of a weekend, it's more likely that people have a good Delve experience at the start of the next work week. 
  
What users see in Delve is influenced by which release program you've chosen for your organization. See [My Office Delve looks different from what you describe](https://support.office.com/article/8fe977a0-cc37-4845-a75d-96994dffca5d) for an overview of the main differences. 
  
## Control access to Delve and related features
<a name="BKMK_DelveOnOff"> </a>

You control access to Delve from the SharePoint admin center. By default, users in your organization have access to Delve. They also have access to certain features in other apps that are powered by the Office Graph, such as the "Suggested" list on the SharePoint start page, and the "Discover" list in OneDrive. When you enable or disable Delve, these other features are also affected. 

If you disable Delve, users will no longer see:
- The Delve app tile in the app launcher
- The "Suggested" list on the SharePoint start page
- The "Discover" list in OneDrive, in the Outlook mobile app, and on the Microsoft Office Home page
- Documents on other users' profile cards and pages

 See [What is the effect of enabling or disabling Delve and related features?](delve-for-office-365-admins.md#BKMK_EffectOfficegraphOnOff) for more information. 
  
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.

3. Select **Settings** in the left pane.
 
4. At the bottom of the page, select **classic settings page**.
    
5.  Under **Delve (powered by Office Graph)**, select one of the following:  
    
  - **Enable Delve and related features**
    
  - **Disable Delve and related features**
    
## Introducing Delve in your organization
<a name="BKMK_DelveIntroduce"> </a>

Here are some resources that you can use to get your organization started with Delve. 
  
 **Before you announce Delve**
  
- SharePoint Online and OneDrive for Business are the primary sources of content in Delve. How you and users manage permissions on documents and sites affects what users see in Delve. Check out [Overview: best practices for managing how people use your team site](https://support.office.com/article/95e83c3d-e1b0-4aae-9d08-e94dcaa4942e) and [Plan your permissions strategy](/sharepoint/plan-your-permissions-strategy) for more information. 
    
 **Using Delve on a day-to-day basis**
  
- You can point users to the Delve help articles. [What is Office Delve?](https://support.office.com/article/1315665a-c6af-4409-a28d-49f8916878ca) is a great starting point, and users may be particularly interested in the information in the articles [Are my documents safe in Office Delve?](https://support.office.com/article/f5f409a2-37ed-4452-8f61-681e5e1836f3), [Connect and collaborate in Office Delve](https://support.office.com/article/46f92806-b52c-4187-b60e-b3bf8d25f73e) and [Store your documents where Office Delve can get to them](https://support.office.com/article/49a0db49-5e6c-4dda-816e-e11dd77de49d).
    
 **Data and geographic region**
  
- When users go to Delve, for example by typing **delve.office.com** in a browser, they're automatically redirected to the geographic region where your organization's Office 365 environment is located. After the redirect, a three letter prefix indicating the region is added to the URL, for example **https://nam.delve.office.com** for North America, or **https://eur.delve.office.com** for Europe. 
    
## Help users troubleshoot Delve
<a name="BKMK_DelveTroubleshoot"> </a>

Use the information in this section to help troubleshoot issues in Delve. 
  
- [ Users don't see Delve in the Office 365 app launcher ](delve-for-office-365-admins.md#BKMK_DelveGlobalNav)
    
- [Users see incorrect colleagues in Delve](delve-for-office-365-admins.md#BKMK_DelveIncorrectColleague)
    
- [Users don't see user pictures in Delve](delve-for-office-365-admins.md#BKMK_DelvePictures)
    
- [Users see documents from other users who have turned off Documents in Delve](delve-for-office-365-admins.md#BKMK_DelveOff)
    
- [Users see very little or no content in Delve](delve-for-office-365-admins.md#BKMK_DelveNotMuchContent)
    
- [Users can't find a specific item in Delve](delve-for-office-365-admins.md#BKMK_DelveNoItem)
    
- [Users are concerned that private or sensitive documents are available in Delve](delve-for-office-365-admins.md#BKMK_DelveHide)
    
### Users don't see Delve in the Office 365 app launcher
<a name="BKMK_DelveGlobalNav"> </a>

There are a few things you should check if one or more users in your organization don't see Delve in the app launcher. All these things need to be in place for your organization before people can start using Delve. 
  
 **Solution(s)**
  
- [Check that you allow your organization to access Delve](#BKMK_OfficeGraphAccess).
    
- Check that you're using an Office 365 plan that supports Delve
    
- Check that you've assigned the correct user licenses
    
 **Check that you allow your organization to access Delve**
<a name="BKMK_OfficeGraphAccess"></a>
  
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  

2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.

3. Select **Settings** in the left pane.
 
4. At the bottom of the page, select **classic settings page**.

5. Under **Delve (powered by Office Graph)**, make sure that you've selected **Enable Delve and related features**. 
    
    > [!NOTE]
    > If you have a SharePoint Online standalone service (SharePoint Online Plan 1 or SharePoint Online Plan 2) you'll see the Delve setting in the SharePoint admin center. However, users won't be able to use Delve or see Delve in the app launcher, because Delve is not available for standalone services yet. 
  
 **Check that you're using an Office 365 plan that supports Delve**
<a name="#BKMK_CheckPlan"></a>
  
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, select **Billing** \> **Products &amp; services**. 
    
3. Verify that you have one of the following subscriptions: 
    
  - Office 365 Enterprise (E1, E3, or E5)
    
  - Office 365 Education
    
  - Office 365 Government (E1, E3 or E5)
    
  - Office 365 Business Essentials 
    
  - Office 365 Business Premium 
    
 **Check that you've assigned the correct user licenses**
<a name="#BKMK_CheckLicense"></a>
  
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. Select **Users** \> **Active users**.
    
3. Select the box in front of the name of the user who you want to check the licenses for.
    
4. Verify that the user has one of the following combinations of licenses: 
    
  - Microsoft Office 365 Plan E1 plus SharePoint Online (Plan 1 or Plan 2)
    
  - Microsoft Office 365 Plan E3 plus SharePoint Online (Plan 1 or Plan 2)
    
  - Microsoft Office 365 Plan E5 plus SharePoint Online (Plan 1 or Plan 2)
    
  - Microsoft Office 365 Business Essentials plus SharePoint Online (Plan 1 or Plan 2)
    
  - Microsoft Office 365 Business Premium plus SharePoint Online (Plan 1 or Plan 2)
    
    For more information on how to manage licenses, see [Assign licenses to users in Office 365 for business](/office365/admin/subscriptions-and-billing/assign-licenses-to-users).
    
### Users see incorrect colleagues in Delve
<a name="BKMK_DelveIncorrectColleague"> </a>

If Azure Active Directory has outdated information or if hasn't been synced with the SharePoint Online user profiles, Delve may not show the most relevant colleagues. 
  
Delve uses information from user profiles in Office 365 to determine who users in your organization work with most closely. These profiles contain information from Azure Active Directory and from SharePoint Online user profiles. Every 24 hours, people information from Azure Active Directory is automatically added to SharePoint Online user profiles. 
  
 **Solution(s)**
  
- Check and clean up your Azure Active Directory, and wait for the information to sync to SharePoint Online user profiles. 
    
- If you're an academic organization, the sync between Azure Active Directory and user profiles is not automatic. Your users will need to sign in to SharePoint Online at least once to create user profiles.
    
- If you have an on-premises Active Directory and if you've set up Active Directory synchronization, make sure it's synced correctly with Azure Active Directory. 
    
### Users don't see user pictures in Delve
<a name="BKMK_DelvePictures"> </a>

The user pictures in Delve are from the SharePoint Online user profiles. If there's no picture for a user in his or her SharePoint Online user profile, Delve has no picture to show. 
  
 **Solution(s)**
  
- Make sure that users upload their user profile picture to SharePoint Online. For more information, point users to [View and update your profile in Office Delve](https://support.office.com/article/4e84343b-eedf-45a1-aeb9-8627ccca14ba). 
    
### Users see documents from other users who have turned off Documents in Delve
<a name="BKMK_DelveOff"> </a>

 Users can turn off **Documents** in Delve which means that they won't see any documents in Delve, and their **activities** and **relationships** in Office 365 won't be included in the Office Graph. 
  
However, if other users still have  *access*  to documents from a user who has turned off **Documents**, they can still see those documents in Delve, just as they can search for them in SharePoint Online. 
  
Other information that's available to everyone in the organization will also be visible even if a user has turned off **Documents**, such as information from the Azure Active Directory. 
  
 **Solution(s)**
  
- No action needed.
    
### Users see very little or no content in Delve
<a name="BKMK_DelveNotMuchContent"> </a>

The content in Delve comes from different content sources across Office 365 such as Exchange Online, Office 365 Video, SharePoint Online and OneDrive for Business. 
  
If users don't have any recently modified or viewed content in these content sources, and they don't have access to other users' content, Delve may have very little or no content to show. Users also need to have licenses to Office 365 services and access to the Office Graph to see content in Delve.
  
 **Solution(s)**
  
- Encourage your users to store and share documents in SharePoint and OneDrive. For more information, point users to [Store your documents where Office Delve can get to them](https://support.office.com/article/49a0db49-5e6c-4dda-816e-e11dd77de49d). 
    
- Check the permission settings on SharePoint sites to make sure that the user has access to the correct sites and their content.
    
- Check that the user is in the Active Directory and that he or she is a member of the correct Active Directory groups. To verify, go to **Microsoft 365 admin center** \> **Users** \> **Active Users**. 
    
- Make sure that the user allows Delve to show documents. To verify, have the user go to **Office 365** \> **Delve** \> ** Feature settings ** and make sure that **Documents in Delve** isn't turned off. 
    
- Make sure that you've assigned users a license to access to the Office 365 services that you've activated.
    
### Users can't find a specific item in Delve
<a name="BKMK_DelveNoItem"> </a>

Delve doesn't change any permissions and users will only see what they already have access to. Not all content types will appear in Delve, and it can take up to 24 hours for new documents to show up. Also, Delve prioritizes content that's been modified or viewed in the last three months.
  
 **Solution(s)**
  
- Check the steps under [Users see very little or no content in Delve](delve-for-office-365-admins.md#BKMK_DelveNotMuchContent).
    
- Make sure that the content type is supported. Currently, in Standard Release, Delve shows PDF, Word, Excel and PowerPoint files, and videos that have been uploaded to Office 365 Video. 
    
- Check when the document was added to Office 365. It can take up to 24 hours for new documents to show up in Delve.
    
### Users are concerned that private or sensitive documents are available in Delve
<a name="BKMK_DelveHide"> </a>

Any document that a user can view or edit in Office 365, can also appear in Delve. Delve doesn't change any permissions and users will only see documents they already have access to. Sometimes, though, you may want to prevent a document from appearing in Delve. 
  
 **Solution(s)**
  
- Check the permission settings for the documents, sites and libraries and make sure that only the intended users have access to the content.
    
- If you want to prevent specific documents from appearing in Delve, follow the steps in [Hide documents from Delve](manage-search-schema.md#BKMK_HideFromDelveSteps). You can keep storing the documents in Office 365, and people can still find them through search - they just won't show up in Delve.
    
## About the Office Graph
<a name="BKMK_AboutOfficeGraph"> </a>

Delve is powered by the Office Graph. The Office Graph stores data representations about all Office 365 items as nodes in a graph index. The Office Graph data is stored in the customer's partition of the SharePoint Online and Exchange Online environments, and has the same data protection and security as other customer data stored in the same cloud services. The Office Graph data and metadata are stored in the same data center region as the services the data was collected from. 
  
The Office Graph uses rich relationships to describe connections between items of different types. In addition, the Office Graph uses advanced analytics and machine learning techniques to create inferred rich relationships - what we call insights.
  
To present the most relevant content in different contexts, for example in Delve, the Office Graph uses a two-step analysis. First, it calculates which users in the Office Graph are most relevant to the current context. Second, it retrieves the most relevant content associated with these users. The content is tailored to each user, and users only see what they already have access to.
  
For developers, the Office Graph insights and rich relationships are exposed through the Microsoft Graph, a single REST API endpoint ([https://graph.microsoft.com](https://graph.microsoft.com)) that exposes multiple APIs from Microsoft cloud services. For more information, see [Microsoft Graph](https://graph.microsoft.io/).
  
### What is the effect of enabling or disabling Delve and related features?
<a name="BKMK_EffectOfficegraphOnOff"> </a>

Delve is powered by the Office Graph. If Delve is enabled, users in your organization will have Delve in the Office 365 app launcher and they can use all the functionality in Delve. Clicking on a person in Delve will open that person's page. The person page contains user profile information such as contact information and org chart details, and also documents relating to the person. 

If you choose to disable Delve for your organization, Delve will be removed from the Office 365 app launcher for all users. When users visit a person's page, for example by clicking on a person in OneDrive for Business, that person's page will contain only user profile information. No documents will be shown. Users can still search for other people, but not for documents or boards. 

If Delve is enabled, users also have access to related features in other apps that are powered by the Office Graph. If you disable Delve, users can no longer see these features:

- The "Suggested" list on the SharePoint start page
- The "Discover" list in OneDrive, in the Outlook mobile app, and on the Microsoft Office Home page
- Documents on other users' profile cards and profile pages

If you disable Delve, users will not have access to the following API's:

- **Trending Insight API** (trending documents for all users) 
- **Used Insight API** (what documents other users have viewed or modified) 

**NOTE:** Disabling Delve does not disable **Microsoft Graph**. Office Graph and Microsoft Graph are different concepts despite their similar names. Microsoft Graph is the API endpoint that surfaces all Office 365 data (such as Azure AD, Outlook/Exchange, Excel, OneDrive, SharePoint), while Office Graph is mainly a code name for the collective set of services and insights generated on top of the infrastructure developed by the FAST Office Graph team. For more information about Microsoft Graph, see [Overview of Microsoft Graph](https://docs.microsoft.com/en-us/graph/overview)


  
## Additional resources
<a name="BKMK_DelveAdditionalResources"> </a>

End users
  
- [What is Office Delve?](https://support.office.com/article/1315665a-c6af-4409-a28d-49f8916878ca)
    
- [What is OneDrive for Business?](https://support.office.com/article/187f90af-056f-47c0-9656-cc0ddca7fdc2)
    
Admins
  
- [SharePoint Online Planning Guide for Office 365 for business](introduction.md)
    
- [Manage SharePoint Online user profiles from the SharePoint admin center](manage-user-profiles.md)
    
- [Office 365 integration with on-premises environments](/office365/enterprise/office-365-integration)
    
- [User Account Management](/office365/servicedescriptions/office-365-platform-service-description/user-account-management)
    
- [Directory synchronization roadmap](/azure/active-directory/hybrid/whatis-hybrid-identity)
    
- [Manage your Office 365 Video portal](https://support.office.com/article/c059465b-eba9-44e1-b8c7-8ff7793ff5da)
    
- [Yammer - Admin Help](https://support.office.com/article/e1464355-1f97-49ac-b2aa-dd320b179dbe)
    
- [Office 365 Plan Options](/office365/servicedescriptions/office-365-platform-service-description/office-365-plan-options)
    
- [Set up the Standard or Targeted release options in Office 365](/office365/admin/manage/release-options-in-office-365)
    

