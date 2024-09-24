---
ms.date: 09/24/2024
title: "Guidance for retiring Delve in your organization"
ms.reviewer: 
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: overview
ms.service: sharepoint-online
ms.collection: M365-collaboration
ms.localizationpriority: medium
ms.custom: admindeeplinkSPO
search.appverid:
- SPO160
- MOE150
- DEL150
- FRP150
- MET150
ms.assetid: 54f87a42-15a4-44b4-9df0-d36287d9531b
description: "With the December 2024 planned retirement of Delve, this article contains information to assist administrators with the Delve offboarding process."

---

# Guidance for retiring Delve in your organization

In December 2024, Delve will be retired. This was first announced in a MC Post available in the [Microsoft 365 Message Center](https://admin.microsoft.com/Adminportal/Home?#/MessageCenter/:/messages/MC698136). There's also an article you can refer to, [Alternatives to Delve in Microsoft 365](https://support.microsoft.com/office/alternatives-to-delve-in-microsoft-365-59e29736-de90-40ce-93ee-0bbe23902a42), that focuses on helping end users find alternatives for their tasks within Microsoft 365. The purpose of this article is to assist administrators with the Delve offboarding process.

## What will be retired?

Delve offers many features that are built on top of multiple Microsoft 365 services. When we say we're retiring Delve, it's important to note that we're not changing or retiring anything on the services side. Both documents and people data that are surfaced in Delve will continue to be stored and managed as today.

There are a couple of exceptions to this. Delve stores a limited set of Delve-specific data such as list of users recently viewed in Delve, Delve favorite documents, Delve favorite tags, and some Delve-specific settings. These will be retired together with Delve. You can export this data before December 16, 2024, in Delve by going to **Select Settings** > **Feature settings** > **Export data**.

## Where can users view user properties currently surfaced in Delve?

Starting December 2024, properties currently surfaced in Delve, including custom user-profile properties, will be added to the Profile cards that are available in search experiences on Microsoft365.com/Office.com and in SharePoint. Eventually, these changes will be enabled everywhere the Profile card is available. However, for technical reasons, this change will take time. For December 2024, we recommend directing users to Microsoft365.com/Office.com or SharePoint, which also offers a people search similar to what's offered in the Delve search.

## Direct links to profile cards

The modern search experiences on Microsoft365.com/Office.com and in SharePoint include profile pages built on the same data as profile cards. They have a unique link and can be used in documentation, email signatures, etc. We handle redirects from Delve profiles to these profile pages on Microsoft365.com. Although there are three places and URLs that offer the same experience, we suggest you refer to the same domain as we use in the Microsoft365.com redirects.

### Example links

- For Microsoft365.com:

  [Example]

- For Office.com:

  [Example]

- For SharePoint:

  [Example]

## What happens to existing URLs pointing to Delve or SharePoint profiles?

Both Delve URLs and SharePoint profile URLs will be redirected to the modern search profile pages on Microsoft365.com. For tenants not using Delve today, there'll be no change to URLs and their profile legacy experiences in SharePoint. However, they will get the extended profile page in modern search and the extended profile cards across Microsoft 365, which will include properties that today are visible in Delve.

## Where can users edit properties currently editable in Delve?

A new edit profile experience, tightly coupled with the profile card, is currently being developed and is targeted for release in November 2024. This allows users to easily edit their profiles across Microsoft 365. Some properties that are viewable in Delve today are not editable in Delve, but are viewable in the SharePoint edit-profile experience.

The same will be true for the new edit experience. Only properties that today are editable in the Delve edit profile experience will be editable in the profile cards. For other properties, for example custom user-profile properties, users will have to go to the legacy edit-profile experience in SharePoint.

The same is true for the visibility attribute users can change for some properties in Delve. For now, they'll not be able to change this in the new edit experience, and must go to the legacy edit profile in SharePoint. The new edit experience will include a direct link to the legacy edit experience in SharePoint, so it's easy for users to get there. This approach is how the visibility attribute is handled in Delve today.

### The link to the legacy SharePoint edit-profile expereince

[Screenshot 1]

### The SharePoint Edit Details dialog box

[Screenshot 2]

## What will the new edit experience in profile cards look like?

The new edit-profile experience is built on top of Microsoft 365 profile cards, and will be presented in an overlay the same way ofile cards are handled today. The most common user pattern is to open their own profile card and selects **Edit profile**. Instead of being redirected to Delve, the edit experience will open in the profile card itself. The following illustrations are an example of this process.

> [!NOTE]
> If the new edit-profile experience isn' yet enabled in the experience for a user, selecting **Edit profile** will redirect the user to the modern search-profile page on Microsoft365.com.

[Screenshot 3]

[Screenshot 4]

