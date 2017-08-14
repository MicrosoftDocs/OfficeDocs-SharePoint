---
title: Manage the lock status for site collections in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: c5d39627-dfa6-4122-8571-a38bdd3ab4d9
---


# Manage the lock status for site collections in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-26* **Summary: ** How to manage lock status for a site collection in SharePoint Server 2016 and SharePoint 2013.You use the lock status of a site collection to control the actions allowed on a site collection.The following table describes the locking options that are available in SharePoint Server.
### 

Option Description **Not locked** <br/> Unlocks the site collection and makes it available to users.  <br/> **Adding content prevented** <br/> Prevents users from adding new content to the site collection. Updates and deletions are still allowed.  <br/> **Read-only** (blocks additions, updates, and deletions) <br/> Prevents users from adding, updating, or deleting content. When a user attempts to add, update, or delete content, the user receives an error message that informs the user that access is denied and that the user does not have permission to perform the action or access the resource. A read-only lock can be either site collection administrator controlled if the site collection is archived or farm administrator controlled  <br/> **No access** <br/> Prevents users from accessing the site collection and its content. Users who attempt to access the site receive an error page that informs the user that the website declined to show the webpage.  <br/> 
> [!NOTE:]

  
    
    


> [!IMPORTANT:]

  
    
    


## Manage the lock status for a site collection by using Central Administration

Use this procedure to lock or unlock a site collection by using the SharePoint Central Administration website. **To manage the lock status for a site collection by using Central Administration**
1. Verify that you have the following administrative credentials. 
    
  - You must be a member of the Site Collection Administrators group for the site collection.
    
  
2. Open Central Administration. On the **Application Management** page, in the **Site Collections** section, click **Configure quotas and locks**.
    
  
3. If the site collection you want is not already selected, in the **Site Collection** section, on the **Site Collection** menu, click **Change Site Collection**. Use the **Select Site Collection** page to select a site collection.
    
  
4. On the **Site Collection Quotas and Locks** page, in the **Site Lock Information** section, select one of the following options:
    
  - **Not locked** to unlock the site collection and make it available to users.
    
  
  - **Adding content prevented** to prevent users from adding new content to the site collection. Updates and deletions are still allowed.
    
  
  - **Read-only (blocks additions, updates, and deletions)** to prevent users from adding, updating, or deleting content. Choose whether you want this to be farm administrator controlled or site collection administrator controlled.
    
  
  - **No access** to prevent users from accessing the site collection and its content. Users who attempt to access the site receive an error message.
    
  
5. If you select **Adding content prevented**, **Read-only (blocks additions, updates, and deletions)**, or **No access**, type a reason for the lock in the **Additional lock information** box.
    
  
6. Click **OK** when you are done.
    
  

## Manage the lock status for a site collection by using Windows PowerShell

Use this procedure to lock or unlock a site collection by using Microsoft PowerShell. **To manage the lock status for a site collection by using Windows PowerShell**
1. Verify that you meet the following minimum requirements: See **Add-SPShellAdmin**.
    
  
2. Open the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command, and then press **ENTER**:
    
  ```
  
Set-SPSite -Identity "<SiteCollection> " -LockState "<State> "
  ```


    Where:
    
  -  *<SiteCollection>*  is the URL of the site collection that you want to lock or unlock.
    
  
  -  *<State>*  is one of the following values:
    
  - **Unlock** to unlock the site collection and make it available to users.
    
  
  - **NoAdditions** to prevent users from adding new content to the site collection. Updates and deletions are still allowed.
    
  
  - **ReadOnly** to prevent users from adding, updating, or deleting content.
    
  
  - **NoAccess** to prevent users from accessing the site collection and its content. Users who attempt to access the site receive an error message.
    
  
 For more information about how to use the Set-SPSite cmdlet, see Set-SPSitehttps://technet.microsoft.com/en-us/library/ff607958(v=office.16).aspx.
# See also

#### 

 [Create, edit, and delete quota templates in SharePoint Server](html/create-edit-and-delete-quota-templates-in-sharepoint-server.md)
  
    
    

#### 

 [Manage site collections and global settings in the SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=845346)
  
    
    

  
    
    

