---
title: "Information architecture principals in SharePoint"
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
ms.custom:
- seo-marvel-apr2020
search.appverid:
- SPO160
- MET150
description: "Use the information you need to make decisions, learn about what is going on, access frequently used tools, and engage with colleagues to help solve specific problems"
---

# Information architecture in modern SharePoint

The most effective SharePoint sites help viewers find what they need quickly so that they can use the information they need to make decisions, learn about what is going on, access frequently used tools, and engage with colleagues to help solve specific problems.

Even when search is available, most viewers start their web experiences by browsing. That pattern persists on internal web sites as well. Good navigation experiences present viewers with a complete picture of what is available, and combined with the home page, provide a comprehensive "story."

**In this article:**

- [Understand basic information architecture principals](#get-organized)
- [Learn more about how to write effective labels and links](#write-clear-and-intuitive-labels)
- [See how to ensure frequently used tools and content are findable](#test-usability-and-findability-with-real-users)


## Information architecture goals

Navigation should always be planned from the perspective of the user. Planning effective navigation involves considering not just the information you want to present, but also thinking about the information your viewers want or need to consume. Therefore, organizing and labeling your navigation links is critical for the purposes of usability and findability. 

Successful intranet and site navigation experiences enable users to:

- **Find information** – Users need to find documents, files, and links most relevant to the work they do without spending time sifting through content. Make sure to present only the most relevant and high-priority information first.
- **Take action** – Users typically have a specific task in mind when they visit a site. Make sure common tasks are built-in to navigational structure as labels and links so that they can be easily identified and accessed. 
- **Understand company structure** – When viewed at-a-glance, users should be able to get a sense for how to organization is structured. Make sure you incorporate hierarchy and structure into site and intranet navigation.

## Get organized
There is no one right way to organize your navigation links. You will make different choices based on the type of site you are creating and your viewers. Organizing concepts might include:

- Services
- Products
- Activities
- Audiences (if your viewers can clearly identify the audience to which they belong – such as student or teacher)
- Expertise areas or functions

As you organize user needs and business needs, consider the following: 

- **How can information architecture reduce the cognitive load for your viewers?** - Cognitive load is the amount of information that a person can process at any given time. Managing the user’s cognitive load helps prevent information overload and time wasted finding resources. Ensure you understand your viewers needs prior to implementing information architecture.
- **What is the current mental model of your users?** - Mental models are the existing models people use while interacting with a website or application. Information is easier to discover when it is in a place that matches the user’s mental model of where it should be.
- **How can information architecture help users make better and more efficient decisions?** - Decision making can be incredibly taxing. Information architects can help us make decisions by providing certain information at key moments.

The default navigation for all SharePoint sites primarily includes type of content. For [communication sites](https://support.office.com/article/94A33429-E580-45C3-A090-5512A8070732), the default navigation includes Documents, Pages, and Site Contents. These categories are helpful as you are building your site, but they are not typically going to add value to your viewers once your site is ready to launch. This is because the consumer of a communication site typically doesn't care about the type of content – they care about the purpose or subject of the content. For communication sites, plan to delete the "out of the box" navigation when you are ready to launch and replace it with something that aligns with the guidance provided in the local navigation section of this guide.

The default navigation for [team sites](https://support.office.com/article/75545757-36c3-46a7-beed-0aaa74f0401e) includes links to the related services provided by Microsoft 365 for modern teams – including a link to the shared team notebook and the conversations for the team in Outlook. These represent the typical features that teams need to effectively collaborate and might be hard for people to find without the experience provided by the navigation. You may choose to supplement or refine these links for your team sites, but you will also likely find that the default navigation experience is a good starting point. You may be more likely to keep most of these links than you would with a communication site.

## Prioritize usability and findability

The key goal when we plan navigation is to make our sites useable and our content findable. The best way to ensure that your navigation meets these goals is to test it. There are several cost-effective approaches that you can use to ensure that your navigation design is effective, including:

- **Card Sorting** - Primarily helpful for planning navigation.
- **Tree Testing** - Helpful for testing suggested navigation paths.
- **Usability Testing** - Task-based scenarios that are helpful for comprehensive testing of site and page navigation.

These two resources provide an overview of techniques and tools for testing the usability and findability of your navigational strategy:

- [Usability Analysis](https://www.nngroup.com/articles/better-usability-tasks)
- [Overview of Testing Approaches](https://www.nngroup.com/articles/quantitative-user-research-methods)

## Write clear and intuitive labels

The words you use for navigation matter – not just because the real estate for navigation is limited – but also because your labels are what guide your viewers to the content. Each label makes a promise: if you select this link, you should get the information you expect to find.

To ensure that your labels keep their promises, make sure they are:

- **Specific** - Tell the viewer exactly what they will find when they select the link. If the target for your link includes Policies and Procedures, make sure the label includes both terms.
- **Comprehensive** - Describe content with your collection of labels. You should not plan to link to every single page or document in your navigation, but your navigation should provide a complete picture of the content on your site.
- **Concise** - Keep your labels short and to the point.
- **Familiar** - Don't make up terms in your labels. Keep your viewers in mind – if you use an unfamiliar term, your viewers will be confused and unable to find what they need.
- **Front-loaded** - Make sure that your labels are "scannable." For example, Company Information is better than Information About our Company.
- **Clear** - As much as possible, you want your navigation labels to be mutually exclusive – at least for the major categories. It is perfectly fine to have a sub-link display in multiple categories – especially if viewers might expect to find it in more than one place – but the major categories need to be easily distinguished from one another.
- **Targeted** - It’s not a good idea to show people links to private sites that they don’t have access to. Where appropriate, use the [audience targeting](https://support.office.com/article/68113d1b-be99-4d4c-a61c-73b087f48a81) features for SharePoint to target navigation links to viewers for whom the link will work. Note that there are exceptions to this guideline. For example, you may want to use your navigation to help people discover sites that they may not have access to today but could be approved to join. If you do provide links in navigation to private sites, be sure that the owner of the site knows that they may be getting a lot of access requests!

## Think about link target interactions

Many usability guidelines recommend [limiting the number of new windows that are automatically opened for site viewers](https://www.w3.org/TR/WCAG20-TECHS/G200.html). Most of the time, opening a link in the same window allows site viewers to use the back button when they want to return to your site. When a viewer wants to open a link in a new window, the guidelines recommend that the viewer be allowed to choose this outcome by "right clicking" the link. An exception to this guideline is the recommendation to always open documents in a new window to prevent users from accidentally closing the browser window when they close the document.

By default, navigation links on modern SharePoint sites open to a link that points to:

- **A page or site in the same tenant** (same site or another site) - Links open in the same tab.
- **A document** (same site or different site) - Links open in a new tab.
- **An external site or document** (internet site) - Links open in a new tab.

In classic SharePoint sites with publishing features, you can choose to open navigation links in a new window. This allows you to consider the context for your site viewers and determine whether it might be helpful to open a link in a new window. There is no way to select how navigation links open in modern SharePoint sites. This means that your navigation links will follow the default guidelines, but you still need to be especially careful about the labels for navigation links to make sure that your viewers know that they are leaving the site when they select the link. 

Make sure that the navigation label accurately describes the destination – a place on a completely different site or an application – and if you know that the back button may not work, consider using an alternative way to present the link, such as the text web part where you can elect to open a link in a new window.

At the current time, only the [Text web part](https://support.office.com/article/using-web-parts-on-sharepoint-pages-336e8e92-3e2d-4298-ae01-d404bbe751e0) lets you create a hyperlink and choose how the link opens. When you add a hyperlink to text, you have the option to choose to open the link in a new tab.


## Test usability and findability with real users

Once you have established a basic working structure for global, hub, or local level navigation experiences, you should test your design with real-life users. Create tasks and ask users to complete the tasks. Ask users to “think out loud” as they are looking for information and resources. Note where improvements to can be made and then implement and test the changes again. Plan to review basic global, hub, and local navigation experiences as your business changes and grows.

Learn more about navigation basics like how to write effective labels, how to test findability, and how to use menu styles.

[**Next: learn about SharePoint information architecture models and examples**](information-architecture-models-examples.md)