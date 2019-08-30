---
title: "Determine strategy for upgrade to SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/26/2017
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: cfc19211-c895-4992-8b46-5a5c73c015fe

description: "Understand how to minimize downtime and plan for special cases during an upgrade to SharePoint."
---

# Determine strategy for upgrade to SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
When you upgrade your environment to SharePoint 2013, you want to limit how much downtime that users experience. You might also have a special case that you must address during upgrade. This article describes how to minimize downtime and work with these special cases.
  
In addition to the information in this article, make sure that you read [Review supported editions and products for upgrading to SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc262747(v=office.14)) to understand exactly which upgrade situations are valid and lead to successful upgrades. 
  
## How to minimize downtime during upgrade
<a name="section1"> </a>

The following table lists the techniques that you can use during upgrade to reduce the time that users cannot access their content or to potentially increase upgrade performance.
  
- **Read-only databases** You can use read-only databases to continue to provide read-only access to content during the upgrade process. For this approach, you set the databases to read-only on the original farm while the upgrade is in progress on another farm. This method reduces perceived downtime for users. Also, if you encounter a problem with upgrade, you can restore the read-only farm to read-write and restore access to users while you rework your plans before you try upgrade again. 
    
- **Parallel database upgrades** You can attach and upgrade multiple databases at a time to speed up the upgrade process overall. The maximum number of parallel upgrades depends on your hardware. This results in faster overall upgrade times for your environment. However, you must monitor the progress and your servers to make sure that the performance is acceptable, and for large databases, parallel upgrades can be slower than single upgrades. 
    
    For more information about upgrade performance, see [Plan for performance during upgrade to SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc262891(v=office.14)) and [Use a trial upgrade to SharePoint 2013 to find potential issues](/previous-versions/office/sharepoint-server-2010/cc262155(v=office.14)).
    
The instructions for using these techniques are included in [Upgrade content databases from SharePoint 2010 to SharePoint 2013](upgrade-content-databases-from-sharepoint-2010-to-sharepoint-2013.md).
  
## Special cases
<a name="section2"> </a>

You might have other requirements or additional goals that you want to achieve when you perform an upgrade. The following table lists special cases and describes how to approach upgrade for each case.
  
|**Case**|**Upgrade approach**|
|:-----|:-----|
|Upgrading an environment that uses forms-based authentication?  <br/> |Additional steps are required to upgrade when you are using forms-based authentication. For more information, see [Configure forms-based authentication for a claims-based web application in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee806890(v=office.14)).  <br/> |
|Upgrading very large databases?  <br/> |In general, very large databases — especially databases that have a large number or large size of document versions inside them — take longer to upgrade than smaller databases. However, the complexity of the data determines how long it takes to upgrade, not the size of the database itself. If the upgrade process times out, it is usually because of connection issues. For more information about how long upgrade might take for your environment, see [Plan for performance during upgrade to SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc262891(v=office.14)).  <br/> |
|Upgrading from the server products in the Office 2007 release?  <br/> |Use a database attach upgrade method to upgrade to SharePoint 2010 Products, and then upgrade to SharePoint 2013.  <br/> |
|Upgrading from SharePoint Foundation 2010 to SharePoint 2013?  <br/> |Attach and upgrade the content databases from SharePoint Foundation 2010 to SharePoint 2013.  <br/> |
|Changing languages?  <br/> | You have two choices, depending on whether a single site or your whole environment is changing languages:  <br/>  To change the multiple user interface (MUI) language for a specific site, upgrade in the same language, and then install the new language pack and change to that language.  <br/> > [!CAUTION]>  You must have the appropriate language packs installed to upgrade any sites based on a localized site definition. If you do not have the new language pack, the sites will not be available. Wait for the new language packs to be released before you try to upgrade those sites.            To change the installation language for your environment, set up your new environment in the new language, and then attach and upgrade your databases in the new language.  <br/> |
   
## See also
<a name="section2"> </a>

#### Other Resources

[Plan for performance during upgrade to SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc262891(v=office.14))
  
[Review supported editions and products for upgrading to SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc262747(v=office.14))
  
[Use a trial upgrade to SharePoint 2013 to find potential issues](/previous-versions/office/sharepoint-server-2010/cc262155(v=office.14))
  
[Overview of the upgrade process from SharePoint 2010 to SharePoint 2013](overview-of-the-upgrade-process-from-sharepoint-2010-to-sharepoint-2013.md)

