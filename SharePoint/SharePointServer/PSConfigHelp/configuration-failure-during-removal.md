---
title: "Configuration failure during removal"
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
ms.assetid: 4451ffa5-3119-4402-9c67-168e58c5154d
description: "Summary: Learn how to remove SharePoint Server during a configuration failure."
---

# Configuration failure during removal

 **Summary:** Learn how to remove SharePoint Server during a configuration failure. 
  
When you choose **Uninstall** from **Uninstall or change a program**, the Setup Wizard starts and attempts to uninstall the product. If an error is encountered, the uninstall process will not complete and the error will be noted in the setup log file.
  
> [!NOTE]
> The setup log file is stored in the temp directory for the user account that is running setup (%USERTEMP% or %WINDIR%\Users\user account\AppData\Local\Temp) and is named "SharePoint Server Setup ( _YYYYMMDDHHMMSSrandomnumber_).log" where  _YYYYMMDD_ is the date and  _HHMMSS_ is the time (hours in 24-hour clock format, minutes, seconds, and milliseconds) and the random number is used to differentiate between possible simultaneous attempts to run the setup program. 
  
You can review the log file for error messages. After you understand why the error occurred, you can address the issue, and then you can choose to either stop the uninstall process, address the problem, and then run **Uninstall** again, or you can continue the uninstall process. 
  
If you exit Setup when an error is encountered, the binary files will not be removed. However, tasks that were successfully completed will not be undone. This approach will enable you to restore the server to working condition by running the configuration wizard in **Repair** mode. 
  
If you choose to continue with the uninstall process, the binary files will be removed. The resulting state of the computer will depend on when the configuration wizard failed. For example, the computer might still:
  
- Be joined to the server farm.
    
- Be registered in the configuration database and the connection string on the local computer could exist.
    
- Include services that are running.
    
With the binary files removed, you will not be able to use the configuration wizard to clean up the configuration settings on the local computer or in the configuration database.
  

