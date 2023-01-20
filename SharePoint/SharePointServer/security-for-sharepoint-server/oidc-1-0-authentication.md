---
title: "OpenID Connect 1.0 authentication"
ms.reviewer: 
ms.author: v-jmathew
author: jitinmathew
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 5cdce2aa-fa6e-4888-a34f-de61713f5096
description: "Learn how to set up OIDC authentication in SharePoint Server."
---

# OpenID Connect 1.0 authentication

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

OpenID Connect (OIDC) 1.0 is a modern authentication protocol that seamlessly integrates applications and devices with the identity and authentication management solutions to keep pace with the
evolving security and compliance needs of your organization.

In SharePoint 2019 and prior versions, SharePoint Server supported three types of authentication methods:

1. Windows authentication (New Technology LAN Manager (NTLM), Kerberos, etc.)
2. Forms-based authentication
3. Security Assertion Markup Language (SAML) 1.1-based authentication

SharePoint Server Subscription Edition now supports OIDC 1.0 authentication protocol. With this new capability, you can now set up an OIDC-enabled `SPTrustedIdentityTokenIssuer` that works with a remote identity provider to enable OIDC authentication.

You can set up OIDC authentication in SharePoint Server with either of these options:

- Microsoft Azure Active Directory (Azure AD). For more information, see [Set up OIDC authentication in SharePoint Server with Microsoft Azure Active Directory (Azure AD)](set-up-oidc-auth-in-sharepoint-server-with-msaad.md).

- Active Directory Federation Services (AD FS). For more information, see [Set up OIDC authentication in SharePoint Server with Active Directory Federation Services (AD FS)](set-up-oidc-auth-in-sharepoint-server-with-adfs.md).
