---
title: "The Viva Connections Dashboard web part(Preview)"
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
description: "Learn how to use the Dashboard web part on your home site"
---

# The Viva Connections Dashboard web part (Preview)

>[!NOTE]
>The information in this article relates to a preview product that may be modified before it's generally available.
> 

Viva Connections is an integrated employee experience, and the Viva Connections Dashboard brings together resources for different employee groups to provide a comprehensive view of everything they need. For example, the Dashboard could include a card that allows users to access cafeteria menus, schedules, reports, shift schedules, HR notices, and more.
Once a Dashboard is authored, you can use the Dashboard web part to display it on your home site. Note that if you want to add, remove, or reorder cards, the existing Dashboard on your site must be edited. To learn how to create or edit a Dashboard, see [Create a Viva Connections Dashboard](https://docs.microsoft.com/en-us/SharePoint/create-dashboard).

## Add the Dashboard web part

To add a Dashboard web part, firstly ensure that you are in the **edit** mode. To do this, select **Edit** at the top-right of the home site page.

Once in **edit** mode, perform the following steps:

1. Hover your mouse around the section within which you want to place the web part, and select the **circled +**.

:::image type="content" source="media/selecting-spot-for-Dashboard-web-part.png" alt-text="The screen displaying the option that allows you to determine the spot at which the web part will be placed":::

2. In the web part search box, enter **Dashboard** to quickly find and select the **Dashboard (Preview) for Viva Connections** web part.

:::image type="content" source="media/searching-selecting-web-part.png" alt-text="The screen on which you can search for a web part and select it once displayed":::

The web part will be added to your page where it is populated with the cards from the existing Dashboard on your site, as in this example where the Dashboard is placed in a vertical column on the right:

:::image type="content" source="media/display-of-web-card.png" alt-text="The screen that displays the web card":::

3. Optionally, you can change the title of the Dashboard by selecting it in the web part and typing over it with your own title.

:::image type="content" source="media/editing-title-of-Dashboard.png" alt-text="The screen that displays the option that allows you to edit the title of a Dashboard":::

4. To move the web part, select the **Move web part** icon and drag the web part to a different section or column on the page.

:::image type="content" source="media/changing-location-of-web-part.png" alt-text="The screen displaying the option that allows you to move the web part to another location":::

5. To set the value for maximum number of cards to display on the web part, select the **Edit web part** pencil icon.

:::image type="content" source="media/editing-web-part.png" alt-text="The screen displaying the option that allows you to edit a web part":::

6. Use the slider to indicate the maximum number of cards to display.

:::image type="content" source="media/defining-threshold-cards-to-display.png" alt-text="The screen displaying the option by which you can define the count of the cards to be displayed":::

> [!NOTE]
> When there are more cards available than the maximum number set for the web part, users can select **See all** to see the rest of them.

7. Once the card-count threshold is set, select **Publish** or **Republish** to make the page available with your newly placed Dashboard web part.

:::image type="content" source="media/republishing.png" alt-text="The screen displaying the republish option":::


## Additional information

- **The Dashboard web part is hidden when there are no cards to show**: There may be no cards to show when the Dashboard author has targeted cards for specific audiences, and people outside of those audiences are viewing the page. For example, if all cards are targeted to your development group, only people in the development group will see the Dashboard.

> [!IMPORTANT]
> *Known issue (7/30/21): The title of the Dashboard shows even when the Dashboard is hidden. A temporary workaround is to make the title blank. This issue will be fixed before General Release.*

- **We recommend you use the Dashboard web part in a vertical section**: Although a vertical section is recommended, the web part can be used in any section in 1, 2, or 3 column layouts. Here’s an example of a Dashboard web part in a horizontal section:

:::image type="content" source="media/Dashboard-web-part-horizontal-section.png" alt-text="The screen displaying the web part in a horizontal layout":::

- **The Dashboard web part can be added to any page on your home site**: The Dashboard is most useful on your home page, but it is possible to add it to any page on your home site. One practical use for doing this is to experiment with your page layout to see where you think the Dashboard will fit best. To do this, just create a copy of your home page and start experimenting.
- **The Dashboard web part can be used in sections with a colored background**: When editing a section, you can change the background of the section and the cards of the Dashboard will have a different color from that background.

> [!IMPORTANT]
> *Known issue (7/30/21): Card color sometimes match the section background color. This will be fixed prior to General Release.*

:::image type="content" source="media/card-color.png" alt-text="The screen indicating the color of the card":::

- **“See all” appears on the top-right of the Dashboard web part** when there are more Dashboard cards available than can be displayed in the Dashboard web part. When **See all** is selected, a page that shows the entire Dashboard is displayed.

:::image type="content" source="media/full-display-Dashboard.png" alt-text="The screen displaying a full view of the Dashboard":::


