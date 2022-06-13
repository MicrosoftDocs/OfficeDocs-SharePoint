---
title: "Install Microsoft Identity Manager for User Profiles in SharePoint Server"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 84972766-6527-4791-ae68-02d3a50b67f0
description: "Learn about Microsoft Identity Manager (MIM) and how it's used for importing user profile information in SharePoint Server."
---

# Install Microsoft Identity Manager for User Profiles in SharePoint Server

[!INCLUDE[appliesto-xxx-2016-2019-SUB-xxx-md](../includes/appliesto-xxx-2016-2019-SUB-xxx-md.md)]
  
 **Contents**
  
- [What is Microsoft Identity Manager?](#what-is-microsoft-identity-manager)
    
- [Choosing MIM for use with SharePoint Server](#choosing-mim-for-use-with-sharepoint-server)
    
- [Installing Microsoft Identity Manager (MIM)](#installing-microsoft-identity-manager-mim)
    
- [MIM configuration scenarios with SharePoint Server](#mim-configuration-scenarios-with-sharepoint-server)
    
> [!IMPORTANT]
> The solutions files referenced in this article are available for download [here](https://github.com/OfficeDev/PnP-Tools/tree/master/Solutions/UserProfile.MIMSync). You will need a GitHub account for access. For more information, see the section 'Download the solutions files that you need'. > Microsoft Identity Manager 2016 is available for download from the [Microsoft Volume Licensing Center](https://www.microsoft.com/Licensing/servicecenter/default.aspx). (Log in and search on the product name.) > On your MIM server, be sure to install [KB3092179](https://support.microsoft.com/kb/3092179).
  
## What is Microsoft Identity Manager?
<a name="BKMK_WhatIsMIM1"> </a>

Previous versions of SharePoint Server had a built-in copy of ForeFront Identity Manager (FIM) that ran inside SharePoint Server. That version of FIM powered the User Profile Synchronization for products like SharePoint Server 2010 and SharePoint Server 2013. But from SharePoint Server 2016, FIM has been removed in favor of Microsoft Identity Manager, which is the successor to the FIM technology. MIM is a separate server technology (not built-in to SharePoint Server). That means, if you have MIM running in your company, more than one SharePoint Server farm can rely upon it.
  
It's also important to note, here, that Active Directory Import (sometimes called Active Directory Direct Import) is also included with SharePoint Server, and is a User Profile Synchronization alternative that will not need a separate server installation. This means that SharePoint Server offers two options for User Profile Sync.
  
Which option is right for you?
  
|&nbsp;|&nbsp;|&nbsp;|
|:-----|:-----|:-----|
||**Microsoft Identity Management server** <br/> |**Active Directory Import** <br/> |
|Pros  <br/> |1. Flexibility allows for customized import.  <br/> 2. Can be customized for bidirectional flow.  <br/> 3. Imports user profile photos automatically.  <br/> 4. Supports non-Active Directory LDAP sources.  <br/> 5. Multi-forest scenarios are supported.  <br/> |1. Very fast and performant.  <br/> 2. Known to be reliable (used by Microsoft 365).  <br/> 3. Configurable inside of Central Administration. (Less complex.)  <br/> |
|Cons  <br/> |1. A separate MIM server is recommended for use with your SharePoint farm.  <br/> 2. The more customized the more complex the architecture, deployment, and management.  <br/> |1. Import is unidirectional (changes go from Active Directory to SharePoint Server Profile).  <br/> 2. Import from a single Active Directory forest only.  <br/> 3. Does not import user photos.  <br/> 4. Supports Active Directory LDAP only.  <br/> 5. Multi-forest scenarios are not supported.  <br/> |
   
> [!TIP]
> If you need details, or you need to set up Active Directory Import for your SharePoint Server installation? Try [these steps](./configure-profile-synchronization-by-using-sharepoint-active-directory-import.md). 
  
## Choosing MIM for use with SharePoint Server 
<a name="BKMK_ChooseMIM"> </a>

If you choose MIM, there are some **prerequisites** of which you should be aware. You will need:
  
1. For SharePoint Server 2016, a Windows Server 2012 R2 computer or virtual machine for the installation of MIM components. For SharePoint Server 2019, a Windows Server 2016 computer is required. For SharePoint Server Subscription Edition, a Windows Server 2019 computer is required.
    
2. SQL Server 2008 or above, to be installed either on the same machine as the MIM components, or remotely.
    
    > [!NOTE]
    > If you have SQL Server running on a  *separate*  server from MIM, you'll need to install SQL Server native client (either for [2008](/sql/sql-server/) or [2012](https://www.microsoft.com/download/details.aspx?id=29065)) where you installed MIM.
  
3. You'll need to create a service account in your domain to run the MIM Synchronization Service. This account should have the "Log on as a service" permissions granted to it on the machine where the MIM Synchronization Service will be installed. These permissions will normally be assigned automatically during setup of the service but can be manually assigned via the Local Security Policy (secpol.msc).
    
    > [!IMPORTANT]
    > If SQL Server is on the same server as MIM, you may use a local account for this service. However, if you use a  *remote*  SQL, you must use a domain account. If the account is in another domain from the SQL Server, it must be in the same forest. 
  
4. A domain user account must be created and [permissioned properly](./user-profile-service-administration.md) for use in the Active Directory Connector. 
    
5. The account running setup for MIM must be a SQL Server Admin on the instance of SQL Server where the MIM sync database will be hosted. The account must have local administrator permissions on the machine where the MIM Synchronization service will be installed.
    
6. Be sure that any accounts you maintain and use for testing/validation of the process have an email address configured in Active Directory. This will help you verify the success of your MIM configuration after import.
    
## Installing Microsoft Identity Manager (MIM)
<a name="BKMK_InstallMIM"> </a>

During these steps, you'll actually install three different elements essential to MIM. The first install will be of the MIM software, itself. You'll also need the SharePoint Management Agent.
  
1. First, download and install MIM to the server where you want to install.
    
2. Extract the .zip file and double-click Setup.exe. (Setup.exe is usually found in the SynchronizationService folder of the MIM media.)
    
3. Click **Next** > accept the end-user license agreement, and click **Next** through the feature selection screen. (You don't need to change the default selection.) 
    
4. The next screen in the wizard will ask you to supply some information about the instance of SQL Server that you want MIM to use. Choose This Computer if SQL Server is local, or type the name of the remote SQL Server instance. Indicate if SQL Server uses the default instance, or type the named instance. Click **Next**.
    
5. Next, you type the credentials you want to use to run the MIM service. You won't need to configure extra permissions or policies in SQL server for this account (whether SQL Server is local or remote).
    
    > [!NOTE]
    > If you're installing to a remote instance of SQL Server, the SQL Server Native Client must already be installed on the MIM server before you install the MIM Synchronization Service. 
  
6. Next, set up the security groups that are needed for MIM to function. You can leave these as default if you wish, but in that case your security groups will be created on the local machine were MIM is being installed. If you have more than one machine configured to run MIM, you may want to create these security groups in Active Directory (AD). Do this in the same domain as the machines where MIM is configured, and enter the group names into this page of the wizard.
    
7. The next step (firewall rules) is optional. We recommend you do not check the firewall rule checkbox.
    
8. Click to install MIM.
    
    > [!NOTE]
    > You may see a Warning here (Warning 25051). Click **OK** to continue. 
  
9. Next, the wizard will create a backup of the encryption key set that it has created.
    
    > [!NOTE]
    > You will need to backup the keys generated at this point if you are to move to another database server. Save these keys to a secure location and make certain you backup the key file along with the database backup so they're both available in a disaster recovery scenario. 
  
10. MIM installation should complete. You should log off and back onto your server again to ensure the MIM cache is updated.
    
11. Once you log on again, ensure the MIM service is running on the server by going to Services (or Start or Windows key> **Run** > services.msc) and then locating the **Forefront Identity Manager Synchronization Service**. No mistake. The service name has not changed!
    
### Install the SharePoint Management Agent (Forefront Identity Manager Connector for SharePoint)

SharePoint Management Agent (SPMA) is an essential if you need to connect MIM to your SharePoint Server installation. We'll install and configure it now.
  
1. You need to install the SPMA on the same server as is running MIM. Install the latest SPMA bits from [here](https://www.microsoft.com/download/details.aspx?id=41164).
    
2. Click **Download** and run the installation. You won't need to make any selections during this installation process. 
    
3. Restart the Forefront Identity Manager Synchronization Service (again, you can get to this via Start or Windows key > **Run** > services.msc)
    
4. Once the installation completes, check Programs and Features in Control Panel on your MIM server to ensure you see **Forefront Identity Manager SharePoint Connector**.
    
5. Launch the 'Synchronization Service' on the server to be certain that it opens. On a Windows Server 2012 R2 server, you'll find the icon for the Synchronization Service under Apps.
    
The Synchronization Service Manager will open on your MIM server. At this point you must configure MIM for use with SharePoint Server.
  
## MIM configuration scenarios with SharePoint Server
<a name="BKMK_ConfigScene"> </a>

For configuration steps, please see:
  
- [Use a sample MIM solution in SharePoint Server](use-a-sample-mim-solution-in-sharepoint-server.md)
