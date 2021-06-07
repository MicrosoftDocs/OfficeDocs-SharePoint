---
title: "Manage site access based on sensitivity label"
ms.reviewer: samust
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.custom:
-  Adm_O365
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- M365-collaboration
search.appverid:
- MET150
description: "Learn about how to use Azure Active Directory authentication context with SharePoint sites."
---

# Manage site access based on sensitivity label


Create an authentication context
1. In [Azure Active Directory Conditional Access](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/ConditionalAccessBlade), under **Manage**, click **Authentication context (Preview)**.

2. Click **New authentication context**.

3. Type a name and description and select the **Publish to apps** check box.

    ![Screenshot of add authentication context UI](media/aad-add-authentication-context.png)

4. Click **Save**.


Update a sensitivity label
1. In the [Microsoft 365 compliance center](https://compliance.microsoft.com/informationprotection), on the **Information protection** tab, click the label that you want to update and then click **Edit label**.

2. Click **Next** to the **Define protection settings for groups and sites**.

3. Ensure that the **External sharing and Conditional Access settings** check box is selected, and then click **Next**.

4. On the **Define external sharing and device access settings page**, select the **Use Azure AD Conditional Access to protect labeled SharePoint sites** check box.

5. Select the **Choose an existing authentication context (preview)** option.

    ![Screenshot of Azure AD authentication context sensitivity label settings](media/aad-authentication-context-label-setting.png)

6. Click **Next** to the **Review your settings and finish** screen, and then click **Save label**.



[Azure Active Directory terms of use](/azure/active-directory/conditional-access/terms-of-use)

[Use sensitivity labels to protect content in Microsoft Teams, Microsoft 365 groups, and SharePoint sites](/microsoft-365/compliance/sensitivity-labels-teams-groups-sites)

[Authentication context](/azure/active-directory/conditional-access/concept-conditional-access-cloud-apps#configure-authentication-contexts)

## See also

[Conditional Access: Cloud apps, actions, and authentication context](/azure/active-directory/conditional-access/concept-conditional-access-cloud-apps)