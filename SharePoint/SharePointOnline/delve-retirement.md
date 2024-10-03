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

In December 2024, Delve will be retired. This change was first announced in an MC Post available in the [Microsoft 365 Message Center](https://admin.microsoft.com/Adminportal/Home?#/MessageCenter/:/messages/MC698136). There's also an article you can refer to, [Alternatives to Delve in Microsoft 365](https://support.microsoft.com/office/alternatives-to-delve-in-microsoft-365-59e29736-de90-40ce-93ee-0bbe23902a42), that focuses on helping end users find alternatives for their tasks within Microsoft 365. The purpose of this article is to assist administrators with the Delve offboarding process.

## What will be retired?

Delve offers many features that are built on top of multiple Microsoft 365 services. When we say we're retiring Delve, it's important to note that we're not changing or retiring anything on the services side. Both documents and people data that are surfaced in Delve will continue to be stored and managed as today.

There are a couple of exceptions regarding data storage. Delve stores a limited set of Delve-specific data, such as list of users recently viewed in Delve, Delve favorite documents, Delve favorite tags, and some Delve-specific settings. These will be retired together with Delve. You can export this data before December 16, 2024, in Delve by going to **Select settings** > **Feature settings** > **Export data**.

## Where can users view user properties currently surfaced in Delve?

Starting December 2024, properties currently surfaced in Delve, including custom user profile properties, will be added to the profile cards available in search experiences on Microsoft365.com, Office.com, and in SharePoint. Eventually, these changes will be enabled everywhere the profile card is available. However, for technical reasons, this change will take time. For December 2024, we recommend directing users to Microsoft365.com, Office.com, or SharePoint, which also offer a people search similar to what's offered in the Delve search.

## Direct links to profile cards

The modern search experiences on Microsoft365.com, Office.com, and in SharePoint include profile pages built on the same data as profile cards. They have a unique link and can be used in documentation, email signatures, etc. Starting December 16, we'll handle redirects from Delve profiles to these profile pages on Microsoft365.com. Although there are three places and URLs that offer the same experience, we suggest you refer to Microsoft365.com.

### Example links

- For Microsoft365.com:

  :::image type="content" source="media/delve-retirement-microsoft365-links.png" alt-text="Screenshot showing an example link syntax for Microsoft 365.":::

- For Office.com:

  :::image type="content" source="media/delve-retirement-office-links.png" alt-text="Screenshot showing an example link syntax for Office.com.":::

- For SharePoint:

  :::image type="content" source="media/delve-retirement-sharepoint-links2.png" alt-text="Screenshot showing an example link syntax for SharePoint.":::

## What happens to existing URLs pointing to Delve or SharePoint profiles?

Both Delve URLs and SharePoint profile URLs will be redirected to the modern search profile pages on Microsoft365.com. For tenants not using Delve today, there will be no change to URLs and their legacy profile experiences in SharePoint. However, they get the extended profile page in modern search and the extended profile cards across Microsoft 365, which will include the properties that are visible in Delve.

## Where can users edit properties currently editable in Delve?

A new edit profile experience, tightly coupled with the profile card, is currently being developed and is targeted for release in November 2024. This will allow users to easily edit their profiles across Microsoft 365. Some properties that are viewable in Delve today aren't editable in Delve, but in the SharePoint edit profile experience.

The same will be true for the new edit experience. Only properties that today are editable in the Delve edit profile experience will be editable in the profile cards. For other properties, for example custom user profile properties, users will have to go to the legacy edit profile experience in SharePoint.

Visibility attributes follow the same pattern. Users won't be able to change them in the new edit experience and will have to go to the legacy edit profile experience in SharePoint. To make this effortless, a link to the legacy edit profile experience will be part of the new experience.

:::image type="content" source="media/delve-retirement-legacy-edit-experience-in-sharepoint.png" alt-text="Screenshot showing how to access the legacy edit experience in SharePoint.":::
The link to the legacy SharePoint edit profile experience.

:::image type="content" source="media/delve-retirement-edit-profile-in-sharepoint.png" alt-text="Screenshot showing the Edit Details dialog box in SharePoint." lightbox="media/delve-retirement-edit-profile-in-sharepoint.png":::
The SharePoint Edit Details dialog box.

## What will the new edit experience in profile cards look like?

The new edit profile experience is built on top of Microsoft 365 profile cards, and it will be presented in an overlay as profile cards are handled today. A most common user pattern is for the user to open their own profile card and select "edit profile." Instead of being redirected to Delve, the edit experience will open in the profile card. Below is an example of what this process will look like.

Please note that if the new edit profile experience isn't yet enabled in the experience where a user is, clicking "edit profile" will redirect the user to the modern search profile page on Microsoft365.com.

:::image type="content" source="media/delve-retirement-profile-card-with-update-button.png" alt-text="Screenshot showing an example of a profile card with the Update button.":::

:::image type="content" source="media/delve-retirement-lpe-with-background.png" alt-text="Screenshot showing an example of a profile card and personal data." lightbox="media/delve-retirement-lpe-with-background.png":::

## Where can users search for people and user profile properties that are currently supported in Delve?

Users can search for people in the modern search experience in Microsoft365.com, Office.com, and SharePoint. Classic search will continue to work as before and clicks on people results that today link to Delve will redirect to the modern search profile page on Microsoft365.com.

Note that people are presented in multiple ways in modern search. Clicks on a people result in the "all" vertical will take the user to the modern search profile experience. Clicks on people results in the people vertical will open the large profile card. Both experiences will include properties that today are surfaced in Delve.

## Custom people search solutions

If your tenant depends on custom solutions for people search it should continue to work as before. They're built on services powering Delve and not on the Delve experience itself. One common third-party solution in use is the PnP Modern Search app. This particular app allows administrators to create custom search-based experiences based on SharePoint web parts. It's easy to configure people results to support opening profile cards on hover and click. It's also possible to include links to Delve profiles and the legacy SharePoint profile (_person.aspx_/_personimmersive.aspx_). These links will continue to work as users will be redirected to the modern search profile page in Microsoft365.com.

## Properties not supported by the new edit experience

In general, the new edit experience built on profile cards will support editing properties in the profile card, but there are exceptions. One exception is with properties hosted by Microsoft Entra ID and synced to UPA (SharePoint). By default, these aren't editable in Delve or in the legacy profile edit experience in SharePoint. However, administrators can override the default behavior to make them editable for the user. If administrators make this change, some properties can be edited in Delve, and some can be edited in the legacy edit profile experience in SharePoint.

The new edit profile experience built on profile cards won't support editing these properties. Users can still edit them if administrators have made the setting changes mentioned above, in the legacy edit profile experience, but by default they'll not be visible anywhere and only provide value if you have a custom solution. The following list contains these properties.

### Properties synced from Microsoft Entra ID that aren't editable (by default) in Delve

- UserPrincipalName
- DisplayName
- GivenName
- Sn
- telephoneNumber
- proxyAddresses
- PhysicalDeliveryOfficeName
- Title
- Department
- WWWHomePage
- PreferredLanguage
- msExchHideFromAddressList
- Manager

## When will Delve no longer be available?

Delve will be retired on December 16, 2024. The extended profile card experience, the updated profile pages in modern search, and the new edit profile experience will be available before Delve is retired. For a limited period, both Delve and the new experiences will be available for users. Delve retires when the redirect of Delve URLs is activated.

## What do we recommend administrators do?

- Educate your users about the upcoming changes by updating internal documentation and training material relevant for the Delve retirement.
- Once released, validate that your users can solve their Delve tasks in the new edit profile experience, updated profile pages in modern search, people search in Microsoft365.com, and in the extended profile cards.

## More resources

[Alternatives to Delve in Microsoft 365](https://support.microsoft.com/office/alternatives-to-delve-in-microsoft-365-59e29736-de90-40ce-93ee-0bbe23902a42)

[Add and edit user profile properties in SharePoint](add-and-edit-user-profile-properties.md)

[Tips and tricks on how to search for organizational content more effectively](https://techcommunity.microsoft.com/t5/microsoft-search-blog/tips-and-tricks-on-how-to-search-for-organizational-content-more/ba-p/3838452)

[Profile cards in Microsoft 365](https://support.microsoft.com/en-us/office/profile-cards-in-microsoft-365-e80f931f-5fc4-4a59-ba6e-c1e35a85b501)

[User profile synchronization](user-profile-sync.md)
