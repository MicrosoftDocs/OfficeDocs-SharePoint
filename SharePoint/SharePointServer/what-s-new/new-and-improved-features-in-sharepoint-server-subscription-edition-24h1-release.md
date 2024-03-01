---
ms.date: 09/06/2023
title: "New and improved features in SharePoint Server Subscription Edition Version 24H1"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: overview
ms.service: sharepoint-server-itpro
ms.localizationpriority: high
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
description: "Learn about the new features and updates to existing features in SharePoint Server Subscription Edition Version 24H1."
---

# New and improved features in SharePoint Server Subscription Edition Version 24H1

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Learn about the new features and updates introduced in the SharePoint Server Subscription Edition Version 24H1 feature update.

## Summary of the features

The following table provides a summary of the new features introduced in the SharePoint Server Subscription Edition Version 24H1 feature update.

|**Feature**|**Release ring**|**More information**|
|:-----|:-----|:-----|
|  **Custom branding in the Suite Bar**  |  Standard release   |  For more information, see [Custom branding in the Suite Bar](new-and-improved-features-in-sharepoint-server-subscription-edition-23h2-release.md#custom-branding-in-the-suite-bar) |
|  **Search vertical customization in modern search results**  | Early release  | For more information, see [Search vertical customization in modern search results](#search-vertical-customization-in-modern-search-results). |
|  **OpenID Connect (OIDC) integration with SharePoint certificate management**  | Early release  | For more information, see [OpenID Connect (OIDC) integration with SharePoint certificate management](#openid-connect-oidc-integration-with-sharepoint-certificate-management). |
| **Customer feedback experience in Central Administration**   |Early release   |For more information, see [Customer feedback experience in Central Administration](#customer-feedback-experience-in-central-administration).  |

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition Version 24H1.

> [!NOTE]
> Features previously introduced in the Version 23H2 feature update will not be described here. For more information on Version 23H2, see [New and improved features in SharePoint Server Subscription Edition Version 23H2](new-and-improved-features-in-sharepoint-server-subscription-edition-23h2-release.md). 

### Search vertical customization in modern search results

SharePoint Server Subscription Edition Version 24H1 introduced search vertical customization to the modern search experience, previously available only in the classic search experience. This  customization feature allows users to add a custom search vertical to their search results page at the site and organizational levels.

The configuration of this feature is based on the same architecture as the existing classic UI, so the steps to configure this feature in the modern UI are similar to the classic UI.

For more information, see [How to add a custom search vertical to your search results page in SharePoint Server.](../search/how-to-add-a-custom-search-vertical-to-your-search-results-page.md)


### OpenID Connect (OIDC) integration with SharePoint certificate management

OpenID Connect (OIDC) is a modern authentication protocol that seamlessly integrates applications and devices with the identity and authentication management solutions to keep pace with the evolving security and compliance needs of your organization. 

SharePoint Server Subscription Edition Version 24H1 introduces the ability to manage OIDC nonce cookie certificates via SharePoint Certificate Management. The nonce cookie certificate is part of the infrastructure that ensures OIDC authentication tokens are secure.

SharePoint farm administrators can now use the SharePoint Certificate Management feature to manage the full lifecycle of the OIDC nonce cookie certificate. This will automatically deploy the OIDC nonce cookie certificate to all servers on the farm and automatically configure the necessary permissions. A new SharePoint Health Analyzer health rule has been added to notify administrators if the nonce cookie certificate is not managed through SharePoint Certificate Management.

For more information, see [Set up OIDC authentication in SharePoint Server with Microsoft Entra ID.](../security-for-sharepoint-server/set-up-oidc-auth-in-sharepoint-server-with-msaad.md)

