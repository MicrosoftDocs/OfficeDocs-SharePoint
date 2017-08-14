---
title: Schedule profile synchronization in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 53038195-cb59-4779-9bdb-ba0b1cad6f07
---


# Schedule profile synchronization in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-08-01* **Summary:** Learn how to schedule profile synchronization in SharePoint Server 2013 and SharePoint Server 2016.Follow this procedure to schedule profile synchronization. You must have first performed a full synchronization before you can set the incremental synchronization schedule. You need to be a farm administrator or an administrator of the User Profile service application to perform this procedure. **To schedule profile synchronization**
1. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
  
2. On the Manage Service Applications page, click the link for the User Profile service application.
    
  
3. On the Manage Profile Service page, in the **Synchronization** section, click **Configure Synchronization Timer Job**.
    
  
4. On the Edit Timer Job page, in the **Recurring Schedule** section, select the frequency at which you want recurring profile synchronization to occur.
    
  - If you select **Minutes**, type the number of minutes that should pass between the start of each timer job.
    
  
  - If you select **Hourly**, type the number of minutes past every hour that the timer job should start to run at the earliest, and type the number of minutes past every hour that the timer job should start to run at the latest.
    
  
  - If you select **Daily**, select the time at which the timer job should start to run, at the earliest and at the latest, every day.
    
  
  - If you select **Weekly**, select the earliest and latest day and time at which the timer job should start to run every week.
    
  
  - If you select **Monthly**, either select the earliest and latest date and time at which the timer job should start to run every month, or select a day and time at which the timer job should start to run every month.
    
  

    > [!NOTE:]
      
5. Click **OK**, or, if you want to start the profile synchronization immediately, click **Run Now**.
    
  

# See also

#### 

 [Start profile synchronization manually in SharePoint Server](html/start-profile-synchronization-manually-in-sharepoint-server.md)
  
    
    

  
    
    

