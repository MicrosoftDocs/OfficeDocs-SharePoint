---
title: Plan customizations - SharePoint Online
ms.reviewer: lucaband
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: conceptual
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: b7898ebf-69b7-4196-81e3-b04e1a4e7d67
description: Learn about the range of options, such as branding, navigation, and workflows available for configuring and customizing SharePoint sites.
ms.custom: seo-marvel-jun2020
---

# Customizing SharePoint

In earlier versions of SharePoint, it was possible to make changes to a SharePoint environment by deploying custom code that would run in the physical SharePoint server environment. Changes made to SharePoint that didn't require the deployment of custom code were referred to as "customizations", because the changes were not fundamentally changing the product's functioning but were rather configuring the existing product in a unique way.

Examples of customizing SharePoint Server have included deploying custom branding elements such as master pages and style sheets to a site collection; deploying pre-configured web parts to a web part gallery; creating custom workflows in SharePoint Designer; changing the look and feel of list forms using InfoPath; and more.

Because of the shared nature of the SharePoint infrastructure, Microsoft does not allow the deployment of custom code to its environment. As a result, the concept of customizing SharePoint as opposed to deploying custom code is no longer a relevant paradigm. However, it's still helpful to think of ways that SharePoint can be customized, or configured uniquely, in a broader sense of the word.

The purpose of this document is to help you understand how you can customize your SharePoint environment using modern tools and techniques.

## Branding

