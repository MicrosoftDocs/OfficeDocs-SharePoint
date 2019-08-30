---
title: "Overview of profile synchronization in SharePoint Server 2016"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/27/2018
audience: ITPro
ms.topic: interactive-tutorial
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: e283aaec-e962-46b4-92e4-b8a825521641
description: "Learn about profile synchronization, also known as profile sync,in SharePoint Server 2016."
---

# Overview of profile synchronization in SharePoint Server 2016

[!INCLUDE[appliesto-xxx-2016-xxx-xxx-md](../includes/appliesto-xxx-2016-xxx-xxx-md.md)] 
  
A user profile is a collection of properties that describes a SharePoint user. Features such as My Sites and People Search use user profiles to provide a rich, personalized experience for the users in your organization. You can create user profiles by importing data from directory services, such as Active Directory Domain Services (AD DS). You can augment user profiles by importing data from business systems, such as SAP or SQL Server. The process of importing profile data from external systems and writing data back to these systems is called profile synchronization.
  
## Options for profile synchronization

Previous versions of SharePoint Server had a built-in copy of ForeFront Identity Manager (FIM) that ran inside SharePoint Server. That version of FIM powered the User Profile Synchronization for products like SharePoint Server 2010 and SharePoint Server 2013. But in SharePoint Server 2016, FIM has been removed in favor of [Microsoft Identity Manager (MIM)](https://go.microsoft.com/fwlink/?LinkId=760650), which is the successor to the FIM technology. MIM is a separate server technology (not built-in to SharePoint Server). That means, if you have MIM running in your company, more than one SharePoint Server 2016 farm can rely upon it. 
  
It's also important to note, here, that Active Directory Import (sometimes called Active Directory Direct Import) is still included with SharePoint Server 2016, and is a User Profile Synchronization alternative that does not need a separate server installation. This means that SharePoint Server 2016 offers two options for User Profile Sync.
  
A third option, if you're using Office 365, is to use [hybrid profiles](https://go.microsoft.com/fwlink/p/?LinkID=746962) as part of a [SharePoint hybrid deployment](https://go.microsoft.com/fwlink/p/?LinkID=746868). With hybrid profiles, SharePoint Server 2016 on-premises profiles aren't necessary, as users are automatically redirected to their profile in SharePoint Online.
  
Which option is right for you?
  
|||||
|:-----|:-----|:-----|:-----|
||**Microsoft Identity Manager 2016** <br/> |**Active Directory Import** <br/> |**Hybrid profiles** <br/> |
|Pros  <br/> | Supports customized import.  <br/>  Supports bidirectional flow.  <br/>  Imports user profile photos automatically.  <br/>  Supports non-Active Directory LDAP sources.  <br/>  Supports multi-forest scenarios.  <br/> | Very fast, high performance.  <br/>  Configurable inside of Central Administration. (Less complex.)  <br/> | Single profile for users who use both SharePoint Server and SharePoint Online.  <br/>  Can include Delve, depending on your Office 365 configuration.  <br/> |
|Cons  <br/> | A separate MIM server is recommended for use with your SharePoint Server farm.  <br/>  Customization can lead to more complex architecture, deployment, and management.  <br/> | Import is unidirectional (changes go from AD DS to SharePoint Server).  <br/>  Import from a single Active Directory forest only.  <br/>  Does not import user photos automatically.  <br/>  Supports Active Directory LDAP only.  <br/>  Multi-forest scenarios are not supported.  <br/> | Can require a custom solution to move on-premises properties to Office 365.  <br/> |
   
These three options are mutually exclusive. Each is further described in the following sections.
  
### Importing profiles by using SharePoint Active Directory Import
<a name="importDS"> </a>

You can create new profiles and import profile properties by synchronizing with AD DS by using SharePoint Active Directory Import. When you do this, SharePoint Server 2016 does the following:
  
- Creates a user profile for each new user in the AD DS containers that are being synchronized, and fills in the properties of each new profile with data from the directory service.
    
- Deletes the profile of any user who was removed from the directory service.
    
- For properties that are being imported, updates the property in the SharePoint user profile if the corresponding value in AD DS has changed.
    
You can synchronize the same users from two directory services. The connection to the logon forest provides the users. The connection to the resource forest merely augments the properties of existing profiles, similarly to a connection to a business system.
  
 **Synchronization options**
  
You can perform two kinds of synchronization: full and incremental. Full synchronization can take a long time—for directories that contain hundreds of thousands of users, it could take several days. Incremental synchronization only synchronizes data that has changed in AD DS or SharePoint Server 2016, and is more efficient. You must perform a full synchronization the first time that you synchronize. After that, you can use incremental synchronization unless there have been changes to mapped properties or connections.
  
You can [configure a timer job to run an incremental synchronization on a set schedule](schedule-profile-synchronization.md), ranging from every few minutes through monthly. You can also [start either a full synchronization or an incremental synchronization manually](start-profile-synchronization-manually.md).
  
### Importing profiles using an external identity manager
<a name="MIM"> </a>

If you need capabilities that go beyond what SharePoint Active Directory Import can do, you can use Microsoft Identity Manager 2016 (MIM). MIM installs on a separate server and is separately managed from SharePoint Server.
  
To learn how to configure MIM for use with SharePoint Server 2016, see the following resources:
  
- [Install Microsoft Identity Manager for User Profiles in SharePoint Server 2016](install-microsoft-identity-manager-for-user-profiles-in-sharepoint-server-2016.md)
    
- [Use a sample MIM solution in SharePoint Server 2016](use-a-sample-mim-solution-in-sharepoint-server-2016.md)
    
### Hybrid profiles
<a name="MIM"> </a>

Hybrid profiles can be configured as part of an overall SharePoint Hybrid deployment. Hybrid features help you integrate the user experience between SharePoint Server and Office 365 by linking common features together or by automatically redirecting users to Office 365 to use a given feature.
  
With hybrid profiles, your users' profiles are handled entirely in Office 365. If there is data in your on-premises network that you want to include in your Office 365 profiles, you can create a custom solution to copy this data to Office 365.
  

