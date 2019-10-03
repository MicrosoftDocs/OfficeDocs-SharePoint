---
title: "Microsoft PowerShell cmdlets for the SharePoint Products Configuration wizard"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/8/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ROBOTS: NOINDEX
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 44f04bd5-7130-4c02-9485-73e59e93ce04
description: "Summary: Learn how to use Microsoft PowerShell to control certain features in SharePoint Server."
---

# Microsoft PowerShell cmdlets for the SharePoint Products Configuration wizard

 **Summary:** Learn how to use Microsoft PowerShell to control certain features in SharePoint Server. 
  
In SharePoint Server, you can use Microsoft PowerShell cmdlets as an alternate interface to perform several operations that control how the SharePoint products are configured. You must be a member of the Administrators group on the local computer to perform these operations.
  
You run the Microsoft PowerShell cmdlets from the **SharePoint Management Shell** window. To access **SharePoint Management Shell** window, go to **Start** -> **All Programs**- > SharePoint Management Shell.
  
The cmdlets must be run in a specific order to run successfully. If you use SharePoint 2016 Products Configuration Wizard to configure your installation, it calls the commands (also called configuration tasks) in the correct order for you. However, if you use cmdlets, you must ensure that you are performing the tasks in the correct order. The Microsoft PowerShell cmdlets must be performed in the following order:
  
1. **New-SPConfigurationDatabase**
    
2. **Install-SPHelpCollection**
    
3. **Initialize-SPResourceSecurity**
    
4. **Install-SPService**
    
5. **Install-SPFeature**
    
6. **New-SPCentralAdministration**
    
7. **Install-SPApplicationContent**
    

