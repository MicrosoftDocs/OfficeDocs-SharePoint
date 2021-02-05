---
title: Use the new SharePoint app bar and set up global navigation
ms.reviewer: 
ms.author: hokavian
author: Holland-ODSP
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection:  
- Strat_SP_modern
- M365-collaboration
search.appverid:
- SPO160
- MET150
ROBOTS: NOINDEX, NOFOLLOW
description: "Use the SharePoint app bar to enhance intranet wayfinding and display personalized content "
---

# Introduction to the SharePoint app bar

Help users find important content and resources no matter where they are in SharePoint. The SharePoint app bar is designed to improve the global wayfinding experience while dynamically displaying personalized sites, news, and files. The app bar can be accessed on the left-hand side anywhere in SharePoint.

<<<image 1>>>


## The SharePoint app bar experience
The SharePoint app bar brings together intranet resources and personalized content like sites, news, and files. Enable global navigation to allow users to easily navigate to important intranet resources anywhere in SharePoint. Customize global navigation details and [Microsoft Graph](https://docs.microsoft.com/graph/overview) will do the rest of the work by dynamically displaying and updating personalized content for sites, news, and files.

<<<image 2>>>

>[!NOTE]
> - Global navigation is the only app bar tab that can be customized. 
> -	When global navigation is disabled or not configured, the home icon links to the SharePoint start page.
> -	Specific SharePoint app bar tabs cannot be disabled. 
> -	The SharePoint app bar cannot be disabled on specific sites. 
> -	The SharePoint app bar is not available on classic SharePoint sites today, however soon administrators will be able to add it to classic sites manually. 
> -	The SharePoint app bar may impact current page customizations specifically those that appear on the left side. 
> -	Personalized content in the SharePoint app bar is enabled by Microsoft Graph.
> -	When Microsoft Graph is disabled, the news and sites experience will be degraded.
> -	The SharePoint app bar can be temporarily disabled between today and when it becomes available to all customers to give customers more time to prepare for this change. Temporarily disabling the ap bar will delay the roll out of this feature in your organization until October 2021.


## Customize global navigation in the app bar
Global navigation can be enabled and customized in the SharePoint app bar. Customize the global navigation logo, title, and source depending on your users’ and organization’s needs. If you choose to keep global navigation disabled, the home icon will link to the SharePoint start page.


>[!NOTE]
> -	When global navigation is disabled, the home icon will link to the SharePoint start page.
> -	Customizing global navigation requires a [home site](https://docs.microsoft.com/sharepoint/home-site).
> -	Site owner permissions (or higher) to the home site are required to enable global navigation.
> -	Users need read access (or higher) to the home site to view the global navigation links. 
> -	[Audience targeting](https://support.microsoft.com/office/target-content-to-a-specific-audience-on-a-sharepoint-site-68113d1b-be99-4d4c-a61c-73b087f48a81?ui=en-US&rs=en-US&ad=US) can be applied to menu links in global navigation.
> -	Implementing global navigation may take up to 24 hours for the changes to take effect for users.


### Get started customizing the global navigation tab
1.	Set up a [home site](https://docs.microsoft.com/sharepoint/home-site) if your organization doesn’t already have one and make sure to [share the home site](https://support.microsoft.com/office/share-a-site-958771a8-d041-4eb8-b51c-afea2eae3658) with everyone in your tenant to ensures all users can access the global navigation links. 
2.	Navigate to your organization’s home site. 
3.	Select **Settings** and then select **Global navigation settings**.

<<<image 3>>>

>[!NOTE]
> -	If you do not see **Global navigation** in the **Settings** pane on the home site, you may not have site owner permissions (or higher) to the home site.

4.	Switch the **Enable global navigation** toggle to **On**.

<<<image 4>>>

5.	Next, add the **Logo** for global navigation that will be recognizable to users to replace the home icon in the app bar. No action is needed if you choose to keep the default home icon. 
<br>
Global navigation logo specifications:
- The logo size should be 20x20 pixels
- PNG file type
- Transparent background recommended 

6.	Then, enter a **Title** that will be displayed at the top of the global navigation pane.

<<<image 5>>>

7.	Finally, determine the **Navigation source**. Learn more about selecting a source.
8.	Make edits to the selected global navigation source if needed by selecting **Edit global navigation**. Select **Save** when you are done. Updates to global navigation may take several minutes before they appear.

<<<image 6>>>

>[!NOTE] 
> -	The global navigation source can be edited at any time by site owners or admins of the home site.
> -	The site and global navigation [links and labels](https://support.microsoft.com/office/customize-the-navigation-on-your-sharepoint-site-3cd61ae7-a9ed-4e1e-bf6d-4655f0bf25ca) can be edited at any time by editors of the home site.
> -	Implementing global navigation may take up to 24 hours for the changes to take effect.


### Determine the global navigation source depending on your home site’s configuration:
If you haven’t set up your [home site](https://docs.microsoft.com/sharepoint/home-site), do that first and if you are setting up a home site specifically to implement global navigation, review this guidance.

#### For home sites that are a hub, you have two source options:

<<<image 7>>>

- Select the site navigation source to display the home site’s navigation.
- Select the Hub or global navigation source to display the home site’s hub navigation.

>[!NOTE] 
> When you apply the extended header layout to the site, you will no longer see the hub navigation.


#### For home sites that are not a hub, you have two source options:

- Select the site navigation source to display the home site navigation.
- Create a secondary set of navigation notes specifically for the global navigation panel by selecting **Hub or global navigation**. Then, select **Edit global navigation** to create the new global navigation menu. Select **Save** when you are done.


>[!NOTE]
> For home sites that are not a [hub site](https://support.microsoft.com/office/what-is-a-sharepoint-hub-site-fe26ae84-14b7-45b6-a6d1-948b3966427f) and choose to create a secondary set of navigational nodes for the global navigation pane - if you decide to make your home site a hub in the future, the new hub site navigation will inherit the current navigational nodes for global navigation and can be [edited at any time](https://support.microsoft.com/office/customize-the-navigation-on-your-sharepoint-site-3cd61ae7-a9ed-4e1e-bf6d-4655f0bf25ca). 


## See all the different ways you can set up global navigation
Depending on the content you want to make available in the global navigation, you can configure your home site navigation and global navigation in three different ways.

<<<image 8>>>

### Display the home site’s navigation in global navigation
Display hub and site navigation on the home page, and the home site navigation in the global navigation panel.
1.	Navigate to the home site’s **Settings** and then **Global navigation**.
2.	**Enable** global navigation, enter a **Title**, and then select **Home site navigation** as the source.
3.	Select **Save**. Changes may take a few minutes to reflect.

<<<image 9>>>

### Display the home site’s hub navigation in global navigation
Display hub and site navigation on the home page, and the hub navigation in the global navigation panel. 
1.	Navigate to the home site’s **Settings** and then **Global navigation***.
2.	**Enable** global navigation, enter a **Title**, and then select **Hub or global navigation** as the source.
3.	Select **Save**. Changes may take a few minutes to reflect.

<<<image 10>>>

### Hide the site navigation and display it in the global navigation
Display just the hub navigation on the home page, and the site navigation in the global navigation panel. 
1.	Start by hiding the site navigation using one of two methods:
<br>

- Go to **Setting** then **Change the look**, then **Navigation** and toggle the **Display site navigation** to **Hide**
- Go to **Setting**, then **Change the look**, then **Header** and choose **Extended**

2.	Then, navigate to the home site’s **Settings** and then **Global navigation**.
3.	**Enable** global navigation, enter a **Title**, and then select **Home site navigation** as the source.
4.	Select **Save**. Changes may take a few minutes to reflect.

<<<image 11>>>





