---
ms.date: 05/27/2020
title: "Migration Manager Government Cloud settings"
ms.reviewer: 
ms.author: mactra
author: MachelleTranMSFT
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
description: "Explanation of Government Cloud configuration settings when using Migration Manager for file share migrations." 
---
# Government cloud settings for Migration Manager 

>[!Note]
>Migration Manager only supports **File Share migration** for the Government cloud. 

If your tenant resides in a government cloud, you may have additional steps to perform before using Migration Manager.


- [Configuration values](#configuration-values)
- [GCC High and DoD customers](#gcc-high-and-dod-customers)
- [Endpoints for Government](#endpoints-for-government)


## Configuration values

Configuration values for government cloud tenants are listed below.  The default setting is **0**.

|Cloud|Setting value|
|:-----|:-----|
|Consumer|0|
|GCC|0|
|GCC High|2|
|DoD|3|


</br>


## GCC High and DoD customers

If you are either a **GCC high** or **DoD** customer, you need to make a change to configuration file before you install the agent. All other cloud customers do not have to make this change as the default is already set to 0.


1. Download the agent setup file.
2. Open the setup file and remain on the **Welcome** page. 
3. Open *C:\Users\<user>\AppData\Roaming\Microsoft\SPMigration\Bin\microsoft.sharepoint.migration.common.dll.config*.
4. Open *C:\Users\<user>\AppData\Local\Temp\SPMigrationAgentSetup\SPMigrationAgentSetup\microsoft.sharepoint.migration.common.dll.config*.
5. For GCCH, change the value of *SPOEnvironmentType* from 0 to 2, and for DoD, change the value of *SPOEnvironmentType* from 0 to 3.
    </br>
  
    ![Change SPOEnvironmentType](media/gov-cloud-setting.png)

5. On the Welcome page, click **Next**. Follow the prompts to enter your SharePoint admin username and password to your GCC High or DoD account.
6. Enter your Windows credentials that will provide access to **all** the file shares that contain the content you want to migrate. Select **Install**.
7. Test agent access (optional) or click **Close**.
</br>

## Endpoints for Government

For the complete list of all required endpoints:  [Prerequisites & Endpoints for Migration Manager](mm-prerequisites.md)

|Government endpoints|For|
|:-----|:-----|
|https://\<spam\>\<spam\>*.blob.core.usgovcloudapi.\<spam\>\<spam\>net|Migration API Azure Government requirement|
|https://\<spam\>\<spam\>*.queue.core.usgovcloudapi.\<spam\>\<spam\>net|Migration API Azure Government requirement|
