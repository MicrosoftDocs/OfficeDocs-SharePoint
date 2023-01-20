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

Microsoft Viva Amplify is an internal communication campaign that allows you to create something once and publish it to multiple distribution channels to share throughout their organization. Hence, creating a campaign is the first step in the end-to-end content management process that involves creating content and publishing it using distribution channels.

Once you create a campaign, you can create the content on the **Main canvas** screen, and then publish the content using [distribution channels](#distribution-channels).

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
   The campaign is successfully created.

Once you've created your campaign, you've to create the content on the **Main canvas** screen, and then publish it using distribution channels.

To create the content and publish it, perform the following steps:

> [!NOTE]
> Once you've created your campaign, you land on the **Main canvas** screen, by default.

1. Create the content.
1. Select the **Distribution channels** tab.

   > [!NOTE]
   > Microsoft Viva Amplify supports **Outlook** and **SharePoint** distribution channels, currently.
   >  
   > :::image type="content" source="media/distribution-channel-options.png" alt-text="The distribution channel options on the Main canvas screen.":::

1. Select **Outlook**.

   > [!NOTE]
   > You can also select **SharePoint**. In this procedure, selection of **Outlook** is emphasized because certain deviations occur, as specified in [Deviations](#deviations).

   > [!NOTE]
   > When you've selected **Outlook**, not all the web parts available on the **Main canvas** page are available, because of compatibility issues. Moreover, whatever web parts are compatible with Outlook, they undergo a modification in their behavior, distinct from the web parts' default behavior. Such impact on the web parts is referred to as deviations. For more information, see [Deviations](#deviations).

   > [!NOTE]
   > When you select the **SharePoint** distribution channel, there are no deviations in the composition of the web parts or in the web parts' properties. The reason is that the **Main canvas** screen itself is a type of SharePoint site. Hence, there won't be any changes in the web parts when they are being transpiled to the **SharePoint** distribution channel.

### Deviations

Deviations can be classified as:

- **Modifications to certain web parts on selection of a distribution channel**: When you select a **Outlook** distribution channel, and then select certain web parts, there may be changes in the properties of the web parts. Such changes result in the web parts displaying a behavior different from its default behavior.
- **Removal of certain web parts on selection of a distribution channel**: When you select a specific distribution channel, certain web parts may be removed and hence become unavailable for use. For example, when you select the **Outlook** distribution channel, the spacer, the large people web part, and the countdown timer web part don't appear as these web parts aren't compatible with Outlook.

For more information about the deviations that occur in the **Outlook** distribution channel, see [Deviations in Outlook distribution channel](#deviations-in-outlook-distribution-channel).

#### Deviations in Outlook distribution channel

The following web parts get modified when you select them on the **Outlook** distribution channel screen:

- Image web part
- Text web part
- People web part

For more information on the deviations occurring in these web parts, see:

- [Deviations in Image web part](#deviations-in-image-web-part)
- [Deviations in Text web part](#deviations-in-text-web-part)
- [Deviations in People web part](#deviations-in-people-web-part)

##### Deviations in Image web part

1. Text on the image isn't supported (Text will be dropped.).

   :::image type="content" source="media/text-on-image-not-supported.png" alt-text="The text on the image not being supported in Outlook.":::

1. Image Hyperlink isn't supported. Transpiled images aren't clickable to link.

   :::image type="content" source="media/image-hyperlink-not-supported.png" alt-text="The image hyperlink not being supported in Outlook.":::

##### Deviations in Text web part

1. Theme colors for table aren't supported (Table style is changed to **default**.).

   :::image type="content" source="media/theme-colors-not-supported.png" alt-text="The deviation of theme colors not being supported in Outlook.":::

1. Table Alignment isn't supported. Tables can only be left aligned.

   :::image type="content" source="media/table-alignment-not-supported.png" alt-text="The table alignment not being supported in Outlook.":::

##### Deviations in People web part

Only the **Small** layout is supported for **People** web part (Descriptions and links added to medium or large versions will be dropped.).

:::image type="content" source="media/only-small-layout-supported.png" alt-text="Only the Small layout is supported in Outlook.":::

##### Sections layout

**Sections** is a layout-associated element that presents a template to the content in the **Main canvas** page so that the content is structured properly.

Each section consists of 1-3 columns.

For information on the default properties of sections and its columns, see [Add sections and columns on a SharePoint modern page](https://support.microsoft.com/office/add-sections-and-columns-on-a-sharepoint-modern-page-fc491eb4-f733-4825-8fe2-e1ed80bd0899).

However, the following deviations have occurred in the default properties of sections and its columns:

1. Multi Columns aren't supported; transpiled content created with options other than the **One Column** layout option will be stacked like in the **One Column** layout option.

   :::image type="content" source="media/multi-column-layout-option-not-supported.png" alt-text="The Multi Column layout option not being supported in Outlook.":::

1. Collapsible sections aren't supported, including section titles (which will be dropped).

   :::image type="content" source="media/option-to-make-sections-collapsible.png" alt-text="The option to make sections collapsible.":::
   :::image type="content" source="media/section-title-being-dropped.png" alt-text="Section title being dropped.":::

1. Dividers between sections aren't supported.

   :::image type="content" source="media/dividers-between-sections-not-supported.png" alt-text="Dividers between sections not being supported in Outlook.":::