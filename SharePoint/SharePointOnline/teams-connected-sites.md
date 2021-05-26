---
title: "Manage Teams connected sites"
ms.reviewer: 
ms.author: hokavian
author: Holland-ODSP
manager: pamgreen
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
ms.custom:
search.appverid:
- SPO160
- MET150

description: "Learn how to manage Teams connected sites."
---

# Learn how to manage Teams connected sites
  
In this article, learn more about how to identify, manage, and navigate between teams in Microsoft Teams, SharePoint team sites and channel sites.

### What’s a Teams connected channel site?
When you create a team in Microsoft Teams, a Microsoft 365 connected team site in SharePoint gets automatically created. This site is referred to as a Teams connected team site. This team site contains folders for each standard channel created from Microsoft Teams. Also, when you create a private channel in Microsoft Teams, a team site in SharePoint also gets automatically created. 

![Image of teams and channels in Microsoft Teams](media/overview-of-teams-channel-sites.png)

These sites are referred to as Teams connected channel sites. The SharePoint sites that are Teams connected team sites and channel sites are a specialized site type of SharePoint team site that has been optimized for its Teams connection.

![Image of Microsoft Teams channel site types](media/Teams-connected-sites.png)

You’ll notice that a handful of typical SharePoint team site features aren’t available in Teams connected team sites and channel sites, such as:
- The ability to select the start symbol (follow links) on sites, lists, and libraries.
- 2013 Workflows
- The InfoPath form option is not available


## How to identify and navigate between Microsoft Teams and connected sites

Teams connected team sites and channel sites include additional information to indicate the connection to Microsoft Teams. In the SharePoint team site header, you will see the Microsoft Teams icon following the site logo and site title. 


## Home site capabilities

When you set a site as your home site:

- It's easily accessible from the SharePoint mobile app for Android and iOS. All users that have access to the home site will see a home button on the Find tab of the mobile app. Being communication sites, home sites are designed to be mobile friendly from the start.

    ![Link to the home site in the SharePoint mobile app](media/home-site-fre.png)

- Search for the site is scoped to all sites within the organization. Having a great search experience is critical for the success of the home site. [Learn more about Microsoft Search](/microsoftsearch/overview-microsoft-search)

- The site is automatically set up as an [organization news site](organization-news-site.md). (Although you can have only one home site, you can have multiple organization news sites.)
- The site is enabled for [configuring the global navigation in the SharePoint app bar](sharepoint-app-bar.md#get-started-customizing-the-global-navigation-tab).

- Having a home site enables you to use [Viva Connections](https://docs.microsoft.com/SharePoint/viva-connections).

> [!NOTE]
> Integration between the home site and [SharePoint start page](https://support.office.com/article/6b85097a-87e0-4611-a29a-dfd49b1a1220) (where the branding, theming, header, navigation, and footer elements from the home site are applied to the start page and users can easily navigate between the pages) is not available at this time. Please watch for updates in the [Microsoft 365 roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=SharePoint).

## Plan and create your home site

To set a site as your organization's home site, you first need to create and customize the site you want to use.

1. When you design your organization's top landing page, consider the goals from the perspective of your IT department, your organization's communications team, and end users of the experience.
2. Create a communication site to use for the home site, and customize it using built-in features as much as possible:
    - Use the megamenu style for navigation and add a site footer. For info, see [Change the look of your SharePoint site](https://support.office.com/article/06bbadc3-6b04-4a60-9d14-894f6a170818).
    - Try out various page layouts, including the vertical section. For info, see [Add sections and columns](https://support.office.com/article/fc491eb4-f733-4825-8fe2-e1ed80bd0899).
    - Use [audience targeting](https://support.office.com/article/68113d1b-be99-4d4c-a61c-73b087f48a81) with SharePoint news and navigation links to tailor the experience for your audiences.
    - Use personalized web parts, preferably in a unique visual location like the vertical section with background color, which allows users to quickly consume organization content and get back to their work. 
    - Extend the site as needed by using the SharePoint Framework (SPFx). To get started building custom web parts, see [SharePoint Framework Tutorial 1](https://www.youtube.com/watch?v=S3tG2DE8tR8). For info about app extensions, see [Getting started with SharePoint Framework Application customizers](https://www.youtube.com/watch?v=gp056PEZoRQ&list=PLR9nK3mnD-OV6WhWHOMAvW-T_EBGKIs3u&index=18&t=0s).
    - Make sure the site is set up for regular content updates. Turn on [content approval](https://support.office.com/article/a8b2e689-d4a1-4639-8028-333c0ece30d9) to ensure high-quality content.
    - Consider making the site a [hub site](create-hub-site.md). Your home site can be registered as a hub site, but can't be associated with another hub.
3. Create a launch plan for redirecting from your current solution to the new home site and notifying users of the change.
**Important**: Make sure the site adheres to the [guidelines for healthy portals](./portal-health.md).
4. Optional (recommended): When you're ready to launch, [replace your root site with the new site](modern-root-site.md#replace-your-root-site).
5. To make the site a home site, follow the steps in the next section.
6. Make sure to [customize the Microsoft 365 theme for your organization](/office365/admin/setup/customize-your-organization-theme), adding your logo and linking it to the home site. 

## Set a site as your home site

After you create and customize the communication site that you want to use as your home site, you need to run a PowerShell cmdlet to set it as your home site. To run this cmdlet, you must be a site admin of the site.

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." <br>On the Download Center page, select your language and then click the Download button. You'll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you're running the 64-bit version of Windows or the x86 file if you're running the 32-bit version. If you don't know, see [Which version of Windows operating system am I running?](https://support.microsoft.com/help/13443/windows-which-operating-system). After the file downloads, run it and follow the steps in the Setup Wizard.

2. Connect to SharePoint as a [global admin or SharePoint admin](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run `Set-SPOHomeSite -HomeSiteUrl <siteUrl>`.

    (Where siteUrl is the site you want to use)
    
### Next, set up global navigation in the SharePoint app bar

The [SharePoint app bar](https://docs.microsoft.com/SharePoint/sharepoint-app-bar) is being released to customers. Once the SharePoint app bar is available in your tenant, [enable and customize global navigation](https://docs.microsoft.com/SharePoint/sharepoint-app-bar#customize-global-navigation-in-the-app-bar). Then, consider [integrating your home site in Microsoft Teams using Viva Connections](https://docs.microsoft.com/SharePoint/viva-connections). 

> [!NOTE]
> You can set only one site in your organization as a home site. The site can be registered as a hub site, but can't be associated with a hub. The first time you set up a home site, it might take up to several minutes for the changes to take effect. If you run the command again to switch your home site to a different site, it might take up to 2 hours.
