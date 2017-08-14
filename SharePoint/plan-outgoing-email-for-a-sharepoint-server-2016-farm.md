---
title: Plan outgoing email for a SharePoint Server 2016 farm
ms.prod: SHAREPOINT
ms.assetid: 75401651-ef01-4348-878e-8a636f0b072d
---


# Plan outgoing email for a SharePoint Server 2016 farm
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-12* **Summary: ** Learn how to configure outgoing email to relay email alerts and notifications in your SharePoint Server 2016 and SharePoint Server 2013 farm or web application.Outgoing email is the foundation on which site administrators can implement several email notification features. These features help end users track changes and updates to individual site collections and allow site administrators to deliver status messages.In this article:
-  [About outgoing email](#section1)
    
  
-  [Key planning phases of outgoing email](#section2)
    
  

## About outgoing email
<a name="section1"> </a>

Properly configuring outgoing email is a requirement for implementing email alerts and notifications. The outgoing email feature uses an outbound Simple Mail Transfer Protocol (SMTP) service to relay email alerts and notifications. These email features include the following:
- **Alerts**
    
    In a large and growing site collection, users need a way to keep up with updates to lists, libraries, and discussions. Alerts help to keep users aware of changes. For example, if many users work on the same document, the owner of the document can set up alerts to be notified whenever there are changes to this document. Users can specify which areas of the site collection or which documents they want to track and decide how often they want to receive alerts.
    
    > [!NOTE:]
      
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
    
  

## Outbound SMTP server

The SMTP service is a component of Internet Information Services (IIS); however, it is not enabled by default with IIS. It can be enabled by using **Add Roles and Features Wizard** in Server Manager.After determining which SMTP server to use, the SMTP server must be configured to allow anonymous access and to allow email messages to be relayed. Additionally, the SMTP server must have Internet access if you want the ability to send messages to external email addresses.For more information about installing, configuring, and managing the SMTP service, see  [Install and configure the SMTP service](configure-outgoing-email-for-a-sharepoint-server-farm.md#section3) .
> [!NOTE:]

  
    
    


## From and Reply-to addresses

When configuring outgoing email, you can configure the following two addresses:
- **From address**
    
    Alerts and notifications are sent from an administrative account on the server farm. This account is probably not the one you want to be displayed in the From field of an email message. The address that you use does not need to correspond to an actual email account; it can be a simple friendly address that is recognizable to an end user. For example, "Site administrator" might be an appropriate From address.
    
  
- **Reply-to address**
    
    This is the address that is displayed in the To field of a message when a user replies to an alert or notification. The Reply-to address should also be a monitored account to ensure that end users receive prompt feedback for issues they might have. For example, a help desk alias might be an appropriate Reply-to address.
    
  

## Character set

When you configure outgoing email, you will need to specify the character set to use in the body of email messages. A character set is a mapping of characters to their identifying code values. The default character set for outgoing email is Unicode UTF-8, which allows most combination of characters (including bidirectional text) to co-exist in a single document. In most cases, the default setting of UTF-8 works well, although East Asian languages are best rendered with their own character set.Be aware that if you select a specific language code, the text is less likely to appear correctly in mail readers configured for other languages.
# See also

#### 

 [Configure outgoing email for a SharePoint Server farm](html/configure-outgoing-email-for-a-sharepoint-server-farm.md)
  
    
    

  
    
    

