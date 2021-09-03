---
title: "SharePoint Central Administration - Support for host header bindings and easier Alternate Access Mappings (AAM) configuration"
ms.reviewer: 
ms.author: v-jmathew
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 5cdce2aa-fa6e-4888-a34f-de61713f5096
description: "Learn how SharePoint Central Administration now supports host header bindings and allows for easier Alternate Access Mappings (AAM) configuration."
---

# SharePoint Central Administration - Support for host header bindings and easier Alternate Access Mappings (AAM) configuration

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

## Host header bindings

You can now configure the SharePoint Central Administration web site to use a host header binding, which will allow it to share the same Transmission Control Protocol (TCP) port number as other web sites. This would typically be used to let the SharePoint Central Administration site and your content web site to be hosted on the same TCP port, such as port 443 for Secure Sockets Layer (SSL).

To configure the SharePoint Central Administration web site, specify the host header binding with the `-HostHeader` parameter of the `New-SPCentralAdministration` and `Set-SPCentralAdministration` cmdlets, or with the `-hostheader` parameter of the `psconfig.exe -cmd adminvs` command.

## Easier AAM configuration

Setting up Central Administration in AAM configurations required users to run multiple commands in the past.

You can now specify the public AAM URL directly in the Central Administration command line tools, bringing them to parity with the content web application command line tools. This can now be specified via the optional "`-Url <String>`" parameter in the following PowerShell cmdlets and PSConfig.exe command line utility:

- `New-SPCentralAdministration`
- `Set-SPCentralAdministration`
- `PSConfig.exe -cmd adminvs`
