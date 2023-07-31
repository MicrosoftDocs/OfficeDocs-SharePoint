---
title: "Antimalware Scan Interface (AMSI) protection may not be working (SharePoint Server)"
ms.author: v-bshilpa
author: Benny-54
manager: serdars
ms.date: 7/31/2023
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
description: "Learn what to do, if AMSI protection isn't working."
---

# Antimalware Scan Interface (AMSI) protection may not be working (SharePoint Server)

[!INCLUDE[appliesto-xxx-2016-2019-SUB-xxx-md](../includes/appliesto-xxx-2016-2019-SUB-xxx-md.md)]

**Rule Name:** Antimalware Scan Interface (AMSI) protection may not be working.

**Summary:** Antimalware Scan Interface (AMSI) protection is enabled for one or more web applications in the SharePoint farm. However, SharePoint didn't receive the expected response from the antimalware scan engine when verifying that this protection is working. Web applications may not be protected on the servers listed in the Failing Servers section of this health analyzer report.

**Cause:** AMSI running prerequisites aren't met, or the real-time protection service of the antimalware scan engine isn't enabled.

**Resolution: Ensure the prerequisites to activate AMSI**

For example, AMSI would only work on Windows Server 2016 or higher. For more information on other prerequisites, see [Prerequisites](/sharepoint/security-for-sharepoint-server/configure-amsi-integration#prerequisites).

**Resolution: Enable the real-time protection service**

Ensure that real-time protection is enabled on each server listed in the Failing Servers section of this health report, if you're using Microsoft Defender as your antimalware scan engine.

 1. Select the Start button.
    
 2. Select Settings.
  
 3. Select Update & Security.
  
 4. Select Windows Security.
  
 5. Select Virus & protection settings.
 
 6. Select Manage settings.
  
 7. Ensure Real-time protection is set to On.

