---
title: InfoPath form library forms cannot be filled out in a Web browser (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 7ebd1422-4f3d-44b9-8df6-75274c65b7e5
---


# InfoPath form library forms cannot be filled out in a Web browser (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "InfoPath form library forms cannot be filled out in a Web browser", in SharePoint Server 2016. **Rule Name:**    InfoPath form library forms cannot be filled out in a Web browser **Summary:**    InfoPath Forms Services users can publish browser-enabled form templates to a SharePoint Server 2016 form library but cannot open the forms in a Web browser.
> [!NOTE:]

  
    
    

 **Cause:**    One or more of the following might be causing this:
- The **Render form templates that are browser-enabled by users** check box in the SharePoint Central Administration website is cleared.
    
  
- The following Windows PowerShell command has been run: Set-SPInfoPathFormsService -AllowUserFormBrowserRendering $false.
    
  
 **Resolution:   Enable browser rendering of user forms by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group. 
    
  
2. Start SharePoint 2016 Central Administration.
    
    For Windows Server 2008 R2, on the **Start** screen, click **SharePoint 2016 Central Administration**.
    
    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows](http://go.microsoft.com/fwlink/?LinkID=715712&amp;clcid=0x409).
    
  
3. In Central Administration, click **General Application Settings**.
    
  
4. On the General Application Settings page, in the **InfoPath Forms Services** section, click **Configure InfoPath Forms Services**.
    
  
5. On the Configure InfoPath Forms Services page, in the **User Browser-enabled Form Templates** section, select the **Render form templates that are browser-enabled by users** check box.
    
  
6. Click **OK** at the bottom of the page.
    
  
 **Resolution:   Enable browser rendering of user forms by using Microsoft PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 Products cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
    For Windows Server 2012 R2, on the **Start** screen, click **SharePoint 2016 Management Shell**.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Set-SPInfoPathFormsService -AllowUserFormBrowserRendering $true
  ```

For more information, see Set-SPInfoPathFormsService.
