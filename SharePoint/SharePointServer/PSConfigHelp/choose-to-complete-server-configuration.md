---
title: "Choose to complete server configuration"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/1/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ROBOTS: NOINDEX
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 6b5f08b7-844a-4a9e-adaf-66b9796bf68e
description: "Summary: Learn how to complete server configuration in SharePoint Server."
---

# Choose to complete server configuration

 **Summary:** Learn how to complete server configuration in SharePoint Server. 
  
## Setup completed successfully

The Setup Wizard has just completed the following:
  
- Validate software prerequisites.
    
- Install necessary files.
    
- Install all components and services.
    
The next required step is to run the SharePoint Products Configuration Wizard. The configuration wizard configures all run-once type activities and configures the services. After the configuration wizard completes, you can begin the SharePoint configuration, including:
  
- Configure server role.
    
- Enable or disable services.
    
- Gather more information for the specific computer role.
    
- Perform other necessary configuration.
    
You can run the configuration wizard at the completion of the Setup Wizard or, if you need to collect more configuration information, you can run the configuration wizard later.
  
### To run the SharePoint Products Configuration Wizard at the completion of the Setup Wizard

- Select **Run the SharePoint Products Configuration Wizard now**, and then click **Close**. The configuration wizard automatically starts.
    
To run the configuration wizard later, clear the **Run the SharePoint Products Configuration Wizard now** check box, and then click **Close**. When you are ready to run the configuration wizard, complete the procedure in [How to: Start the SharePoint Products Configuration wizard](how-to-start-the-sharepoint-products-configuration-wizard.md).
  
## Setup failed

If an error was encountered, the setup process will not be completed and an error will be noted in the Setup log file. The Setup log file is stored in the temp directory for the user account that is running setup (%USERTEMP% or %WINDIR%\Users\user account\AppData\Local\Temp) and is named "SharePoint Server Setup (YYYYMMDDHHMMSSrandomnumber).log" where YYYYMMDD is the date and HHMMSS is the time (hours in 24-hour clock format, minutes, seconds, and milliseconds) and the random number is used to differentiate between possible simultaneous attempts to run the setup program. You can review the log file for error messages. After you understand why the error occurred, you can address the issue, and then you can run Setup again .
  
> [!NOTE]
> If you encounter a failure during the removal process, you can find more information in [Configuration failure during removal](configuration-failure-during-removal.md). 
  

