---
title: "Required URLs and ports for OneDrive consumer"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 04/3/2018
audience: Admin
f1.keywords:
- NOCSH
ms.topic: reference
ms.service: one-drive
localization_priority: Normal
search.appverid:
- ODC160
- MET150
ms.assetid: ce15d2cc-52ef-42cd-b738-d9c6f9b03f3a
description: "Learn the FQDNs and ports to include in your allow lists to let users use the consumer version of OneDrive."
---

# Required URLs and ports for OneDrive

 This reference article lists every endpoints used by the consumer version of OneDrive. If your organization restricts computers on your network from connecting to the Internet, this article lists the Fully Qualified Domain Names (FQDNs) and ports that you should include in your outbound allow lists to ensure your computers can successfully use the consumer version of OneDrive.
  
> [!IMPORTANT]
> Filtering internet traffic requires advanced networking knowledge and isn't suitable for all customers.
  
 **If you are looking for a listing of endpoints used by OneDrive in Office 365, see [Office 365 URLs and IP address ranges](/office365/enterprise/urls-and-ip-address-ranges).**
  
## Supported hosts and ports for OneDrive

To use OneDrive, the following endpoints need to be accessible to client computers.
  
|**Row**|**Destination host**|**Destination Port**|
|:-----|:-----|:-----|
|1  <br/> |onedrive.com  <br/> \*.onedrive.com  <br/> onedrive.live.com  <br/> login.live.com  <br/> spoprod-a.akamaihd.net  <br/> \*.mesh.com  <br/> p.sfx.ms  <br/> \*.microsoft.com  <br/> fabric.io  <br/> \*.crashlytics.com  <br/> vortex.data.microsoft.com  <br/> https://posarprodcssservice.accesscontrol.windows.net  <br/> redemptionservices.accesscontrol.windows.net  <br/> token.cp.microsoft.com/  <br/> tokensit.cp.microsoft-tst.com/  <br/> \*.office.com  <br/> \*.officeapps.live.com  <br/> \*.aria.microsoft.com  <br/> \*.mobileengagement.windows.net  <br/> \*.branch.io  <br/> \*.adjust.com  <br/> \*.servicebus.windows.net  <br/> vas.samsungapps.com  <br/> odc.officeapps.live.com  <br/> login.windows.net  <br/> login.microsoftonline.com  <br/> |TCP 80, TCP 443  <br/> |
|2  <br/> |\*.files.1drv.com  <br/> \*.onedrive.live.com  <br/> \*.\*.onedrive.live.com  <br/> storage.live.com  <br/> \*.storage.live.com  <br/> \*.\*.storage.live.com  <br/> \*.groups.office.live.com  <br/> \*.groups.photos.live.com  <br/> \*.groups.skydrive.live.com  <br/> favorites.live.com  <br/> oauth.live.com  <br/> photos.live.com  <br/> skydrive.live.com  <br/> api.live.net  <br/> apis.live.net  <br/> docs.live.net  <br/> \*.docs.live.net  <br/> policies.live.net  <br/> \*.policies.live.net  <br/> settings.live.net  <br/> \*.settings.live.net  <br/> skyapi.live.net  <br/> snapi.live.net  <br/> \*.livefilestore.com  <br/> \*.\*.livefilestore.com  <br/> storage.msn.com  <br/> \*.storage.msn.com  <br/> \*.\*.storage.msn.com  <br/> |TCP 80, TCP 443  <br/> |
