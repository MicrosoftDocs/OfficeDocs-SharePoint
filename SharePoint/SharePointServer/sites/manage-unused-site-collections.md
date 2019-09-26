---
title: "Manage unused site collections in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/26/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 4737381b-24e5-4c32-bdff-10dd4a81e648
description: "How to manage unused site collections and how to delete site collections automatically in SharePoint Server."
---

# Manage unused site collections in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
> [!NOTE]
> To send email notifications, you must configure outgoing email settings. For more information, see [Configure outgoing email for a SharePoint Server farm](../administration/outgoing-email-configuration.md). 
  
Site usage confirmation and deletion can help to free resources that are used by site collections that are no longer needed. Site collections can be deleted automatically after a specified period of inactivity or can depend on the site collection owner's response to a notification.
  
## Before you begin

Before completing the procedure in this article, you should determine the following:
  
- How long to wait before you check whether a site collection is inactive.
    
- How often to send email notifications to site owners to see whether their sites collections are inactive. After the first email notification, if the site collection owner does not respond, you can continue to send additional notices at daily, weekly, or monthly intervals.
    
- Whether you want to automatically delete unused site collections or delete a site collection if the owner does not respond to multiple email notifications. If you delete site collections without an owner's approval, we recommend that you first back up the site.
    
- If you plan to automatically delete unused site collections, determine how many email notifications you will send to the site owner before you do so. By default, 28 daily notices are sent before site collection deletion. You can configure this number from a minimum of 28 notices to a maximum of 168 notices. For weekly notices, you can send a minimum of four notices and a maximum of 24 notices. For monthly notices, you can send a minimum of two notices and a maximum of six notices to site owners. The email notification contains links to confirm whether a site collection is active or inactive. After an email notification is sent to the site collection owner, there are three possible results:
    
  - If the site collection owner confirms that the site collection is active by clicking the confirmation link in the email notification, the certification date of the site collection is renewed.
    
  - The site collection owner continues to receive periodic email notifications according to the interval specified by a member of the Farm Administrators group, until the site collection owner confirms that the site collection is active or deletes the site collection.
    
  - If the site collection is not active, and a member of the Farm Administrators group has turned on the automatic deletion feature, email notifications are sent to the site collection owner for the specified number of times. If the site collection owner does not confirm the status of the site collection, the site collection is deleted automatically.
    
We recommend the following best practices to safeguard against the automatic deletion of a site collection:
  
- Require a secondary site collection owner when users create site collections. By default, the site collection creator is listed as the primary site collection owner. A site collection owner can also specify a secondary site collection owner. Confirmation notifications are automatically sent to the primary and the secondary site collection owners.
    
- Keep the organization informed about vacations and leave a contingency plan. For example, if a site collection owner is unavailable for four weeks, and a member of the Farm Administrators group has set the site collection and deletion policy, after four missed weekly confirmations, the site could be deleted without giving the site collection owner an opportunity to confirm the usage of the site.
    
- Ensure that there is a schedule to back up site collections regularly so that you can restore a recent copy if a site collection is deleted.
    
    > [!NOTE]
    > Automatic deletion permanently removes all the content and information from the site collection and any sites within the site collection. 
  
## Manage unused site collections

Use this procedure to manage unused site collections. You can follow these steps to determine the schedules for notifying site collection owners of site collection inactivity before deleting unused site collections.
  
 **To manage unused site collections**
  
1. Verify that you meet the following minimum requirements:
    
   - You must be a member of the Farm Administrators group on the computer running the SharePoint Central Administration website.
    
2. In Central Administration, on the **Application Management** page, in the **Site Collections** section, click **Confirm site use and deletion**.
    
3. On the **Site Use Confirmation and Deletion** page, in the **Web Application** section, if the web application that you want to configure is not listed, expand the **Web Application** list, and then click **Change Web Application**.
    
4. In the **Select Web Application** dialog box, click the web application that you want to configure. 
    
5. In the **Confirmation and Automatic Deletion Settings** section: 
    
   - Select or clear the **Send e-mail notification to owners of unused site collections** check box. 
    
     If you select this check box, type the number of days, after the site collection creation or after the site collection usage is confirmed, to start to send notifications. The default number of days is 30, and the maximum is 365.
    
   - Specify a daily, weekly, or monthly schedule for email notifications. By default, the schedule is daily. You can also specify the exact time to run the check for the site collection usage. By default, the time is midnight.
    
   - Select or clear the **Automatically delete the site collection if use is not confirmed** check box. 
    
     If you select this check box, type the number of notifications to send before the site collection is deleted. By default, it is 28 notifications.
    
6. Click **OK**.
    
## See also

#### Concepts

[Delete and restore site collections in SharePoint Server](delete-and-restore-site-collections.md)

