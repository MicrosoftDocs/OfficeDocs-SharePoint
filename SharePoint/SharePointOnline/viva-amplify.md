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

Microsoft Viva Amplify is a content creation platform that uses [multiple supported distribution channels](#multiple-supported-distribution-channels) to publish the content.

The content creation platform is the **Main canvas** screen, which is the default screen in Microsoft Viva Amplify.

## Multiple supported distribution channels

The following distribution channels are supported in Microsoft Viva Amplify for publish of content:

- Outlook
- SharePoint

:::image type="content" source="media/distribution-channel-options.png" alt-text="The distribution channel options on the Main canvas screen.":::

Once the content is created, you should select the **Distribution channels** tab and select either **Outlook** or **SharePoint** to publish the content.

### Deviations

Deviations can be referred to as:

- **Modifications to certain web parts on selection of a distribution channel**: When you select a specific distribution channel, and when they select certain web parts, there may be changes in the properties of the web part. Such changes result in the web part displaying a behavior different from its default behavior.
- **Removal of certain web parts on selection of a distribution channel**: When you select a specific distribution channel, certain web parts may be removed and hence become unavailable to use. For example, when you select the **Outlook** distribution channel, the spacer, the large people web part and the countdown timer web part don't appear as these web parts aren't compatible with Outlook.

For more information about the deviations that occur for the **Outlook** distribution channel, see [Deviations in Outlook distribution channel](#deviations-in-outlook-distribution-channel).

> [!NOTE]
> There is no deviation in the composition of the web parts and in their properties when you select the **SharePoint** distribution channel. The reason is that the **Main canvas** screen itself is a type of SharePoint site. Hence, there won't be any changes in the web parts when they are being transpiled to the **SharePoint** distribution channel.

#### Deviations in Outlook distribution channel

The following web parts get modified when you select them under the **Outlook** distribution channel:

- Image web part
- Text web part
- People web part

:::image type="content" source="media/webparts-supported-by-default.png" alt-text="The web parts supported by default in Microsoft Viva Amplify.":::

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

Only the **Small** layout is supported for People web part (Descriptions and links added to medium or large versions will be dropped.).

:::image type="content" source="media/only-small-layout-supported.png" alt-text="Only the Small layout is supported in Outlook.":::

##### Sections layout

**Sections** is a layout-associated element that presents a template to the content in the **Main canvas** page so that the content is structured properly.

Each section consists of 1-3 columns. 

For information on the default properties of sections and its columns, see [Add sections and columns on a SharePoint modern page](https://support.microsoft.com/office/add-sections-and-columns-on-a-sharepoint-modern-page-fc491eb4-f733-4825-8fe2-e1ed80bd0899).

However, the following deviations have been spotted in the default properties of sections and its columns:

1. Multi Columns aren't supported; transpiled content created with options other than the **One Column** layout option will be stacked like in the **One Column** layout option.

   :::image type="content" source="media/multi-column-layout-option-not-supported.png" alt-text="The Multi Column layout option not being supported in Outlook.":::

1. Collapsible sections aren't supported, including section titles (which will be dropped).

   :::image type="content" source="media/option-to-make-sections-collapsible.png" alt-text="The option to make sections collapsible.":::
   :::image type="content" source="media/section-title-being-dropped.png" alt-text="Section title being dropped.":::

1. Dividers between sections aren't supported.

   :::image type="content" source="media/dividers-between-sections-not-supported.png" alt-text="Dividers between sections not being supported in Outlook.":::