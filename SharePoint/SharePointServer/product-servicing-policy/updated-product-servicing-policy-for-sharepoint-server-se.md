---
title: "Updated Product Servicing Policy for SharePoint Server Subscription Edition"
ms.reviewer:
ms.author: serdars
author: SerdarSoysal
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: reference
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SP2019
description: "This article explains the updated product servicing policy of SharePoint Server Subscription Edition."
---

# Updated Product Servicing Policy for SharePoint Server Subscription Edition

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

When SharePoint Server Subscription Edition is being supported, Microsoft releases new Public Update (PU) builds for SharePoint Server Subscription Edition each month. These builds contain the latest functionality, performance, and stability improvements for the product. To ensure that customers have a high-quality experience, Microsoft is adopting the following product servicing policy for SharePoint Server Subscription Edition.

## Policy overview

The RTM build and all PUs for SharePoint Server Subscription Edition released before January 10, 2023 will be supported until December 12, 2023. From the January 10, 2023 PU for SharePoint Server Subscription Edition, each Public Update build will be supported for one year from its release date. Support for a Public Update build will end on the second Tuesday of the same month of its release in the following year.

Customers must be running a supported build of SharePoint Server Subscription Edition to remain supported. If a customer contacts Microsoft Support and their SharePoint Server farm isn't running a minimum supported build or higher, they may be required to upgrade to a supported build before support can be offered.

The product servicing policy timeline for SharePoint Server Subscription Edition is described in the following table:

|SharePoint Server Subscription Edition Build|Release Date|Support End Date|
|---|---|---|
|RTM (16.0.14326)|11/2/2021|12/12/2023|
|December 2021 Public Update - December 2022 Public Update|12/14/2021-12/13/2022|12/12/2023|
|January 2023 Public Update|1/10/2023|1/9/2024|
|February 2023 Public Update|2/14/2023|2/13/2024|
|March 2023 Public Update|3/14/2023|3/12/2024|
|April 2023 Public Update|4/11/2023|4/9/2024|
|Future Public Updates|Release Date|Release Date + 1 Year (second Tuesday of the Month)|

## Frequently Asked Question

***Question:** Why is Microsoft changing the servicing policy for SharePoint Server Subscription Edition compared to previous versions of SharePoint Server?

**Answer:** In previous versions of SharePoint Server, the support end date for each PU was tied to the anniversary of the product’s RTM date. This correlation effectively created a single month each year where customers had to update their SharePoint Server farms to remain in support.

SharePoint Server Subscription Edition introduces our new continuous update model, also known as "evergreen". This update model is more flexible and will allow Microsoft to introduce new feature experiences regularly. Giving each PU its own one-year window of support will ensure that customers are up to date with the latest functionality, performance, and stability improvements while also giving customers flexibility to update their farms in a timeframe that works best for them.

**Question:** Why is Microsoft adopting a one-year window of support for each PU?

**Answer:** A one-year window of support balances the need to stay up to date with the latest functionality, performance, and stability improvements with the awareness that a faster update cadence may be difficult to achieve in some SharePoint Server environments. Microsoft encourages customers to go beyond these minimum supportability requirements and deploy new PUs as soon as they’re available, where possible.

**Question:** Will Microsoft release service packs for SharePoint Server Subscription Edition?

**Answer:** No, Microsoft has no plans to release service packs for SharePoint Server Subscription Edition. Functionality, performance, and stability improvements for SharePoint Server Subscription Edition will be delivered by way of our monthly PUs. New feature experiences will be delivered in our Feature Updates.

**Question:** How are Feature Updates different from PUs?

**Answer:** Functionality, performance, and stability improvements for SharePoint Server Subscription Edition may appear in any of our monthly PUs. New feature experiences will be bundled together in Feature Updates, which will be released twice a year (once in the spring and once in the autumn). Feature Updates are delivered to customers inside PUs.

For more information about Feature Updates, see [Feature release rings](../administration/feature-release-rings.md).

**Question:** Where can I find the PUs for SharePoint Server Subscription Edition?

**Answer:** The current list of PUs for SharePoint Server Subscription Edition can be found in the [SharePoint Updates](/officeupdates/sharepoint-updates) article.

**Question:** Do the monthly PUs contain all of the fixes included in the previous PUs?

**Answer:** Yes, the monthly PUs are cumulative. Each PU contains all of the fixes provided in the previous PUs.

**Question:** Do I need to install an earlier PU before I can install the latest PU?

**Answer:** No, you don’t need to install an earlier PU before you install the latest PU. You can install any PU directly on an RTM installation, or on top of any previous PU.

**Question:** Should I install the monthly PUs for SharePoint Server Subscription Edition immediately or should I install them only if they contain a fix for a specific issue I’m having?

**Answer:** Microsoft recommends that all customers install PUs for SharePoint Server Subscription Edition as soon as they become available. Microsoft performs rigorous validation of each PU, both internally and with a select set of partners and customers, before it's released to ensure it has the highest quality.
