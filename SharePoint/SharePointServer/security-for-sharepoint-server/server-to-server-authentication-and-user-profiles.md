---
title: "Server-to-server authentication and user profiles in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/24/2017
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 3efb6e12-ad3c-41c7-9def-446df626aefd
description: "Learn how to plan user profiles for server-to-server authentication in SharePoint Server."
---

# Server-to-server authentication and user profiles in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
Server-to-server authentication allows for servers that are capable of server-to-server authentication to access and request resources from one another on behalf of users. Therefore, the server that runs SharePoint Server and that services the incoming resource request must be able to complete two tasks: 
  
- Resolve the request to a specific SharePoint user
    
- Determine the set of role claims that are associated with the user, a process known as rehydrating the user's identity 
    
To rehydrate a user's identity, a server that can perform server-to-server authentication requests access to SharePoint resources. SharePoint Server takes the claims from the incoming security token and resolves it to a specific SharePoint user. By default, SharePoint Server uses the built-in User Profile service application to resolve the identity.
  
The key user attributes for locating the corresponding user profile are as follows:
  
- The Windows Security Identifier (SID)
    
- The Active Directory Domain Services (AD DS) user principal name (UPN)
    
- The Simple Mail Transfer Protocol (SMTP) address
    
- The Session Initiation Protocol (SIP) address
    
Therefore, at least one of these user attributes must be current in user profiles. 
  
> [!NOTE]
> For SharePoint Server 2013 only, we recommend a periodic synchronization from identity stores to the User Profile service application. For more information, see [Plan profile synchronization for SharePoint Server 2013](../administration/plan-profile-synchronization-for-sharepoint-server-2013.md). 
  
Furthermore, SharePoint Server expects only one matching entry in the User Profile service application for a given lookup query that is based on these four attributes. Otherwise, it returns an error condition that multiple user profiles were found. Therefore, you should delete obsolete user profiles in the User Profile service application periodically to avoid multiple user profiles that share these four attributes.
  
If a user profile and the relevant group memberships for the user are not synchronized, SharePoint Server may incorrectly deny access to a given resource. Therefore, make sure that group memberships are synchronized with the User Profile service application. For Windows claims, the User Profile service application imports the four key user attributes previously described and group memberships. 
  
For forms-based and Security Assertion Markup Language (SAML)-based claims authentication, you must do one of the following:
  
- Create a synchronization connection to a data source that the User Profile service application supports and associate the connection with a specific forms-based or SAML authentication provider. Additionally, you have to map attributes from the user store to the four user attributes previously described, or as many of them as you can obtain from the data source.
    
- Create and deploy a custom component to perform the synchronization manually. This is the most likely option for users who do not use Windows. Note that the forms-based or SAML authentication provider is invoked when the user's identity is rehydrated to get their role claims.
    
## User rehydration for requesting servers

If the requesting server is running Exchange Server 2016 or Skype for Business Server 2015, which use standard Windows authentication methods, the incoming security token sent by the requesting server contains the UPN of the user and may contain other attributes such as SMTP, SIP, and the SID of the user's identity. SharePoint Server, the receiving server, uses this information to locate the user profile.
  
For a requesting server that is running SharePoint Server, the receiving server rehydrates the user through the following claims-based authentication methods:
  
- For Windows claims authentication, SharePoint Server uses AD DS attributes to find the user profile for the user (for example, the UPN or SID values) and their role claims (group membership).
    
- For forms-based authentication, SharePoint Server uses the Account attribute to locate the user's profile and then invokes the role provider and all additional custom claims providers to obtain the corresponding set of role claims. For example, SharePoint Server uses attributes in AD DS, in a database such as a SQL Server database, or in an Lightweight Directory Access Protocol (LDAP) data store to find the user profile that represents the user (for example, the UPN or SID values). Your component to synchronize your forms-based provider should at a minimum populate user profiles with the user's account name. You can also create a custom claim provider to import additional claims as attributes into user profiles.
    
- For SAML-based claims authentication, SharePoint Server uses the AccountName attribute to locate the user's profile and then invokes the SAML provider and all additional custom claims providers to obtain the corresponding set of role claims. The user identity claim should be mapped to the Account attribute in user profiles through the corresponding SAML claims provider, which should be configured to populate your user profiles. Similarly, a UPN claim should be mapped to the UPN attribute and the SMTP claim should be mapped to the SMTP attribute. To duplicate the set of claims that the user would usually obtain from their identity provider, you must add those claims, including the role claims, through claims augmentation. A custom claim provider must import those claims as attributes into user profiles.
    
## See also

#### Concepts

[Plan for server-to-server authentication in SharePoint Server](plan-server-to-server-authentication.md)
  
[Authentication overview for SharePoint Server](authentication-overview.md)

