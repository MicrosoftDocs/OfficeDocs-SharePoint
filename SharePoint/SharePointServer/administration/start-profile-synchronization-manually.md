---
title: "Start profile synchronization manually in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/1/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 6cdcb2e3-8a77-4219-ba08-cc1d0ae8944f
description: "Learn how to start profile synchronization manually in SharePoint Server."
---

# Start profile synchronization manually in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article describes how to start profile synchronization for SharePoint Server manually. You can start a full synchronization or an incremental synchronization of profile information. You might want to consider starting profile synchronization manually if you have made considerable changes to user profiles, and you don't want to wait for the next scheduled synchronization.
  
Note that this procedure is only for SharePoint Server farms that are using SharePoint Active Directory Import. If you are using an external identity manager, see the documentation for your identity manager.
  
You can also [configure profile synchronization to run automatically according to a schedule](schedule-profile-synchronization.md).
  
## Start profile synchronization manually
<a name="proc1"> </a>

You can manually start a full synchronization or an incremental synchronization of profile information. You need to be a farm administrator or an administrator of the User Profile service application to perform this procedure.
  
Usually, an incremental synchronization is fine, but you should use a full synchronization if any of the following are true.
  
- A mapped property has changed. For example, you mapped a new property, or added or changed a mapping associated with a property.
    
- You changed the containers that a connection uses to synchronize with AD DS.
    
- You added or deleted a synchronization connection.
    
Keep in mind that a full synchronization can take a long time, depending on the size of your directory.
  
 **To start profile synchronization manually**
  
1. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
2. On the **Manage Service Applications** page, click the link for the User Profile service application. 
    
3. On the **Manage Profile Service** page, in the **Synchronization** section, click **Start Profile Synchronization**.
    
4. On the **Start Profile Synchronization** page, select **Start Incremental Synchronization** to synchronize only profiles that have changed since the last synchronization, or select **Start Full Synchronization** to synchronize all profiles. 
    
5. Click **OK**.
    
    > [!NOTE]
    > Refresh the **Manage Profile Service** page to view the profile synchronization status. 
  
## See also
<a name="proc1"> </a>

#### Concepts

[Overview of profile synchronization in SharePoint Server 2013](profile-synchronization-in-sharepoint-server-2013.md)
  
[Synchronize user and group profiles in SharePoint Server 2013](configure-profile-synchronization.md)

