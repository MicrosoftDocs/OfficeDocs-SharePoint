---
title: "The Application Discovery and Load Balancer Service is not running in this farm (SharePoint Server)"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 12/5/2017
ms.audience: ITPro
ms.topic: troubleshooting
ms.prod: office-online-server
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 70d6f3af-2ad4-497d-a449-d75bacfd8aea
description: "Summary: Learn how to resolve the SharePoint Health Analyzer ruleThe Application Discovery and Load Balancer Service is not running in this farmfor SharePoint Server 2016 and SharePoint 2013."
---

# The Application Discovery and Load Balancer Service is not running in this farm (SharePoint Server)

 **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The Application Discovery and Load Balancer Service is not running in this farm" for SharePoint Server 2016 and SharePoint 2013. 
  
 **Rule Name:** The Application Discovery and Load Balancer Service is not running in this farm. 
  
 **Summary:** The Application Discovery and Load Balancer service provides information about the topology of the farm to users who are using services offered by the farm. Users can use this information to perform load balancing. The Application Discovery and Load Balancer Service should be running on at least one server in the farm. 
  
 **Cause:** The Application Discovery and Load Balancer service is stopped. 
  
 **Resolution: Start the Application Discovery and Load Balancer service on at least one server in the farm.**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the Microsoft PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](http://technet.microsoft.com/library/2ddfad84-7ca8-409e-878b-d09cb35ed4aa.aspx). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command: 
  
 `Get-SPServiceInstance -ALL`
    
    For more information, see [Get-SPServiceInstance](http://technet.microsoft.com/library/14bbe36e-c73c-428a-955c-2c1e4d8a1d83.aspx).
    
4. Find the GUID of the Application Discovery and Load Balancer service.
    
5. Type the following command: 
  
 `Start-SPServiceInstance [-Identity]`
    
    Where  _[-Identity]_ is the GUID for the Application Discovery and Load Balancer service. For more information, see [Start-SPServiceInstance](http://technet.microsoft.com/library/fcb4a4f8-a95f-468e-918b-d9a2d736cd2d.aspx).
    

