---
title: "Plan outgoing email for a SharePoint Server farm"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 9/7/2017
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 75401651-ef01-4348-878e-8a636f0b072d
description: "Summary: Learn how to configure outgoing email to relay email alerts and notifications in your SharePoint Server 2016 and SharePoint 2013 farm or web application."
---

# Plan outgoing email for a SharePoint Server farm

 **Summary:** Learn how to configure outgoing email to relay email alerts and notifications in your SharePoint Server 2016 and SharePoint 2013 farm or web application. 
  
Outgoing email is the foundation on which site administrators can implement several email notification features. These features help end users track changes and updates to individual site collections and allow site administrators to deliver status messages.
  
    
## About outgoing email
<a name="section1"> </a>

Properly configuring outgoing email is a requirement for implementing email alerts and notifications. The outgoing email feature uses an outbound Simple Mail Transfer Protocol (SMTP) service to relay email alerts and notifications. These email features include the following:
  
- **Alerts**
    
    In a large and growing site collection, users need a way to keep up with updates to lists, libraries, and discussions. Alerts help to keep users aware of changes. For example, if many users work on the same document, the owner of the document can set up alerts to be notified whenever there are changes to this document. Users can specify which areas of the site collection or which documents they want to track and decide how often they want to receive alerts.
    
    > [!NOTE]
    > Users must have at least View permissions to set up alerts. 
  
- **Administrative messages**
    
    Site administrators might want to receive notices when users request access to a site or when site owners have exceeded their specified storage space. Setting up outgoing email enables site administrators to receive automatic notifications for site administration issues.
    
Outgoing email support can be enabled at both the server farm level (available in the **System Settings** section of the SharePoint Central Administration website and at the web application level (available in the **Application Management** section of Central Administration). Outgoing email settings at the web application level override those set up at the server farm level. You can also specify different settings for a specific web application. 
  
## Key planning phases of outgoing email
<a name="section2"> </a>

You must consider the following components when planning your outgoing email settings:
  
- An SMTP service to relay email alerts and notifications. You will need the DNS name or IP address of the SMTP mail server to use.
    
- An address to use in the header of an alert message that identifies the sender of the message.
    
- A Reply-to address that is displayed in the To field of a message when a user replies to an alert or notification.
    
- A character set to use in the body of alert messages.
    
### Outbound SMTP server

The SMTP service is a component of Internet Information Services (IIS); however, it is not enabled by default with IIS. It can be enabled by using **Add Roles and Features Wizard** in Server Manager. 
  
After determining which SMTP server to use, the SMTP server must be configured to allow anonymous access and to allow email messages to be relayed. Additionally, the SMTP server must have Internet access if you want the ability to send messages to external email addresses.
  
For more information about installing, configuring, and managing the SMTP service, see [Outgoing email configuration](outgoing-email-configuration.md) . 
  
> [!NOTE]
> Only a member of the Farm Administrators group can configure an SMTP server. The user must also be a member of the local Administrators group on the server. 
  
### From and Reply-to addresses

When configuring outgoing email, you can configure the following two addresses:
  
- **From address**
    
    Alerts and notifications are sent from an administrative account on the server farm. This account is probably not the one you want to be displayed in the From field of an email message. The address that you use does not need to correspond to an actual email account; it can be a simple friendly address that is recognizable to an end user. For example, "Site administrator" might be an appropriate From address.
    
- **Reply-to address**
    
    This is the address that is displayed in the To field of a message when a user replies to an alert or notification. The Reply-to address should also be a monitored account to ensure that end users receive prompt feedback for issues they might have. For example, a help desk alias might be an appropriate Reply-to address.
    
### Character set

When you configure outgoing email, you will need to specify the character set to use in the body of email messages. A character set is a mapping of characters to their identifying code values. The default character set for outgoing email is Unicode UTF-8, which allows most combination of characters (including bidirectional text) to co-exist in a single document. In most cases, the default setting of UTF-8 works well, although East Asian languages are best rendered with their own character set.
  
Be aware that if you select a specific language code, the text is less likely to appear correctly in mail readers configured for other languages.
  
## See also
<a name="section2"> </a>

#### Concepts

[Configure outgoing email for a SharePoint Server farm](outgoing-email-configuration.md)

