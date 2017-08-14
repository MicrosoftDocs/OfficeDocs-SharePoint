---
title: Outbound e-mail has not been configured (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 53885793-4150-4212-af04-6ea2e6e066f7
---


# Outbound e-mail has not been configured (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Outbound email has not been configured" for SharePoint Server 2016. **Rule Name:**   Outbound email has not been configured. **Summary:**    An outgoing email server has not been configured on this SharePoint Server deployment. With no SMPT server configured for outgoing email, SharePoint Server can't send email messages, including alert email, confirmation email, invitation email, and email about exceeding quotas. **Cause:**   An SMPT email server hasn't yet been configured in the farm. **Resolution: Configure outgoing email settings in Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the SharePoint Central Administration website, click **System Settings**.
    
  
3. On the System Settings page, in the **E-Mail and Text Messages (SMS)** section, click **Configure outgoing e-mail settings**.
    
  
4. On the Outgoing E-Mail Settings page, type the SMTP server information in the **Outbound SMTP server** box, and then specify the addresses and the character set that you want to use.
    
  
5. Click **OK**.
    
  

