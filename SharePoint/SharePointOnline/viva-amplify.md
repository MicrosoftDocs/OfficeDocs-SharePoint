---
title: "Formatting changes for Microsoft Viva Amplify - Private preview"
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
description: Learn about the formatting changes in Microsoft Viva Amplify
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
---

# Formatting changes for Microsoft Viva Amplify - Private preview

> [!NOTE]
> Microsoft Viva Amplify is currently in Private preview and, hence, available only to Private preview customers.

Microsoft Viva Amplify is an internal communication campaign that allows you to create something once and publish it to multiple distribution channels to share throughout the organization. Hence, creating a campaign is the first step in the end-to-end content management process that involves creating content and publishing it.

Once you create a campaign, you can create the content on the **Main canvas** screen, and then publish the content.

To create a campaign, perform the following steps:

1. Go to the Microsoft Viva Amplify portal.
2. Provide your credentials and sign in.
3. Select **+ Create a campaign**.
   The **Create a new campaign** screen is displayed.
4. Select **Create a campaign** on the bottom-left corner of the screen.
5. Enter the details for the text boxes and select **Next**.
6. From the **Add members to your campaign** text box, choose the person whom you want to add as a member of your campaign.
7. Select **Add to list**.
   The chosen person is successfully added as a member of your campaign.
8. Select **Create a campaign**.
   The campaign is successfully created and listed on the **Amplify Hub** screen.

You can create content using the created campaign and then transpile it to the distribution channels. Only after you transpile the content, you can view the formatting changes that occur.

> [!NOTE]
> Formatting changes are applicable only to the **Outlook** distribution channel and not to the **SharePoint** distribution channel because the **Main canvas** screen itself is a type of SharePoint site. For more information, see [Formatting changes](#formatting-changes) and [Formatting changes in Outlook distribution channel](#formatting-changes-in-outlook-distribution-channel).

For example, when you click the "preview" icon under the **Outlook** distribution channel, you're presented with a message that reads as follows:

**[Some properties like text on images, columns, and medium and large people web parts may have been changed for this distribution channel.](#formatting-changes)**

:::image type="content" source="media/viva-amplify.png" alt-text="The formatting change message for the Outlook distribution channel.":::

When you click **Learn more about formatting changes and editing**, you're taken to the screen that displays information about [formatting changes](#formatting-changes).

## Formatting changes

Formatting changes can be classified as:

1. **Modifications to certain web parts**: When you use **Outlook** distribution channel, and then select certain web parts, there may be changes in the properties of the web parts. Such changes result in the web parts displaying a behavior different from its default behavior.

For example, in the **Sections** layout, when you organize content into two or three columns, the same content gets stacked into a single column when being published.

1. **Removal of certain web parts**: When you use **Outlook** distribution channel, certain web parts such as the spacer, the large people, and the countdown timer don't appear as they're removed automatically on account of their incompatibility with Outlook.

For detailed information about such other formatting changes in web parts for the **Outlook** distribution channel, see [Formatting changes in Outlook distribution channel](#formatting-changes-in-outlook-distribution-channel).

### Formatting changes in Outlook distribution channel

For the **Outlook** distribution channel, there are:

- [Formatting changes in Image web part](#formatting-changes-in-image-web-part)
- [Formatting changes in People web part](#formatting-changes-in-people-web-part)
- [Formatting changes in Section layout](#formatting-changes-in-sections-layout)

#### Formatting changes in Image web part

Text on the image is now transpiled to appear on top of the image on Outlook endpoint.

:::image type="content" source="media/text-over-image.png" alt-text="The screenshot that depicts the display of the text on top of the image.":::

#### Formatting changes in People web part

The **Small**, **Medium**, and **Large** layouts are supported.

:::image type="content" source="media/only-small-layout-supported.png" alt-text="Only the Small layout is supported in Outlook.":::

However, even if you transpile the content using the **Medium** and **Large** layouts, the descriptions and links added in these two layouts will be dropped. The content's output defaults to the **Small** layout view.  

#### Formatting changes in Sections layout

**Sections** is a layout-associated element that presents a template to the content in the **Main canvas** page so that the content is structured properly.

Each section consists of 1-3 columns.

For information on the default properties of sections and its columns, see [Add sections and columns on a SharePoint modern page](https://support.microsoft.com/office/add-sections-and-columns-on-a-sharepoint-modern-page-fc491eb4-f733-4825-8fe2-e1ed80bd0899).

The sections and its columns too - much like other web parts - have experienced the following formatting changes in its default properties:

1. When you use the **Two columns**, **Three columns**, **One-third left**, or the **One-third right** layout options to organize your content, the content gets stacked into a single column, similar to the **One Column** layout option's output.

   :::image type="content" source="media/multi-column-layout-option-not-supported.png" alt-text="The Multi Column layout option not being supported in Outlook.":::

1. Collapsible sections aren't supported, including section titles (which will be dropped).

   :::image type="content" source="media/option-make-sections-collapsible.png" alt-text="The option to make sections collapsible.":::
   :::image type="content" source="media/section-title-being-dropped.png" alt-text="Section title being dropped.":::

1. Dividers between sections aren't supported.

   :::image type="content" source="media/dividers-between-sections-not-supported.png" alt-text="Dividers between sections not being supported in Outlook.":::
