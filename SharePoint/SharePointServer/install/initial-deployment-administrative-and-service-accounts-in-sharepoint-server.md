---
title: "Initial deployment administrative and service accounts in SharePoint Server"
ms.reviewer: 
ms.author: kirks
author: Techwriter40
manager: pamgreen
ms.date: 8/3/2017
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SP2019
ms.assetid: 06765032-fedb-4b73-a019-f096b48cd2a8
description: "Learn about the administrative and service accounts you need to initially install SharePoint Server."
---

# Initial deployment administrative and service accounts in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
This article provides information about the administrative and service accounts that you need for an initial SharePoint Server deployment. Additional accounts and permissions are required to fully implement all aspects of a production farm.
  
> [!NOTE]
> For a complete list of permissions for SharePoint Servers 2013, 2016 and 2019, see [Account permissions and security settings in SharePoint Servers 2013, 2016 and 2019](account-permissions-and-security-settings-in-sharepoint-server.md).
  
> [!IMPORTANT]
> Do not use service account names that contain the symbol $. 

## SharePoint Server account recommendations
<a name="Section2"> </a>

The following sections describe recommendations on SharePoint Service accounts.

Microsoft recommends using a minimal number of Service Application Pool accounts in the farm. This is to reduce memory usage and increase performance while maintaining the appropriate level of security.

- Use an elevated, personally identifiable account for SharePoint installation, maintenance, and upgrades. This account will hold the roles required as outlined by the **SharePoint Farm Administrator account** outlined below. Each SharePoint administrator should use a separate account to clearly identify activity performed by the administrator on the farm.

- If possible use a security group, **SharePoint Farm Administrators Groups**, to unify all individual SharePoint Farm Administrator accounts and grant permissions as outlined below. This simplify the management of the SharePoint Farm Administrator accounts significally.

- The **SharePoint Farm Service account** should only run the SharePoint Timer service, SharePoint Inights (if applicable), the IIS Application Pools for Central Administration, SharePoint Web Services System (used for the topology service), and SecurityTokenServiceApplicationPool (used for the Security Token Service).

- A single account should be used for all Service Applications, named **Service Application Pool account**. This allows the administrator to use a single IIS Application Pool for all Service Applications. In addition, this account should run the following Windows Services: SharePoint Search Host Controller, SharePoint Server Search, and Distributed Cache (AppFabric Caching Service).

- A single account should be used for all Web Applications, named **Web Application pool account**. This allows the administrator to use a single IIS Application Pool for all Web Applications. The exception is the Central Administration Web Application, which as noted above, is run by the SharePoint farm service account.

- With the exception of the Claims to Windows Token Service account, no Service Application Pool account should have Local Administrator access to any SharePoint server, nor any elevated SQL Server role, for example, the *sysadmin* fixed role. The SharePoint Farm Administrator account will require the *dbcreator* and *securityadmin* fixed roles unless you pre-provision SharePoint databases and manually assign permissions to each database.

- Service Application Pool accounts, with the exception of the account running the Claims to Windows Token Service, should have *Deny logon locally* and *Deny logon through Remote Desktop Services* in the Local *Security Policy\User Rights Assignment*. This is set via *secpol.msc*.

- Use separate accounts for the **Content access** (Search crawler), **Portal Super Reader**, **Portal Super User**, and **User Profile Service Application Synchronization**, if applicable.

- The Claims to Windows Token Service account is a highly privledged account on the farm. Prior to deploying this service, verify it is required. If required, use a separate account for this service.

### Service accounts recommendations overview

Service account name|What is it used for?|How many should be used?
----|----|----
SharePoint Farm Administrator account|Personally identifiable account for a SharePoint Administrator|1-n
SharePoint Farm Service Account| Timer Service, Insights, IIS App for CA, SP Web Services System, Security Token Service App Pool|1
Default content access account|search crawling internal and external sources SP2016|1-n
Content access accounts|search crawling internal and external sources SP2016 and SP2019|1-n
Web Application Pool account|All Web Applications without Central Administration|1
SharePoint Service Application Pool account|All Service Applications|1
Portal Super Reader|Object caching|1
Portal Super User|Object caching|1
User Profile Service Application Synchronization|Used for Active Directory Import|1-n

## SharePoint Server least-privilege administration

> [!NOTE]
> We recommend that you install SharePoint Server by using least-privilege administration. 

> [!IMPORTANT]
> Please keep in mind, there is a difference between SharePoint least-privilege administration and making SharePoint Server least-privilege. Due to the product design of SharePoint, it's close to impossible to make SharePoint Server use least-privilege.

The table above gives an overview of the current recommended SharePoint service and administrative accounts. Please be aware of the following remakrs:
- It's highly recommended to use these distinct accounts and ActiveDirectory groups to assign permissions to users.
- Please make yourself familiar with the permission management within SharePoint Server Central Administration. The recommendations above do not necessarily lead to least-privilege administration.
- Use personalized accounts for adminsitrators
- Tailor the set of permissions given to an administrator according to the target service applications and this administrators responsibility..