Modern SharePoint sites allow you [to change the look of the site](https://support.office.com/article/06bbadc3-6b04-4a60-9d14-894f6a170818) by modifying elements such as the site logo and the colors used throughout the site. [Branding your SharePoint site](/sharepoint/branding-sharepoint-online-sites-modern-experience) can help you match a site to a brand as well as help users differentiate between multiple SharePoint sites. While several themes options are available by default, it&#39;s also possible to [specify unique theme colors](/sharepoint/dev/declarative-customization/site-theming/sharepoint-site-theming-overview) by supplying SharePoint with a custom configuration file. Older, "classic" SharePoint sites allow administrators to [apply custom branding](/sharepoint/dev/general-development/master-pages-the-master-page-gallery-and-page-layouts-in-sharepoint) and page layouts to a SharePoint site by applying a custom master page, [applying a custom theme](/sharepoint/dev/declarative-customization/site-theming/sharepoint-site-theming-overview) to a site, deploying custom page layouts, and more. Because classic sites are not as fast and mobile-friendly as modern sites, Microsoft recommends using modern sites going forward.

## Navigation

Navigation helps users find the information they need quickly by providing links to pertinent information in a persistent manner. [Planning your navigational strategy in modern sites](/sharepoint/plan-navigation-modern-experience) is a critical element in the usability of your SharePoint environment. Modern SharePoint sites provide a streamlined model for [adding navigational elements](https://support.office.com/article/3cd61ae7-a9ed-4e1e-bf6d-4655f0bf25ca) using the browser. The position of the navigation is determined by the kind of site being viewed, the size of a user&#39;s screen, and whether the [megamenu option](https://support.office.com/article/06bbadc3-6b04-4a60-9d14-894f6a170818) has been enabled for the site. Additionally, modern sites can take advantage of hub site navigation.

Note that legacy versions of SharePoint allowed navigational elements to be dynamically generated using the structured navigation and managed metadata navigation providers. These options are no longer available in modern sites. However, if you are using a classic site with modern pages, you can still use these providers and the modern pages will reflect the correct navigational links. In terms of layout, because modern sites do not allow you to customize the site&#39;s master page or style sheet, it&#39;s not possible to move the position of the navigation elements on the page as could be done in classic SharePoint sites.

## Page content

Nearly every version of SharePoint has had a way of creating custom layouts for web pages, whether that was by selecting a web part page, a wiki page layout, or a publishing page layout. Modern sites also provide a similar functionality. However, rather than providing a static layout that provides a set number of editable regions on the page, modern pages provide the ability for page editors to ["stack" column layouts on a row-by-row basis](https://support.office.com/article/fc491eb4-f733-4825-8fe2-e1ed80bd0899). Page editors can also choose various options related to [how the title region of the page](https://support.office.com/article/b3d46deb-27a6-4b1e-87b8-df851e503dec#bkmk_customizetitle) is displayed. Finally, the most fundamentally way to customize a modern page is to place custom content on the page. This can be done [by adding modern web parts](https://support.office.com/article/336e8e92-3e2d-4298-ae01-d404bbe751e0) to the page. Note that web parts used in classic web sites will not work in modern sites. However, it is possible [to create and deploy custom ("client-side") web parts](/sharepoint/dev/spfx/web-parts/get-started/build-a-hello-world-web-part) that were created using the SharePoint Framework.

## Workflows

Microsoft recommends using [Power Automate](https://flow.microsoft.com) for configuring and executing all workflows in your Microsoft 365 environment, including SharePoint. For example, it's possible to create [unique approval workflows](/flow/modern-approvals) for content stored in SharePoint. Additionally, it's possible to use Power Automate as the default workflow engine [for approving SharePoint page content](https://support.office.com/article/a8b2e689-d4a1-4639-8028-333c0ece30d9), directly from the SharePoint user interface. Flows can be [triggered by SharePoint](/connectors/sharepointonline/#triggers) actions (such as when an item is created in a list), or perform [actions within SharePoint](/connectors/sharepointonline/#actions) (such as update a list item). While SharePoint Designer workflows are still supported, new workflows should be created using Power Automate.

## Forms

[Power Apps](https://powerapps.microsoft.com) can be used to create custom forms for use in modern SharePoint sites. There are several ways in which these Power Apps forms can be used in your SharePoint site:

- [As a custom SharePoint list form](/powerapps/maker/canvas-apps/customize-list-form)
- [As a custom SharePoint list view](https://support.office.com/article/9338b2d2-67ac-4b81-8e67-97da27e5e9ab)
- [As a stand-alone app that uses a SharePoint as its data source](/powerapps/maker/canvas-apps/connections/connection-sharepoint-online)

You can [embed a Power App form in a modern page](https://support.office.com/article/6285f05e-e441-408a-99d7-aa688195cd1c) using the Power Apps web part.

Forms that were previously created using InfoPath and hosted in SharePoint using InfoPath Forms Services should be converted to Power Apps forms, as Microsoft has announced [the deprecation of InfoPath](https://www.microsoft.com/microsoft-365/blog/2014/01/31/update-on-infopath-and-sharepoint-forms/).

[Microsoft Forms](https://forms.office.com/) can also be used for [easily creating light-weight forms](https://support.office.com/forms). Like Power Apps, it's possible to [embed a Microsoft Form in a page](https://support.office.com/article/d4b4d3ce-7860-41e4-8a98-76380efe7256) using the Microsoft Forms web part.

## Customize your SharePoint site programmatically

Legacy versions of SharePoint Server relied on solution packages to deploy content and make configuration changes to SharePoint sites. It's still possible [to programmatically provision sites](/sharepoint/dev/solution-guidance/modern-experience-customizations-provisioning-sites) as well as customize [team sites](/sharepoint/dev/solution-guidance/modern-experience-customizations-customize-sites), [lists and libraries](/sharepoint/dev/solution-guidance/modern-experience-customizations-customize-lists-and-libraries), and [site pages](/sharepoint/dev/solution-guidance/modern-experience-customizations-customize-pages). There are [various methods](/sharepoint/dev/solution-guidance/office-365-development-patterns-and-practices-solution-guidance) for making programmatic changes to your SharePoint environment, including using the [Office Developer Patterns and Practices APIs,](https://github.com/SharePoint/PnP) the [Microsoft 365 CLI](https://pnp.github.io/office365-cli/), the [Microsoft Graph API](https://developer.microsoft.com/graph/), the [SharePoint Framework](/sharepoint/dev/spfx/sharepoint-framework-overview?view=sp-typescript-latest), and more.

Use the [SharePoint Framework (SPFx)](/sharepoint/dev/spfx/sharepoint-framework-overview?view=sp-typescript-latest) to render custom web parts on a modern SharePoint page. Additionally, [Extensions to the SPFx](/sharepoint/dev/spfx/extensions/overview-extensions) provide the ability to add scripts to pages, create modified views of data, and surface new commands in the SharePoint user interface. SPFx application packages can be deployed to SharePoint sites using the [SharePoint App Catalog](use-app-catalog.md).

## Use third-party add-ins and solutions

Not only can you deploy custom apps (also known as add-ins) to your environment, but you can also purchase add-ins from the SharePoint Store. You can make these add-ins available to all users across the sites in your organization by acquiring licenses for all users in your organization. Or, you can acquire licenses for only those who need to use it, and assign those licenses to the designated users. For more information, see [Buy an app from the SharePoint Store](https://support.office.com/article/dd98e50e-d3db-4ecb-9bb7-82b189822d43) and [Manage app licenses for a SharePoint environment](manage-app-licenses.md).

If you want to change the settings for whether or not site users can acquire apps from the SharePoint Store, see [Configure settings for the SharePoint Store](configure-sharepoint-store-settings.md).

If you are interested in exploring services or applications from Microsoft partners that are available for SharePoint, browse Microsoft 365 apps on [Microsoft AppSource](https://go.microsoft.com/fwlink/?linkid=865097). There are also many open-source solutions developed by the collective SharePoint community, including Microsoft, MVPs, Partners, and Customers on the [Microsoft 365 Developer Patterns and Practices GitHub site](https://github.com/OfficeDev/PnP).

## Examples of modern customization approaches

The following table gives an example of older methods for customizing sites along with a current recommended approach:

| Legacy | Modern |
| --- | --- |
| Implement branding using custom master pages, page layouts, and themes | Use the "apply a look" option to customize branding elements like logo, header, footer and colors |
| Use custom navigation providers such as structured navigation or managed metadata navigation to dynamically generate navigational elements | Manually specify navigational links |
| Create a wiki page and choose a text layout option to modify the layout of the page | Create a modern page and add section layouts to the page to arrange web parts on the page. |
| Create a workflow using SharePoint Designer | Create a workflow using Power Automate |
| Customize a SharePoint form using InfoPath | Customize a SharePoint form using a Power App |
| Deploy a web part to a site using a sandbox solution | Use the SharePoint App Catalog to deploy a client-side web part to a site |
