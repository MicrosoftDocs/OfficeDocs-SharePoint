---
title: "Configure hybrid OneDrive"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 10/20/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- Ent_O365_Hybrid
- IT_OneDriveAdmin
- IT_OneDriveAdmin_Top
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- M365-collaboration
- SPO_Content
ms.custom:
- seo-marvel-apr2020
ms.assetid: f1dfdac2-81ad-452f-b5b6-df9e5a8e976e
description: "Connect your on-premises SharePoint Server environment with OneDrive."
---

# Configure hybrid Microsoft OneDrive

[!INCLUDE[appliesto-2013-2016-2019-SUB-SPO-md](../includes/appliesto-2013-2016-2019-SUB-SPO-md.md)]
  
 **This article is part of a roadmap of procedures for configuring SharePoint in Microsoft 365 hybrid solutions. Be sure you're [following a roadmap](configuration-roadmaps.md) when you do the procedures in this article.**
  
You can redirect users to Microsoft OneDrive, on the navigation bar or the app launcher, when they select **OneDrive** or **Sites**. This article provides the steps to configure your on-premises environment to connect with OneDrive. You can find an overview of the process in [Plan for hybrid OneDrive](./plan-hybrid-onedrive-for-business.md).
  
## Video demonstration

This video shows a walkthrough of configuring hybrid OneDrive.
  
**Video: Configure hybrid OneDrive**

> [!VIDEO https://www.microsoft.com/videoplayer/embed/a65546fb-4981-4a66-a9b6-0659382b5efb?autoplay=false]
> [!NOTE]
> The SharePoint Migration Tool demonstrated in the video is currently in preview. It is only supported for SharePoint Server 2013. [Download the SharePoint Migration Tool](https://spmtreleasescus.blob.core.windows.net/install/default.htm).
  
## Configure user permissions

To use OneDrive, your users must have **Create Personal Site** and **Follow People and Edit Profile** permissions. Both are controlled by the user permissions in the User Profile service application. 
  
1. Verify that the user account that is performing this procedure is a member of the Farm Admins group.
    
2. In your on-premises SharePoint Server environment, go to **Central Administration** > **Manage Service Applications**.
    
3. Click the User Profile Service Application.
    
4. On the **Manage Profile Service** page, under **People**, select **Manage User Permissions**.
    
5. In the **Permissions for User Profile Service Application** dialog, select **All Authenticated Users** (or a specific audience that you intend to use as a pilot group of users). 
    
6. Verify that the **Create Personal Site** and **Follow People and Edit Profile** permission check boxes are selected. 
    
## Configure hybrid OneDrive
<a name="Configure"> </a>

To configure hybrid OneDrive, you must be both a SharePoint Server farm administrator and a Microsoft 365 global admin. Perform these steps on a server in your SharePoint Server farm.
  
 **To configure hybrid OneDrive**
  
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](../../SharePointOnline/sharepoint-admin-role.md) for your organization.

2. Under **Hybrid picker**, select **Open**.
    
3. Click **Go to Hybrid Picker Download Page**.
    
4. On the SharePoint in Microsoft 365 Hybrid Configuration Wizard page, select **click here**.
    
5. Accept the security prompts to install and run the wizard.
    
6. On the **SharePoint Hybrid Configuration Wizard** page, select **Next**.
    
7. On the **Credentials** page, verify your on-premises credentials and enter your global admin credentials. Select **Validate credentials**, and then select **Next**.
    
8. On the **Checking prerequisites** page, select **Next**.
    
9. On the **Select the features you want to use in your hybrid environment** page, select the Hybrid OneDrive check box and deselect any other check boxes. Select **Next**.
    
10. When the configuration completes, select **Next**.
    
11. Add a rating and comments if desired, and then select **Close**.
    
## Create an audience (if necessary)
<a name="CreateAudience"> </a>

If you want to redirect only a specific set of your users from your on-premises environment to OneDrive, you need to use an audience to identify that set of users. If you have an audience set up already that contains just those users, you can use that. Otherwise, you need to create an audience in SharePoint Server. See [Create an audience for SharePoint Server](../administration/create-an-audience-for-sharepoint-server.md) for information about how to create an audience for SharePoint. You can also use Microsoft PowerShell cmdlets to create an audience. 
  
 **To configure a OneDrive redirection audience**
  
1. On the **Central Administration** website, select **Microsoft 365** > **Configure hybrid OneDrive and Sites features**.
    
2. Select **Use a specific audience**, and for the audience that contains your Microsoft 365 users, enter the  *audience name*. 
    
3. Select **OK**.
    
## Verify that then OneDrive links work as expected
<a name="Verify"> </a>

It can take up to a minute for the changes to be updated in the User Profile service application for your on-premises farm. Because the link may be stored in the user's browser cache, we recommend you wait 24 hours and then verify the links are working.
  
To check that the links are working as expected, have one of the users in the audience that is using the Microsoft 365 option for OneDrive sign in to your on-premises environment. From the user's personal site, and from the navigation bar or app launcher, have the user select **OneDrive**. 
  
If the user is redirected to Microsoft 365 for OneDrive, everything is working as expected.
  
If users want to browse to their OneDrive directory directly, they can go to https:// _\<yourtenant name\>_.onedrive.com in the browser. For example, https://contoso.onedrive.com will take users of Contoso tenancy to their OneDrive document library. This is a simple way to bookmark the link for users of OneDrive. Rich clients might not recognize this short URL.
  
## (Optional) Create a search vertical
<a name="Verify"> </a>

You can set up a search vertical so that you can search content stored in OneDrive. The specific steps to set up the search vertical are in the article [Set up Search of OneDrive from SharePoint Server](set-up-search-of-onedrive-for-business-in-office-365-from-sharepoint-server.md).
  
## (Optional) Customize the Microsoft 365 navigation experience (SharePoint Server 2013)
<a name="CustomNav"> </a>

Now that your users are set up to be redirected to Office 365, you can customize what they see on the navigation bar there. By default, the navigation bar contains the following links: SkyDrive, Yammer or Newsfeed, and Sites. If you intend for your users to use only OneDrive, you can remove the other links. If you want to allow your users to interact with Yammer or the SharePoint Newsfeed features or to create team sites in Office 365, you can leave those links on the nav bar.
  
> [!NOTE]
> Turn on the appropriate navigation bar links for the set of SharePoint in Microsoft 365 service features that you have purchased. For example, if you have OneDrive with Office on the web, then you would turn on only the OneDrive link, and not the Sites or Newsfeed links. OneDrive with Office on the web does not include the Sites and Newsfeed features and users would see Access Denied messages if they selected the links. You can, however, still choose to turn on Yammer as your social network and then turn on the Yammer/Newsfeed navigation link. 
  
 **To customize the navigation bar**
  
1. Log on to Office 365 with an organization administrator account.
    
2. On the **Admin** tab, select **SharePoint**.
    
3. On the left, select **Settings**. 
    
4. In the **Top Navigation Bar User Experience** section, specify the links to show or hide on the nav bar. 
    
5. To save the settings and update the navigation bar, select **OK**. 
    
## See also
<a name="CustomNav"> </a>

#### Other Resources

[Plan for hybrid OneDrive](./plan-hybrid-onedrive-for-business.md)