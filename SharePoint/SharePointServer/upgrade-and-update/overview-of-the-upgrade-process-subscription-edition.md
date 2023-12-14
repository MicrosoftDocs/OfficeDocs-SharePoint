---
title: "Overview of the upgrade process to SharePoint Server Subscription Edition"
ms.reviewer: 
ms.author: serdars
author: jitinmathew
manager: serdars
ms.date: 07/09/2021
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
- SP2019
ms.custom: 
ms.assetid: 4d7a8038-4b27-4bd8-a855-585db4e924a8
description: "Learn about the process of upgrading databases, service applications, My Sites, and site collections to SharePoint Server Subscription Edition."
---

# Overview of the upgrade process to SharePoint Server Subscription Edition

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

To upgrade from Microsoft SharePoint Server 2019 and Microsoft SharePoint Server 2016 to SharePoint Server Subscription Edition, you use the database-attach method. In the database-attach method, you first create and configure a SharePoint Server Subscription Edition farm. Then you copy the content and service application databases from SharePoint Server 2019 and SharePoint Server 2016, and then attach and upgrade the databases. This upgrades the data to the new version. Site owners can then upgrade individual site collections.

SharePoint Server Subscription Edition supports an upgrade from RTM version of SharePoint Server 2019 and SharePoint Server 2016.

> [!NOTE]
> All databases must be upgraded to version 16.0.4351.1000 or higher, otherwise upgrade to SharePoint Server Subscription Edition will be blocked.

After you've configured a new SharePoint Server Subscription Edition environment, you can copy the content and service application databases from SharePoint Server 2019 and SharePoint Server 2016 to the SharePoint Server Subscription Edition environment. You use a backup and restore process to copy the database. You can also choose to set the databases to read-only in SharePoint Server 2019 and SharePoint Server 2016 environments so that users can continue to access their information, but not change it.

Before you attach and upgrade the content databases, review the following information and take any recommended actions.
  
- Ensure that the account that you use to attach the databases is a member of the **db_owner fixed** database role for the content databases that you want to upgrade.

- Ensure that the account that you use to create web applications is a member of the Farm administrators group in the SharePoint Central Administration website.

This article helps you to understand the upgrade sequence so that you can plan an upgrade project. To get detailed steps for an upgrade, see [Overview of the upgrade process to SharePoint Server Subscription Edition](upgrade-databases-subscription-edition.md) and [Upgrade site collections to SharePoint Server Subscription Edition](upgrade-a-site-collection-subscription-edition.md).

## Create the SharePoint Server Subscription Edition farm
<a name="CreateFarm"> </a>

The first stage in the upgrade process creates the new SharePoint Server Subscription Edition farm:

1. A server farm administrator installs SharePoint Server Subscription Edition to a new farm. The administrator configures farm settings and tests the environment.

2. A server farm administrator sets the SharePoint Server 2019 and SharePoint Server 2016 farms to read-only so that users can continue to access the old farm while upgrade is in progress on the new farm.
  
## Copy the SharePoint Server 2019 and SharePoint Server 2016 databases
<a name="CopyDatabases"> </a>

The second stage in the upgrade process copies the databases to the new environment. You use SQL Server Management Studio for these tasks.

1. With the farm and databases in read-only mode, a server farm administrator backs up the content and service application databases from the SQL Server instance on the SharePoint Server 2019 and SharePoint Server 2016 farms.

2. The server farm administrator restores a copy of the databases to the SQL Server instance on the SharePoint Server Subscription Edition farm and sets the databases to read-write on the new farm.
  
## Upgrade SharePoint Server 2019 and SharePoint Server 2016 databases and service applications
<a name="Databases"> </a>

The third stage in the upgrade process upgrades the databases and service applications.

1. A server farm administrator configures the service applications for the new farm. The following service applications have databases that you can upgrade during this process:

    - Business Data Connectivity service application

    - Managed Metadata service application

    - Search service application

    - Secure Store Service application

    - User Profile service application

2. A server farm administrator creates a web application on the SharePoint Server Subscription Edition farm for each web application on the SharePoint Server 2019 and SharePoint Server 2016 farms.

3. A server farm administrator installs all server-side customizations.
  
4. A server farm administrator then attaches the content databases to the new farm and upgrades the content databases for those web applications.
  
5. A server farm administrator confirms that the upgrade is successful.

## Upgrade SharePoint Server 2019 and SharePoint Server 2016 site collections
<a name="UpgradeSites"> </a>

The final stage in the upgrade process is to upgrade the site collections. The upgrade process for My Sites is slightly different from other types of site collections.
  
### Upgrade My Sites
<a name="MySites"> </a>

> [!IMPORTANT]
> This section applies to SharePoint Server Subscription Edition only.
  
A server farm administrator upgrades the My Site host and then individual users can upgrade their My Sites or the farm administrator can upgrade them by using PowerShell. The following list shows four stages for the My Site host and My Sites during the upgrade process:
  
1. The My Site host has not been upgraded. My Sites cannot be upgraded yet.

2. A server farm administrator has upgraded the My Site host. No My Sites have been upgraded.

3. Some users have upgraded their My Sites.

4. All My Sites have been upgraded.

> [!NOTE]
> A server farm administrator can choose to force an upgrade of My Sites without waiting for users to upgrade them. For details and steps, read [Upgrade site collections to SharePoint Server Subscription Edition](upgrade-a-site-collection-subscription-edition.md).

### Upgrade other SharePoint Server 2019 and SharePoint Server 2016 site collections
<a name="SiteCollections"> </a>

For information about how to upgrade a site collection, see [Upgrade site collections to SharePoint Server Subscription Edition](upgrade-a-site-collection-subscription-edition.md).

> [!NOTE]
> A server farm administrator can also force specific site collections to be upgraded without waiting for the site owners to upgrade them. For details and steps, read [Upgrade site collections to SharePoint Server Subscription Edition](upgrade-a-site-collection-subscription-edition.md).
