---
title: "Outbound e-mail has not been configured (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/31/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 53885793-4150-4212-af04-6ea2e6e066f7
description: "Learn how to resolve the SharePoint Health Analyzer rule: Outbound email has not been configured, for SharePoint Server."
---

# Outbound e-mail has not been configured (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Outbound email has not been configured. 
  
 **Summary:** An outgoing email server has not been configured on this SharePoint Server deployment. With no SMPT server configured for outgoing email, SharePoint Server can't send email messages, including alert email, confirmation email, invitation email, and email about exceeding quotas. 
  
 **Cause:** An SMPT email server hasn't yet been configured in the farm. 
  
 **Resolution: Configure outgoing email settings in Central Administration**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, click **System Settings**.
    
3. On the System Settings page, in the **E-Mail and Text Messages (SMS)** section, click **Configure outgoing e-mail settings**.
    
4. On the Outgoing E-Mail Settings page, type the SMTP server information in the **Outbound SMTP server** box, and then specify the addresses and the character set that you want to use. 
    
5. Click **OK**.
    
## See also

#### Concepts

[Plan email integration for a SharePoint Server farm](../administration/email-integration-planning.md)
  
[Configure email integration for a SharePoint Server farm](../administration/configure-email-integration.md)

