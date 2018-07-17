---
title: "One or more servers can't retrieve People Picker credentials (SharePoint Server 2019 Public Preview)"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 7/12/2018
ms.audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 
description: "Summary: Learn how to resolve the SharePoint Health Analyzer rule One or more servers can't retrieve People Picker credentials for SharePoint Server 2019 Public Preview."
---

# One or more server can't retrieve People Picker credentials (SharePoint Server 2019 Public Preview)

**Applies to:** SharePoint Server 2019 Public Preview

**Summary:** Learn how to resolve the SharePoint Health Analyzer rule "One or more servers can't retrieve People Picker credentials" for SharePoint Server 2019 Public Preview.

**Rule Name:** One or more servers can't retrieve People Picker credentials.

**Summary:** The People Picker is configured to use specific credentials when searching for users in certain forests or domains. There are one or more servers in this farm that can't retrieve these credentials. Without these credentials, the People Picker won't be able to search for users in those forests or domains from these servers.

**Cause:** The application credential key wasn't found on these servers or they don't have the same application credential key originally used to store the People Picker credentials. Servers must have an application credential key to store and retrieve People Picker credentials. The application credential key must be identical on each server.

**Resolution:** Use the **stsadm.exe -o setapppassword -password "&lt;application credential key&gt;"** command on each failing server to set the application credential key. If the current People Picker credentials were stored using a different application credential key, you must set the new application credential key on every server in the farm and then save the People Picker credentials again.