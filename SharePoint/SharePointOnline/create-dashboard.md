---
title: "Create the Viva Connections Dashboard (Preview)"
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
description: "Learn how to create the Viva Connections Dashboard"
---

# Create a Viva Connections Dashboard (Preview)

>[!NOTE]
>The information in this article relates to a preview product that may be modified before it's generally available.

The Viva Connections Dashboard provides fast and easy access to key employee data and job-related tasks targeted to users across roles, markets, and job functions. A Dashboard can be built with no code, or a developer can create custom cards to meet the specific needs of an organization.

![Image of a Dashboard example.](media/vc-hero2.png)

Once certain prerequisites are met, the Dashboard is authored on your home site.  You can add it to Teams so that it's easily accessible to your users' mobile devices and desktops. And, you can add it to your home page using the Dashboard web part.

The Dashboard consists of cards that provide for user interaction such as existing Teams apps, third-party apps, custom solutions, and internal and external links. 

As you are building the Dashboard, you can see an approximation of how it will look on different devices. If you've audience targeted by any of the cards, use **preview** mode to see how it will look for different audiences. Then publish your Dashboard to make it available to users who have access to your home site.

>[!NOTE]
>Images are an important aspect to making your cards rich and inviting. If you're a SharePoint admin, we recommend enabling a Content Delivery Network (CDN) to improve performance for getting images. Consider when storing images that /siteassets is by default a CDN source when Private CDN is enabled while /style library is the default source when the Public CDN is enabled. [Learn more about CDNs](/office365/enterprise/content-delivery-networks).  


This article includes:

