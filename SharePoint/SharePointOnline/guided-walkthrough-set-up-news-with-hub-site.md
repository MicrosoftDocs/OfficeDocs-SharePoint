---
title: Guided walkthrough - Setting up news for your organization using a hub site
ms.reviewer: 
ms.author: daisyfeller
author: daisyfell
manager: pamgreen
recommendations: true
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
description: "Use a hub site to set up news for your organization"
---

# Guided walkthrough: Setting up news for your organization using a hub site

With SharePoint, you can share news content across your organization in a meaningful and discoverable way. By default, SharePoint news is shown on the SharePoint start page, on team sites, communication sites, hub sites, and on the mobile app according to how relevant the news is for the user. For example, if an important news story is posted by someone in your close sphere of work or posted to a site where you are active, it will be shown to the user.

Organizations have many options as to the kind of news shown, where it's shown, who has the ability to author posts, and more.

In this article, we'll show you how to implement a comprehensive strategy for setting up news at all levels of your organization.

<!-- daisy confirm with holland whether the big TOC thing needs to go here-->

## The strategy

In this walkthrough, we'll do more than just set up News web parts on various sites - we'll show you a comprehensive strategy that includes setting up an "official" news site for news that is visually distinguished as organization news; setting up categories for different types of news; and even setting up an approval process for news posts. We'll display news on an intranet [hub site](https://support.microsoft.com/office/what-is-a-sharepoint-hub-site-fe26ae84-14b7-45b6-a6d1-948b3966427f) that comes from a corporate [communication site](https://support.microsoft.com/office/use-the-sharepoint-topic-showcase-and-blank-communication-site-templates-94a33429-e580-45c3-a090-5512a8070732), a department communication site, and a department [team site](https://support.microsoft.com/office/use-the-sharepoint-team-collaboration-site-template-75545757-36c3-46a7-beed-0aaa74f0401e).

The hub site homepage displays all approved news stories for any site associated with the hub. That means users see all news posts created in the Corporate News site, all news posts created in departmental communication sites, and news stories for just their department’s team site.

<!-- daisy 1-->

1. News from an official corporate communication site that's part of the hub site
2. News from a department communication site that's part of the hub site
3. News from a department team site that's part of the hub site

Content is displayed in the following way on the sites in the hub:

- Each departmental communication site displays news posts for just that department.
- Each departmental team site displays news posts created in that team site as well as posts created in the Corporate News site.

Here's how the news flow works:

- All employees have permission to [create news](https://support.microsoft.com/office/create-and-share-news-on-your-sharepoint-sites-495f8f1a-3bef-4045-b33a-55e5abe7aed7) on their team sites. Posts can be tagged as being a “milestone” or simply “departmental.”
- Each department has one or more employees assigned the task of creating news posts in their department’s communication site.
- All news stories created in departmental communication sites go through a [page approval flow](https://support.microsoft.com/office/approval-flow-for-modern-pages-a8b2e689-d4a1-4639-8028-333c0ece30d9) in which a designated person from the Corporate Communications department approves posts.
- Official news posts from the Corporate Communications department are created in a special site called Corporate News, which is not associated with the hub site. [This site is designated as “official” news](https://support.microsoft.com/office/create-and-share-news-on-your-sharepoint-sites-495f8f1a-3bef-4045-b33a-55e5abe7aed7#bmk_wherenewsisshown).
- On a monthly basis, a newsletter containing selected news stories from Corporate Communications is [emailed to all employees](https://support.microsoft.com/office/create-and-send-a-news-digest-42efc3c6-605f-4a9a-85d5-1f9ff46019bf).

## The hub site structure

All team and communication sites, with the exception of the Corporate communication site, are associated with a single hub site.

Each department has a communication site to share information with the rest of the organization, and a [team site](https://support.microsoft.com/office/use-the-sharepoint-team-collaboration-site-template-75545757-36c3-46a7-beed-0aaa74f0401e) for internal communication among department employees.

<!-- daisy 2-->

## Implementing the strategy

In this section, you'll walk through the process of setting up your SharePoint environment to meet the requirements of this news strategy. This involves setting up the News web part and creating a Page approval process in a Pages library, creating categories for news, and designating one site as "official news."

In this example, the assumption is that each of the communication and team sites is already associated with a hub site (with the exception of Corporate Communications) and there are already several news posts in the Corporate Communications site. If you need to know how to set up these types of sites, see [Set up your SharePoint hub site](https://support.microsoft.com/office/set-up-your-sharepoint-hub-site-e2daed64-658c-4462-aeaf-7d1a92eba098), [Create a communication site in SharePoint Online](https://support.microsoft.com/office/create-a-communication-site-in-sharepoint-7fb44b20-a72f-4d2c-9173-fc8f59ba50eb), and [Create a team site in SharePoint](https://support.microsoft.com/office/create-a-team-site-in-sharepoint-ef10c1e7-15f3-42a3-98aa-b5972711777d).

## Set up your corporate communications site for official organization news

Setting up your corporate communication site for "official" organization news allows news stories from Corporate Communications to appear with emphasis so your users know immediately that this is official company news, like in this example:

<!-- daisy 3-->

To enable this feature and specify the site for organization news, a SharePoint admin must use the [SharePoint Online Powershell commands](https://docs.microsoft.com/powershell/module/sharepoint-online/?view=sharepoint-ps):

[Get-SPOOrgNewsSite](/powershell/module/sharepoint-online/get-spoorgnewssite?view=sharepoint-ps)

[Set-SPOOrgNewsSite](/powershell/module/sharepoint-online/set-spoorgnewssite?view=sharepoint-ps)

## Set up news on a department team site

In your department team site, you'll add the News web part to the page three times. Each web part will display different news information based on news source and categories. To create the categories, add a column to the Pages library to [allow authors to tag their pages with the appropriate category](https://support.microsoft.com/office/view-edit-and-add-page-details-778018d3-8269-4fd2-a55d-8c0e5b72b938).

## Create columns for categories

1. On your department team site, select the **Pages** link in the site navigation to go to the pages library.
2. Select **+ Add column** or the **+** to the right ot the last column name at the top of the pages. <!-- daisy you stopped here-->

<!-- daisy confirm with holland that this bottom bit should be here-->

## Want more?

Get inspired with more examples in the [SharePoint look book](https://sharepointlookbook.azurewebsites.net/).

See other [guided walkthroughs](https://support.microsoft.com/office/guided-walkthroughs-creating-sites-for-your-organization-7cc52ac9-394e-417e-85fe-33070e0cd13c?ui=en-us&rs=en-us&ad=us) for creating sites for your organization.
