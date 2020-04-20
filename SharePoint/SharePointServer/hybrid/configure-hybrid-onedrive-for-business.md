---
title: "Configure hybrid OneDrive for Business"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 10/20/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
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
description: "Learn how to connect your on-premises SharePoint Server environment with OneDrive for Business in Office 365."
---

# Configure hybrid OneDrive for Business

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]
  
 **This article is part of a roadmap of procedures for configuring SharePoint hybrid solutions. Be sure you're [following a roadmap](configuration-roadmaps.md) when you do the procedures in this article.**
  
You can redirect users to OneDrive for Business in Office 365 when they click **OneDrive** or **Sites** on the navigation bar or the app launcher. In this article are the steps you need to configure your on-premises environment to connect with OneDrive for Business in Office 365. You can find an overview of the process in [Plan for hybrid OneDrive for Business](/sharepoint/hybrid/plan-hybrid-onedrive-for-business).
  
## Video demonstration

This video shows a walkthrough of configuring hybrid OneDrive for Business.
  
**Video: Configure hybrid OneDrive for Business**

> [!VIDEO https://www.microsoft.com/videoplayer/embed/a65546fb-4981-4a66-a9b6-0659382b5efb?autoplay=false]
> [!NOTE]
> The SharePoint Migration Tool demonstrated in the video is currently in preview. It is only supported for SharePoint Server 2013. [Download the SharePoint Migration Tool](https://spmtreleasescus.blob.core.windows.net/install/default.htm).
  
## Configure user permissions

To use OneDrive for Business in Office 365, your users must have **Create Personal Site** and **Follow People and Edit Profile** permissions. Both are controlled by the user permissions in the User Profile service application. 
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. In your on-premises SharePoint Server environment, go to **Central Administration** > **Manage Service Applications**.
    
3. Click the User Profile Service Application.
    
4. On the **Manage Profile Service** page, under **People**, click **Manage User Permissions**.
    
5. In the **Permissions for User Profile Service Application** dialog box, click **All Authenticated Users** (or a specific audience that you intend to use as a pilot group of users). 
    
6. Verify that the **Create Personal Site** and **Follow People and Edit Profile** permission check boxes are selected. 
    
## Configure hybrid OneDrive for Business
<a name="Configure"> </a>

To configure hybrid OneDrive for Business, you must be both a SharePoint Server farm administrator and an Office 365 global administrator. Perform these steps on a server in your SharePoint Server farm.
  
 **To configure hybrid OneDrive for Business**
  
1. In the SharePoint Online admin center, in the left navigation, click **configure hybrid**.
    
2. Click **Go to Hybrid Picker Download Page**.
    
3. On the SharePoint Hybrid Picker page, click **click here**.
    
4. Accept the security prompts to install and run the wizard.
    
5. On the **SharePoint Hybrid Picker** page, click **Next**.
    
6. On the **Credentials** page, verify your on-premises credentials and enter your global administrator credentials. Click **Validate credentials**, and then click **Next**.
    
7. On the **Checking prerequisites** page, click **Next**.
    
8. On the **Select the features you want to use in your hybrid environment** page, select the Hybrid OneDrive check box and deselect any other check boxes. Click **Next**.
    
9. When the configuration completes, click **Next**.
    
10. Add a rating and comments if desired, and then click **Close**.
    
## Create an audience (if necessary)
<a name="CreateAudience"> </a>

If you want to redirect only a specific set of your users from your on-premises environment to OneDrive for Business in Office 365, you need to use an audience to identify that set of users. If you have an audience set up already that contains just those users, you can use that. Otherwise, you need to create an audience in SharePoint Server. See [Create an audience for SharePoint Server](../administration/create-an-audience-for-sharepoint-server.md) for information about how to create an audience for SharePoint. You can also use Microsoft PowerShell cmdlets to create an audience. 
  
 **To configure a OneDrive for Business redirection audience**
  
1. On the Central Administration website, choose **Office 365** > **Configure hybrid OneDrive and Sites features**.
    
2. Choose **Use a specific audience** and type the  *audience name*  for the audience that contains your Office 365 users. 
    
3. Click **OK**.
    
## Verify that then OneDrive for Business links work as expected
<a name="Verify"> </a>

It can take up to a minute for the changes to be updated in the User Profile service application for your on-premises farm. Because the link may be stored in the user's browser cache, we recommend you wait 24 hours and then verify the links are working.
  
To check that the links are working as expected, have one of the users in the audience that is using the Office 365 option for OneDrive for Business sign in to your on-premises environment. From the user's personal site, have the user choose **OneDrive** from the navigation bar or app launcher. 
  
If the user is redirected to Office 365 for OneDrive for Business, everything is working as expected.
  
If users want to browse to their OneDrive for Business directory directly, they can go to https:// _\<yourtenant name\>_.onedrive.com in the browser. For example, https://contoso.onedrive.com will take users of Contoso tenancy to their OneDrive for Business document library. This is a simple way to bookmark the link for users of OneDrive for Business. Note that rich clients might not recognize this short URL.
  
## (Optional) Create a search vertical
<a name="Verify"> </a>

You can set up a search vertical so that you can search content stored in OneDrive for Business. The specific steps to set up the search vertical are in the article [Set up Search of OneDrive for Business in Office 365 from SharePoint Server](set-up-search-of-onedrive-for-business-in-office-365-from-sharepoint-server.md).
  
## (Optional) Customize the Office 365 navigation experience (SharePoint Server 2013)
<a name="CustomNav"> </a>

Now that your users are set up to be redirected to Office 365, you can customize what they see on the navigation bar there. By default, the navigation bar contains the following links: SkyDrive, Yammer or Newsfeed, and Sites. If you intend for your users to use only OneDrive for Business, you can remove the other links. If you want to allow your users to interact with Yammer or the SharePoint Newsfeed features or to create team sites in Office 365, you can leave those links on the navigation bar.
  
> [!NOTE]
> Turn on the appropriate navigation bar links for the set of SharePoint Online service features that you have purchased. For example, if you have OneDrive for Business with Office on the web, then you would turn on only the OneDrive for Business link, and not the Sites or Newsfeed links. OneDrive for Business with Office on the web does not include the Sites and Newsfeed features and users would see Access Denied messages if they clicked the links. You can, however, still choose to turn on Yammer as your social network and then turn on the Yammer/Newsfeed navigation link. 
  
 **To customize the navigation bar**
  
1. Log on to Office 365 with a tenant administrator account.
    
2. On the **Admin** tab, choose **SharePoint**.
    
3. Choose **Settings** on the left. 
    
4. In the **Top Navigation Bar User Experience** section, specify the links to show or hide on the navigation bar. 
    
5. Choose **OK** to save the settings and update the navigation bar. 
    
## See also
<a name="CustomNav"> </a>

#### Other Resources

[Plan for hybrid OneDrive for Business](/sharepoint/hybrid/plan-hybrid-onedrive-for-business)

