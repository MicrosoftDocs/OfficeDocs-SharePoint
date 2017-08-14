---
title: Configure hybrid OneDrive for Business
ms.prod: SHAREPOINT
ms.assetid: f1dfdac2-81ad-452f-b5b6-df9e5a8e976e
---


# Configure hybrid OneDrive for Business
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** Office 365, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-06-22* **Summary:** Connect your on-premises SharePoint Server environment with OneDrive for Business in Office 365. **This article is part of a roadmap of procedures for configuring SharePoint hybrid solutions. Be sure you're  [following a roadmap](html/sharepoint-server-2016-hybrid-configuration-roadmaps.md) when you do the procedures in this article.**You can redirect users to OneDrive for Business in Office 365 when they click **OneDrive** or **Sites** on the navigation bar. In this article are the steps you need to configure your on-premises environment to connect with OneDrive for Business in Office 365. You can find an overview of the process in [Plan for hybrid OneDrive for Business](html/plan-for-hybrid-onedrive-for-business.md).
## Some things that you need

To use OneDrive for Business in Office 365, your users must have **Create Personal Site** and **Follow People and Edit Profile** permissions. Both are controlled by the user permissions in the User Profile service application. ****
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. In your on-premises SharePoint Server environment, go to **Central Administration** > **Manage Service Applications**.
    
  
3. Click the User Profile Service Application.
    
  
4. On the **Manage Profile Service** page, under **People**, click **Manage User Permissions**.
    
  
5. In the **Permissions for User Profile Service Application** dialog box, click **All Authenticated Users** (or a specific audience that you intend to use as a pilot group of users).
    
  
6. Verify that the **Create Personal Site** and **Follow People and Edit Profile** permission check boxes are selected.
    
  
When you configure the OneDrive for Business link, you need to know the URLs for your My Sites site collection in SharePoint Server and in SharePoint Online.To find the My Sites URL in Office 365, on the **Admin** menu, click **SharePoint**. In the **Site Collections** list, look for the site collection that contains <domain>-my.sharepoint.com.
## Create an audience (if necessary)
<a name="CreateAudience"> </a>

If you want to redirect only a specific set of your users from your on-premises environment to OneDrive for Business in Office 365, you need to use an audience to identify that set of users. If you have an audience set up already that contains just those users, you can use that. Otherwise, you need to create an audience in SharePoint Server 2016. See **Create an audience for SharePoint 2013** for information about how to create an audience for SharePoint. You can also use Microsoft PowerShell cmdlets to create an audience.If you want all users to be redirected to Office 365 for OneDrive for Business, select **Everyone** instead of using a specific audience when you configure the settings.For specific steps to create an audience, see **Create an audience for SharePoint 2013**.
## Configure hybrid OneDrive for Business settings in Central Administration
<a name="ConfigureCA"> </a>

Now you can configure the settings in Central Administration to set up the redirection to Office 365. **To configure OneDrive for Business redirection**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the Central Administration website, choose **Office 365** > **Configure hybrid OneDrive and Sites features**.
    
  
3. On the **Configure hybrid OneDrive and Sites features** links page, in the **My Site URL** box, type the *My Site*  *URL*  that you got from Office 365 portal administration.
    
  
4. Specify an audience. Choose **Everyone** if you want all users to be redirected. Or choose **Use a specific audience** and type the *audience name*  for the audience that contains your Office 365 users.
    
  
5. Choose the **OneDrive only** option.
    
  
6. Choose **OK**.
    
  

## Verify that then OneDrive for Business links work as expected
<a name="Verify"> </a>

It can take up to a minute for the changes to be updated in the User Profile service application for your on-premises farm. Because the link may be stored in the user’s browser cache, we recommend you wait 24 hours and then verify the links are working.To check that the links are working as expected, have one of the users in the audience that is using the Office 365 option for OneDrive for Business sign in to your on-premises environment. From the user's personal site, have the user choose **OneDrive** from the app launcher.If the user is redirected to Office 365 for OneDrive for Business, everything is working as expected.If users want to browse to their OneDrive for Business directory directly, they can go to https:// *<yourtenant name>*  .onedrive.com in the browser. For example, https://contoso.onedrive.com will take users of Contoso tenancy to their OneDrive for Business document library. This is a simple way to bookmark the link for users of OneDrive for Business. Note that rich clients might not recognize this short URL.
## (Optional) Create a search vertical
<a name="Verify"> </a>

You can set up a search vertical so that you can search content stored in OneDrive for Business. The specific steps to set up the search vertical are in the article  [Set up Search of OneDrive for Business in Office 365 from SharePoint Server](html/set-up-search-of-onedrive-for-business-in-office-365-from-sharepoint-server.md).
## (Optional) Customize the Office 365 navigation experience
<a name="CustomNav"> </a>

Now that your users are set up to be redirected to Office 365, you can customize what they see on the navigation bar there. By default, the navigation bar contains the following links: SkyDrive, Yammer or Newsfeed, and Sites. If you intend for your users to use only OneDrive for Business, you can remove the other links. If you want to allow your users to interact with Yammer or the SharePoint Newsfeed features or to create team sites in Office 365, you can leave those links on the navigation bar.
> [!NOTE:]

  
    
    

 **To customize the navigation bar**
1. Log on to Office 365 with a tenant administrator account.
    
  
2. On the **Admin** tab, choose **SharePoint**.
    
  
3. Choose **Settings** on the left.
    
  
4. In the **Top Navigation Bar User Experience** section, specify the links to show or hide on the navigation bar.
    
  
5. Choose **OK** to save the settings and update the navigation bar.
    
  

# See also

#### 

 [Plan for hybrid OneDrive for Business](html/plan-for-hybrid-onedrive-for-business.md)
  
    
    

  
    
    

