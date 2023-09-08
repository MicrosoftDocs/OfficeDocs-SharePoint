---
title: "Basic authentication is being deprecated (SharePoint Server)"
ms.author: v-aljupudi
author: alekyaj
manager: serdars
ms.date: 09/08/2023
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
description: "Learn how to disable Basic authentication as it is being deprecated."
---

# Basic authentication is being deprecated (SharePoint Server)

[!INCLUDE[appliesto-xxx-2016-2019-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

**Rule Name:** Basic authentication is being deprecated

**Summary:** Basic authentication is currently enabled in one or more web applications within SharePoint Server. It's important to note that Basic authentication is being deprecated and will no longer be supported in SharePoint Server for all scenarios. For more information, see [What's deprecated or removed from SharePoint Server Subscription Edition](../what-s-new/what-s-deprecated-or-removed-from-SharePoint-Server-Subscription-Edition.md#basic-authentication).

Basic authentication doesn't provide confidentiality protection for the transmitted credentials. To better protect your SharePoint Server, it's highly recommended that you migrate web applications to a modern authentication mechanism (for example, Trusted Identity providers) as soon as possible.

**Cause:** One or more web applications in your SharePoint Server are using Basic authentication, which is being deprecated.

**Resolution: Disable Basic authentication**

Ensure that Basic authentication is disabled in both SharePoint Server and IIS settings:

Follow these steps to disable Basic authentication in SharePoint Server:

1. Verify that you're the farm admin.
2. Navigate to **Central Administration,** select **Application Management,**  and then select **Manage web applications**.
3. Select the web application you want to disable Basic authentication.
4. Click on the **Authentication Providers** link in the ribbon.
5. Choose the appropriate zone for the web application.
6. Uncheck the option **Basic authentication (password is sent in clear text)**.

Follow these steps to disable Basic authentication in IIS:

1. Verify that you're a member of the Administrators group on the server where you're configuring IIS.
2. On the Start menu, point to All Programs, select **Administrative Tools,** and then select **Internet Information Services (IIS) Manager** to start the IIS Management Console.
3. Expand Sites on the console tree, right-click the IIS Web site that corresponds to the Web application zone where you want to disable Basic authentication.
4. In the middle pane, double-click the **Authentication** icon.
5. In the Authentication pane, locate **Basic authentication** and select it.
6. In the Actions pane on the right-hand side, click **Disable** to disable Basic authentication.