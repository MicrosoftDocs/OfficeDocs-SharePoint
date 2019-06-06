---
title: "Mobile security and authentication in SharePoint 2013"
ms.reviewer: 
ms.author: toresing
author: tomresing
manager: pamgreen
ms.date: 7/20/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 0fe9d4a1-faf9-4941-a45a-b54f47a5dea5

description: "Learn how to help secure a SharePoint mobile infrastructure, and learn about the different authentication types supported in SharePoint Server 2013."
---

# Mobile security and authentication in SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
This article provides security guidance and recommendations to help ensure that access to SharePoint Server 2013 and specific data in SharePoint is not compromised on a mobile device. This article also details the supported authentication types for select devices, and authentication specifics for the SharePoint Newsfeed App. 
  
    
## Security for mobile devices
<a name="section1"> </a>

This section provides security recommendations for using devices that are external to your corporate network. A lost or stolen device could be devastating to an organization on many levels. Therefore, necessary measures must be put in place if one were to be compromised.
  
General security considerations include the following:
  
- Mobile devices can contain sensitive data or documents. Because mobile devices can be lost or stolen, we recommend that you set policies around mobile devices to help protect sensitive data and documents. This can include securing the mobile device by using a PIN or lock, and ensuring that you can remotely wipe the data on the mobile device. Available programs and features vary by mobile device. For more information about a possible method to implement these policies in your organization, see [Exchange ActiveSync](mobile-security-and-authentication.md#activesync) later in this article. 
    
- You can educate users about how they can help protect their user credentials. This can include signing out of sites when they have finished, not enabling any option that keeps them signed in or remembers their password, and frequently deleting cookies in the mobile browser. This can help prevent others from using their user credentials to log on to a SharePoint site if their mobile device is lost or stolen.
    
- We recommend that you enable SSL to help secure communication between mobile browsers and the computer that is running SharePoint Server 2013. For more information about how to use a reverse proxy server, such as Forefront Unified Access Gateway (UAG), to help secure communication, see [Forefront Unified Access Gateway (UAG)](https://go.microsoft.com/fwlink/p/?LinkID=196384) in the Forefront Technical Library. 
    
### Exchange ActiveSync
<a name="activesync"> </a>

Microsoft Exchange ActiveSync is a communications protocol that enables mobile access, over the air, to e-mail messages, scheduling data, contacts, and tasks. Exchange ActiveSync is available on Windows Phone and third-party phones and slates that are enabled for Exchange ActiveSync such as the Apple iPhone. One of the benefits of implementing Exchange ActiveSync in your organization is device-side security, and administration through policy enforcement. If SharePoint Server 2013 is deployed in an extranet topology, mobile devices access the computer that is running SharePoint Server 2013 via a public-facing URL. If the mobile device were to become lost or stolen, it is necessary to ensure that SharePoint data is not compromised. For example, by using Exchange ActiveSync you can wipe data contents from the device remotely, such as SharePoint configurations, or enforce a complex password at the lock screen to help prevent unauthorized access.
  
The following table lists a selection of Exchange ActiveSync features and policies that you can apply to some devices.
  
**Table: Exchange ActiveSync policies for mobile devices**

|**Exchange ActiveSync policy**|**Description**|
|:-----|:-----|
|Remote wipe (this is a feature and not an Exchange ActiveSync policy)  <br/> |If a mobile phone is lost, stolen, or otherwise compromised, you can issue a remote wipe command from the Exchange computer or from any web browser by using Outlook Web App. This command restores the device to factory defaults.  <br/> > [!IMPORTANT]> After a remote device wipe has occurred, data recovery is very difficult. However, no data removal process leaves a device as free from residual data as when it is new. Recovery of data from a device may still be possible using sophisticated tools.           |
|Enforce password on device (DevicePasswordEnabled)  <br/> |This setting enables the mobile phone password.  <br/> |
|Minimum password length (MinDevicePasswordLength)  <br/> |This option specifies the length of the password for the mobile phone. The default length is 4 characters, but as many as 18 can be included.  <br/> |
|Require alphanumeric password (AlphanumericDevicePasswordRequired)  <br/> |This setting requires that a password contains numeric and non-numeric characters.  <br/> |
|Allow simple password (AllowSimpleDevicePassword)  <br/> |This setting enables or disables the ability to use a simple password such as 1234.  <br/> |
|Maximum inactivity time lock (MaxInactivityTimeDeviceLock)  <br/> |This option determines how long the mobile phone must be inactive before the user is prompted for a password to unlock the mobile phone.  <br/> |
   
> [!IMPORTANT]
> The selection of Exchange ActiveSync policies that can be used might differ on a device-by-device basis. For more information about which policies are supported on a specific device platform, such as Windows Phone and Apple iPhone, see [Understanding Exchange ActiveSync Mailbox Policies](http://go.microsoft.com/fwlink/?LinkId=253672). 
  
### Finding a lost device
<a name="lostdevice"> </a>

When a device is lost or stolen it may be useful to find the location of that device, and be able to wipe all data contents if it is necessary. There are various third-party services and solutions that can provide this functionality. An example is the Windows Phone Find My Phone service that can make it easier to recover your mobile device by locating it, or prevent someone from using it without your consent.
  
The functionality this service can provide includes the following:
  
- Map your mobile device location.
    
- Make your mobile device ring.
    
- Lock your mobile device and show a message.
    
- Wipe your mobile device data.
    
> [!NOTE]
> To learn more about the Find My Phone service for Windows Phone, see [Find a lost phone](https://go.microsoft.com/fwlink/?LinkId=253669). 
  
## Authentication for mobile devices
<a name="section2"> </a>

SharePoint Server 2013 supports multiple authentication methods and authentication modes. Not all mobile browsers and devices work with all the available authentication methods. When you plan for mobile device access, you must do the following:
  
- Determine the mobile devices that you must support. Then, learn the authentication methods that are supported by the mobile devices. This information varies by manufacturer.
    
- Determine the sites that you want to make available to your mobile device users.
    
- Determine whether you want to make SharePoint sites available for mobile devices when the devices are used outside the corporate firewall. If you do, the method that you use to enable external access can also affect mobile device authentication.
    
The following tables detail the authentication types supported for browsers, OneDrive for Business, and the Office Hub Windows Phone experience in SharePoint Server 2013. For the below, OrgID refers to Microsoft Online Services ID, the identity provider for Office 365. Also, MSOFBA refers to Microsoft Office Forms Based Authentication. 
  
**Table: Mobile authentication support for SharePoint browsers**

|**SharePoint Infrastructure**|**Mobile Devices**|
|:-----|:-----|
|**Authentication Type** <br/> |**Authentication Protocol** <br/> |**ID Provider** <br/> |**SharePoint deployment** <br/> |**Windows Phone 7.5 (Internet Explorer Mobile)** <br/> |**Windows Phone 8 (Internet Explorer Mobile)** <br/> |**Windows 8 (Internet Explorer)** <br/> |**iOS 5.x or later versions (Safari Browser)** <br/> |**Android 4.x or later versions (Android Browser** )  <br/> |
|**Windows Authentication** <br/> |NTLM  <br/> |Active Directory  <br/> |On-premises  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |
|Basic Authentication  <br/> |Active Directory  <br/> |On-premises, extranet  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |
|**Forms-Based Authentication (FBA)** <br/> |FBA  <br/> |Active Directory, LDAP, SQL  <br/> |On-premises, extranet  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |
|FBA  <br/> |OrgID  <br/> |SharePoint Online, hybrid -based scenarios  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |
|**SAML (Token-based)** <br/> |SAML  <br/> |WS-Federation 1.1 compatible Identity Provider  <br/> |On-Premises, SharePoint Online, hybrid-based scenarios  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |
   
**Table: Supported authentication types for the OneDrive for Business app**

|**Authentication type**|**Description**|**Supported**|**Administrator type required for configuration**|
|:-----|:-----|:-----|:-----|
|**Org-ID** <br/> |Organizations with an Office 365 or SharePoint Online tenant without any federation.  <br/> |Yes  <br/> |Global admin  <br/> |
|**ADFS and Org-ID federation** <br/> |Organizations with a hybrid Office 365 or SharePoint Online tenant with users federated from an on-premises directory.  <br/> |Yes  <br/> |Global admin plus the on-premises network administrator plus the SharePoint administrator  <br/> |
|**Windows authentication (NTLM)** <br/> |Organizations with a SharePoint environment configured to allow NTLM claims-based Windows authentication.  <br/> |Yes  <br/> |SharePoint administrator  <br/> |
|**Forms-based authentication (FBA)** <br/> |Organizations with a SharePoint environment configured to allow Forms-based authentication or other compatible claims-based authentication via a standard web control.  <br/> |Yes  <br/> |SharePoint administrator  <br/> |
|**Qualified non-ADFS identity providers** <br/> |Organizations with an Office 365 or SharePoint Online environment configured to allow user sign-in that is federated with an identity provider qualified for rich clients in the [Works with Office 365 - Identity program](https://go.microsoft.com/fwlink/p/?LinkId=511982).  <br/> |Yes  <br/> |SharePoint administrator plus the on-premises Network administrator or Global admin (in some organizations the Global admin is a requirement, not an option.)  <br/> |
|**All other non-ADFS identity providers** <br/> |Organizations with a SharePoint environment configured to allow a non-ADFS identity provider.  <br/> |No  <br/> |SharePoint administrator plus the on-premises network administrator  <br/> |
|**Kerberos authentication** <br/> |Organizations with a SharePoint environment configured to support Kerberos authentication.  <br/> |No  <br/> |SharePoint administrator plus the on-premises network administrator  <br/> |
|**Basic authentication** <br/> |Organizations with a SharePoint environment configured to support Basic authentication.  <br/> |No  <br/> |SharePoint administrator plus the on-premises network administrator  <br/> |
   
> [!NOTE]
> If you're an Office 365 multi-tenant user you can connect from the OneDrive for Business app in any network environment including Wi-Fi and cellular data. If you're not using multi-tenant Office 365, you can connect only when using your organization's on-site Wi-Fi network. Contact your SharePoint administrator if you're unsure which user you are. 
  
**Table: Mobile authentication support matrix for Office Hub**

|**SharePoint Infrastructure**|**Client side**|**Mobile devices**|
|:-----|:-----|:-----|
|**Authentication Type** <br/> |**Authentication Protocol** <br/> |**ID Provider** <br/> |**SharePoint deployment** <br/> |**Handled through:** <br/> |**Windows Phone 7.5 (Internet Explorer Mobile)** <br/> |**Windows Phone 8 (Internet Explorer Mobile)** <br/> |
|**Windows Authentication** <br/> |NTLM  <br/> |Active Directory  <br/> |On-premises  <br/> |NTLM  <br/> |Yes  <br/> |Yes  <br/> |
|Basic Authentication  <br/> |Active Directory  <br/> |On-premises, extranet  <br/> |Basic Authentication  <br/> |No  <br/> |Yes (https)  <br/> |
|**Forms-Based Authentication (FBA)** <br/> |FBA  <br/> |Active Directory, LDAP, SQL  <br/> |On-premises, extranet  <br/> |MSOFBA  <br/> |Yes  <br/> |Yes  <br/> |
|FBA  <br/> |OrgID  <br/> |SharePoint Online, hybrid -based scenarios  <br/> |MSOFBA  <br/> |Yes  <br/> |Yes  <br/> |
|FBA  <br/> |OrgID  <br/> |SharePoint Online, hybrid -based scenarios  <br/> |Active Authentication(IDCRL)  <br/> |No  <br/> |Yes  <br/> |
|**SAML (token-based)** <br/> |SAML  <br/> |WS-Federation 1.1 compatible Identity Provider  <br/> |On-premises, SharePoint Online, hybrid -based scenarios  <br/> |MSOFBA  <br/> |Yes  <br/> |Yes  <br/> |
|SAML  <br/> |WS-Federation 1.1 compatible Identity Provider  <br/> |On-premises, SharePoint Online, hybrid -based scenarios  <br/> |Active Authentication(IDCRL)  <br/> |No  <br/> |Yes  <br/> |
   
> [!NOTE]
> In order for mobile devices to communicate with SharePoint servers, Internet Protocol Security (IPSec) must be disabled on the servers. The reason this must be done is that mobile devices are not domain-joined. 
  
### Authentication for the SharePoint Newsfeed App
<a name="News"> </a>

This section provides authentication guidance and considerations for the SharePoint Newsfeed app. This includes information for on-premises based deployments, and using SharePoint Online. 
  
 **Authentication support for the SharePoint Newsfeed App**
  
The following table details the authentication types supported for the SharePoint Newsfeed App in SharePoint Server 2013. For the below, OrgID refers to Microsoft Online Services ID, the identity provider for Office 365. Also, MSOFBA refers to Microsoft Office Forms Based Authentication.
  
**Table: Mobile authentication support matrix for the SharePoint Newsfeed App**

|**SharePoint Infrastructure**|**Client side**|**Mobile devices**|
|:-----|:-----|:-----|
|**Authentication Type** <br/> |**Authentication Protocol** <br/> |**ID Provider** <br/> |**SharePoint deployment** <br/> |**Handled through:** <br/> |**Windows Phone 7.5 Apps** <br/> |**Windows Phone 8 Apps** <br/> |**Windows 8 Apps** <br/> |**iOS 6.x or later versions Apps** <br/> |
|**Windows Authentication** <br/> |NTLM  <br/> |Active Directory  <br/> |On-premises  <br/> |NTLM  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |
|Basic Authentication  <br/> |Active Directory  <br/> |On-premises, extranet  <br/> |Basic Authentication  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes (https)  <br/> |
|**Forms-Based Authentication (FBA)** <br/> |FBA  <br/> |Active Directory, LDAP, SQL  <br/> |On-premises, extranet  <br/> |MSOFBA  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |
|FBA  <br/> |OrgID  <br/> |SharePoint Online, hybrid -based scenarios  <br/> |MSOFBA  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |
|FBA  <br/> |OrgID  <br/> |SharePoint Online, hybrid -based scenarios  <br/> |Active Authentication(IDCRL)  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |
|**SAML (token-based)** <br/> |SAML  <br/> |WS-Federation 1.1 compatible Identity Provider  <br/> |On-premises, SharePoint Online, hybrid -based scenarios  <br/> |MSOFBA  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |
|SAML  <br/> |WS-Federation 1.1 compatible Identity Provider  <br/> |On-premises, SharePoint Online, hybrid -based scenarios  <br/> |Active Authentication(IDCRL)  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |
   
> [!IMPORTANT]
> For federated scenarios in SharePoint Online, only Active Directory Federation Services (ADFS) 2.0 is supported. During the setup process it is necessary to support a passive federation authentication URI of:  *"urn:oasis:names:tc:SAML:2.0:ac:classes:Password"*  . 
  
 **Authentication Workflows**
  
The SharePoint Newsfeed App is supported for both on-premises and SharePoint Online use. Each option can present differences with end user authentication workflow. For example, this table provides sample authentication experiences for each type of implementation. 
  
|**Deployment**|**Workflow**|**Details**|
|:-----|:-----|:-----|
|**On-premises** <br/> |![SPNewsfeed On-premises](../media/SP15Mobile_SPNewsOnPrem.jpg)| Supported Authentication Types  <br/>  Windows Authentication  <br/>  Forms Based Authentication  <br/>  SAML  <br/> |
|**SharePoint Online** <br/> |![SPNewsfeed SPO](../media/SP15Mobile_SPNewsSPO.jpg)| Supported Authentication Types  <br/>  Forms Based Authentication  <br/>  SAML  <br/> |
   
For more information on how to deploy the SharePoint Newsfeed App in your network, including configuring cross-firewall access, see [Configure external access for mobile devices in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ff393835(v=office.14)).
  
## See also
<a name="section2"> </a>

#### Concepts

[Overview of mobile devices and SharePoint Server 2013](mobile-devices-overview.md)

