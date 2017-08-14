---
title: Configure object cache user accounts in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: cd646bb3-28c6-4040-866c-7d7936837ade
---


# Configure object cache user accounts in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-19* **Summary: ** Learn how to configure the Portal Super User and Portal Super Reader accounts that are used by the object cache in SharePoint Server 2016 and SharePoint Server 2013.The object cache stores properties about items in SharePoint Server. Items in this cache are used by the publishing feature when it renders web pages. The goals of the object cache are to reduce the load on the computer on which SQL Server is running, and to improve request latency and throughput. The object cache makes its queries as one of two out-of-box user accounts: the Portal Super User and the Portal Super Reader. These user accounts must be properly configured to ensure that the object cache works correctly. The Portal Super User account must be an account that has Full Control access to the web application. The Portal Super Reader account must be an account that has Full Read access to the web application.
> [!IMPORTANT:]

  
    
    

This article explains why these object cache user accounts must to be configured and describes how to configure the accounts. For information about the object cache, see  [Cache settings operations in SharePoint Server](html/cache-settings-operations-in-sharepoint-server.md).In SharePoint Server, querying for items is linked with the user account that makes the query. Various parts of the publishing feature make queries for which the results are cached in the object cache. These results are cached based on the user making the query. To optimize the cache hit rate and memory requirements, the queries must be based on whether a user can see draft items. When a publishing control requests the object cache to make a query to get data for the control, the cache makes the query, not as the user making the request, but instead it makes the query twice: once as the Portal Super User account and once as the Portal Super Reader account. The results of these two queries are stored in the object cache. The results for the Portal Super User account include draft items, and the results for the Portal Super Reader account include only published items. The object cache then checks the access control lists (ACLs) for the user who initiated the request and returns the appropriate results to that user based on whether that user can see draft items. By adding the Portal Super User and Portal Super Reader accounts to the web application, the cache must store results for only two users. This increases the number of results that are returned for a query and decreases the amount of memory that is needed to store the cache.By default, the Portal Super User account is the site’s System Account, and the Portal Super Reader account is NT Authority\\Local Service. There are two main issues with using the out-of-box accounts.
1. The first issue is that some items get checked out to System Account, so when a query that includes these items is made, the checked out version of the item is returned instead of the latest published version. This is a problem because it is not what a user would expect to have returned, so the cache has to make a second query to fetch the correct version of the file. This negatively affects server performance for every request that includes these items. The same problem would occur for any user who has items checked out, if that user’s account was set to be the Portal Super User account. This is why the accounts configured to be the Portal Super User and the Portal Super Reader should not be user accounts that are used to log into the site. This ensures that the user does not inadvertently check items out and cause problems with performance.
    
  
2. The default Portal Super Reader account is NT Authority\\Local Service, which is not correctly resolved in a claims authentication application. As a result, if the Portal Super Reader account is not explicitly configured for a claims authentication application, browsing to site collections under this application will result in an "Access Denied" error, even for the site administrator. This error will occur on any site that uses any feature that explicitly uses the object cache, such as the SharePoint Server Publishing Infrastructure, metadata navigation, the Content Query Web Part, or navigation.
    
  

## Configure object cache user accounts by using Central Administration and Windows PowerShell
<a name="section2"> </a>

You can configure the user accounts for the object cache by the the SharePoint Central Administration website and Microsoft PowerShell. You must first create the accounts in Central Administration and then add the accounts to the web application by using PowerShell. You must add the user accounts to each web application.
> [!CAUTION:]

  
    
    

 **To create the user accounts by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group on the computer that is running the SharePoint Central Administration website.
    
  
2. In Central Administration, in the **Application Management** section, click **Manage web applications**, and then click the name of the web application that you want to configure.
    
  
3. On the **Web Applications** tab, in the **Policy** group, click **User Policy**.
    
  
4. In the Policy for Web Application window, click **Add Users**.
    
  
5. From the **Zones** list, select **All zones**, and then click **Next**.
    
  
6. In the **Users** box, type the user name for the Portal Super User account and then click **Check Names** to ensure that the account name can be resolved by the authentication providers on the application server.
    
  
7. In the **Choose Permissions** section, check the **Full Control - Has full control** box and then click **Finish**.
    
  
8. Repeat Steps 5 through 7 for the Portal Super Reader account.
    
  
9. In the **Choose Permissions** section, check the **Full Read - Has full read-only access** box.
    
  
10. Click **Finish**.
    
  
11. Make note of how the names for the Object Cache Super Reader and Object Cache Super User accounts are displayed in the **User Name** column. The displayed strings will be different depending on whether you are using claims authentication for the web application.
    
  
 **To add the user accounts to the web application by using Microsoft PowerShell**
1. Verify that you have the following memberships: 
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running PowerShell cmdlets.
    
  
  - Add memberships that are required beyond the minimums above.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Paste the following code into a text editor, such as Notepad:
    
  ```
  
$wa = Get-SPWebApplication -Identity "<WebApplication> "
$wa.Properties["portalsuperuseraccount"] = "<SuperUser> "
$wa.Properties["portalsuperreaderaccount"] = "<SuperReader> "
$wa.Update()
  ```

3. Replace the following placeholders with values:
    
  -  *<WebApplication>*  is the name of the web application to which the accounts will be added.
    
  
  -  *<SuperUser>*  is the account to use for the Portal Super User account as you saw it displayed in the **User Column** field mentioned in Step 14 of the previous procedure.
    
  
  -  *<SuperReader>*  is account to use for the Portal Super Reader account as you saw it displayed in the **User Column** field mentioned in Step 14 of the previous procedure.
    
  
4. Save the file, naming it SetUsers.ps1.
    
    > [!NOTE:]
      
5. Close the text editor.
    
  
6. Open **SharePoint Management Shell**.
    
  
7. Change to the directory where you saved the file.
    
  
8. At the PowerShell command prompt, type the following command: ./SetUsers.ps1
    
  
9. Reset Internet Information Services (IIS). For more information about IISReset, see  [Start or Stop the Web Server (IIS 8)](http://go.microsoft.com/fwlink/?LinkID=718159&amp;clcid=0x409).
    
  

# See also

#### 

 [Cache settings operations in SharePoint Server](html/cache-settings-operations-in-sharepoint-server.md)
  
    
    

  
    
    