- [Create a Dashboard and add cards to it](#create-a-dashboard-and-add-cards)
- [Add a Web link card](#add-a-web-link-card)
- [Add a Teams app card](#add-a-teams-app-card)
- [Audience targeting](#apply-audience-targeting-to-cards)
- [Preview your Dashboard to see how it will display for different audiences](#preview-your-dashboard-to-see-how-it-will-display-for-different-audiences)
- [Put the Dashboard on your home site using the Dashboard web part](#put-the-dashboard-on-your-home-site-using-the-dashboard-web-part)

## Create a Dashboard and add cards

You’ll need [edit permissions](/sharepoint/customize-sharepoint-site-permissions) on your home site.

1. On your home site, select the **Settings** gear at the top of the page.
2. Select **Set up Viva Connections**.
3. Select the **+ Create Dashboard** button.

The Dashboard page opens in Mobile view by default. 


   >[!NOTE]
   > - You can choose Mobile, Tablet, and Desktop views interchangeably as you’re authoring.
   > - Image recommendations for cards in the Dashboard: medium cards should be 300x150 to 400x200 with 2:1 aspect ratio and large cards 300x300 to 400x400 with 1:1 aspect ratio in order to prevent stretching in the mobile app.
   > - Image URLS in card properties must be an absolute URL in order for the link to work in the mobile app.


4. Select **+ Add a card**.

   ![Image of adding a dashboard card.](media/add-a-card.png)


5. Select the type of card you want to add from the Dashboard card toolbox and then follow the steps below to set up each type of card. As you’re building the Dashboard, you can preview its appearance in mobile, desktop, and tablet for different audiences.
Here are the built-in cards available now:

   [Web link](#add-a-web-link-card): Add an internal or external link

   [Assigned tasks](#add-the-assigned-tasks-card): Automatically display information to users about their assigned tasks.
 
   [Teams app](#add-a-teams-app-card): Use an existing Teams app or bot

 
6. When you're done adding cards and targeting audiences, and you’re satisfied with how the Dashboard looks in preview, select **Publish** at the top-right of your Dashboard to make it available for use on your home site, in Teams, and in Teams mobile app. The view will default to Desktop view after you’ve published the Dashboard.

## Add a Web link card

Add a web link card when you want your users to go to an internal or external link on a web site. To do this task, perform the following steps:

1. While in **edit** mode, select **+ Add a card** from the Dashboard.
2. Select **Web link** from the web toolbox.

   ![Adding a web link card.](media/add-web-link-card.png)


3. In the property pane on the right side of the page, select your options.

   ![Choosing options.](media/choosing-options.png)

4. Select a size for the card from the **Card size** drop-down list.
5. Enter the URL for your link in the **Link** text box. 
6. Set the card-display options:
   - Enter a title for the card in the **Card title** text box. (This title won't change your page title; it is the title that will be displayed on the top of the card.)
   - Enter a description for the card in the **Card description** text box. This description will be displayed in larger text under the title.
3. Under **Thumbnail**, select one of the following options:
   - **Auto-selected**: This option when chosen automatically displays an image at the top of your card that comes from your page.
   - **Custom image**: This option when chosen enables the **Change** button.  You can select this button to choose an image you want to use.
4. Under **Card icon**, select one of the following options that enable the icon to be displayed on the left side of the card title:
   - **Auto-selected**: This option when chosen automatically displays a built-in icon associated with the page.
   - **Custom image**: This option when chosen enables the **Change** button.  You can select this button to choose an image you want to use.
    - **Icon**: This option when chosen enables the **Change** button.  You can select this button to choose from a set of stock icons.
5. If you want to target your card to specific audiences (that is, only the audience you specify will see the card in the dashboard), select one or more groups to target from the **Audiences to target**. For more information on audience targeting, see [Audience targeting](#audience-targeting).



## Add the Assigned tasks card

The Assigned tasks card enables automatic display of information to users about their assigned tasks. This information is retrieved from the Tasks app in Teams.

![Adding a tasks card.](media/tasks-card.png)


1. While in edit mode, click **+ Add a card** from the dashboard.
2. Select **Assigned Tasks** from the Dashboard toolbox.

   ![Adding a tasks card in the dashboard.](media/assigned-tasks.png)

3. In the property pane on the right, choose your card size from the **Card size** drop-down list.

   ![Choosing card size.](media/choosing-card-size.png)

4. If you want to target your card to specific audiences (that is, only audience you specify will see the card in the dashboard), select one or more groups to target. For more information on audience targeting, see [Audience targeting](#audience-targeting).


## Add a Teams app card

A Teams app card allows you to create a card for an existing Teams app. To add a Teams app card:

1. While in **edit** mode, select **+ Add a card** from the Dashboard.
2. Select **Teams app** from the web toolbox.


   ![Adding a Teams app card.](media/teamsappicon.png)


3. In the **property** pane on the right side of the page, select your options.

   ![Teams app property pane.](media/teamsapp.png)

4. Select a size for the card from the **Card size** drop-down list.
5.  Search for the Teams app you want to use, and then select it from the list.
6.  Set the card-display options:
    - Enter a title for the card in the **Card title** text box. (This title won't change your page title; it is the title that will be displayed on the top of the card.)
    - Enter a description for the card in the **Card description** text box. This description will be displayed in larger text under the title.
7. If you want to target your card to specific audiences (that is, only audience you specify will see the card in the dashboard), select one or more groups to target. For more information on audience targeting, see [Audience targeting](#audience-targeting).

## Set up 3rd party applications and Microsoft apps

The Viva Connections dashboard and mobile experience can be extended and customized using cards, which are based on [adaptive cards](https://adaptivecards.io/) and the [SharePoint Framework (SPFx)](/sharepoint/dev/spfx/sharepoint-framework-overview). These adaptive cards are used to display data, complete tasks, and connect to Teams Apps, Websites, and mobile apps on Viva Connections. They provide a low-code solution to bring your line-of-business apps into the Dashboard. To create custom experiences on Viva Connections Dashboard and Viva Connections Mobile App, developers must use the SPFx to create custom ACEs. To learn more about creating ACEs, see the following tutorial: [Build your first SharePoint Adaptive Card Extension](/sharepoint/dev/spfx/viva/get-started/build-first-sharepoint-adaptive-card-extension). Learn more about [Viva Connections extensibility.](/sharepoint/dev/spfx/viva/overview-viva-connections)


### Use 3rd party applications
There are 2 ways to acquire partner solution packages and install them on the Viva Connections dashboard:
1.	Through Microsoft AppSource
    a.	Add an App via the SharePoint Homesite
    b.	Add an App via App Catalog
2.	Directly from the ISV/Partner

#### Acquire the solution package from a Microsoft AppSource

**Option A:** Add an App via the SharePoint Homesite - [Learn how to explore and deploy SharePoint Framework solutions from partners in SharePoint.](https://techcommunity.microsoft.com/t5/microsoft-sharepoint-blog/explore-and-deploy-sharepoint-framework-solutions-from-partners/ba-p/2645289)

**Option B:** Add an App via the App Catalog - [Learn how to manage apps using the App Catalog.](use-app-catalog#work-with-sharepoint-store-apps.md)

 >[!NOTE]
 > SharePoint administrative permissions are required to complete option B.

#### Or, acquire the solution package directly from the ISV

 >[!NOTE]
 > SharePoint administrative permissions are required to complete this task.

Once you receive the package from the ISV partner, follow the **Work with Custom Apps** steps in the [App Catalog guidance.](use-app-catalog#work-with-custom-apps.md) 



## Apply audience targeting to cards

By using audience targeting, you can promote cards to specific groups of people. This kind of targeting is useful when you want to present information that is especially relevant to a particular group of people. For example, you can target cards to a specific department.

### Set the target audiences for a card

1. If your page is not already in **edit** mode, click **Edit** at the top-right of the dashboard page.
2. Select the card you want to target to one or more audiences, and click the **Edit card** pencil from the toolbar on the left.
3. In the property pane on the right, under **Audiences to target**, type or search for the audience group(s) you want to target.


    >[!NOTE] 
    > If you've selected an audience group that you recently created or changed, it may take some time to see targeting applied for that group.


4. When a card is successfully audience targeted, you’ll see a **people** icon in the lower-left corner of the card.

   ![Audience targeting confirmation.](media/card-targeted-audience.png)


### Preview your dashboard to see how it will display for different audiences

What you see in *preview mode* approximates how the Dashboard will display for certain audiences and devices. When you apply audience targeting to cards, you can preview how different people will view the Dashboard depending on the audience or device - mobile, desktop, and tablet.
 
#### To preview different audiences:

   1. While in edit mode, select **Preview** on the top right.

      ![Audience targeting icon.](media/preview-option.png)


   2. Open the **Select audiences to preview as** drop-down list. (if no cards are audience targeted, you will see a disabled **Audience targeting** label).


   3. Search for and select a groups. Once added, the group will be selected by default. You can select the group again in the **Select audiences to preview as** drop-down list to de-select it.

     ![Audience targeting group label.](media/selecting-groups.png)

    - Cards that targeted to a specific group will display.
    - When one or more audiences are selected, cards that *do not* have audience targeting applied will also display.
    - If no audiences are targeted, only cards that *are not* audience targeted will display. If there aren't any cards with audience targeting applied, none will display.
    - If you are not part of one of the audiences you've selected, you will only see cards that are not audience targeted. If none are audience targeted, you won't see any cards.

   You can also see how your Dashboard will display on Mobile, Tablet, and Desktop by selecting those options.

   #### Examples:

   In the following example, the preview is set for Mobile.

   - The image on the left shows the view for a specific audience that includes 2 specific cards. 
   - In the second image on the right, the top two cards are not displayed when previewing a different audience group.

   ![Audience targeting example.](media/dashboard-preview-examples.png)
   


## Use the Dashboard web part for Viva Connections

>[!NOTE] 
> - After editing content on the Dashboard, it may take several minutes until the new content is available in the Dashboard web part.
> - For best results, we recommend placing the Dashboard web part in a right vertical section.

Once a Dashboard is authored and published, you can use the Dashboard web part to display it on your home site. You can add the web part to any section on your page.  

When added, it will automatically be populated with the cards from the existing Dashboard on your site. You'll be able to set the maximum number of cards you want to display. [Learn how to use the Dashboard web part](use-dashboard-web-part-on-home-site.md).



## More resources

[Step-by-step guide to setting up Viva Connections](guide-to-setting-up-viva-connections.md)