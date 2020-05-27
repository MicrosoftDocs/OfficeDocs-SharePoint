---
title: "Migration Manager Goverment Cloud settings"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
description: "Explanation of Government Cloud configuration settings when using Migration Manager." 
---
# Government Cloud

## Configuration values

Configuration values for goverment cloud tenants are listed below.  The default setting is **0**.

|**Cloud**|**Setting value**|
|:-----|:-----|
|Consumer|0|
|GCC|0|
|GCC High|2|
|DoD|2|
</br>


## GCC High and DoD customers

If your are either a **GCC high** or **DoD** customer, you need to make a change to configuration file before you install the agent. All other cloud customers do not have to make this change as the default is already set to 0.


1. Download the agent setup file.
2. Open the setup file and remain on the **Welcome** page. 
3. Open  *%temp%\SPMigrationAgentSetup\SPMigrationAgentSetup\microsoft.sharepoint.migration.common.dll.config*.
4. Change the value of *SPOEnvironmentType* from 0 to 2.
    </br>
  
    ![Change SPOEnvironmentType](media/gov-cloud-setting.png)

5. On the Welcome page, click **Next**. Follow the prompts to enter your SharePoint admin username and password to your GCC High or DoD account.
6. Enter your Windows credentials that will provide access to **all** the file shares that contain the content you want to migrate. Select **Install**.
7. Test agent access (optional) or click **Close**.
</br></br>