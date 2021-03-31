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
description: "Prepare your environment for the retirement of Internet Explorer 11."
---

# Preparing for the retirement of Internet Explorer 11


As Microsoft 365 evolves, we periodically evaluate the capabilities of apps and services to make sure we deliver the most value to customers. Last August, we announced [the end of support for Internet Explorer 11](/lifecycle/announcements/internet-explorer-11-support-end-dates) and we've shifted web browser development resources to the new Microsoft Edge browser. 

Focusing on Microsoft Edge allows us to accelerate innovation in modern Microsoft 365 experiences from the browser and in modern apps, such as Microsoft Teams, OneDrive, Lists and more.

Beginning on August 17, 2021, Microsoft 365 apps and services will no longer support Internet Explorer 11. With this change, the following classic SharePoint features will no longer be available or no longer supported:

- Open with Explorer. The modern replacement is to [Sync SharePoint files with your computer](https://support.microsoft.com/office/6de9ede8-5b6e-4503-80b2-6190f3354a88) and then work with them in Windows Explorer just like other files on your computer. Sync is actually better because users cna see all their files in the cloud, but the files don’t take up space on local hard drives. 
- InfoPath forms solutions that depend on Internet Explorer 11. The modern replacement is Power Apps that allows you to build and deploy business solutions without writing code. 
- Connect to Office. 

While we know this change will be difficult for some customers, we believe that customers will get the most out of Microsoft 365 when using the new Microsoft Edge. We are committed to helping make this transition as smooth as possible.


## Transitioning to Sync instead of Open with Explorer

We recommend using OneDrive to [Sync SharePoint files](https://support.microsoft.com/office/6de9ede8-5b6e-4503-80b2-6190f3354a88), rather than Open with Explorer. To get started deploying and configuring OneDrive in your environment and migrating files, start at the [OneDrive resources page](../../OneDrive/onedrive.yml). 


### Environments in which OneDrive Sync doesn’t work or isn’t supported 

- On premises SharePoint Server 2016 environments or earlier versions of SharePoint Server 
- SharePoint Server 2019 with certain types of authentication (SAML, etc.) 
- Non-persistent virtual desktop environments in which the sync client isn’t installed on each computer. For more information, read [use the sync app on virtual desktops](../../OneDrive/sync-vdi-support.md). 
- OneDrive Files On-Demand requires Windows 10 Fall Creators Update (version 1709 or later) or Windows Server 2019. We don’t recommend the sync client as a replacement for Open with Explorer in environments that don’t support Files On-Demand.

In environments where OneDrive Sync isn’t supported, you can use Internet Explorer mode in Edge.

### Transitioning to Power Apps instead of InfoPath forms
  
We recommend using Power Apps to [transform your InfoPath forms to Power Apps](/powerapps/maker/canvas-apps/transform-infopath) that automate your business processes. Learn how to [Administer Power Platform](/power-platform/admin/admin-documentation).

### Transitioning to ?? instead of Connect to Office

