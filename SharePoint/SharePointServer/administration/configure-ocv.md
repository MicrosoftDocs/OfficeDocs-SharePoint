---
title: "Configure the One Customer Voice (OCV) feedback"
ms.author: serdars
author: serdars
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

> [!Note]
> This feature is now available only for preview channel. Your SharePoint Server can't use this feature.

Microsoft aspires to bring the best possible experiences for users around the world through its innovative product offerings. Play a key role in helping Microsoft build the features that you need as we develop our products or services.

SharePoint Server uses One Customer Voice (OCV) as our 1st-party solution to collect customer feedback from the farm administrators. The SharePoint Server asks farm administrators to provide Net Promoter Score (NPS) with an OCV pop-up dialog when each admin launches the Central Administration page either locally or remotely through a browser. Your feedback goes directly to our engineers and helps us shape the future of SharePoint Server and services for our users.

The following data is collected from the customers: NPS score, the admin provides the score (optional), contact email (optional), Farm ID, and SharePoint Server Version.

As of now, this survey is a two question survey, which automatically shows up based on the following rules:

- The first NPS survey pops up every two weeks after a farm administrator visits the Central Administration site for the first time after the update is installed. The admin sees the following survey dialog:
  :::image type="content" source="../media/feedback-microsoft-ocv.png" alt-text="Screenshot that shows the feedback to Microsoft survey.":::
- The NPS survey shows up again after six months, if the administrator completes the survey.
- The NPS survey pops up every two weeks until it's completed by the administrator.

In the survey, you can provide recommendation for the SharePoint Server product, feedback, and e-mail ID, if you would like to be contacted.

> [!Note]
> By default, this feature is enabled.

For more information on how to disable this feature for the farm administrators or specific users, see:

- [To disable OCV feedback for current Farm Administrator](#to-disable-ocv-feedback-for-current-farm-administrator)
- [To disable OCV feedback for current Farm](#to-disable-ocv-feedback-for-current-farm)

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
     Disable-SPCustomerFeedbackForUser -UserSid $user.Sid 
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
      Enable-SPCustomerFeedbackForUser -UserSid $user.Sid
      ```
This `$user` is obtained from Step 1. 
  
## To disable OCV feedback for current Farm 

Use the following cmdlet to disable OCV feedback for current farm:  
  
  ```
  Disable-SPCustomerFeedbackForFarm
  ```
  
## To enable OCV feedback for current Farm 

Use the following cmdlet to enable OCV feedback for current farm:
  
  ```
  Enable-SPCustomerFeedbackForFarm
  ```