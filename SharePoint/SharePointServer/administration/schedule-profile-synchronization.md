---
title: "Schedule profile synchronization in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/1/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 53038195-cb59-4779-9bdb-ba0b1cad6f07
description: "Learn how to schedule profile synchronization in SharePoint Server."
---

# Schedule profile synchronization in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
Follow this procedure to schedule profile synchronization. You must have first performed a full synchronization before you can set the incremental synchronization schedule. 
  
You need to be a farm administrator or an administrator of the User Profile service application to perform this procedure.
  
 **To schedule profile synchronization**
  
1. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
2. On the Manage Service Applications page, click the link for the User Profile service application.
    
3. On the Manage Profile Service page, in the **Synchronization** section, click **Configure Synchronization Timer Job**.
    
4. On the Edit Timer Job page, in the **Recurring Schedule** section, select the frequency at which you want recurring profile synchronization to occur. 
    
  - If you select **Minutes**, type the number of minutes that should pass between the start of each timer job.
    
  - If you select **Hourly**, type the number of minutes past every hour that the timer job should start to run at the earliest, and type the number of minutes past every hour that the timer job should start to run at the latest.
    
  - If you select **Daily**, select the time at which the timer job should start to run, at the earliest and at the latest, every day.
    
  - If you select **Weekly**, select the earliest and latest day and time at which the timer job should start to run every week.
    
  - If you select **Monthly**, either select the earliest and latest date and time at which the timer job should start to run every month, or select a day and time at which the timer job should start to run every month.
    
    > [!NOTE]
    > If you want to specify an exact starting time for the timer job to run, set the same value in the start and end times of the interval in which the timer job should start. 
  
5. Click **OK**, or, if you want to start the profile synchronization immediately, click **Run Now**.
    
## See also

#### Concepts

[Start profile synchronization manually in SharePoint Server](start-profile-synchronization-manually.md)

