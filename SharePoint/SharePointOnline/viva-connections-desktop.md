---
title: Add Viva Connections desktop to Microsoft Teams (Desktop only)
ms.reviewer: 
ms.author: hokavian
author: Holland-ODSP
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: viva
ms.subservice: viva-connections
ms.localizationpriority: high
ms.collection:  
- Strat_SP_modern
- M365-collaboration
search.appverid:
- SPO160
- MET150
description: "Add Viva Connections desktop to integrate SharePoint resources into Microsoft Teams"
---

# Add the Viva Connections desktop app to Microsoft Teams (Desktop only)

>[!IMPORTANT]
> - This article covers the steps to deploy the Viva Connections desktop app, which is a custom line of business app for Microsoft Teams and is built using PowerShell provided by Microsoft. **This app includes the desktop experience only**. 
> - To set up the Viva Connections desktop *and* mobile experience, [review the step-by-step guidance.](guide-to-setting-up-viva-connections.md)

Microsoft [Viva Connections desktop](https://techcommunity.microsoft.com/t5/microsoft-viva-blog/microsoft-viva-connections-to-start-rollout-to-general/ba-p/2175802) was formerly known as the [Home site app](https://techcommunity.microsoft.com/t5/microsoft-sharepoint-blog/the-home-site-app-for-microsoft-teams/ba-p/1714255), which combines the power of your intelligent SharePoint intranet with chat and collaboration tools in Microsoft Teams. Viva Connections desktop enables users to discover and search relevant content, sites, and news from across the organization right from the Team’s app bar. Viva Connections desktop also allows you to incorporate your organization’s brand and identity directly in Teams. 

>[!NOTE]
> - Learn more about the different types of [Apps, bots, & connectors in Microsoft Teams](/microsoftteams/deploy-apps-microsoft-teams-landing-page).
> - Viva Connections desktop is available for GCC, but not GCC High or DoD environments.


## Benefits of using Viva Connections desktop

![Image of the SharePoint home site in Teams.](media/viva-features-2.png)

1.	**Highlight specific resources:** Viva Connections desktop uses the company-curated [global navigation](sharepoint-app-bar.md) links along with personalized content like sites and news, which are powered by [Microsoft Graph](/graph/overview). Global navigation is configured in SharePoint and can be accessed by selecting the icon in Teams app bar.

2.	**Navigate intranet resources in Teams:** Navigate to all modern SharePoint sites, pages, and news within Teams without losing context. All files will open in the Teams file preview window. 


3.	**Search for intranet content in Teams:** On the home page, you can search for intranet content in SharePoint by searching in the Teams search bar. Search results will be displayed on a SharePoint site in the browser.

    ![Image of a search on the home site in Teams.](media/viva-search-2.png)

4.	**Share content easily:** Features in the SharePoint site header will dynamically display tools that help users collaborate depending on the type of content being viewed. Tasks such as sharing a link to a SharePoint page in a Teams chat are much easier. 


> [!IMPORTANT]
> - You need SharePoint admin permissions (or higher) to create the Viva Connections desktop app in PowerShell, and you need Teams admin permissions (or higher) to apply the app in the Teams Admin Center.
> - Viva Connections desktop is not supported in the Teams mobile app. 
> - Only [modern SharePoint sites and pages](/sharepoint/dev/transform/modernize-classic-sites) can be viewed in Teams and all other content will open in a browser.
> - Some functionality will not be available for SharePoint pages viewed in Microsoft Teams such as social gestures like the ability to like, or comment on a page as well as the ability to add an event automatically to an Outlook calendar.
> - [Global navigation in the SharePoint app bar](sharepoint-app-bar.md) can be enabled to display global SharePoint resources in the Microsoft Teams app bar for Viva Connections desktop.
> - Global navigation menu links can be [audience targeted](https://support.microsoft.com/office/target-content-to-a-specific-audience-on-a-sharepoint-site-68113d1b-be99-4d4c-a61c-73b087f48a81) so that specific content is surfaced to certain groups of people. Audience targeting settings in the SharePoint global navigation menu will carry over to global navigation in Teams.
> - Search customizations applied to SharePoint sites will apply to search results in Teams when on the home site.
> All SharePoint out-of-the-box site headers are compatible with Viva Connections desktop. However, if you modify your SharePoint site to remove, or significantly change the site header, then these contextual actions may not be available to the user. 
> - Viva Connections desktop was originally announced as the [Home site app](https://techcommunity.microsoft.com/t5/microsoft-sharepoint-blog/the-home-site-app-for-microsoft-teams/ba-p/1714255).
> - Viva Connections will become generally available in fall 2021 and will include enhancements to the overall configuration and deployment experience.
> - The [Viva Connections desktop PowerShell script](https://www.microsoft.com/download/confirmation.aspx?id=102888) is available now in the [Microsoft download center](https://www.microsoft.com/download/default.aspx).
> - The vanity domain is only supported if the home site has the same domain as the [root site](modern-root-site.md).
> - Viva Connections is not supported on the Linux operating system.


## Watch how to create the app package and then upload it to Teams

 > [!VIDEO https://www.microsoft.com/videoplayer/embed/RWAVk1]  




## Prepare for Viva Connections desktop and Viva Connections
Viva Connections desktop can be provisioned through PowerShell and then will be [uploaded as an app in the Teams Admin Center](/microsoftteams/upload-custom-apps). Download the [Viva Connections for desktop PowerShell script](https://www.microsoft.com/download/confirmation.aspx?id=102888). The future version of Viva Connections will be automatically available through the Teams Admin Center. Prepare your organization for Viva Connections now, or soon, by reviewing the following requirements and recommendations:

> [!div class="mx-imgBorder"]
> ![Image of global navigation icon in the Teams app bar.](media/viva-landing-large.png)

#### Viva Connections desktop requirements:

- **Modern SharePoint sites and pages -** Only modern SharePoint sites and pages can be viewed in Teams and all other content will open in a browser. Learn more about how to [modernize classic SharePoint sites and pages](/sharepoint/dev/transform/modernize-userinterface-site-pages).


#### Viva Connections desktop recommendations:

- **SharePoint home site -** We highly recommend that you use the SharePoint home site as the landing experience for Viva Connections. If you don't already have a SharePoint [home site](home-site-plan.md), learn more about how to [plan home site navigation](information-architecture-modern-experience.md) and review considerations for [planning a global intranet](set-up-global-intranet.md).

- **Global navigation is enabled in SharePoint -** It is recommended that global navigation is enabled and customized in the [SharePoint app bar](sharepoint-app-bar.md) so that SharePoint resources appear in Teams.


## Step-by-step guide to setting up Viva Connections (desktop only)

Complete the following steps to enable Viva Connections desktop using [SharePoint PowerShell.](/powershell/sharepoint/sharepoint-online/introduction-sharepoint-online-management-shell)


1.	**Set up a SharePoint home site:** We highly recommend that you set up a [SharePoint home site](home-site.md) and use that site as the default landing experience for your users in Teams. 

2.	**Enable global navigation and customize navigational links:** We recommend you [set up and customize global navigation in the SharePoint app bar](sharepoint-app-bar.md). Learn about the different ways you can [set up the home site navigation and global navigation](./sharepoint-app-bar.md#see-all-the-different-ways-you-can-set-up-global-navigation) to surface the right content at the right time.

3.	**Create a Viva Connections app package in PowerShell:** The SharePoint admin needs to download and run PowerShell script from the Microsoft download center to create the Viva Connections desktop package. Ensure that you are using the [latest version](https://www.powershellgallery.com/packages/Microsoft.Online.SharePoint.PowerShell/16.0.20912.12000) of the [SharePoint Management Shell](/powershell/sharepoint/sharepoint-online/introduction-sharepoint-online-management-shell) tool before running the script. 

    > [!IMPORTANT]
    > - Updates to the required fields (mentioned below) in the manifest file are the only supported changes. Any other updates will not be supported. 
    > - SharePoint admin credentials are required to use SharePoint PowerShell.
    > - The SharePoint admin who creates the Viva Connections desktop package needs site owner permissions (or higher) to the home site in SharePoint.
    > - If your tenant is using an older version of PowerShell, uninstall the older version and replace it with the most [up to date version](https://www.powershellgallery.com/packages/Microsoft.Online.SharePoint.PowerShell/16.0.20912.12000).
    > - Icons need to be PNG files.

4.	**Provide tenant and site information to create the package:** Download the [Viva Connections for desktop PowerShell script](https://www.microsoft.com/download/confirmation.aspx?id=102888) and provide the information below.

> [!IMPORTANT]
> Updates to the required fields (mentioned below) in the manifest file are the only supported changes. Any other updates will not be supported. To take advantage of a mobile experience for Viva Connections, follow the guidance to [provision Viva Connections for desktop and mobile](/viva/connections/guide-to-setting-up-viva-connections).


**When you create a new package in PowerShell, you will be required to complete the following fields:**
    
 - **URL of your SharePoint modern communications site:** Provide the URL starting with "https://". This site will become the default landing experience for Viva Connections Desktop.

    - Provide the following details when requested:
    
       - **Name:** The name of your Viva Connections desktop package, as it should appear in Teams app bar.

       - **App short description (80 characters):** A short description for your app, which will appear in Teams app catalog.

       - **App long description (4000 characters):** A long description for your app, which will appear in Teams app catalog.

       - **Privacy policy:** The privacy policy for custom Teams apps in your organization (needs to start with https://). If you do not have a separate privacy policy, press `Enter` and the script will use the default SharePoint privacy policy from Microsoft.

       - **Terms of use:** The terms of use for custom Teams apps in your organization (needs to start with https://). If you do not have separate terms of use, press `Enter` and the script will use the default SharePoint terms of use from Microsoft.

       - **Company name:** Your organization name that will be visible on the app page in Teams app catalog in “Created By” section.

       - **Company website:** Your company’s public website (needs to start with https://) that will be linked to your company’s app name on the app page in Teams app catalog in “Created By” section.

       - **Icons:** You are required to provided two PNG icons, which will be used to represent your Viva Connections desktop app in Teams; a 192X192 pixel colored icon for Teams app catalog and a 32X32 pixel monochrome icon for Teams app bar. [Learn more about Teams icon guidelines](/microsoftteams/platform/concepts/build-and-test/apps-package#app-icons).
    
    > [!NOTE]
    > Microsoft does not have access to any information provided by you while running this script.

5.	**Upload the Viva Connections desktop package in the Teams Admin Center:** Once you successfully provide the details, a Teams app manifest, which is a .zip file, will be created and saved on your device. The Teams administrator of your tenant will then need to upload this app manifest to **Teams admin center > Manage apps**. 

Learn more about [how to upload custom apps in Teams admin center](/microsoftteams/upload-custom-apps).

6.	**Manage and pin the app by default for your users:** Once the Viva Connections desktop package is successfully uploaded in the Teams admin center, it can be managed like any other app. You can [configure user permissions](/microsoftteams/teams-app-permission-policies) to make this app available to the right set of users. Permitted users can then find this app in Teams app catalog. 

    We *highly recommend* that you pin this app by default for users in your tenant so that they can easily access their company’s intranet resources without having to discover the app in Teams app catalog. Use [Teams app setup policies](/MicrosoftTeams/teams-app-setup-policies) to pin this app by default in Teams app bar and then [apply this policy to a batch of users](/microsoftteams/assign-policies#assign-a-policy-to-a-batch-of-users).


### Then, onboard end users for Viva Connections desktop

Help end users understand [how to use Viva Connections](https://support.microsoft.com/office/your-intranet-is-now-in-micosoft-teams-8b4e7f76-f305-49a9-b6d2-09378476f95b) to improve workplace communication and collaboration. 

## How to add the mobile experience
If you have already provisioned Viva Connections desktop via PowerShell, and you want to add the mobile experience, you'll want to disable and uninstall the PowerShell version, and enable the [Viva Connections first party app from the Teams Admin Center](/viva/connections/add-viva-connections-app). 
<br>
Follow these instructions:

1. Follow the steps to [set up the Viva Connections app](/viva/connections/guide-to-setting-up-viva-connections#step-6-enable-the-viva-connections-app-in-the-microsoft-teams-admin-center) starting at Step 6. 
2. Keep the new instance of the Viva Connections app blocked but complete all of the other requirements.
3. Next, enable the new Viva Connections app.
4. Finally, disable and uninstall the **first version** of Viva Connections desktop.



## FAQs

**Q: Can any site be pinned as default landing experience in Teams?**

**A:** Modern SharePoint communication sites are eligible for pinning in Teams via Viva Connections. However, we **highly recommend** that you nominate a [home site in SharePoint](home-site.md) and pin that as the default landing experience for your users in Teams.
<br>
<br>


**Q: Can my classic SharePoint site be pinned in Teams?**

**A:** No, classic SharePoint sites are not supported in Microsoft Teams.
<br>
<br>

**Q: Do I need Viva Connections for the global navigation to show up in Teams?**

**A:** Yes, the global navigation menu links are stored in the home site of a tenant, and is required in order for the navigation panel to appear in Viva Connections in Teams. Learn more about how to [enable and set up global navigation in the SharePoint app bar](sharepoint-app-bar.md).
<br>
<br>

**Q: What happens if I don’t configure global navigation links before setting up Viva Connections?**

**A:** The user will still be able to access followed sites and recommended news by selecting the global navigation icon in Teams but will not have direct access to intranet navigational items.
<br>
<br>

**Q: What is the difference between using Viva Connections and adding a SharePoint page as a tab in Microsoft Teams?**

**A:** Viva Connections allows organizations to pin an organization-branded entry point to their intranet that creates an immersive experience, complete with navigation, megamenus, and support for tenant-wide search.  Viva Connections also provides quick access to organization curated resources, followed sites, and news like those provided by the SharePoint app. SharePoint pages can be [pinned as tabs in Teams](https://support.microsoft.com/office/add-a-sharepoint-page-list-or-document-library-as-a-tab-in-teams-131edef1-455f-4c67-a8ce-efa2ebf25f0b) channels provide ways to bring content directly into Team collaboration workspace, and these pages do not feature navigation and search elements.
<br>
<br>

**Q: Is this the same feature that was announced in fall 2020 as the Home site app?**

**A:** Viva Connections was originally announced as the [Home site app](https://techcommunity.microsoft.com/t5/microsoft-sharepoint-blog/the-home-site-app-for-microsoft-teams/ba-p/1714255) but will be called Viva Connections desktop moving forward.
<br>
<br>

**Q: When will Viva Connections for mobile become available?**

**A:** Following on our spring release of the desktop experience for Viva Connections desktop, we are rolling out an update that includes native mobile experiences for Teams on iOS and Android, enhancements to the overall IT configuration and deployment experience for the combined desktop and mobile app, as well as new Dashboard and Feed web parts for the desktop to complement the experience in the fall 2021. The experience that includes both mobile and desktop will be called Viva Connections.
<br>
<br>

**Q: What is the difference between Viva Connections desktop that's currently available through Powershell and the Viva Connections app that will become available this fall?**

**A:** The current iteration of the Viva Connections desktop (formerly known as the Home site app) is a Microsoft Teams custom app that customers build with the Viva Connections desktop PowerShell script and upload to Teams Admin Center to configure and deploy. This *only* includes the desktop experience.  The Viva Connections app that will be available in the fall is a Microsoft developed app, and when generally available, it will automatically appear in Teams Admin Center. This app includes *both* the desktop *and* mobile experiences.
<br>
<br>

**Q: Is there any difference in the desktop experience between the Viva Connections desktop app and Viva Connections app?**

**A:** No, there is no difference in the desktop experiences between the two Viva Connections app versions. 
<br>
<br>

**Q: I have already deployed Viva Connections desktop, and I would like to also deploy the mobile experience. Can I use Viva Connections app when it is available in the Teams admin center this fall?**

**A:** Yes, you can switch from Viva Connections desktop to Viva Connections app by blocking the first version and enabling the new version in the Teams Admin Center. You will need to ensure that you have completed the steps to prepare the mobile experience prior to enabling the new Viva Connections app. 



## More resources

[Set up a home site for your organization](home-site-plan.md)

[Enable and set up global navigation in the SharePoint app bar](sharepoint-app-bar.md)

[Introduction to SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/introduction-sharepoint-online-management-shell)

[Learn more about Viva Connections](viva-connections-overview.md)
