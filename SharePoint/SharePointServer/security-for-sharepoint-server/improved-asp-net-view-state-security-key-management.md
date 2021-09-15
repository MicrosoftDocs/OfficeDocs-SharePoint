---
title: Improved ASP.NET view state security and key management
ms.reviewer: 
ms.author: v-bshilpa
author: Benny-54
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 5cdce2aa-fa6e-4888-a34f-de61713f5096
description: "Learn how to setup improved ASP.NET view state security and key management"
---

# Improved ASP.NET view state security and key management

Multiple improvements have been made to SharePoint's integration with the ASP.NET view state feature. First, SharePoint now encrypts the machineKey section of its web.config files by default. This prevents attackers from reading your ASP.NET view state encryption and validation keys even if they gain access to those web.config files.

Second, we introduce the ability to change the ASP.NET view state decryption and validation keys of a SharePoint web application through 2 new PowerShell cmdlets. This allows you to rotate those keys in your farm.

NAME
Set-SPMachineKey

SYNOPSIS
Configures the ASP.NET view state decryption and validation keys of a web application.

SYNTAX
Set-SPMachineKey -WebApplication <SPWebApplicationPipeBind> [-DecryptionKey <String>] [-ValidationKey <String>] [-Local] [<CommonParameters>]

PARAMETERS
-WebApplication <SPWebApplicationPipeBind>
Specifies the name, URL, or GUID of the Web application.

-DecryptionKey [<String>]
Specifies the new ASP.NET view state decryption key. The key should be represented as a 64-character long hexadecimal string (0-9 and A-F).

If this parameter is not specified, a random decryption key will be generated and used.

-ValidationKey [<String>]
Specifies the new ASP.NET view state validation key. The key should be represented as a 64-character long hexadecimal string (0-9 and A-F).

If this parameter is not specified, a random decryption key will be generated and used.

-Local
Deploy the new decryption and validation keys only to the local server. Other servers in the farm will continue to use the previous decryption and validation keys. Web sessions that are load balanced across multiple servers in the farm will fail if these keys are not synchronized on every server in the farm. Use the Update-SPMachineKey cmdlet to deploy the keys to additional servers in the farm.

If this parameter is not specified, the new decryption and validation keys will be deployed to all servers in the farm.

NAME
Update-SPMachineKey

SYNOPSIS
Deploys ASP.NET view state decryption and validation keys to servers in the farm.

SYNTAX
Update-SPMachineKey -WebApplication <SPWebApplicationPipeBind> [-Local] [<CommonParameters>]

PARAMETERS
-WebApplication <SPWebApplicationPipeBind>
Specifies the name, URL, or GUID of the Web application.

-Local Deploy the decryption and validation keys only to the local server. Other servers in the farm will continue to use the previous decryption and validation keys. Web sessions that are load balanced across multiple servers in the farm will fail if these keys are not synchronized on every server in the farm.

If this parameter is not specified, the decryption and validation keys will be deployed to all servers in the farm.
  
  
