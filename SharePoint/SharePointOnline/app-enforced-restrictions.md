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
description: Learn how to set a conditional access policy in the Azure AD admin center to use app-enforced restrictions in SharePoint.
---

# Use app-enforced restrictions

These steps in the Azure AD admin center tell Azure to use the SharePoint site-level access settings you specify.
  
1. On the [Conditional Access | Policies page](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/ConditionalAccessBlade/Policies) of the Azure AD admin center, select **New policy**.

    ![Conditional access policies in the Azure AD admin center](media/azure-ca-new-policy.png)

2. Enter a suitable name for the policy you are creating.

3. Select **Users and groups**, and then select whether you want the policy to apply to all users or only select users or groups.

4. Select **Cloud apps or actions**, select **Select apps**, search for **SharePoint**, select **Office 365 SharePoint Online**, and then select **Select**.

    ![Selecting the SharePoint app](media/azure-ca-policy-cloud-app.png)

5. Select **Conditions**, select **Client apps**, switch **Configure** to **Yes**, keep all the clients selected, and then select **Done**.

6. Select **Session**, select **Use app enforced restrictions**, and then select **Select**. 

    ![Selecting to control access using app enforced restrictions](media/azure-ca-policy-session.png)

7. Enable the policy and select **Create**.
