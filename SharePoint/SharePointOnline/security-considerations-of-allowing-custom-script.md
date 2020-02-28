---
title: "Security considerations of allowing custom script"
ms.reviewer: lucaband
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 6/15/2017
audience: Admin
f1.keywords:
- NOCSH
ms.topic: conceptual
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- SPB160
- BSA160
- MET150
ms.assetid: b0420ab0-aff2-4bbc-bf5e-03de9719627c
description: "Learn about security factors to consider before you allow users to run custom script on SharePoint sites or OneDrive. "
---

# Security considerations of allowing custom script

Allowing users to customize sites and pages in SharePoint by inserting script can give them the flexibility to address different needs in your organization. However, you should be aware of the security implications of custom script. When you allow users to run custom script, you can no longer enforce governance, scope the capabilities of inserted code, block specific parts of code, or block all custom code that has been deployed. Instead of allowing custom script, we recommend using the SharePoint Framework. For more info, see [An alternative to custom script](security-considerations-of-allowing-custom-script.md#spframework).
  
## What custom script can do

Every script that runs in a SharePoint page (whether it's an HTML page in a document library or a JavaScript in a Script Editor Web Part) always runs in the context of the user visiting the page and the SharePoint application. This means:
  
- Scripts have access to everything the user has access to.
    
- Scripts can access content across several Office 365 services and even beyond with Microsoft Graph integration.
    
## You can't audit the insertion of script

As a global admin, security admin, or SharePoint admin, you can allow or block custom script capabilities for the whole organization or for specific site collections. (For info on how to do this, see [Allow or prevent custom script](allow-or-prevent-custom-script.md).) However, once you allow scripting, you can't identify:
  
- What code has been inserted
    
- Where the code has been inserted
    
- Who inserted the code
    
Any user who has "Add and Customize Pages" permission (part of the Design and Full Control permission levels) to any page or document library can insert code that can potentially have a powerful effect on all users and resources in the organization. The script has access to more than just the page or site - it can access content across all site collections and other Office 365 services in the organization. There are no boundaries for executing script. For info about site activity you can audit, see [Configure audit settings for a site collection](https://support.office.com/article/a9920c97-38c0-44f2-8bcb-4cf1e2ae22d2).
  
## You can't block or remove inserted script

If you've allowed custom script, you can change the setting to later prevent users from adding custom script, but you can't block the execution of script that has already been inserted. If dangerous or malicious script was inserted, the only way you can stop it is to delete the page that hosts it. This might result in data loss.
  
## An alternative to custom script
<a name="spframework"> </a>

The [SharePoint Framework](https://dev.office.com/sharepoint/docs/spfx/sharepoint-framework-overview) is a page and web part model that provides a governed and fully supported way to build solutions using scripting technologies with support for open source tooling. Key features of the SharePoint Framework: 
  
- The framework runs in the context of the current user and connection in the browser. It doesn't use iFrames.
    
- The controls are rendered in the normal page Document Object Model (DOM).
    
- The controls are responsive and accessible.
    
- Developers can access the lifecycle. In addition to render, they can access load, serialize and deserialize, configuration changes, and more.
    
- You can use any browser framework you like: React, Handlebars, Knockout, AngularJS, and more.
    
- The toolchain is based on common open source client development tools like npm, TypeScript, Yeoman, webpack, and gulp.
    
- Office 365 admins have governance tools to immediately disable solutions regardless of the number of instances that have been used and the number of pages or sites across which they've been used.
    
- Solutions can be deployed in web parts and pages that use the classic experience or the new experience.
    
- Only global admins, SharePoint admins, and people who have been given permission to manage the App Catalog can add solutions. (For info about giving users permission to manage the app catalog, see [Request app installation permissions](request-app-installation-permissions.md).)
    

