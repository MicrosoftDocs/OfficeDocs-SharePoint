---
title: Configure the maximum number of co-authoring authors in SharePoint 2013
ms.prod: SHAREPOINT
ms.assetid: dca8b241-85f9-486c-97eb-ed9ef23622b8
---


# Configure the maximum number of co-authoring authors in SharePoint 2013
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013*  * **Topic Last Modified:** 2017-07-20* **Summary:**  Learn how to limit the number of users who can co-author a Word document or PowerPoint presentation at the same time.The CoauthoringMaxAuthors property lets you specify the maximum number of users who can co-author a Word document or PowerPoint presentation at the same time in SharePoint Server 2013. This article describes how to configure the CoauthoringMaxAuthors property by using Microsoft PowerShell.
## Configure the maximum number of co-authoring authors for SharePoint 2013

You can limit the number of users who can co-author a document at the same time by setting the CoauthoringMaxAuthors property. This property only applies to Word 2010, Word 2013, Word Web App, PowerPoint 2010, PowerPoint 2013 and PowerPoint Web App documents. There is no upper limit to the number of users who can co-author OneNote notebooks. **To configure the maximum number of co-authoring users for Word documents and PowerPoint presentations by using Windows PowerShell (save as script and run script)**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2013 cmdlets.
    
    > [!NOTE:]
      
2. Paste the following code into a text editor, such as Notepad:
    
  ```
  
$siteurl = "<ServerName> "
$mysite=new-object Microsoft.SharePoint.SPSite($siteurl)
$mysite.WebApplication.WebService.CoauthoringMaxAuthors = <MaxAuthors> 
$mysite.WebApplication.WebService.Update()
  ```

3. Replace:
    
  -  *<ServerName>*  with the name of the server.
    
  
  -  *<MaxAuthors>*  with the maximum number of authors to allow.
    
  
4. Save the file and add the .ps1 extension, such as SuggestedNameOfFile.ps1.
    
    > [!NOTE:]
      
5. Start the SharePoint 2013 Management Shell as Administrator.
    
    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](https://technet.microsoft.com/en-us/library/hh831491.aspx).
    
  
6. Change to the directory to which you saved the file.
    
  
7. At the PowerShell command prompt, type the following command: ./SuggestedFileName.ps1
    
  

# See also

#### 

 [Overview of co-authoring in SharePoint 2013](html/overview-of-co-authoring-in-sharepoint-2013.md)
  
    
    

  
    
    

