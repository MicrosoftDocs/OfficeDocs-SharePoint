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
|  **Search vertical customization in modern search results**  | Early release  | For more information, see [Search vertical customization in modern search results](#search-vertical-customization-in-modern-search-results). |
|  **OpenID Connect (OIDC) integration with SharePoint certificate management**  | Early release  | For more information, see [OpenID Connect (OIDC) integration with SharePoint certificate management](#openid-connect-oidc-integration-with-sharepoint-certificate-management). |
| **Customer feedback experience in Central Administration**   |Early release   |For more information, see [Customer feedback experience in Central Administration](#customer-feedback-experience-in-central-administration).  |
|  **Custom branding in the Suite Bar**  |  Standard release   |  For more information, see [Custom branding in the Suite Bar](#custom-branding-in-the-suite-bar). |

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition Version 24H1.

> [!NOTE]
> Features previously introduced in the Version 23H2 feature update will not be described here. For more information on Version 23H2, see [New and improved features in SharePoint Server Subscription Edition Version 23H2](new-and-improved-features-in-sharepoint-server-subscription-edition-23h2-release.md). 

### Search vertical customization in modern search results

The search vertical feature is now available in the modern search experience. This customization capability allows users to add a custom search vertical to their search results page at the site level and organizational level.
The configuration of this feature is based on the same architecture as the existing classic UI, so the steps to configure this feature in the modern UI are similar to the classic UI. 

For more information, see [How to add a custom search vertical to your search results page in SharePoint Server.](../search/how-to-add-a-custom-search-vertical-to-your-search-results-page.md)


### OpenID Connect (OIDC) integration with SharePoint certificate management

OpenID Connect (OIDC) is a modern authentication protocol that seamlessly integrates applications and devices with the identity and authentication management solutions to keep pace with the evolving security and compliance needs of your organization. 

SharePoint Server Subscription Edition Version 24H1 introduces the ability to manage OIDC nonce cookie certificates via SharePoint Certificate Management. The nonce cookie certificate is part of the infrastructure that ensures OIDC authentication tokens are secure.

SharePoint farm administrators can now use the SharePoint Certificate Management feature to manage the full lifecycle of the OIDC nonce cookie certificate. This will automatically deploy the OIDC nonce cookie certificate to all servers on the farm and automatically configure the necessary permissions. A new SharePoint Health Analyzer health rule has been added to notify administrators if the nonce cookie certificate is not managed through SharePoint Certificate Management.


For more information, see [Set up OIDC authentication in SharePoint Server with Microsoft Entra ID.](../security-for-sharepoint-server/set-up-oidc-auth-in-sharepoint-server-with-msaad.md)

### Customer feedback experience in Central Administration

SharePoint Server Subscription Edition Version 24H1 introduces One Customer Voice (OCV) into the SharePoint Central Administration site to collect customer feedback from the SharePoint farm administrators. The feedback goes directly to the SharePoint Server product team at Microsoft to help us to continue to improve the product to meet customer needs.

The OCV experience currently offers a two-question survey, which automatically appears in SharePoint Central Administration based on these rules:
1. The first survey appears two weeks after a farm administrator visits the Central Admin site after the update is installed. 
1. The second survey will appear after six months if the SharePoint farm administrator completes the first survey. 
1. If the SharePoint Administrator chooses to skip the survey, it will appear again every two weeks until the survey is completed.


For more information, see [Configure the One Customer Voice (OCV) feedback.](../administration/configure-ocv.md)

### Custom branding in the Suite Bar

The SharePoint Server modern UX provides a powerful yet intuitive user interface that scales from desktop to mobile devices. However, the architecture of the modern UX enables organizations to apply custom branding to the Suite Bar, which is the global navigation bar that provides access to the App Launcher, contextual settings menu, and user profile in SharePoint sites.

SharePoint Server Subscription Edition Version 24H1 introduces the ability for organizations to apply custom branding in the Suite Bar to better align with their branding standards. SharePoint farm administrators are now able to specify custom text, logos, hyperlinks, and color schemes in the Suite Bar that apply to all sites within a web application.

For more information, see [Custom branding in Suite Navigation Bar.](/sharepoint/sites/custom-branding-in-suite-bar)
