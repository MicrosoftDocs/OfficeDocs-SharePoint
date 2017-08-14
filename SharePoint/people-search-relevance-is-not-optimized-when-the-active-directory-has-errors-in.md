---
title: People Search relevance is not optimized when the Active Directory has errors in the manager reporting structure (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 982d3ab2-d1a6-4625-b4c6-e12a1f4532d5
---


# People Search relevance is not optimized when the Active Directory has errors in the manager reporting structure (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "People Search relevance is not optimized when the Active Directory has errors in the manager reporting structure", for SharePoint Server 2016. **Rule Name:**   People Search relevance is not optimized when the Active Directory has errors in the manager reporting structure. **Summary:**   In Active Directory Domain Services (AD DS), only company leaders should have the **Manager** property set to NULL. If the **Manager** property is set to NULL for other users, people search relevance is reduced. To optimize people search relevance, explicitly specify company leaders. People search can then use this information to improve relevance. **Cause:**   Company leaders have not been explicitly specified. **Resolution: Specify company leaders.**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the Microsoft PowerShell cmdlets.
    
  
  - Add memberships that are required beyond the minimums above.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
    For Windows Server 2012 R2, on the **Start** screen, click **SharePoint 2016 Management Shell**.
    
    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows](http://go.microsoft.com/fwlink/?LinkID=715712&amp;clcid=0x409).
    
  
3. At the PowerShell command prompt, type the following command:
    
    
    


  ```
  
$upaProxy = Get-SPServiceApplicationProxy <AppID>
  ```


    where  *<AppID>*  is the GUID of the User Profile service application proxy. For more information, see **Get-SPProfileLeader**.
    
  
4. Type the following command:
    
    
    


  ```
  Add-SPProfileLeader -ProfileServiceApplicationProxy $upaProxy -Name "<Domain\\UserName> "
  ```


    where  *<Domain\\UserName>*  is the user account that you want to add as a leader — for example, Contoso\\Joe.Healy. For more information, see **Add-SPProfileLeader**.
    
  
5. You are prompted to confirm. Type **Y** to confirm.
    
  
6. Run a full crawl on the content source that contains the start address (URL) of the User Profile application.
    
  
Repeat the commands to add more user accounts as company leaders.
# See also

#### 

 **Add-SPProfileLeader**
  
    
    

  
    
    

