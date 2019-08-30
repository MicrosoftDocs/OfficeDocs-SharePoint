---
title: "Plan incoming email for a SharePoint Server farm"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: ca092ed2-4aa2-4c2e-b273-661ca6a76e01
description: "Learn how to configure incoming email for SharePoint Server."
---

# Plan incoming email for a SharePoint Server farm

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
The incoming email feature of SharePoint Server enables SharePoint sites to receive and store email messages and attachments in lists and libraries. This article helps administrators understand the choices they need to make before deploying the incoming email feature.
  
    
## About incoming email
<a name="section1"> </a>

The incoming email feature enables teams to store the email that they send to other team members without opening the SharePoint site and uploading the content that was sent in email. This is possible because most types of lists and libraries can be assigned a unique email address.
  
 **Important:**
  
MinRole now manages the incoming email feature in SharePoint Server 2016. The incoming email feature can only be used on the following MinRole roles:
  
- Application
    
- Application with Search
        
- Single Server Farm

- Custom
    
MinRole doesn't manage the incoming email service on the Custom server role. However, SharePoint farm administrators can turn this service on and off on each server that is assigned the Custom server role. For more information see [Planning for a MinRole server deployment in SharePoint Server 2016](../install/planning-for-a-minrole-server-deployment-in-sharepoint-server.md).
  
Before configuring incoming email, you must perform the following tasks:
  
- The basic scenario simply applies to a single server farm. If you're using the basic scenario, each SharePoint Application or Front-end server must be running the Simple Mail Transfer Protocol (SMTP) service and the SharePoint Foundation web application service.
    
- The advanced scenario mainly applies to a multiple server farm. If you're using the advanced scenario, you can use one or more servers in the server farm to run the SMTP service and to have a valid SMTP server address. Alternatively, you must know the name of a server outside the farm that is running the SMTP service and the location of the email drop folder.
    
For more information about installing the SMTP service, see [Configure incoming email for a SharePoint Server farm](incoming-email-configuration.md).
  
## Key decisions for planning incoming email
<a name="section2"> </a>

When planning incoming email, you must decide whether to use a basic or an advanced scenario, as described in the following sections.
  
### Using a basic scenario

You can enable a basic incoming email scenario by installing the SMTP service on the server running SharePoint Server and enabling incoming email by using the automatic settings mode with all default settings. In this scenario, email is delivered directly to your SMTP server and SharePoint Server periodically checks for email in the default email drop folder that is automatically configured by the SMTP service.
  
Selecting the automatic settings mode and accepting all the default settings is the easiest way to enable incoming email because all configuration settings are made for you and, therefore, little expertise is required. For most organizations, this configuration is all that is needed.
  
You enable a basic incoming email scenario in the following steps:
  
1. The server administrator uses the Add Roles and Features Wizard to install the SMTP Server feature on the server you want to receive incoming email. This installs and starts the SMTP service on that server.
    
2. The farm administrator enables incoming email by using the automatic settings mode and accepting all the default values.
    
3. The site collection administrator enables the incoming email feature on the libraries and lists in which they want to store incoming email and assigns each library and list a unique email address in the form  _address_@ _SMTPserveraddress_, for example, sharedfiles@SMTPserver.contoso.com.
    
When users send email to the address of a list or library, SharePoint Server detects that new email has been delivered and sends it to the appropriate list or library based on the email address.
  
