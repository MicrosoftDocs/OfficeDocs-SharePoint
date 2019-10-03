---
title: "People Picker and claims providers overview in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/28/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: bf8717c2-463d-4e8d-acaf-f186b5907df1

description: "Get an overview of People Picker and links to topics about how to plan for People Picker in SharePoint Server."
---

# People Picker and claims providers overview

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
People Picker is a web control that is used to find and select users, groups, and claims to grant permission to items such as lists, libraries, or sites in SharePoint. For web applications that use claims-based authentication, the People Picker control uses claims providers to list, resolve, search, and determine the "friendly" display of users, groups, and claims. A claims provider in SharePoint issues claims, which SharePoint then packages into security tokens for users. Although People Picker is used by site, list, and library owners to assign permissions to sites and content in SharePoint, its behavior is heavily dependent on how authentication is configured for the whole web application. It is important to plan for People Picker and claims providers when you plan authentication methods for your SharePoint solution.
  
    
## People Picker architecture
<a name="architecture"> </a>

The People Picker control is a central component of SharePoint. The control is connected to a repository so that you can find and select users, groups, and claims to assign permissions in a site. The exact sources of those users, groups, and claims depend on the authentication method that is used by the web application that contains the site collection. For more information about authentication methods, see [People Picker and authentication](#auth) later in this article. 
  
People Picker is configured at the zone level for a farm by using the Stsadm **setproperty** operation. By configuring the settings for the control, you can filter and restrict the results that are displayed when a user searches for a user, group, or claim. Those settings will apply to every site in a specific site collection. For more information about how to configure People Picker, see [Configure People Picker in SharePoint Server](/previous-versions/office/sharepoint-server-2010/gg602075(v=office.14)).
  
When a web application is configured to use claims-based authentication, People Picker uses claims providers to resolve and display users, groups, and claims in the user or group text box. The information that SharePoint displays depends on the claims provider that is used by the authentication method that was configured for the web application. For more information about claims providers, see [Plan for custom claims providers for People Picker in SharePoint](plan-for-custom-claims-providers-for-people-picker.md).
  
## About the People Picker control
<a name="about"> </a>

When you type the first three characters of a user name, group name, or claim (such as an e-mail address) into the text box, People Picker automatically searches for results that match the first three typed characters. You can then select from a drop-down list, which displays up to thirty suggested names with titles. If you rest the mouse pointer on a suggestion, SharePoint displays the email address and claims provider. To resolve a name, select it from the drop-down, or use your arrow keys to select it, and then press ENTER. You can also type the complete name followed by a semicolon. If a unique name is found, SharePoint will resolve it. Otherwise, SharePoint shows suggestions or indicates that the name was not found. You can delete a resolved name in the text box by using the BACKSPACE key or by clicking the "x" next to the name.
  
When a web application is configured to use Windows authentication, you can limit the suggested results by using the Stsadm **setproperty** operation to change the settings for the People Picker control. For example, you can configure People Picker to return only users, groups, and claims that belong to a certain Active Directory domain or are members of a specific site collection. For more information about how to configure the People Picker control, see [Configure People Picker in SharePoint Server](/previous-versions/office/sharepoint-server-2010/gg602075(v=office.14)).
  
## People Picker and authentication
<a name="auth"> </a>

People Picker relies on the authentication method that is used by the web application that contains the site collection from which it is queried to determine what results to display to a user. If the web application is configured to use claims-based authentication (recommended), you can specify whether to use Windows authentication, forms-based authentication, or Security Assertion Markup Language (SAML) token-based authentication. In claims mode, People Picker searches and resolves queries that are based on the claims provider that is specified for the authentication method that is used by the web application and zone. If the web application is configured to use Windows authentication in classic mode, SharePoint treats user accounts as Active Directory Domain Services (AD DS) accounts. The following sections describe People Picker behavior for both claims-based and classic mode authentication. For more information about zones and authentication, see [Plan for user authentication methods in SharePoint Server](../security-for-sharepoint-server/plan-user-authentication.md).
  
### Claims-based authentication

When claims-based authentication is used, People Picker uses the claims provider that is specified for the authentication method to retrieve a list of users, groups, or claims that is used by the web application and zone that match the search item typed in the text box. For more information about claims mode authentication and zones, see [Plan for user authentication methods in SharePoint Server](../security-for-sharepoint-server/plan-user-authentication.md).
  
You can write a custom claims provider to control what information is displayed and what results are returned in response to a query from the People Picker control. When a custom claims provider is registered on the server, you can also configure it for use in a specific web application and zone. For more information about custom claims providers, see [Plan for custom claims providers for People Picker in SharePoint](plan-for-custom-claims-providers-for-people-picker.md).
  
> [!NOTE]
> In the Central Administration website, People Picker will return users, groups, and claims from all claims providers used in all web applications in the farm, regardless of the web application or zone in which the claims providers are configured. 
  
By default, when you use SAML token-based authentication, all queries entered in the text box are automatically displayed as if they were resolved, regardless of whether they are valid users or groups. If your SharePoint solution will use SAML token-based authentication, you should plan to create a custom claims provider that will implement custom search, name resolution, and list features. For more information about custom claims providers, see [Plan for custom claims providers for People Picker in SharePoint](plan-for-custom-claims-providers-for-people-picker.md).
  
For information about how to create a web application that uses claims-mode authentication, see [Create claims-based web applications in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee806885(v=office.14)). For information about how to configure claims-based authentication for web applications, see [Configure claims authentication](/previous-versions/office/sharepoint-server-2010/ee806886(v=office.14)).
  
### Classic mode authentication

When classic mode authentication (also known as Windows classic authentication) is used, the People Picker control queries Active Directory to retrieve a list of users, groups, or claims that match the search item typed in the text box. You can configure People Picker to query AD DS by using Lightweight Directory Access Protocol (LDAP) queries, which enables you to apply custom Active Directory filters, limit the scope of search queries, and search across forests and domains.
  
For more information about classic mode authentication, see [Plan for user authentication methods in SharePoint Server](../security-for-sharepoint-server/plan-user-authentication.md). For information about how to create a web application that uses classic mode authentication, see [Create web applications that use classic mode authentication in SharePoint Server](/previous-versions/office/sharepoint-server-2010/gg276326(v=office.14)).
  
## Articles about People Picker and custom claims providers
<a name="links"> </a>

The following articles about People Picker and custom claims providers are available to view online. Writers update articles on a continuing basis as new information becomes available and as users provide feedback.
  
|**        ![Checklist icon (not checked)](../media/mod_icon_checklist_.png)                 **|**Content**|**Description**|
|:-----|:-----|:-----|
||[Plan for People Picker in SharePoint](plan-for-people-picker.md) <br/> |Describes the People Picker control and how it works, its relationship to authentication and claims providers, and includes planning considerations for People Picker.  <br/> |
||[Plan for custom claims providers for People Picker in SharePoint](plan-for-custom-claims-providers-for-people-picker.md) <br/> |Describes the use and benefits of claims providers, their architecture, special considerations for custom claims providers, and planning considerations for them.  <br/> |
   
## See also
<a name="links"> </a>

[Configure People Picker in SharePoint Server](/previous-versions/office/sharepoint-server-2010/gg602075(v=office.14))

