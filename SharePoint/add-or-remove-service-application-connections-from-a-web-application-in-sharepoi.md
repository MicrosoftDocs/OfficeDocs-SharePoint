---
title: Add or remove service application connections from a web application in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 6a7cfa97-f4b1-4b3f-9b98-303ee1e836c2
---


# Add or remove service application connections from a web application in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** Search Server 2013, SharePoint Foundation 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-25* **Summary:** Learn how to add or remove service application connections to a service application connection group in SharePoint Server 2016 and SharePoint 2013.When you create a service application in SharePoint Server, a  *service application connection*  is created. A service application connection is also referred to as an *application proxy*  . A service application connection associates the service application to web applications via membership in a *service application connection group*  (also referred to as *application proxy group*  ).
> [!IMPORTANT:]

  
    
    

By default, a new service application connection is added to the farm’s Default group of service application connections when you create the service application by using Central Administration. You can override this default membership. If a new service application is created by using Microsoft PowerShell instead of by using Central Administration, the new service application does not automatically become a member of the Default service application connections group unless the **default** parameter is supplied.
> [!NOTE:]

  
    
    

By default, all web applications are associated with the farm’s Default group of service application connections, although you can change this setting. You can also create one custom connection group for each web application in the farm. You can change the service applications with which a web application is associated at any time, and you can change the service applications that are included in the Default service application connection group.
## Editing a service connection group
<a name="Section2"> </a>

You can add or remove service application connections to a service application connection group by using Central Administration or by using PowerShell cmdlets. **To edit a service connection group by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
  
2. Start Central Administration.
    
  
3. On the Central Administration Home page, click **Application Management**.
    
  
4. On the Application Management page, in the **Service Applications** section, click **Configure service application associations**.
    
  
5. On the Service Application Associations page, select **Web Applications** from the **View** drop-down menu.
    
  
6. In the list of Web applications, in the **Application Proxy Group** column, click the name of the service application connection group that you want to change.
    
  
7. To add a service connection to the group, select the check box that is next to the service application that you want to add to the connection group. To remove a service application connection from the connection group, clear the check box next to the service application that you want to remove from the connection group. When you have made the changes that you want, click **OK**.
    
    > [!NOTE:]
      
 **To add a service application connection to a service application connection group by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Add-SPServiceApplicationProxyGroupMember -Identity < the service application proxy group >  -Member <members to add to the service application proxy group>
  ```


    For more information, see **Add-SPServiceApplicationProxyGroupMember**.
    
  
 **To remove a service application connection from a service application connection group by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - Add memberships that are required beyond the minimums above.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Remove-SPServiceApplicationProxyGroupMember -Identity <SPServiceApplicationProxyGroupPipeBind>  -Member <SPServiceApplicationProxyPipeBind >
  ```


    For more information, see **Remove-SPServiceApplicationProxyGroupMember**.
    
  

# See also

#### 

 [Share service applications across farms in SharePoint Server](html/share-service-applications-across-farms-in-sharepoint-server.md)
  
    
    

  
    
    

