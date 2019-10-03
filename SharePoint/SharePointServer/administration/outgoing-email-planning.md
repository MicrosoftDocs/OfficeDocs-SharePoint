---
title: "Plan outgoing email for a SharePoint Server farm"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 06/22/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 75401651-ef01-4348-878e-8a636f0b072d
description: "How to configure outgoing email to relay email alerts and notifications in SharePoint Server."
---

# Plan outgoing email for a SharePoint Server farm

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
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

### SMTP server authentication

The SMTP server authentication feature is only available in SharePoint Server 2019.

SharePoint Server 2019 supports connecting to SMTP servers anonymously or with authentication. If your SMTP server requires authentication, you'll need to provide credentials that SharePoint will use to authenticate to the SMTP server. It's recommended to use account credentials that match the From address. If you wish to use credentials for a different account, ensure that account has "Send As" permission to impersonate the From address.

> [!NOTE]
> If you're using a Windows account to authenticate to the SMTP server, you can specify the user name using either the Universal Principal Name (UPN) format (user@domain.com) or the NT4 login format (DOMAIN\user). If you're using a non-Windows account to authenticate to the SMTP server, contact your email administrator to determine the correct user name format.

You must set an application credential key on each server in the farm before providing credentials. The application credential key is a separate password that is used to encrypt and decrypt the SMTP password. The application credential key must be identical on all servers in the farm. Microsoft recommends using a strong password for the application credential key and avoid reusing the same password as your farm passphrase, farm service accounts, etc.

SharePoint supports the following Simple Authentication and Security Layer (SASL) mechanisms to authenticate to an SMTP server:

- GSSAPI (Kerberos, NTLM)

- NTLM

- LOGIN
  
> [!NOTE]
> SharePoint uses the following Service Principal Name (SPN) to authenticate to the SMTP server during Kerberos and NTLM authentication, where &lt;host&gt; is the SMTP server name you provided: <br/> SMTPSVC/&lt;host&gt;

### Use TLS connection encryption

Set **Use TLS connection encryption** to Yes to require SharePoint to extablish an encrypted connection to the SMTP server before sending email. A valid server certificate must be installed on the SMTP server to establish an encrypted connection. If this is set to Yes and an encrypted connection can't be established, no emails will be sent.

> [!Note]
> SharePoint supports STARTTLS to establish TLS connection encryption to an SMTP server. It doesn't support SMTPS to establish SSL connection encryption to an SMTP server.

> [!Note]
> Although SharePoint can require TLS connection encryption when sending email to an SMTP server, it can't control whether connection encryption will be used when that SMTP server sends the email to other SMTP servers. Work with your email administrator to configure your SMTP servers to favor connection encryption.

### Email impersonation

Some SharePoint features may impersonate end users when sending email to personalize the message. For example, when a user requests access to a site, SharePoint will set the "From" address of the email notification to be the user who made the request.

Some SMTP servers may block impersonation to protect users from unauthorized attempts to spoof their identities. If your SMTP server blocks impersonation, there are several options for allowing SharePoint emails to be sent:

- [Grant permission for the SharePoint authenticated email account to impersonate users](#users)

- [Disable SharePoint email impersonation](#disable)

- [Use an externally secured receive connector](#connector)

####Grant permission for the SharePoint authenticated email account to impersonate users <a name="users"> </a>

Microsoft Exchange Server allows you to grant permission for a user to impersonate other users when sending email through a receive connector. Those permissions include:

|**Receive connector permission**|**Description**|
|:-----|:-----| 
| ms-Exch-SMTP-Submit <br/> | The session must be granted this permission or it will be unable to submit messages to this receive connector. If a session doesn't have this permission, the MAIL FROM and AUTH commands will fail.  <br/> |   
| ms-Exch-SMTP-Accept-Any-Recipient <BR/> | This permission allows the session to relay messages through this connector. If this permission isn't granted, only messages that are addressed to recipients in accepted domains are accepted by this connector.  <BR/> |
| ms-Exch-SMTP-Accept-Any-Sender <br/> | This permission allows the session to bypass the sender address spoofing check. <br/> **NOTE:** This permission is only necessary if SharePoint will impersonate users whose email account is not managed by your organization. <br/> |
| ms-Exch-SMTP-Accept-Authoritative-Domain-Sender <br/> | This permission allows senders that have email addresses in authoritative domains to establish a session to this receive connector. <br/> |
| ms-Exch-Accept-Headers-Routing <br/> | This permission allows the session to submit a message that has all received headers intact. If this permission isn't granted, the server will strip all received headers. <br/> |

Run this command on your Microsoft Exchange Server to grant permission for the SharePoint authenticated email account to impersonate other users through a receive connector:

<pre><code>Get-ReceiveConnector "&lt;Receive Connector Name&gt;" | Add-ADPermission -User &lt;DOMAIN\AuthenticatedEmailAccount&gt; -ExtendedRights ms-Exch-SMTP-Submit, ms-Exch-SMTP-Accept-Any-Recipient, ms-Exch-SMTP-Accept-Any-Sender, ms-Exch-SMTP-Accept-Authoritative-Domain-Sender, ms-Exch-Accept-Headers-Routing</code></pre>

> [!Note]
> When using Microsoft Exchange Server 2013 or later, this permission should be applied to the client proxy receive connector. When using Microsoft Exchange Server 2010 or earlier, this permission should be applied to the client frontend receive connector.

### Disable SharePoint email impersonation <a name="disable"> </a>

You can configure each SharePoint web application to disable email impersonation. This will ensure that SharePoint always uses the From and Reply-To address specified at the web application level. Run the following to disable SharePoint email impersonation:

1.  Launch the **SharePoint 2019 Management Shell**.
2. Run the following commands:

```powershell
...
$webapp = Get-SPWebApplication <web application URL>
$webapp.OutboundMailOverrideEnvelopeSender = $true
$webapp.Update()
...
```
### Use an externally secured receive connector <a name="connector"> </a>

Microsoft Exchange Server receive connectors can be configured to automatically trust all emails as authenticated, even if no authentication is performed. SharePoint will then send emails to this receive connector anonymously. Follow these steps to create an externally secured receive connector:

1.	Create a dedicated "Custom" receive connector for the SharePoint farm.
2.	Set the receive connector's permission group to "Exchange Servers."
3.	Set the receive connector's authentication type to "externally secured."

Due to the risk of spoofing in this configuration, it's recommended to restrict the IP addresses this receive connector will accept email messages from to just the servers in your SharePoint farm.

## See also
<a name="section2"> </a>

#### Concepts

[Configure outgoing email for a SharePoint Server farm](outgoing-email-configuration.md)

