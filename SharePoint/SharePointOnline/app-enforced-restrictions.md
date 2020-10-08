---
title: "Use app-enforced restrictions"
ms.reviewer: samust
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- MET150
- BSA160
ms.assetid: 5ae550c4-bd20-4257-847b-5c20fb053622
description: Learn how to block or limit access to SharePoint and OneDrive content on devices that aren't compliant or joined to a domain.
ms.custom: seo-marvel-apr2020
---

# Use app-enforced restrictions

Follow these steps in the Azure AD admin center to tell Azure to use the SharePoint site-level settings you specify in PowerShell.
  
1. On the [Conditional Access | Policies page](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/ConditionalAccessBlade/Policies) of the Azure AD admin center, select select **New policy**.
    
2. Under **Users and groups**, select whether you want the policy to apply to all users or only specific security groups.
    
3. Under **Cloud apps**, select **Office 365 SharePoint Online**.
    
4. Under **Conditions**, select **Client apps**, then select both **Mobile apps and desktop clients** and **Browser**.
    
5. Under **Session**, select **Use app enforced restrictions**. 
    
6. Enable the policy and save it.

    ![Creating a policy in the Azure AD admin center to use app-enforced restrictions](media/c6467cd8-612d-4f8e-98bf-4913b35f49f1.png)

