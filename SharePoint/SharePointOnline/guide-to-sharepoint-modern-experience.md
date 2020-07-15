---
title: Guide to the modern experience in SharePoint
ms.reviewer: 
ms.author: loreenl
author: loreenla
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
ms.custom:
- seo-marvel-apr2020
search.appverid:
- SPO160
- MET150
description: "In this article, you'll learn about the modern experience in SharePoint and how you can begin to take advantage of it."
---

# Guide to the modern experience in SharePoint

The modern experience in Microsoft SharePoint is designed to be compelling, flexible, and more performant. The modern experience makes it easier for anyone to create beautiful, dynamic sites and pages that are mobile-ready. But what are the differences between the classic and modern experiences, and how do you go about creating a modern experience for your organization? This guide is a starting point for people familiar with the classic experiences in SharePoint to help you learn about the modern experience and how you can begin to take advantage of it.

## Information architecture and hub sites

Classic SharePoint architecture is typically built using a hierarchical system of site collections and sub-sites, with inherited navigation, permissions, and site designs. Once built, this structure can be inflexible and difficult to maintain. In the modern SharePoint experience, every site is a site collection and can be associated to a hub, which is a flat collection of sites that share navigation, branding, and other elements. This type of structure is far more flexible and adaptive to the changing needs of your organization. [Learn about how to plan for Hub sites](planning-hub-sites.md).

## Navigation

The most effective SharePoint sites (and web sites in general) help visitors find what they need quickly so that they can use the information they find to make decisions, learn about what is going on, access the tools they need, or engage with colleagues to help solve a problem. The fundamental principles and good practices for site and page navigation are equally applicable to both classic and modern SharePoint architectures. However, your options for *implementing* navigation differs based on the framework for your sites and intranet. For example, the “inherited” navigation experiences available in classic SharePoint site hierarchies (sites with subsites) are not available in the modern experience, but [*hubs*](https://support.office.com/article/fe26ae84-14b7-45b6-a6d1-948b3966427f) provide a great way to achieve the cross-site navigation features previously available in managed navigation and site hierarchies in classic SharePoint.  

No matter which framework you are using, you can use the guidance in [Plan navigation in the modern experience](plan-navigation-modern-experience.md) to help make good decisions for navigation. 

## Branding

In the classic SharePoint experience, there are a set of default themes and site designs that can require a considerable amount of customization to get them to match your organization’s brand. Also, they aren’t very responsive, making the experience on different devices inconsistent. Most site branding requires the use of custom master pages or alternate CSS configurations. SharePoint includes an updated set of default site themes and site designs (or templates) that are responsive and look great on any device. With site themes, you can customize your site’s logo and colors to match your brand. You can also align the mobile SharePoint app for your users to match your company branding. Site designs provide specific layouts and other functionality for your site. Additional branding can be achieved using custom themes or site designs without worrying about something breaking when SharePoint is updated. To learn more about modern branding options, see [Branding SharePoint sites in the modern experience](branding-sharepoint-online-sites-modern-experience.md).

## Publishing

If you’ve implemented publishing sites or publishing-enabled sites in your organization, you know how important it is to create attractive and performant pages to distribute communication to a large number of people. In the modern experience, communication sites make it easy to create beautiful, dynamic, and performant sites and pages that are mobile-ready. There are differences from classic publishing, though, and things you’ll want to think about planning your move to the modern experience. For more info, see [Moving from Publishing sites to Communication sites](publishing-sites-classic-to-modern-experience.md).

## Search

Search is an important part of any site – you want people to be able to find what they are looking for quickly and easily. SharePoint has both a classic and a modern search experience. Microsoft Search in SharePoint is the modern experience. The most visible difference is that the Microsoft Search box is placed at the top of SharePoint, in the header bar. Another difference is that Microsoft Search is personal and contextual. The results you see are different from what other people see, even when you search for the same words. You will also see different results based on where you are when you search. For example, searching at the root of your tenant looks across all of SharePoint. Searching from a hub finds content in all sites associated to the hub. Searching from an individual site finds content on that site. Searching from a list or library finds content in the list or library. You will also see results before you start typing in the search box, based on your previous activity and trending content in Microsoft 365, and the results update as you type. To learn more about the Microsoft Search experience for users, see [Find what you need with Microsoft Search](https://support.office.com/article/d5ed5d11-9e5d-4f1d-b8b4-3d371fe0cb87). There are other differences, especially around customization. To decide which experience your organization should use, see [When to use which search experience](get-started-with-modern-search-experience.md).

## Sharing and permissions

SharePoint continues to provide both SharePoint groups as well as security groups maintained by Azure Active Directory. Microsoft 365 also provides a third grouping option for SharePoint, [Microsoft 365 groups](https://support.office.com/article/b565caa1-5c40-40ef-9915-60fdb2d97fa2). Microsoft 365 groups are similar to security groups, although Microsoft 365 groups include many additional benefits. Microsoft 365 groups are provided a group email address as well as additional tools such as a group calendar, notebook, Planner, and a SharePoint Team site. Users assigned to an Microsoft 365 group may also be classified as either a group owner or a group member, in comparison to security groups where all group members have equal access under the group. To learn about the differences, benefits, and best practices for permissions and sharing in the modern experience, see [Sharing and permissions in the SharePoint modern experience](sharing-permissions-modern-experience.md).

## Performance

The modern experience in SharePoint is designed to be compelling, flexible and – importantly - more performant. Both SharePoint performance as a whole and the performance of individual SharePoint components such as search, lists, and document libraries are affected by many factors, all of which contribute to the decisive performance metric: perceived end user latency, or the speed with which pages are rendered in the client browser. For more info, see [Performance in the modern SharePoint experience](https://docs.microsoft.com/sharepoint/modern-experience-performance).

## Multilingual

Classic SharePoint publishing sites can use a feature called [variations](https://support.microsoft.com/office/da0b5614-8cf5-4905-a44c-90c2b3f8fbb6) to create a site that supports multiple languages. Modern communication sites leverage a multilingual experience to make content in your intranet sites available in multiple languages. User interface elements like site navigation, site title, and site description can be shown in the user's preferred language. Additionally, you can provide pages and news posts on communication sites that you translate and that are shown in the user's preferred language. One of the most important differences in the modern experience is that, unlike the variations feature, which creates a separate *sub-site* for each language, the modern multilingual experience creates a corresponding page in the same site, but in a language-specific *folder* in the Site Pages library. To learn more, see [Create modern multilingual communication sites, pages, and news](https://support.office.com/article/create-multilingual-communication-sites-pages-and-news-2bb7d610-5453-41c6-a0e8-6f40b3ed750c).
