---
title: "Preparing for the retirement of Internet Explorer 11"
ms.reviewer: aharmetz
ms.author: matteva
author: matteva
manager: pamgreen
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.collection:  
- M365-collaboration
description: "Prepare your SharePoint environment for the retirement of Internet Explorer 11 for Microsoft 365 apps and services."
---
# Prepare your SharePoint environment for the retirement of Internet Explorer 11 for Microsoft 365 apps and services

As Microsoft 365 evolves, we continually evaluate our apps and services to make sure that we deliver the most value to customers. Last August, we
[announced that in one year we would say farewell to Internet Explorer 11](https://techcommunity.microsoft.com/t5/microsoft-365-blog/microsoft-365-apps-say-farewell-to-internet-explorer-11-and/ba-p/1591666).

Although support for Internet Explorer 11 continues, we’ve shifted web browser development resources to the
[Microsoft Edge browser](https://www.microsoft.com/edge/business). Focusing on Microsoft Edge helps us accelerate innovation in Microsoft 365 experiences from the browser and in modern apps, such as Microsoft Teams, OneDrive, SharePoint, Lists, and more.

Beginning on August 17, 2021, [Microsoft 365 apps and services will no longer support Internet Explorer 11](/lifecycle/announcements/internet-explorer-11-support-end-dates). While we know this change will be difficult for some customers, we believe that you'll get the most out of Microsoft 365 when using Microsoft Edge. To ease the transition for document libraries, we will fall back to the Classic experience when you use Internet Explorer 11. Also, we’ve identified considerations and practices for admins as you transition off classic SharePoint features that rely on Internet Explorer 11.

## Deploy a modern browser such as Microsoft Edge

Start by [ensuring Microsoft Edge is deployed and configured in your environment](/deployedge/deploy-edge-plan-deployment). The article guides customers through key questions and steps in the transition to Microsoft Edge.

Customers with Microsoft Unified Support can reach out to that support service for help with transitioning to Microsoft Edge.

For customers who want guidance on how to plan, deploy, or adopt Microsoft Edge, there’s [FastTrack](/fasttrack/products-and-capabilities#the-new-microsoft-edge). FastTrack is available at no extra charge to customers with 150 or more paid seats of Windows 10 Enterprise. To get started, submit a [Request for Assistance](/fasttrack/products-and-capabilities#the-new-microsoft-edge) through the FastTrack site.

And for customers who prefer to get started on their own, we have [self-guided deployment and configuration materials](/deployedge/) on our Docs site, complete with a [series from Microsoft Mechanics](https://www.youtube.com/playlist?list=PLXtHYVsvn_b-uXh1tMeYpT-0iD8tD3tFy).

## Transition to Sync instead of Open with Explorer

Open with Explorer relies on Internet Explorer 11 and isn’t available in newer browsers like Microsoft Edge. We recommend using the OneDrive sync app to [sync SharePoint files with your computer](https://support.microsoft.com/office/6de9ede8-5b6e-4503-80b2-6190f3354a88), rather than using Open with Explorer.

Sync with [OneDrive Files On-Demand](https://support.microsoft.com/office/0e6860d3-d9f3-4971-b321-7092438fb38e) helps you work with all your cloud files in File Explorer without having to download all the files and use storage space on your device. For easy access to files that people share with you or that you find in SharePoint or Teams, you can [add shortcuts to shared folders](https://support.microsoft.com/office/d66b1347-99b7-4470-9360-ffc048d35a33). The shortcuts then appear in your OneDrive so you can find and work with the files.

We understand that some customers continue to depend on Open with Explorer. To ease this transition, customers who go to a document library in Internet Explorer 11 will see the Classic experience with this feature available.

To get started deploying and configuring OneDrive in your environment and migrating files, start at the [OneDrive resources page](/onedrive/onedrive). Keep in mind, though, that some environments aren’t compatible with OneDrive sync.

### Environments in which OneDrive Sync doesn’t work or isn’t supported

- On premises SharePoint Server 2016 environments or earlier versions of SharePoint Server.
- SharePoint Server 2019 with certain types of authentication, such as Security Assertion Markup Language (SAML). For more information, read [Plan for user authentication methods in SharePoint Server](/sharepoint/security-for-sharepoint-server/plan-user-authentication).
- Non-persistent virtual desktop environments in which the sync client isn’t installed on each computer. For more information, read [use the sync app on virtual desktops](/onedrive/sync-vdi-support).
- Versions of Windows that don't support [Files On-Demand](https://support.microsoft.com/office/0e6860d3-d9f3-4971-b321-7092438fb38e). Files On-Demand requires Windows 10 Fall Creators Update (version 1709 or later) or Windows Server 2019.

## Use Power Apps to automate business processes
  
To automate your business processes, we recommend that you create new custom forms solutions in Power Apps and [transform your InfoPath forms to Power Apps](/powerapps/maker/canvas-apps/transform-infopath). Power Apps allows you to build and deploy business solutions without writing code. Learn how to [Administer Power Platform](/power-platform/admin/admin-documentation).

## Use the Create a list experience, rather than the old Import Spreadsheet app

Follow the steps to [create a list based on a spreadsheet](https://support.microsoft.com/office/380cfeb5-6e14-438e-988a-c2b9bea574fa). The older Import Spreadsheet app under Add an app on the Site contents page relies on Internet Explorer 11 and will no longer be supported in Microsoft 365 after August 17, 2021.
