---
title: "Validate the My Site Host and individual My Sites are on a dedicated Web application and separate URL domain (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/30/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: b5f098eb-219a-4483-adee-75d7b6b3089a
description: "Learn how to resolve the SharePoint Health Analyzer rule: Validate the My Site Host and individual My Sites are on a dedicated Web application and separate URL domain."
---

# Validate the My Site Host and individual My Sites are on a dedicated Web application and separate URL domain (SharePoint Server)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
>[!IMPORTANT]
>This health analyzer rule only applies to SharePoint 2010 as this was removed in [KB4011601](https://support.microsoft.com/help/4011601) for SharePoint Server 2013 and [KB4011576](https://support.microsoft.com/help/4011576) for SharePoint Server 2016.

 **Rule Name:** Validate the My Site Host and individual My Sites are on a dedicated Web application and separate URL domain. 
  
 **Summary:** For performance and manageability reasons, we recommend that the My Site host and individual My Sites be deployed in a dedicated Web application. The owner of each individual My Site is the site collection administrator for that My Site. Having a dedicated Web application for the My Site host and individual My Sites reduces the security risk that a My Site owner can introduce same-domain scripting attacks on other sites that are hosted on the same Web application. 
  
 **Cause:** The My Site host and individual My Sites are deployed in the same Web application as the root site collection. If the User Profile Service was configured by using the Farm Configuration Wizard, this is how My Sites are set up. 
  
 **Resolution: Set up a dedicated Web application**
  
- We recommend that you have a separate, dedicated Web application to host the My Site host and individual My Sites.
    
    For more information, see [Create a web application in SharePoint Server](/previous-versions/office/sharepoint-server-2010/cc261875(v=office.14)).
    
## See also
<a name="server"> </a>

#### Concepts

[Configure My Sites in SharePoint Server](../install/configure-my-sites.md)

