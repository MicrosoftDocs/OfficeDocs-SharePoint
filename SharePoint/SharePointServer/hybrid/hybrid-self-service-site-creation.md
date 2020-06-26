---
title: "Hybrid self-service site creation"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/12/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- IT_SharePoint_Hybrid_Top
- Strat_SP_gtc
- M365-collaboration
- SPO_Content
ms.custom: 
ms.assetid: 27d3e6b8-7922-4015-a5fd-8c240eaa6357
description: "Hybrid self-service site creation redirects the default self-service site creation page in SharePoint Server to the SharePoint in Microsoft 365 Group Creation page. By configuring this feature, you can help your users to create their sites in SharePoint in Microsoft 365 instead of SharePoint Server."
---

# Hybrid self-service site creation

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]

Hybrid self-service site creation redirects the default self-service site creation page in SharePoint Server (/_layouts/15/scsignup.aspx) or (/_layouts/16/scsignup.aspx) to the SharePoint in Microsoft 365 Group Creation page. By configuring this feature, you can help your users to create their sites in SharePoint in Microsoft 365 instead of SharePoint Server.
  
Hybrid self-service site creation respects your hybrid audience settings. If you use a hybrid audience, members of the hybrid audience will be redirected to SharePoint in Microsoft 365 for self-service site creation, while on-premises only users will continue to be directed to self-service site creation in SharePoint Server.
  
This setting can be configured independently for each web application in your farm.
  
Hybrid self-service site creation is available in SharePoint Server 2013 with the March 2017 PU. <br> Hybrid self-service site creation is available in SharePoint 2016 with November 2017 PU. 
  
## Configure hybrid self-service site creation using the Hybrid Picker

Configuring hybrid self-service site creation is done by using the hybrid picker in the SharePoint admin center.
  
> [!NOTE]
> If you've previously configured other hybrid features with the hybrid picker, you can go directly to the SharePoint Central Administration website to manage hybrid self-service site creation. In this case, the hybrid connection has been made and there's no need to run the hybrid picker again. 
  
 **To configure hybrid self-service site creation**
  
1. Log on to a server in your SharePoint Server farm as the farm administrator. 
    
2. From your SharePoint Server computer, open a web browser.
    
3. go to the [More features page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) in Microsoft 365. 

4. Under **Hybrid picker**, select **Open**.
    
5. On the hybrid picker page, select **Hybrid Picker**.
    
6. Follow the wizard, and when prompted, select **Hybrid self-service site creation**. 
    
7. When prompted, select the web application with which you want to use hybrid self-service site creation.
    
When the hybrid picker wizard completes, hybrid self-service site creation will be enabled for the web application that you selected.
  
## Manage hybrid self-service site creation

Once you have configured hybrid self-service site creation, you can manage it in the SharePoint Central Administration website.
  
 **To manage hybrid self-service site creation**
  
1. In Central Administration, select **Application Management**.
    
2. On the **Application Management** page, under **Site Collections**, select **Configure self-service site creation**.
    
3. In the **Web Application** section, select the web application where you want to manage hybrid self-service site creation, and then select or clear the **Create Site Collections in SharePoint** check box. 
    
    > [!NOTE]
    > While hybrid users of this web application will be redirected to SharePoint in Microsoft 365 for self-service site creation, the other settings on this page continue to apply to any on-premises only users. 
  
4. Select **OK**.
    

