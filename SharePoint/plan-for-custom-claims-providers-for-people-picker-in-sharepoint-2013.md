---
title: Plan for custom claims providers for People Picker in SharePoint 2013
ms.prod: SHAREPOINT
ms.assetid: 3fca2556-ebca-4395-8f66-b3a645c05878
---


# Plan for custom claims providers for People Picker in SharePoint 2013
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013*  * **Topic Last Modified:** 2017-08-01* **Summary:** Learn about how to plan for custom claims providers for the People Picker web control in SharePoint Server 2013.You can use the claims providers that are included with SharePoint Server 2013, or you can create your own custom claims providers to connect to additional sources of claims and provide additional claims in the security token for a user. For example, if you have a customer relationship management (CRM) application that contains roles that are not found in the user repository in Active Directory Domain Services (AD DS), you can create a custom claims provider to connect to the CRM database and add CRM role data to a user's original security token. For more information about claims provider usage scenarios, see  [Claims Provider](https://technet.microsoft.com/en-us/library/ee535894.aspx).A claims provider in SharePoint Server 2013 is used to augment claims and to provide name resolution. In the claims augmentation role, a claims provider augments a user security token with additional claims during sign-in. For more information about claims augmentation, see  [Claims Provider](https://technet.microsoft.com/en-us/library/ee535894.aspx). In the name resolution role, a claims provider lists, resolves, searches, and determines the "friendly" display of users, groups, and claims in the People Picker. Claims picking enables an application to surface claims in the People Picker, for example when you configure the security of a SharePoint site or SharePoint service. For more information about People Picker, see  [Plan for People Picker in SharePoint 2013](html/plan-for-people-picker-in-sharepoint-2013.md).By default, the information that is resolved in People Picker when a query is performed depends on the information supplied by the claims provider. You can’t change what information is supplied and how it is displayed when you use an out-of-box claims provider. To do this, you must create a custom claims provider that will meet the needs of your solution for finding and selecting users, groups, and claims when a user assigns permissions to items such as a site, list, or library.When you create a custom claims provider, you can control what information is displayed and what results are returned in response to a query from the People Picker control. By default, you configure the web application to use claims authentication, and then register the claims provider on the server.Before reading this article, you should understand the concepts described in  [Plan for user authentication methods in SharePoint Server](html/plan-for-user-authentication-methods-in-sharepoint-server.md) and [The Role of Claims](https://technet.microsoft.com/en-us/library/ee913589.aspx). For additional information about claims-based authentication, see  [SharePoint Claims-Based Identity](https://technet.microsoft.com/en-us/library/ee535242.aspx)and  [A Guide to Claims-based Identity and Access Control](https://technet.microsoft.com/en-us/library/ff423674.aspx).In this article:
-  [Architecture](#architecture)
    
  
-  [Example custom claims provider configuration](#deploying)
    
  
-  [Using custom claims on more than one farm](#multifarm)
    
  
-  [Considerations for custom claims providers](#planning)
    
  

## Architecture
<a name="architecture"> </a>

When a web application is configured to use claims-based authentication, SharePoint Server 2013 automatically uses two default claims providers:
- The **SPSystemClaimProvider** class provides claims information related to the server farm where SharePoint Server 2013 is installed.
    
  
- The **SPAllUserClaimProvider** class provides an All Users claim.
    
  
Depending on the authentication method selected for a zone of a web application, SharePoint Server 2013 also uses one or more of the default claims providers that are listed in Table 1.
### Table 1. Authentication methods and default claims providers

Authentication methodClaims providerWindows authentication  <br/> **SPActiveDirectoryClaimProvider** <br/> Forms-based authentication  <br/> **SPFormsClaimProvider** <br/> Security Assertion Markup Language (SAML) token-based authentication  <br/> **SPTrustedClaimProvider** <br/> You can see a list of claims providers for a farm by using the **Get-SPClaimProvider** Microsoft PowerShell cmdlet.
> [!NOTE:]

  
    
    

Claims providers are registered on a server farm as features that are deployed to the farm. They are scoped at the farm level. Each claims provider object uses the SPClaimProviderDefinition class to include information about the claims provider, such as display name, description, assembly, and type. Two important properties of the SPClaimProviderDefinition class are IsEnabled and IsUsedByDefault. These properties determine whether a registered claims provider is enabled for use in the farm, and whether the claims provider is used by default in a particular zone. By default, all claims providers are enabled when they are deployed to a server farm. For information about the SPClaimProviderDefinition class, see **SPClaimProviderDefinition**.For more information about zones and authentication, see  [Plan for user authentication methods in SharePoint Server](html/plan-for-user-authentication-methods-in-sharepoint-server.md).
## Example custom claims provider configuration
<a name="deploying"> </a>

By default, when you register a custom claims provider on the farm, the IsEnabled and IsUsedByDefault properties are both set to True. Depending on the number of zones needed for your SharePoint Server 2013 solution, the authentication methods that are used by each zone, and the users for each zone, you may want to limit the zones in which your custom claims provider is displayed in People Picker.Because claims providers are scoped at the farm level and enabled at the zone level, you must carefully plan the zones in which you want the custom claims provider to be displayed. In general, you should ensure that the IsUsedByDefault property is set to False, and then configure the **SPIisSettings** class for each zone in which you want to use the custom claims provider. To configure a custom claims provider for select zones, you can create a PowerShell script that sets the claims provider for a zone by using the **ClaimsProviders** property, or you can create a custom application to allow you to enable a custom claims provider for select zones.For example, consider a scenario in which there are two web applications: 
- The first web application, PartnerWeb, has two zones — one intranet that uses Windows claims-based authentication and one extranet that uses forms-based authentication — and is used for collaboration among employees and partners.
    
  
- The second web application, PublishingWeb, has only one zone that uses forms-based authentication and is an Internet publishing site for employees, business partners, and customer partners.
    
  
 Now, suppose that for the extranet zone on PartnerWeb, you want employees to be able to collaborate with business partners but not customer partners. To do this, you write a custom claims provider that determines whether the current user is a business partner or customer partner, based on the user's identity. In this example, users from fabrikam.com are business partners, but users from contoso.com are customer partners. When a user who is a business partner is authenticated in the PartnerWeb web application, a claim for a role called BusinessPartner is added to the claim token. When a customer partner is authenticated, a claim for a role called CustomerPartner is added to the claim token.To make sure that customer partners are never added to the extranet collaboration site, you add a web application policy on the PartnerWeb web application for the extranet zone that explicitly denies access to any user who has a claim for a role called CustomerPartner. The custom claims provider would also have to implement search and type-in support for the web application policy to resolve the CustomerPartner role claim so that it can be added to the web application policy. Finally, to enable this functionality on the extranet zone, you configure the **SPIisSettings** class for that zone to use the custom claims provider. The following diagram shows the authentication methods and claims provider settings for each web application and zone. **Figure 1. Example of the authentication methods and claims provider settings for Web applications and zones**
  
    
    
![SPIisSettings diagram](images/)
  
    
    
You can set the IsUsedByDefault property by configuring it in a feature receiver that you create for your custom claims provider. You can also override the settings of the IsEnabled and IsUsedByDefault properties by using the **Set-SPClaimProvider** PowerShell cmdlet.
    
> [!IMPORTANT:]

  
    
    


## Using custom claims on more than one farm
<a name="multifarm"> </a>

Claim values are a combination of the claim itself, the claims provider name, and the order in which the claims provider was installed on the server. Therefore, if you want to use a claim across multiple farms or environments, you must install the claims providers in the same order on each farm in which you want to use the claim. Use the following steps when you have installed a custom claims provider on a farm and you want to use the same claim on additional farms:
1. Register the claims providers on the additional farms in the same order that they were registered on the first farm.
    
  
2. Perform a backup of the first farm. For information about how to back up a farm, see  [Back up farms in SharePoint Server](html/back-up-farms-in-sharepoint-server.md).
    
  
3. Use the back up from the first farm to restore the other farms. For information about how to restore a farm, see  [Restore farms in SharePoint Server](html/restore-farms-in-sharepoint-server.md).
    
  

## Planning considerations for custom claims providers
<a name="planning"> </a>

As you plan custom claims providers for use with People Picker in your SharePoint solution, consider the following questions:
- What zones does your web application have, and what authentication methods are used in each zone?
    
  
- Are there any custom claims that should be added to users to enable more advanced permissions or security scenarios?
    
  
- Will you be using SAML authentication with a trusted identity provider?
    
  
- What will be the source of the values for the users and roles that will be displayed in People Picker query results?
    
  
The SharePoint Server 2013 Content Publishing team wants to thank Steve Peschka for contributing to this article. Take a look at Steve Peschka’s  [Share-n-dipity TechNet blog](https://go.microsoft.com/fwlink/p/?LinkId=210274).
# See also

#### 

 [People Picker and claims providers overview (SharePoint 2013)](html/people-picker-and-claims-providers-overview-sharepoint-2013.md)
  
    
    
 [Plan for user authentication methods in SharePoint Server](html/plan-for-user-authentication-methods-in-sharepoint-server.md)
  
    
    

  
    
    

