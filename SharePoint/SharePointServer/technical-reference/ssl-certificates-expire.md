---
title: "SSL certificates are about to expire"
ms.reviewer: 
ms.author: serdars
author: serdars
manager: serdars
audience: ITPro
f1.keywords:
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid:
description: "Learn how to replace the SSL certificates that are about to expire."
---

# SSL certificates are about to expire

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)] 

 **Rule Name:** SSL certificates are about to expire.
  
 **Summary:** SSL certificates currently in use in the farm will expire within the certificate expiration warning threshold (15 days by default). Once an SSL certificate expires, it's no longer valid to secure the resource. Users will receive error messages from their web browsers and client applications when accessing web sites that use expired SSL certificates.
  
 **Cause:** SSL certificates currently in use in the farm are about to expire.
  
 **Resolution: Renew or replace these certificates to ensure uninterrupted access to these resources. You can renew or replace these certificates from the Certificate Management page in Central Administration.**
