---
title: "Migration Manager Government Cloud settings"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- SPMigration
- M365-collaboration
description: "Explanation of Government Cloud configuration settings when using Migration Manager." 
---
# Government Cloud

If your tenant resides in a government cloud, you may have additional steps to perform before using Migration Manager.

- [Configuration values](#configuration-values)
- [GCC High and DoD customers](#gcc-high-and-dod-customers)
- [Endpoints for Goverment](#endpoints-for-government)


## Configuration values

Configuration values for government cloud tenants are listed below.  The default setting is **0**.

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
</br>

## Endpoints for Government

For the complete list of all required endpoints:  [Prerequisites & Endpoints for Migration Manager](mm-prerequisites.md)

|Government endpoints|For|
|:-----|:-----|
|https://\<spam\>\<spam\>*.blob.core.usgovcloudapi.\<spam\>\<spam\>net|Migration API Azure Government requirement|
|https://\<spam\>\<spam\>*.queue.core.usgovcloudapi.\<spam\>\<spam\>net|Migration API Azure Government requirement|