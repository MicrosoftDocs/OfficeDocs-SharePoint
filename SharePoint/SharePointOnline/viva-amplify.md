---
title: "Microsoft Viva Amplify - Private preview"
ms.reviewer:
ms.author: v-smandalika
author: v-smandalika
manager: dansimp
recommendations: true
ms.date: 01/04/2023
audience: Admin
f1.keywords:
- CSH
ms.topic: overview
ms.service: sharepoint-online
ms.collection: M365-collaboration
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 479cfd6b-900b-46aa-b497-c13787771d3f
description: Learn about Viva Amplify
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
---

# Microsoft Viva Amplify - Private preview

> [!NOTE]
> Microsoft Viva Amplify is currently in Private preview and, hence, available only to Private preview customers.

Microsoft Viva Amplify is an internal communication campaign that allows you to create something once and publish it to multiple distribution channels to share throughout the organization. Hence, creating a campaign is the first step in the end-to-end content management process that involves creating content and publishing it.

Once you create a campaign, you can create the content on the **Main canvas** screen, and then publish the content.

To create a campaign, perform the following steps:

1. Launch the URL https://microsoft.sharepoint-df.com/_layouts/15/viva-amplify.aspx.
2. Provide your credentials and sign in to the Microsoft Viva Amplify portal.
3. Select **+ Create a campaign**.
   The **Create a new campaign** screen is displayed.
4. Select **Create a campaign** on the bottom-left corner of the screen.
5. Enter the details for the text boxes and select **Next**.
6. From the **Add members to your campaign** text box, choose the person whom you want to add as a member of your campaign.
7. Select **Add to list**.
   The chosen person is added as a member of your campaign.
8. Select **Create a campaign**.
   The campaign is successfully created and is listed on the **Amplify Hub** screen.

Once your campaign is displayed on the **Amplify Hub** screen, select the campaign. You're taken to the screen that is specific to the created campaign.

1. Select **Amplify Template** under the **Create** pane.

   :::image type="content" source="campaign-screen.png" alt-text="The screen displaying details of the created campaign.":::

   You're taken to the screen on which the **Distribution channels** tab is selected by default.

   :::image type="content" source="media/distribution-channels-screen.png" alt-text="Distribution channels screen you're taken to by default after selecting Amplify Template":::

   > [!NOTE]
   > Currently, Microsoft Viva Amplify supports **Outlook** and **SharePoint** distribution channels. 

2. Enter a title in the portion that reads **Add a title**

   :::image type="content" source="media/add-a-title.png" alt-text="The portion in the Distribution channels screen at which you enter a title.":::

1. Hover over the screen and you'll be presented with the **+** icon.
1. Select this icon, and the list of web parts are launched.

   :::image type="content" source="list-of-web-parts.png" alt-text="The list of web parts being displayed.":::

1. Select the web part you want and create the content.

   > [!NOTE]
   > You have the auto save option and hence you don't need to manually save the content and for every subsequent change made.

   For example: 
    1. If you select the **Image** web part to insert images, you're taken to the **Recent images** screen.
        1. Select **Stock images** and select the image you want to import into the article.
        1. Once the image is imported into the article, click anywhere on the image pane. You're presented with the options bar.
        :::image type="content" source="media/options-bar.png" alt-text="The menu bar for the web parts.":::
        1. Click the "pencil" icon. The **Image** pane on the right side of the screen is displayed.
           :::image type="content" source="media/image-pane.png" alt-text="The Image pane.":::
           You can enter a link for the image to be accessed, text on the image by enabling the **Add text over image** option.

    1. If you select the **Text** web part to add text, text boxes are displayed for you to add text.
      :::image type="content" source="media/text-boxes-for-text-web-part.png" alt-text="Text boxes displayed after selecting Text web part.":::

      You can add theme colors, insert images or tables within the text boxes.

    1. If you select the **People** web part to add names and/or email address(es), you're presented with portions in which you can add names or email addresses.
      :::image type="content" source="media/portion-for-email-name.png" alt-text="The portions in which you can add email addresses or names.":::
        1. Click anywhere on the **People profiles** pane. You're presented with the options bar.
           :::image type="content" source="media/options-bar-people-web-part.png" alt-text="The menu bar containing options.":::
           You can enter names and/or email address(es) in **Small**, **Medium**, or **Large** layouts.

    > [!NOTE]
    > Once you make changes like adding text and links to images, adding tables and theme colors to text, or using multi-sized layouts, click the X button on the right-side pane. You're taken to **Distribution channels** pane.
    > 
    > :::image type="content" source="media/distribution-channels-pane.png" alt-text="The Distribution channels pane on the right side of the screen.":::