> [!NOTE]
> You can also use the automatic settings option in an advanced scenario and select whether to use the Microsoft SharePoint Directory Management service, a safe email server, and an incoming email server display address. These options are all discussed in the [Using an advanced scenario](incoming-email-planning.md#usingadvanced) later in this article. 
  
If using the basic scenario you can skip the rest of this article. If using the advanced scenario, you'll need to perform additional procedures. For more information, see [Configure incoming email for a SharePoint Server farm](incoming-email-configuration.md).
  
### Using an advanced scenario
<a name="usingadvanced"> </a>

For more advanced administrators, additional choices are available, some of which require more expertise to deploy than choosing the basic scenario with all default options. This section describes the following configuration options:
  
- SharePoint Directory Management service
    
- Incoming email server display address
    
- Safe email server
    
- E-mail drop folder
    
If you use the advanced scenario to configure incoming email, you will need to perform additional procedures. For more information, see [Configure incoming email for a SharePoint Server farm](incoming-email-configuration.md).
  
#### SharePoint Directory Management service

The SharePoint Directory Management service connects SharePoint sites to your organization's user directory to provide enhanced email features. The benefit of using this service is that it enables users to create and manage email distribution groups from SharePoint sites. This service also creates contacts in your organization's user directory so people can find email-enabled SharePoint lists in their address books. However, using SharePoint Directory Management service requires more management because it communicates with Active Directory Domain Services (AD DS).
  
> [!NOTE]
> It is recommended that you use Exchange Server together with SharePoint Directory Management service. If you do not, you must customize your own directory management service. 
  
You can configure the SharePoint Directory Management service by using either the automatic or the advanced settings mode. You can choose to enable the SharePoint Directory Management service in your SharePoint server farm, or you can use the SharePoint Directory Management service of another farm. One advantage of using the service running on another farm is that Active Directory permissions are managed in a centralized place (that is, on the other farm).
  
To enable this service on a server or farm, the Central Administration application pool account used by SharePoint Server must have write access to the container that you specify in Active Directory. This requires an Active Directory administrator to set up the organizational unit (OU) and the permissions on the OU. The advantage of using the SharePoint Directory Management service on a remote farm is that you do not need the help of an Active Directory administrator to create and configure the OU if the OU already exists.
  
> [!NOTE]
> For details about using SharePoint Directory Management service, see [Configure incoming email for a SharePoint Server farm](incoming-email-configuration.md). 
  
A typical directory management scenario proceeds in the following steps:
  
1. A site collection administrator creates a new SharePoint group.
    
2. The administrator chooses to create a distribution list to associate with that SharePoint group and assigns an email address to that distribution list.
    
3. Over time, the administrator adds users to and removes users from this SharePoint group. As users are added to and removed from the group, the SharePoint Directory Management service automatically adds and removes them from the distribution list, which is stored in the Active Directory directory service. Because distribution lists are associated with a particular SharePoint group, this distribution list is available to all members of that SharePoint group.
    
4. By default, email addresses are automatically generated for discussion boards and calendars on team sites and then added to the team distribution list. The email addresses for these two lists will be in the following form, by default:  _GroupAddress_.discussions and  _GroupAddress_.calendar.
    
5. By including email addresses for discussion boards and calendars in the distribution list, all email and meeting invitations sent to this distribution list will be archived in the team site.
    
#### SharePoint Directory Management service configuration options

When you configure the SharePoint Directory Management service to create distribution groups and contacts in Active Directory, you must provide the following information:
  
- Name of the Active Directory container in which new distribution groups and contacts will be created. This must be provided in the following format:
    
    OU= _ContainerName_, DC= _DomainName_, DC= _TopLevelDomainName_
    
    **Example**
    
    OU=SharePointContacts,DC=Contoso,DC=com
    
- Name of the SMTP server to use for incoming email (or accept the default SMTP server if one exists). This must be provided in the following format:
    
     _Server.subdomain.domain.top-level_domain_
    
    For example, SharePointServer.support.contoso.com
    
- Whether to accept messages from only authenticated users.
    
- Whether to allow users to create distribution groups from SharePoint sites. If you choose yes for this option, you can also choose whether users can do any combination of the following actions:
    
  - Create a new distribution group.
    
  - Change a distribution group's email address.
    
  - Change a distribution group's title and description.
    
  - Delete a distribution group.
    
When configuring the SharePoint Directory Management service to create distribution groups and contacts using a remote SharePoint Directory Management service, you must provide the following information:
  
- The URL of the remote directory management service, for example, http://server:adminport/_vti_bin/SharePointE-mailWS.asmx.
    
- The name of the SMTP server to use for incoming email.
    
- Whether to accept messages from only authenticated users.
    
- Whether to allow users to create distribution groups from SharePoint sites.
    
#### Incoming email server display address

Administrators can specify the email server address that will be displayed in web pages when users create an incoming email address for a site, list, or group. This setting is often used with the SharePoint Directory Management service to provide a friendlier email server address for users to type, for example, mylist@example.com.
  
#### Safe email server

You can configure SharePoint Server to accept email from any email server or only email that has been routed through a safe-email server application.
  
You can get the following benefits by routing email through a safe email server:
  
- **User authentication** The SMTP service cannot authenticate users who send email to your site, but Exchange Server can. The server administrator can use the SharePoint Central Administration website to specify that the system accept email from authenticated users only if the email is sent through Exchange Server. 
    
- **Spam filtering** Exchange Server provides spam filtering to eliminate unsolicited commercial email before it is forwarded to its destination — in this case, the server running SharePoint Server. Another technique that can reduce spam is to allow members of the team site to archive email only in lists on which you have granted write permissions to members. 
    
- **Virus protection** Exchange Server provides virus protection for email routed through it. 
    
> [!NOTE]
> Because this option is only available in automatic mode, you cannot specify one or more safe email servers and also specify an email drop folder. 
  
#### E-mail drop folder

If the SMTP service is running on another server than on the SharePoint server, you must specify the location from which SharePoint Server retrieves incoming email. You specify the email drop folder so that SharePoint Server knows from where to retrieve incoming email. However, if you specify a specific email drop folder, SharePoint Server cannot detect configuration changes on the remote email server that is delivering the email to your drop folder. This means that if an administrator configures the email server to no longer deliver email to this folder, SharePoint Server cannot detect that the configuration has changed, and therefore will not be able to retrieve the files from the new location.
  
> [!NOTE]
> When incoming email is set to advanced mode, you must ensure that you have the proper permissions on the email drop folder. For more information, see [Configure incoming email for a SharePoint Server farm](incoming-email-configuration.md). 
  
> [!NOTE]
> Because this option is only available in advanced mode, you cannot specify an email drop folder and also specify one or more safe email servers. 
  
## Configuration options and settings modes
<a name="section3"> </a>

As a farm administrator, you have two settings modes from which to choose when enabling incoming email: automatic and advanced. As described in the "Using a basic scenario" section, you can choose the automatic settings mode with default settings. However, the automatic settings mode has additional options that you can choose.
  
  
> [!NOTE]
> Automatic mode is not available in SharePoint Server 2019.

The following table describes the configuration options and whether they are configured on the **Configure Incoming E-Mail Settings** page in Central Administration by using the automatic settings mode or the advanced settings mode. 
  
|**Configuration option**|**Automatic settings mode**|**Advanced settings mode**|
|:-----|:-----|:-----|
|**Enable Incoming E-mail** <br/> |Yes  <br/> |Yes  <br/> |
|**SharePoint Directory management service** <br/> |Yes  <br/> |Yes  <br/> |
|**Incoming e-mail server display address** <br/> |Yes  <br/> |Yes  <br/> |
|**E-mail drop folder** <br/> |No  <br/> |Yes  <br/> |
   
The advanced and automatic settings modes are similar in that they both enable farm administrators to configure the SharePoint Directory Management service and the email server address to display in web pages. These settings modes differ in that the automatic settings mode replaces the ability to choose what email servers to accept email from with the ability to specify the folder to which email is dropped. SharePoint Server uses this email drop folder to detect new email messages.
  
> [!NOTE]
> The email drop folder setting is not available in automatic mode, because that mode automatically sets the email drop folder to the folder that is specified by the SMTP service. 
  
## See also
<a name="section3"> </a>

#### Concepts

[Configure incoming email for a SharePoint Server farm](incoming-email-configuration.md)
  
[Plan outgoing email for a SharePoint Server farm](outgoing-email-planning.md)
  
[Configure outgoing email for a SharePoint Server farm](outgoing-email-configuration.md)

