---
title: "Add Yammer to the navigation bar for SharePoint Server"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/5/2018
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 0d32d946-52d0-4913-bfdb-d3c1193cfc4a
description: "Summary: Use a toggle switch to determine whether to show the SharePoint Newsfeed or Yammer in SharePoint Server navigation."
---

# Add Yammer to the navigation for SharePoint Server

 **Summary:** Use a toggle switch to determine whether to show the SharePoint Newsfeed link or Yammer on the navigation bar in SharePoint Server. 

You can choose whether users see a link to Newsfeed or Yammer in the site navigation by using a simple toggle switch.

The user account that is performing this procedure must be a member of the Farm Administrators group.

## In SharePoint Server 2016, change the navigation tile from Newsfeed to Yammer

1. Start the SharePoint Central Administration tool.

2. In the **Office 365** section, Choose **Configure Yammer**.

3. On the **Yammer Configuration** page, choose **Activate Yammer**. 
     ![Yammer Configuration page in Central Admin](../media/Yammer_IntegrationinCentralAdmin.GIF) 
    After a few minutes, the **Activate Yammer** button goes away.

4. Verify that Yammer is selected by clicking the Office 365 icon. You should see the Yammer tile rather than the Newsfeed tile.
     ![Office 365 navigation showing the Yammer tile](../media/Yammer_Tile SharePoint.PNG)

##In SharePoint Server 2013 running Service Pack 1 for SharePoint Server 2013, change the link on the top navigation bar

1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group. 
    
2. On the Central Administration website, choose **Office 365** > **Configure Yammer**.

3. On the **Configure Yammer** page, select **Activate Yammer**. 
     
     ![Yammer Configuration page in Central Admin](../media/Yammer_IntegrationinCentralAdmin.GIF)
  
4. Look at the top navigation bar to verify that the Newsfeed link is replaced with a link to Yammer. 
    

