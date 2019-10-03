---
title: "Configure self-service site creation in SharePoint Server 2019 home page"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
description: "Learn how to configure self-service site creation in different web applications and remote server farms in SharePoint Server."
---

# Configure self-service site creation in SharePoint Server 2019

[!INCLUDE[appliesto-xxx-xxx-2019-xxx-md](../includes/appliesto-xxx-xxx-2019-xxx-md.md)]

The self-service site creation experience in SharePoint supports creating new sites in a different web application, regardless of whether the web application is hosted on the local farm or a remote farm. This gives greater flexibility and control in managing SharePoint farms.

Self-service site creation updates for SharePoint Server 2019 offers the following:

- The ability to create sites in other web applications and in web applications hosted in remote SharePoint farms.
 
- By default the SharePoint home page and team sites only use modern site templates when self-service site creation is enabled. If you want users to only  create classic sites you can add the (/_layouts/15/scsignup.aspx) page for users to use classic site templates.

- The ability for farm administrators to hide the Create Site link from the SharePoint home page, so users have to go through their IT organization to create new sites.
 
## Configure self-service site creation in the SharePoint Central Administration website

SharePoint Farm Administrators control self-service site creation in different web applications on local or remote farms in Central Administration. This is controlled in the **When users select the Create site command, create:** section on the **Self-service Site Creation Management** page in Central Administration.

### To configure self service site creation

1. Open Central Administration and under Application Management, click **Manage web applications**.

2. In the Manage web applications page, click the web application you want and then click **Self-Service Site Creation** in the banner.

3. In the Self-Service Site Creation Management page, you can configure this feature in either Site Collections or Sites.

4. To create sites in the same web application, select **This web application**.

5. To create sites in a different web application on the local farm, select **The following web application** and then select the web application from the drop-down field. Ensure self service site creation is enabled in the target web application.

> [!NOTE]
> When you enable self-service site creation, a link to create a site is added to the SharePoint home page.

> [!NOTE]
> When configuring self-service site creation on remote farms, both farms must be running SharePoint Server 2019. We don’t support self-service site creation in remote farms if the remote farms are running an older version of SharePoint.

### To create sites in a different web application or a remote farm

1. In the local farm hosting the SharePoint home page, use the **Map to External Resource** control in Alternate Access Mappings (AAM) to provide the URL of the web application where you want to create sites.

2. In the local farm that hosts the SharePoint home page, on the Self-service Site Collection Management page for the web application that hosts the SharePoint home page, select **The following web application**, and then select the remote web application from the drop-down field.

3. In the remote farm, use the **Map to External Resource** control in AAM to provide the URL of the web application that hosts the SharePoint home page.

4. In the remote farm, on the Self-service Site Collection Management page for the web application where you want to create the sites, ensure self-service site creation is enabled.

  > [!NOTE]
  > For cross-web application scenarios, you must create the AAM on both web applications to ensure the form reads from the correct named path.

## Self-service site creation in the SharePoint home page supports AAM zones

The self-service site creation experience in the SharePoint home page supports non-Default Alternate Access Mapping zones. This applies to sites created in the same web application, sites created in a different web application on the local farm, and sites created in a different web application on a remote farm. When creating sites in a different web application on a remote farm, make sure that an external resource has been created in AAM on both the local farm and the remote farm.

SharePoint will treat the external resource as an external web application. The external resource on the local farm should be fully populated with the URLs and zones of the web application on the remote farm. And conversely, the external resource on the remote farm should be fully populated with the URLs and zones of the web application on the local farm. Be sure that the zones of the local web application and the remote web application are synchronized.

For more information, see [Plan alternate access mappings for SharePoint Server](/SharePoint/administration/plan-alternate-access-mappings) and [Configure alternate access mappings for SharePoint Server](/SharePoint/administration/configure-alternate-access-mappings).

## See also

[Plan self-service site creation in SharePoint Server](/SharePoint/sites/plan-self-service-site-creation)