2. Once you've created content and made changes, click the "preview" icon under the distribution channel through which you want the content to be published.

   :::image type="content" source="media/preview-icon.png" alt-text="The preview icon associated with the distribution channels.":::

When you make these changes through the web parts and preview the created content with its formatting changes, [deviations](#deviations) occur.

> [!NOTE]
> Deviations are applicable only to the **Outlook** distribution channel and not to the SharePoint distribution channel. For more information, see [Deviations](#deviations) and [Deviations in Outlook distribution channel](#deviations-in-outlook-distribution-channel).
>
> There are no deviations in the web parts when they're being transpiled to the **SharePoint** distribution channel. The reason is that the **Main canvas** screen itself is a type of SharePoint site.

For example, when you click the "preview" icon under the **Outlook** distribution channel, you're presented with a message that reads as follows:

**Some properties like text on images, columns, and medium and large people web parts may have been changed for this distribution channel.**

:::image type="content" source="media/VivaAmplify.png" alt-text="The deviation message for the Outlook distribution channel.":::

## Deviations

Deviations can be classified as:

1. **Modifications to certain web parts**: When you use **Outlook** distribution channel, and then select certain web parts, there may be changes in the properties of the web parts. Such changes result in the web parts displaying a behavior different from its default behavior. 

    For example:

    - In the **Sections** layout, when you organize content into two or three columns, the same content gets stacked into a single column when being published.
    - In the **Image** web part, properties such as "text on image" won't be supported.

1. **Removal of certain web parts**: When you use **Outlook** distribution channel, certain web parts such as the spacer, the large people, and the countdown timer don't appear as they're removed automatically on account of incompatibility with Outlook.

For detailed information about such other deviations in web parts for the **Outlook** distribution channel, see [Deviations in Outlook distribution channel](#deviations-in-outlook-distribution-channel).

### Deviations in Outlook distribution channel

For the **Outlook** distribution channel, there are:

- [Deviations in Image web part](#deviations-in-image-web-part)
- [Deviations in Text web part](#deviations-in-text-web-part)
- [Deviations in People web part](#deviations-in-people-web-part)

#### Deviations in Image web part

1. Text on the image isn't supported (Text will be dropped.).

   :::image type="content" source="media/text-on-image-not-supported.png" alt-text="The text on the image not being supported in Outlook.":::

1. Image Hyperlink isn't supported. Transpiled images aren't clickable to link.

   :::image type="content" source="media/image-hyperlink-not-supported.png" alt-text="The image hyperlink not being supported in Outlook.":::

#### Deviations in Text web part

1. Theme colors for table aren't supported (Table style is changed to **default**.).

   :::image type="content" source="media/theme-colors-not-supported.png" alt-text="The deviation of theme colors not being supported in Outlook.":::

1. Table Alignment isn't supported. Tables can only be left aligned.

   :::image type="content" source="media/table-alignment-not-supported.png" alt-text="The table alignment not being supported in Outlook.":::

#### Deviations in People web part

The **Small**, **Medium**, and **Large** layouts are supported.

:::image type="content" source="media/only-small-layout-supported.png" alt-text="Only the Small layout is supported in Outlook.":::

However, even if you transpile the content using the **Medium** and **Large** layouts, the descriptions and links added in these two layouts will be dropped. The content's output defaults to the **Small** layout view.  

#### Sections layout

**Sections** is a layout-associated element that presents a template to the content in the **Main canvas** page so that the content is structured properly.

Each section consists of 1-3 columns.

For information on the default properties of sections and its columns, see [Add sections and columns on a SharePoint modern page](https://support.microsoft.com/office/add-sections-and-columns-on-a-sharepoint-modern-page-fc491eb4-f733-4825-8fe2-e1ed80bd0899).

However, the following deviations have occurred in the default properties of sections and its columns:

1. When you use the **Two columns** and **Three columns** layout options to organize your content, the content gets stacked into a single column like the content published using the **One Column** layout option.

   :::image type="content" source="media/multi-column-layout-option-not-supported.png" alt-text="The Multi Column layout option not being supported in Outlook.":::

1. Collapsible sections aren't supported, including section titles (which will be dropped).

   :::image type="content" source="media/option-to-make-sections-collapsible.png" alt-text="The option to make sections collapsible.":::
   :::image type="content" source="media/section-title-being-dropped.png" alt-text="Section title being dropped.":::

1. Dividers between sections aren't supported.

   :::image type="content" source="media/dividers-between-sections-not-supported.png" alt-text="Dividers between sections not being supported in Outlook.":::