---
title: "Connect to Box with Migration Manager"
ms.date:  01/21/2021
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: medium
mscollection:
- m365solution-migratefileshares
- m365solution-migratetom365
- m365solution-scenario
- SPMigration
- M365-collaboration
ms.custom: admindeeplinkSPO
search.appverid: MET150
description: "Steps to connect to Box when using Migration Manager in the SharePoint Admin center."
---

# Step 1:  Connect your Box account to Microsoft 365



Sign in to your Box account and add the Microsoft 365 migration app to your Box account custom apps. 

1. From the <a href="https://go.microsoft.com/fwlink/?linkid=2185075" target="_blank">Migration center</a> in the SharePoint admin center, under **Box**, select **Get started**.
2. Select **Connect to Box**. 
3. Select **Authorize Mover**. Sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization. Select **Next**.
4. Select **Go to Enterprise applications**. This step takes you to Azure.
5. Select the **Office 365 migration app**.
6. On the left-hand panel under *Security*, select **Permissions**.
7. Select **Grant admin consent** for your account. You may be prompted for your credentials again. Return to the Migration Manager wizard screen.  Select **Next**.
8. Select **Authenticate account**. 
9. Sign in to grant access to Box. Select **Authorize** and then **Grant access to Box**.
10. You're now connected to Box. Select **Finish** to close the window.

>[!Important]
>For security reasons, you have 10 minutes to complete the steps to connect to Box. After 10 minutes of inactivity, the session will expire.

[**Step 2: Scan and assess**](mm-box-step2-scan-assess.md)


>[!NOTE]
>Migration Manager Box isn't available for users of Office 365 operated by 21Vianet in China.
>
> This feature is also not supported for users of the Government Cloud, including GCC, Consumer, GCC High, or DoD.