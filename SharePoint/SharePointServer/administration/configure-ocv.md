---
title: "Configure the One Customer Voice (OCV) feedback"
ms.author: Benny-54
author: Benny-54
manager: serdars
ms.date: 6/14/2023
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
description: "Learn how to configure the One Customer Voice (OCV) feedback."
---

# Configure the One Customer Voice (OCV) feedback

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Microsoft aspires to bring the best possible experiences for users around the world through its innovative product offerings. Play a key role in helping Microsoft build the features that you need as we develop our products or services.

SharePoint Server uses One Customer Voice (OCV) as our 1st-party solution to collect customer feedback from the farm administrators. Your feedback goes directly to our engineers and helps us shape the future of SharePoint Server and services for our users.

You can disable or enable the OCV feedback function using one of the following options:

## To disable OCV feedback for current Farm Administrator 

  1. Use the following cmdlet in SharePoint Management Shell to get to the current admin Sid:  

     ```
     $user = Get-SPUser -Identity <Login Name of the admin> -Web <The Central Admin Site URL>
     ```

     **For example:**
     
     ```
     $user = Get-SPUser -Identity 'contoso\domain_admin' -Web http://spse-sps:5000 
     ```

  2. Use the following cmdlet to disable the OCV for current admin: 

     ```
     Disable-OCVForUser -UserSid $user.Sid 
     ```

This `$user` is obtained from Step 1. 
  
## To enable OCV feedback for current Farm Administrator

  1. Use the following cmdlet in SharePoint Management Shell to get to the current admin Sid:  

     ```
     $user = Get-SPUser -Identity <Login Name of the admin> -Web <The Central Admin Site URL>
     ```

     **For example:**
  
     ```
     $user = Get-SPUser -Identity 'contoso\domain_admin' -Web http://spse-sps:5000 
     ```

  2.  Use the following cmdlet to enable the OCV for current admin: 

      ```
      Enable-OCVForUser -UserSid $user.Sid
      ```
This `$user` is obtained from Step 1. 
  
## To disable OCV feedback for current Farm 

Use the following cmdlet to disable OCV feedback for current farm:  
  
  ```
  Disable-OCVForFarm
  ```
  
## To enable OCV feedback for current Farm 

Use the following cmdlet to enable OCV feedback for current farm:
  
  ```
  Enable-OCVForFarm
  ```
  
  
  
  
  
  
