---
title: "Secure Store for Business Intelligence service applications"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: a19e8cb8-4b41-492b-b33c-bc490f911f1d
description: "Learn how Secure Store works with Excel Services, PerformancePoint Services, and Visio Services to refresh data on SharePoint Server."
---

# Secure Store for Business Intelligence service applications

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article describes how SharePoint Server business intelligence features use the Secure Store Service to provide access to external data sources (such as SQL Server) for SharePoint Server users. For the purposes of this article, the SharePoint Server business intelligence service applications are: 
  
- Excel Services (SharePoint Server 2013 only)
    
- PerformancePoint Services
    
- Visio Services
    
The SharePoint Server business intelligence service applications offer two methods of data access for users:
  
- Integrated Windows authentication using Constrained Kerberos delegation
    
- Secure Store Service (including an unattended service account)
    
Excel Services and PerformancePoint Services also support the SQL Server Analysis Services (SSAS) EffectiveUserName feature for Analysis Services connections.
  
This article covers Secure Store and its relationship to the business intelligence service applications.
  
For information about configuring specific scenarios in your SharePoint Server farm, see the following articles:
  
- [Use Excel Services with Secure Store Service in SharePoint Server 2016](use-excel-services-with-secure-store.md)
    
- [Use Visio Services with Secure Store Service in SharePoint Server](use-visio-services-with-secure-store.md)
    
- [Use PerformancePoint Services with Secure Store Service in SharePoint Server](use-performancepoint-services-with-secure-store.md)
    
## Secure Store Service and the business intelligence service applications in SharePoint Server

Secure Store is a feature in SharePoint Server that helps provide access to data outside SharePoint Server (for example, SQL Server data) by allowing a business intelligence service application to use a set of credentials with data access on behalf of a SharePoint Server user who is attempting to access that data. Such use of credentials by business intelligence service applications on behalf of users is called impersonation.
  
Secure Store provides this mapping between business intelligence services applications, users, and credentials through the use of a target application. A Secure Store target application is a collection of metadata that specifies which users shall be allowed access to a particular set of credentials that a business intelligence service application will use for impersonation when accessing external data. This metadata is stored in the Secure Store database along with the credentials themselves, which are encrypted.
  
Secure Store target applications can be used in many ways within SharePoint Server, but for the purposes of SharePoint Server business intelligence scenarios, target applications consist of the following settings, configurable by the Farm Administrator:
  
- **Administrators** Target application Administrators are users who have privileges to administer a given Secure Store target application. This can be the Farm Administrator or a specific user or users, depending on your needs. 
    
- **Members** The Members of a target application are the users on behalf of whom the Business Intelligence Service Application will impersonate the target application Credentials when it accesses external data. This could be a single user, multiple users, or an Active Directory group. Members are also referred to as Credential Owners.
    
- **Credentials** Target application Credentials consist of an account with direct access to data sources. (You must grant the required data access to this account directly — access to external data sources is not controlled by SharePoint Server. This should be a low-privileged account that only allows data access.) It is this account that is impersonated by business intelligence service applications to give users access to data. 
    
The Administrators, Members, and Credentials are configurable by the Farm Administrator directly through Secure Store. Additionally, both Excel Services and PerformancePoint Services provide an option to automatically create a Secure Store target application for use with the unattended service account.
  
The business intelligence service applications can use Secure Store by using one of two methods:
  
- **Specified target application** A specific target application is specified by the Excel worksheet, Visio diagram, or PerformancePoint data source. When a user accesses the worksheet, diagram, or dashboard, Secure Store uses the credentials associated with that target application for data access. 
    
- **No specified target application (unattended service account)** The unattended service account is specified by the Excel worksheet, Visio diagram, or PerformancePoint data source. When a user accesses the worksheet, diagram, or dashboard connected to an external data source, Secure Store uses the target application specified in the Global Settings of Excel Services, Visio Services, or PerformancePoint Services. When a target application is specified globally for a business intelligence service application, the target application credentials are referred to as the unattended service account.
    
The basic sequence of events that occurs is as follows:
  
1. A SharePoint Server user accesses a data-connected object such as an Excel Services worksheet, Visio Services diagram, or PerformancePoint Services dashboard.
    
2. The Business Intelligence Service Application accesses the target application specified by the object.
    
3. If the user is a Member of that target application, the credentials stored in the target application are returned and the Business Intelligence Service Application impersonates the credentials while accessing the data.
    
4. The data is displayed to the user within the context of the worksheet, Visio diagram, or dashboard.
    
## Data connection files

All of the business intelligence service applications can use data connection files to specify authentication information. Excel Services and Visio Services use Office Data Connection (.ODC) files and PerformancePoint Services uses PerformancePoint Services Data Connection (.PPSDC) files. Use of such files allows multiple Excel Services worksheets, Visio Services diagrams, or PerformancePoint Services dashboards to share a common set of data access parameters.
  
The SharePoint Server business intelligence service applications each use data connection files differently. For a description of how each uses data connection files, see the section for each service application, below.
  
## Data access from client and server

Excel 2016 and Visio 2016 are client applications that function independently from SharePoint Server. Though they can publish documents to SharePoint Server, they cannot use Secure Store directly for authentication to data sources. When you create or edit a data-connected worksheet or diagram, you must use Integrated Windows authentication or another applicable authentication method to connect directly to a data source from Excel 2016 or Visio 2016. (Other authentication methods you might use include SQL Authentication or an OLEDB connection string.) Once the worksheet or diagram is published to SharePoint Server, Excel Services or Visio Services can use Secure Store to connect to the data source when it displays the content to a user.
  
PerformancePoint Dashboard Designer is directly integrated with SharePoint Server. Dashboard Designer can use Secure Store directly to authenticate by using the unattended service account. As a result, users of Dashboard Designer do not need direct access to data sources through Integrated Windows authentication, provided the unattended service account has the required access.
  
## See also

#### Concepts

[Configure the Secure Store Service in SharePoint Server](configure-the-secure-store-service.md)
#### Other Resources

[Plan for Visio Services in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee663482(v=office.14))

