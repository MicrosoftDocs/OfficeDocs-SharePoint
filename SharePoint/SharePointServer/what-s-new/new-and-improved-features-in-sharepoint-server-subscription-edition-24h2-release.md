---
ms.date: 09/10/2024
title: "New and improved features in SharePoint Server Subscription Edition Version 24H2"
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
description: "Learn about the new features and updates to existing features in SharePoint Server Subscription Edition Version 24H2."
---

# New and improved features in SharePoint Server Subscription Edition Version 24H2

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Learn about the new features and updates introduced in the SharePoint Server Subscription Edition Version 24H2 feature update.

## Summary of the features

The following table provides a summary of the new features introduced in the SharePoint Server Subscription Edition Version 24H2 feature update.

|**Feature**|**Release ring**|**More information**|
|:-----|:-----|:-----|
|  **Search vertical customization in modern search results**  |  Standard release   | For more information, see [Search vertical customization in modern search results](new-and-improved-features-in-sharepoint-server-subscription-edition-24h1-release.md#search-vertical-customization-in-modern-search-results). <br> <br>This was part of *Early release* in the Version 24H1 feature update. <br/> |
|  **OpenID Connect (OIDC) integration with SharePoint certificate management**  | Standard release  | For more information, see [OpenID Connect (OIDC) integration with SharePoint certificate management](new-and-improved-features-in-sharepoint-server-subscription-edition-24h1-release.md#openid-connect-oidc-integration-with-sharepoint-certificate-management). <br> <br>This was part of *Early release* in the Version 24H1 feature update. <br/>  |
| **End of support notification for SharePoint Server builds**   |Standard release   |For more information, see [End of support notification for SharePoint Server builds](#end-of-support-notification-for-sharepoint-server-builds).|
| **Support RSA public key in OIDC authentication configuration**   |Early release   |For more information, see [Support RSA public key in OIDC authentication configuration](#support-rsa-public-key-in-oidc-authentication-configuration).|

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition Version 24H2.

> [!NOTE]
> Features previously introduced in the Version 24H1 feature update will not be described here. For more information on Version 24H1, see [New and improved features in SharePoint Server Subscription Edition Version 24H1](new-and-improved-features-in-sharepoint-server-subscription-edition-24h1-release.md). 


### End of support notification for SharePoint Server builds

SharePoint Server Subscription Edition (SPSE) displays notifications in Central Administration and the SharePoint Management Shell when the build of SPSE that's currently installed is approaching its end of support date. The notifications direct SharePoint farm administrators to install the latest update for SPSE to ensure uninterrupted support.

SharePoint Server Subscription Edition follows the [Modern Lifecycle Policy](/lifecycle/policies/modern) and doesn't have a fixed [End of Support](/lifecycle/definitions#end-of-support) date. However, SharePoint Server Subscription Edition does have a [product servicing policy](../product-servicing-policy/updated-product-servicing-policy-for-sharepoint-server-se.md) that says builds will be supported for one year after its release date. After one year, the build will no longer be supported. This is to ensure that customers stay up to date so they aren't missing important security and quality fixes that are already released, which could cause security breaches in their environments or unnecessary support cases with Microsoft Support.  

The triggers for the notifications are as follows: 

- **6 months until "end of support" date:** Provide an **informational** notice in Central Administration and the SharePoint Management Shell informing the admin that the current build is approaching the end of support, and they should install a newer update. 

- **3 months until "end of support" date:** Provide a **warning notice** in Central Administration and the SharePoint Management Shell informing the admin that the current build is approaching the end of support, and they should install a newer update. 

- **Beyond "end of support" date:** Provide an **error** notice in Central Administration and the SharePoint Management Shell informing the admin that the current build is no longer supported, and they should install a newer update. This error also appears in the Windows Application Event Log. 

### Support RSA public key in OIDC authentication configuration

OIDC is an authentication protocol that uses JSON Web Tokens (JWTs) to verify the identity of users, and grant them access to protected resources. JWTs are digitally signed using either symmetric keys (shared between the issuer and the consumer) or asymmetric keys (public/private key pairs).

Some OIDC providers use RSA public keys that are directly represented with RSA modulus and RSA public exponent. To support these providers, SharePoint Server Subscription Edition Version 24H2 now gives the ability to parse and validate RSA public keys in JWTs. 

For more information, see [Set up OIDC authentication in SharePoint Server using RSA public keys](../security-for-sharepoint-server/set-up-oidc-auth-in-sharepoint-server-using-rsa.md).
