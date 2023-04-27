---
ms.date: 09/15/2021
title: Improved ASP.NET view state security and key management
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 5cdce2aa-fa6e-4888-a34f-de61713f5096
description: "Learn how to set up improved ASP.NET view state security and key management"
---

# Improved ASP.NET view state security and key management

[!INCLUDE[appliesto-xxx-2016-2019-SUB-xxx-md](../includes/appliesto-xxx-2016-2019-SUB-xxx-md.md)]

> [!NOTE]
> SharePoint Server Subscription Edition encrypts the `machineKey` section of its `web.config` files by default. This prevents attackers from reading your ASP.NET view state encryption and validation keys, even if they gain access to those `web.config` files.

Using the following new PowerShell cmdlets, you can change the ASP.NET view state decryption and validation keys of a SharePoint web application, thus allowing you to rotate those keys in your farm.

## PowerShell cmdlets

 1. `Set-SPMachineKey`
 
    Configures the ASP.NET view state decryption and validation keys of a web application.

    #### Syntax
   
    ```PowerShell
    Set-SPMachineKey -WebApplication <SPWebApplicationPipeBind> [-DecryptionKey <String>] [-ValidationKey <String>] [-Local] [<CommonParameters>]
    ```

    #### Parameters
   
     - `-WebApplication <SPWebApplicationPipeBind>`
   
         Specifies the name, URL, or GUID of the Web application.

     - `-DecryptionKey [<String>]`
   
         Specifies the new ASP.NET view state decryption key. The key should be represented as a 64-character long hexadecimal string (0-9 and A-F).

         If this parameter isn't specified, a random decryption key is generated and used.

     -  `-ValidationKey [<String>]`
   
         Specifies the new ASP.NET view state validation key. The key should be represented as a 64-character long hexadecimal string (0-9 and A-F).

         If this parameter isn't specified, a random decryption key is generated and used.

     - `-Local`
   
         Deploy the new decryption and validation keys only to the local server. Other servers in the farm continue to use the previous decryption and validation keys. Web sessions that are load balanced across multiple servers in the farm will fail if these keys are not synchronized on every server in the farm. Use the `Update-SPMachineKey` cmdlet to deploy the keys to additional servers in the farm.

       If this parameter isn't specified, the new decryption and validation keys is deployed to all servers in the farm.
    
 2. `Update-SPMachineKey`
 
    Deploys ASP.NET view state decryption and validation keys to servers in the farm.

    #### Syntax
   
    ```PowerShell
    Update-SPMachineKey -WebApplication <SPWebApplicationPipeBind> [-Local] [<CommonParameters>]
    ```
    
    #### Parameters
    
     - `-WebApplication <SPWebApplicationPipeBind>`
    
       Specifies the name, URL, or GUID of the Web application.

     - `-Local`
    
       Deploys the new decryption and validation keys only to the local server. Other servers in the farm continue to use the previous decryption and validation keys. Web sessions that are load balanced across multiple servers in the farm will fail if these keys are not synchronized on every server in the farm.

       If this parameter is not specified, the decryption and validation keys is deployed to all servers in the farm.
  

