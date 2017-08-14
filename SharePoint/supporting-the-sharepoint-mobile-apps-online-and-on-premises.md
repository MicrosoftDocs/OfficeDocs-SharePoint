---
title: Supporting the SharePoint mobile apps online and on-premises
ms.prod: SHAREPOINT
ms.assetid: 7b24439f-640a-412d-a35b-33007966bb58
---


# Supporting the SharePoint mobile apps online and on-premises
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Topic Last Modified:** 2017-05-05* The SharePoint mobile app makes using your SharePoint sites from a phone and tablet easier than ever. Learn how to troubleshoot common issues when working with the SharePoint mobile app. 
## Overview

If your SharePoint Online users are working on their files and data using mobile devices, they can leverage the new  [SharePoint mobile app for iOS](https://go.microsoft.com/fwlink/?LinkID=808032),  [Android](https://go.microsoft.com/fwlink/p/?linkid=828159 ) and [Windows 10 Mobile](https://go.microsoft.com/fwlink/p/?linkid=828162 ).As an administrator of an on-premises SharePoint Server 2016 farm, there are some guidelines of which you should be aware. In general, the SharePoint mobile app:
- Works best for accessing and working on your sites in SharePoint Online.
    
  
- If your SharePoint environment is on-premises and you use an iOS device, the SharePoint mobile app works best for users working on intranet sites while joined to a corporate network. 
    
  

> [!IMPORTANT:]

  
    
    


## Common messages received by users

While logging in with the SharePoint mobile app, you, or your users, may see messages about the type of SSL or TLS certificate, or authentication methods used. These messages are meant to let users and administrators know about supported methods of SharePoint Online (or on-premises) access. These are some of the most common messages and what they're trying to tell you:
- **The SharePoint Server is using an untrusted SSL certificate which isn’t supported by this app** - The SharePoint mobile app can’t use self-signed certificates, or those issued by an in-house Certificate Authority (CA). If you plan to encrypt your SharePoint web applications, you'll need to do so with SSL or TLS certificates from a public Certificate Authority.
    
  
- **SharePoint Server is using basic authentication which isn’t currently supported by this app** - The SharePoint mobile app can use NTLM authentication, and Forms-based authentication.
    
  

## Is this network traffic from the SharePoint mobile app?

When using your iOS devices against SharePoint Server 2016 (on-premises), administrators may see some unexpected traffic on their network monitors. For example, users may see some query, and query-response traffic to (and from) addresses online, such as  *bl3301-g.1drv.com, bn2.vortex.data.microsoft.com.akadns.net*  , or even *weu-breeziest-in.cloudapp.net*  . This can be confusing for network administrators.These calls are related to data-collection and telemetry services. Telemetry data is used to monitor customer experiences with the Microsoft Office 365 or SharePoint Online services and general information about service reliability, for the purposes of analytics. For example, the first URL mentioned ( *bl3301-g.1drv.com*  ) is related to OneDrive and many of the other URLs will have Microsoft in the domain name.Any suspicious network traffic should be flagged and investigated by administrators. While doing so, please be aware that the data-collection and telemetry services for the SharePoint mobile app cannot be turned off. It helps to have access to the Privacy Statements while making judgements about whether the SharePoint mobile app is right for your organization.
-  [Microsoft Privacy Statment](https://www.microsoft.com/EN-US/privacystatement/OnlineServices/Default.aspx)
    
  
-  [Microsoft Online Services Privacy Statement](https://privacy.microsoft.com/en-us/privacystatement)
    
  
-  [Microsoft Trust Center](https://www.microsoft.com/en-us/trustcenter)
    
  
-  [Microsoft Intune (on the Microsoft Trust Center site)](https://www.microsoft.com/en-us/trustcenter/CloudServices/Intune)
    
  
-  [Office 365 (on the Microsoft Trust Center site)](https://www.microsoft.com/en-us/TrustCenter/CloudServices/Office-365)
    
  

