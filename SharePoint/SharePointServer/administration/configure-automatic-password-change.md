---
title: "Configure automatic password change in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 5eccfa5b-05ec-46b6-935c-a2d8487965da
description: "Learn about how to configure the automatic password changes in SharePoint Server."
---

# Configure automatic password change in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Automatic password change enables SharePoint Server to automatically generate long, encrypted passwords on a schedule that you can determine. 
  
    
## Configure managed accounts
<a name="section1"> </a>

You have to register managed accounts together with the farm to make the accounts available to multiple services. You can register a managed account by using the Register Managed Account page in the SharePoint Central Administration website. There are no options on the Register Managed Account page to create an account in Active Directory Domain Services, or on the local computer. The options can be used to register an existing account on the SharePoint Server farm. Perform the steps in the following procedure to use Central Administration to configure managed account settings.
  
 **To configure managed account settings by using Central Administration**
  
1. Verify that the user account that is performing this procedure is a farm administrator.
    
2. On the Central Administration, select **Security**. 
    
3. Under **General Security**, click **Configure managed accounts**.
    
4. On the Managed Accounts page, click **Register Managed Account**.
    
5. In the **Account Registration** section of the Register Managed Account page, enter the service account credentials. 
    
6. In the **Automatic Password Change** section, select the **Enable automatic password change** check box to allow SharePoint Server to manage the password for the selected account. Next, enter a numeric value that indicates the number of days before password expiration that the automatic password change process will be initiated. 
    
7. In the **Automatic Password Change** section, select the **Start notifying by e-mail** check box, and then enter a numeric value that indicates the number of days before the initiation of the automatic password change process that an e-mail notification will be sent. You can then configure a weekly or monthly e-mail notification schedule. 
    
8. Click **OK**.
    
## Configure automatic password change settings
<a name="section2"> </a>

Use the Password Management Settings page of Central Administration to configure farm-level settings for automatic password changes. Farm administrators can configure the notification e-mail address that will be used to send all password change notification e-mails in addition to monitoring and scheduling options. Perform the steps in the following procedure to use Central Administration to configure automatic password change settings.
  
 **To configure automatic password change settings by using Central Administration**
  
1. Verify that the user account that is performing this procedure is a farm administrator.
    
2. On the Central Administration Home page, click **Security**. 
    
3. Under **General Security**, click **Configure password change settings**.
    
4. In the **Notification E-Mail Address** section of the Password Management Settings page, enter the e-mail address of one person or group to be notified of any imminent password change or expiration events. 
    
5. If automatic password change is not configured for a managed account, enter a numeric value in the **Account Monitoring Process Settings** section that indicates the number of days before password expiration that a notification will be sent to the e-mail address configured in the **Notification E-Mail Address** section. 
    
6. In the **Automatic Password Change Settings** section, enter a numeric value that indicates the number of seconds that automatic password change will wait (after notifying services of a pending password change) before starting the change. Enter a numeric value that indicates the number of times a password change will be tried before the process stops. 
    
7. Click **OK**.
    
## Troubleshooting automatic password change
<a name="section3"> </a>

Use the following guidance to avoid the most common issues that can occur when you configure automatic password change.
  
### Password mismatch

If the automatic password change process fails because there is a password mismatch between Active Directory Domain Services (AD DS) and SharePoint Server, the password change process can result in access denial at logon, an account lockout, or AD DS read errors. If any of these issues occur, make sure that your AD DS passwords are configured correctly and that the AD DS account has read access for setup. Use Microsoft PowerShell to fix any password mismatch issues that might occur, and then resume the password change process.
  
 **To correct for a password mismatch by using PowerShell**
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
   - Add memberships that are required beyond the minimums above.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. From the PowerShell command prompt, type the following:
    
   ```powershell
   Set-SPManagedAccount [-Identity] <SPManagedAccountPipeBind> -ExistingPassword <SecureString> -UseExistingPassword $true
   ```

   For more information, see [Set-SPManagedAccount](/powershell/module/sharepoint-server/Set-SPManagedAccount?view=sharepoint-ps).
    
### Service account provisioning failure

If service account provisioning or re-provisioning fails on one or more servers in the farm, check the status of the Timer Service. If the Timer Service has stopped, restart it. Consider using the following Stsadm command to immediately start Timer Service administration jobs:  `stsadm -o execadmsvcjobs`
  
If restarting the Timer Service does not resolve the issue, use PowerShell to repair the managed account on each server in the farm that has experienced a provisioning failure.
  
 **To resolve a service account provisioning failure**
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
   - Add memberships that are required beyond the minimums above.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. From the PowerShell command prompt, type the following:
    
   ```powershell
   Repair-SPManagedAccountDeployment
   ```

For more information, see [Repair-SPManagedAccountDeployment](/powershell/module/sharepoint-server/Repair-SPManagedAccountDeployment?view=sharepoint-ps).
    
If the previous procedure does not resolve a service account provisioning failure, it is likely because the farm encryption key cannot be decrypted. If this is the issue, use PowerShell to update the local server pass phrase to match the pass phrase for the farm.
  
 **To update the local server pass phrase**
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
   - Add memberships that are required beyond the minimums above.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. From the PowerShell command prompt, type the following:
    
   ```powershell
   Set-SPPassPhrase -PassPhrase <SecureString> -ConfirmPassPhrase <SecureString> -LocalServerOnly $true
   ```

For more information, see [Set-SPPassPhrase](/powershell/module/sharepoint-server/Set-SPPassPhrase?view=sharepoint-ps).
    
### Imminent password expiration

If the password is about to expire, but automatic password change has not been configured for this account, use PowerShell to update the account password to a new value that can be chosen by the administrator or automatically generated. After you have updated the account password, make sure that the Timer Service is started and the Administrator Service is enabled on all servers in the farm. Then, the password change can be propagated to all of the servers in the farm.
  
> [!NOTE]
> When an administrator performs a password change for the servers in the SharePoint search topology, there is an implied query downtime when the services are restarted. The query downtime is typically in the range of 3-5 minutes. 
  
 **To update the account password**
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
   - Add memberships that are required beyond the minimums above.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. To update the account password to a new automatically generated value, from the PowerShell command prompt, type the following:
    
   ```powershell
   Set-SPManagedAccount [-Identity] <SPManagedAccountPipeBind> -AutoGeneratePassword $true
   ```

For more information, see [Set-SPManagedAccount](/powershell/module/sharepoint-server/Set-SPManagedAccount?view=sharepoint-ps).
    
### Requirement to change the farm account to a different account

If you must change the farm account to a different account, use the following Stsadm command:  `stsadm.exe -o updatefarmcredentials -userlogin DOMAIN\username -password password`
  

