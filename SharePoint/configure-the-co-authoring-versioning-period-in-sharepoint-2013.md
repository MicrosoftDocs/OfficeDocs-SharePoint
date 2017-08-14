---
title: Configure the co-authoring versioning period in SharePoint 2013
ms.prod: SHAREPOINT
ms.assetid: 59f3af85-89f9-43ba-b364-28a810cae42e
---


# Configure the co-authoring versioning period in SharePoint 2013
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013*  * **Topic Last Modified:** 2017-07-20* **Summary:**  Learn how to specify how often SharePoint Server 2013 stores a version of a document that is being edited.The CoauthoringVersionPeriod property specifies, in minutes, how often SharePoint stores a version of a document that is being edited. This article describes how to use Microsoft PowerShell to configure the CoauthoringVersionPeriod property. For more information about document library versioning, see  [Configure versioning for co-authoring in SharePoint 2013](html/configure-versioning-for-co-authoring-in-sharepoint-2013.md).
## Configure the co-authoring versioning period in SharePoint Server 2013

When versioning is turned on, SharePoint Server 2013 takes periodic snapshots of documents, saving them for later reference. This information can provide an edit trail that may be useful for seeing who changed a document, rolling back to an earlier version, or for compliance reasons. You can configure the CoauthoringVersionPeriod property by using the Microsoft PowerShell. If the value is set to 0, SharePoint Server 2013 captures every change made by a new user in a different version of the document. If the value is set to a very large number, SharePoint Server 2013 creates one version for the whole editing session. This latter behavior matches the behavior of files that are not co-authored and files that were created in earlier versions of SharePoint Server 2013 or SharePoint Foundation. **To configure the co-authoring versioning period by using Windows PowerShell (save as script and run script)**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2013 cmdlets.
    
    > [!NOTE:]
      
2. Paste the following code into a text editor, such as Notepad:
    
  ```
  
$siteurl ="<ServerName> "
$mysite=new-object Microsoft.SharePoint.SPSite($siteurl)
$mysite.WebApplication.WebService.CoauthoringVersionPeriod = <Time> 
$mysite.WebApplication.WebService.Update()
  ```

3. Specify the following parameters:
    
### Parameters to configure the co-authoring versioning period

Parameter Value  *ServerName*  <br/> Server name  <br/>  *Time*  <br/> Number in minutes  <br/> 4. Save the file and add the .ps1 extension, such as SuggestedNameOfFile.ps1.
    
    > [!NOTE:]
      
5. Start the SharePoint 2013 Management Shell as Administrator.
    
  
6. Change to the directory to which you saved the file.
    
  
7. At the PowerShell command prompt, type the following command:
    
  ```
  
./SuggestedFileName.ps1
  ```


# See also

#### 

 [Configure versioning for co-authoring in SharePoint 2013](html/configure-versioning-for-co-authoring-in-sharepoint-2013.md)
  
    
    
 [Overview of co-authoring in SharePoint 2013](html/overview-of-co-authoring-in-sharepoint-2013.md)
  
    
    

  
    
    

