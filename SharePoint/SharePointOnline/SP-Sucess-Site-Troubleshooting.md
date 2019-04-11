---
title: "Troubleshooting your SharePoint Success Site"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- OSU150
- MET150
description: "SharePoint Success Site Troubleshooting."
---
# Troubleshooting your SharePoint Success Site

Here are troubleshooting tips for problems that may occur with the SharePoint Success Site or the SharePoint Online Provisioning Service.

## How to know if you have Tenant Admin permissions

Signing into the SharePoint Online Provisioning Service and provisioning the SharePoint Success Site requires Tenant Admin permissions. If you are experiencing sign in issues with the SharePoint Online Provisioning Service, make sure that you have been assigned the Global administrator role. The SharePoint Success Site solution requires Tenant Admin permissions, otherwise known as Office 365 Global Administrator role. Here’s how to determine if you have been assigned the Global Administrator role.

1.	Sign in to Office.com.
2.	Click Admin
3.	Under Users, select Active Users
4.	Search for your name
5.	Click your name in Search results. You should see Global administrator for your role.
 
### If you don’t have the Global administrator role
- Find a Global Administrator in your organization and have that person sign into the service or have them assign the Global administrator role to you.


## Tenant App Catalog Troubleshooting
The SharePoint Success Site requires an App Catalog to be provisioned in the target tenant. Creating an app catalog requires Global Administrator permissions. Here’s are troubleshooting steps for common App Catalog issues:

### How to know if you have a Tenant app catalog

For starters, ensure that you have Global administrator permissions. See the steps for Tenant Admin permissions above.

1. From Office 365, click Admin, click the expand arrow >, click Show all > Admin centers > SharePoint.
2. Click Classic Admin SharePoint Center > apps > App Catalog.
3.	Under Apps, you should see a tile titled Distribute apps for SharePoint. If you see the tile, you have a Tenant App Catalog. See the How to ensure your are a Site Colllection... section below. If you don’t see the tile you will need to create a tenant app catalog for your tenant. See the How to create a Tenant App Catalog section below .

### How to ensure you are a Site Collection Owner on the Tenant App Catalog

To provision the SharePoint Success Site, you will need to be a Site Collection Owner on the Tenant App Catalog. Here’s how to determine if you are an Owner.

1.	From Office 365, click Admin, click the expand arrow >, click Show all > Admin centers > SharePoint.
2.	Click Classic Admin SharePoint Center, and then select the app catalog.
3.	Select Owner, and then ensure you are a Site Collection Owner. It should look something like this.
 
### How to create a Tenant App Catalog if one doesn’t exists

1.	Sign in to Office 365 with your SharePoint Online admin account.
2.	Click Admin.
3.	Under Admin centers, click SharePoint.
4.	Click Apps > App Catalog.
5.	Click Create a new app catalog site, and then click OK.
6.	Enter the information for the App Catalog. You may want to include more than one Administrator. The following shows an example.

