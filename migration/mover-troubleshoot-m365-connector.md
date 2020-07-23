---
title: Mover migration - Troubleshoot Office 365 connector
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Mover migration: Troubleshoot Office 365 connector."
---
# Troubleshooting a Office 365 connector

## App access error

If you encounter an error on authorization, try signing out of any Microsoft accounts, and attempt to authorize the **Connector** in an Incognito Window.

## Global admin account provisioning

Your global admin user must have a Office 365 account provisioned in order to administer other Office 365 accounts. If you create a service account for our app, ensure you also assigned a Office 365 license and walked through the Office 365 setup process.

## User provisioning

Are your Office 365 users provisioned? All Office 365 users must log in to their Office 365, and open Office 365 for us to transfer into their accounts. You can also provision Office 365 accounts via Windows PowerShell using the following commands (replace your URL and email appropriately):

`Connect-SPOService -Url https://example-admin.sharepoint.com -credential user@example.com`

`Request-SPOPersonalSite -UserEmails "neverloggedintest@example.onmicrosoft.com"`

## Office 365 permission requirements

Our app requires a global admin for authorization. The following table lists the scopes we require:

|**Permission**|**Allows our app to...**|
|:-----|:-----|
|Create, edit, and delete items and lists in all your site collections|Create or delete document libraries and lists in all site collections on your behalf.|
|View your basic profile|See your basic profile (name, picture, user name).|
|Maintain access to data you have given it access to|See and update the data you gave it access to, even when you are not currently using our app. This does not give our app any additional permissions.|