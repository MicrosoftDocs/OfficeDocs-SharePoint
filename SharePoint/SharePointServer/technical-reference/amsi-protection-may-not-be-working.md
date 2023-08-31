---
title: "Antimalware Scan Interface (AMSI) protection may not be working (SharePoint Server)"
ms.author: v-aljupudi
author: alekyaj
manager: serdars
ms.date: 08/30/2023
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

SharePoint Server Subscription Edition Version 23H2 further improves Antimalware Scan Interface (AMSI) protection with the introduction of a SharePoint health analyzer rule. This health rule is designed to confirm that AMSI protection is functioning as expected and notify SharePoint farm administrators when it isn’t.

Once an hour, this health analyzer rule checks to see if AMSI integration is enabled on any web applications in the farm. If it's enabled, the health analyzer rule will send simulated web requests through AMSI on every server in the farm that hosts a web application. It checks to see if AMSI returns the expected status code showing that the request has been successfully scanned. If any of the simulated web requests don’t result in a successful status code (meaning AMSI didn’t successfully scan the simulated web request), then this health analyzer rule records a failure. The health analyzer rule report in Central Administration lists which servers in the farm experienced a failure and recommended steps to fix it.

If the health analyzer rule for AMSI protection is enabled, admins can expect to see:

:::image type="content" source="../media/health-analyzer-rule-definitions.png" alt-text="Screenshot that shows the Health Analyzer rule for AMSI.":::

**Rule Name:** Antimalware Scan Interface (AMSI) protection may not be working.

**Summary:** Antimalware Scan Interface (AMSI) protection is enabled for one or more web applications in this SharePoint farm. However, SharePoint didn't receive the expected response from the antimalware scan engine when verifying that this protection is working. Web applications may not be protected on the servers listed in the "Failing Servers" section of this health analyzer report.

**Cause:** AMSI running prerequisites aren't met, or the real-time protection service of the antimalware scan engine isn't enabled.

**Resolution: Ensure the prerequisites to activate AMSI**

For example, AMSI would only work on Windows Server 2016 or higher. For more information on other prerequisites, see [Prerequisites](/sharepoint/security-for-sharepoint-server/configure-amsi-integration#prerequisites) or you can [deactivate](/sharepoint/security-for-sharepoint-server/configure-amsi-integration#activatedeactivate-amsi-for-sharepoint-server) AMSI for SharePoint Server to turn off this health rule alarm.

**Resolution: Enable the real-time protection service**

If you're using Microsoft Defender as your antimalware scan engine, ensure that real-time protection is enabled on each server listed in the "Failing Servers" section of this health report.

1. Select the **Start** button.  

2. Select **Settings**.  

3. Select **Update & Security**.  

4. Select **Windows Security**.  

5. Select **Virus & protection settings**.  

6. Select **Manage settings**.  

7. Ensure Real-time protection is set to **On**.

> [!NOTE]
> The **Repair Automatically** button has no effect on this rule and does not implement any repair functionality.

You'll see the following timer job in the **Monitoring** section of Central administration site when the Health Analyzer rule runs.

:::image type="content" source="../media/health-analyzer-running.png" alt-text="Screenshot that shows Health analyzer running.":::

You can expect a similar health report as below, once the run is complete.

:::image type="content" source="../media/amsi-monitoring-screen.png" alt-text="Screenshot that displays the report for AMSI in Health Analyzer.":::