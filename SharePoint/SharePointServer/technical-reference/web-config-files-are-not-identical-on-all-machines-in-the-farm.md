---
title: "Web.config files are not identical on all machines in the farm (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/31/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: c2f1d2a8-dc6a-471c-b373-be420b460306
description: "Learn how to resolve the SharePoint Health Analyzer rule: Web.config files are not identical on all machines in the farm, for SharePoint Server."
---

# Web.config files are not identical on all machines in the farm (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
 **Rule Name:** Web.config files are not identical on all machines in the farm. 
  
 **Summary:** If you have multiple front-end Web servers in the farm and have made manual changes to the Web.config files, you will experience a problem where a front-end Web server cannot read session state that was saved by another server in the farm. 
  
 **Cause:** The Web.config files on the front-end Web servers in the farm are not identical. 
  
 **Resolution: Ensure that the Web.config files are identical on all front-end Web servers in the farm.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. Identify the server on which this event occurs. On the SharePoint Central Administration website, in the **Monitoring** section, click **Review problems and solutions**, and then find the name of the server in the **Failing Servers** column. If there are multiple failing servers in a server farm, you must repeat the following steps on each failing server. 
    
3. Verify that the user account that is performing the following steps is a member of the Administrators group on the local computer that you identified in the previous step.
    
4. Log on to the server on which this event occurs.
    
5. Typically the Web.config file is stored at  `C:\inetpub\wwwroot\wss\VirtualDirectories\Port_Number`. Note the modified date of the Web.config file.
    
6. Repeat the previous steps on other failing servers.
    
7. Compare these Web.config files and decide which one is correct. To view the content of the Web.config file, do the following:
    
1. In **Server Manager**, click **Tools**, and then click **Internet Information Services (IIS) Manager**.
    
2. In the Internet Information Services management console, in the **Connections** pane, expand the tree view of the server name, expand **Sites**, and then click the site for which you want to view the settings of the Web.config file.
    
3. On the site Home page, switch to the Features View, and then in the **Management** section, double-click **Configuration Editor**.
    
4. In the **Section** list, select a section to view the settings of the Web.config file. 
    
8. Delete the incorrect Web.config file on each failing server, and then copy and paste the correct Web.config file.
    
By default, the **Repair Automatically** option is enabled for this rule. You can restore the default setting for this rule by doing the following: 
  
 **Restore default setting**
  
1. In Central Administration, click **Monitoring**.
    
2. On the Monitoring page, in the **Health Analyzer** section, click **Review rule definitions**.
    
3. On the Health Analyzer Rule Definitions - All Rules page, in the **Category: Configuration** section, click the name of the rule. 
    
4. In the **Health Analyzer Rule Definitions** dialog box, click **Edit Item**.
    
5. Select the **Repair Automatically** check box, and then click **Save**.
    

