---
title: "Overview of apps in SharePoint in Microsoft 365"
ms.reviewer: 
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
ms.date: 5/22/2018
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.collection: M365-collaboration
ms.localizationpriority: medium
search.appverid:
- SPO160
- MET150
ms.assetid: 5a25c5b0-bdfb-49f8-8ca3-046edc9cf598
description: "Learn how app requests work in SharePoint in Microsoft 365."
---

# Overview of apps in SharePoint

Apps are small, easy-to-use web applications that add functionality to SharePoint sites. They offer unlimited possibilities for customizing your sites in ways that are specific to your organization. For example, you can add apps that perform general tasks such as time and expense tracking, or apps that make it easy for customers to contact you, or productivity apps that enable you to establish data connections and develop reports for your stakeholders. 
  
Some apps are included with SharePoint, others might be developed by your organization, and still others are created by third-party developers and available for purchase from the SharePoint Store. 
  
Only those users who have the appropriate permission level can add apps to a site. Typically, Full Control permission (or membership in the Site Owners group) is the minimum requirement. But some apps require access to data sources or web services to read data required for the app. This kind of app has permissions associated with it. 
 
When the app requires organization-level permissions, the requestor will need approval from a Microsoft 365 admin to continue with the installation. The approval process includes a workflow, called the permission request flow, which ensures installation requests are directed to the right person. 
  
This article is intended for Global Administrators and SharePoint Administrators at the organization level who receive requests for app installation.

## Make the application available

Once the status has been changed to **Approved**, go to the SharePoint Store and acquire the app. This is done by clicking the link next to **View App Details** on the App Request entry.

At this point, site owners can check the **Your Requests** list to view the status of their request. After the application has been acquired and approved, it will show up in the **Apps you've requested** list.

## Delegate approval authority

As a Global Administrator or SharePoint Administrator in your organization, you can delegate app approval authority as a way of spreading the approval workaround, or alleviating approval bottlenecks. Remember that apps are stored and managed in the Apps site. To grant app approval permission to select users, you can add them as site admins on the Apps site. 
  
> [!CAUTION]
> When you add users as site admins on the Apps site, you are giving them the ability to approve the installation of apps that have organization-wide impact. Consider this decision carefully. 
  
To add site collection admins to the Apps site:

1. Go to the [Active sites page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=siteManagement&modern=true), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

1. Select the Apps site, and then select **Membership** on the command bar to open the details panel. 

1. Make the appropriate selection based on the type of member and provide input and select the name of the person who you want to manage apps, and then select **Save**.
