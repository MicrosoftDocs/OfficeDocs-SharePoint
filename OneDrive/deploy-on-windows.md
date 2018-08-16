---
title: "Deploy the new OneDrive sync client for Windows"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 08/16/2018
ms.audience: Admin
ms.topic: get-started-article
ms.service: one-drive
localization_priority: Priority
ms.collection: Strat_OD_admin
search.appverid:
- MET150
- ODB160
- MOE150
- MED150
- MBS150
- ODB150
ms.assetid: 3f3a511c-30c6-404a-98bf-76f95c519668
description: "Learn how to deploy the OneDrive sync client to your Office 365 organization."
---

# Deploy the new OneDrive sync client for Windows

This article is for IT administrators planning to deploy the new OneDrive sync client to their OneDrive for Business users in work or school environments. To install the OneDrive sync client for yourself, [download it](https://go.microsoft.com/fwlink/?linkid=844652) and read the [Sync files with the new OneDrive sync client in Windows](https://support.office.com/article/615391c4-2bd3-4aae-a42a-858262e42a49).
  
## Software requirements
<a name="Requirements"> </a>

The OneDrive sync client (OneDrive.exe) is supported on:
  
- Windows 10
    
- Windows 8.1
    
- Windows 8
    
- Windows 7
    
- macOS - for info about deploying the OneDrive sync client on macOS, see [Configure the new OneDrive sync client on macOS](deploy-and-configure-on-macos.md)
    
The OneDrive sync client doesn't yet support on-premises instances of OneDrive for Business (when your organization doesn't subscribe to Office 365). For more information about the restrictions and limitations of the OneDrive sync client, see [Restrictions and limitations when you sync files and folders using the new OneDrive sync client](http://go.microsoft.com/fwlink/p/?LinkId=717734).
  
## Planning
<a name="perform"> </a>

For info about estimating the network bandwidth users will need for syncing, see [Network utilization planning for the OneDrive sync client](network-utilization-planning.md). If your users have Windows 10 Fall Creators Update or later, we recommend using [Learn about OneDrive Files On-Demand](https://support.office.com/article/0e6860d3-d9f3-4971-b321-7092438fb38e), so you can deploy to a large number of users at once without causing network performance issues. Make sure you communicate the rollout to your users to set their expectations and give them guidelines and resources for working with OneDrive.
  
## Overview of the deployment process
<a name="Overview"> </a>

There are three steps in the process:
  
1. Install OneDrive.exe on your users' computers.
    
2. Start OneDrive processes and optionally prompt users to sign in with their work or school account.
    
3. Set your update ring (optional).
    
> [!IMPORTANT]
> If your users are currently using the OneDrive for Business sync client (Groove.exe), and you want to move them to the OneDrive sync client, see [Transition from the previous OneDrive for Business sync client](transition-from-previous-sync-client.md) before proceeding. 
  
## Step 1: Install OneDrive.exe
<a name="step2"> </a>

For the most part, you can deploy the new OneDrive sync client sync client like you would traditionally install applications on devices in your organization. If you're deploying to a large number of users, having familiarity with enterprise deployment tools such as System Center Configuration Manager (SCCM) to deploy .exe files and modify local system registries will be helpful.
  
### Check if users already have the OneDrive sync client

If the computers in your organization are running Windows 10, they already have the new sync client installed. If the computers have Office 2016 or Office 2013 (Home &amp; Student, Home &amp; Business, Professional, Personal, Home, or University) installed, they might also have the new sync client. Office is installed per machine, whereas OneDrive needs to be installed per user. If you plan on deploying Office to your organization, you will need to deploy OneDrive.exe separately for additional users on individual machines.
  
### Deploy any administrative settings

To set registry keys on computers in your domain, install OneDrive and copy the OneDrive.admx and OneDrive.adml files from %localappdata%\Microsoft\OneDrive\BuildNumber\adm\ to your Group Policy central store. For more info, see [Use Group Policy to control OneDrive sync client settings](use-group-policy.md).
  
### Use System Center Configuration Manager to deploy the OneDrive sync client

To deploy through System Center Configuration Manager, you can save the OneDriveSetup.exe installer for Windows to a local network share. [Download the Production ring OneDriveSetup.exe installer for Windows](https://go.microsoft.com/fwlink/?linkid=844652) or [download the Enterprise ring OneDriveSetup.exe installer for Windows](https://go.microsoft.com/fwlink/p/?linkid=860987). [Learn more about application management in Configuration Manager](https://go.microsoft.com/fwlink/p/?LinkId=535034).
  
> [!TIP]
> Try the [sample SCCM package](https://go.microsoft.com/fwlink/p/?LinkId=824069). Just update the OneDrive.exe path and the application owner. 
  
To install the OneDrive sync client on Windows, run the following command using System Center Configuration Manager:
  
```
Execute <pathToExecutable>\OneDriveSetup.exe /silent
```

(where pathToExecutable is a location on the local computer or an accessible network share).
  
> [!NOTE]
> This command must be run at user logon and using Administrator permissions. It must be run for each user on a machine. For an example of how to deploy an .exe on every user account, see [How to deploy the OneDrive sync client with SCCM](https://go.microsoft.com/fwlink/?linkid=839723).</br>If you run the command with no command line parameter, users will see the installation status. After installation, OneDriveSetup.exe will automatically execute OneDrive.exe and display OneDrive Setup to users. If you run the command with the /silent parameter, OneDrive.exe will be installed transparently and OneDrive Setup won't appear. You'll need to run OneDrive.exe with an additional command. If you want to control the launch of OneDrive across your organization, we recommend using the /silent parameter. 
  
The installer will install the OneDrive executable file under **%localappdata%\Microsoft\OneDrive**. 
  
### Deploy the RMS client to enable syncing IRM-protected files

The new OneDrive sync client for Windows now supports syncing IRM-protected SharePoint document libraries and OneDrive locations. To create a seamless IRM sync experience for your users, deploy to your users' computers the latest [Rights Management Service (RMS) client](https://aka.ms/odirm) from the Microsoft Download Center. Even if these computers have the Azure Information Protection client installed, which includes the RMS client, the OneDrive sync client still needs a separate installation of the RMS client from the Microsoft Download Center.
  
To silently install the RMS client on computers, use the /qn switch as part of the command-line options of the Microsoft Windows Installer Tool (Msiexec.exe). For example, the following command shows the silent mode installation (assuming the RMS Client installer package is already downloaded to C:\Downloads)
  
```
msiexec /qn c:\downloads\setup.msi
```

You can have the setup file on a network share and use managed software deployment to run the msiexec command.
  
> [!NOTE]
> The sync client does not support IRM policies that expire document access rights. 
  
## Step 2: Help users sign in
<a name="step3"> </a>

OneDrive doesn't support single sign in using existing Office or Windows credentials, but you can help users sign in to the sync client in these other ways:
  
- Use the following URL to start OneDrive Setup on users' computers. When users click to begin Setup, a sign-in window will appear for users can enter email address.
    
  ```
  odopen://launch
  ```

- Use the following URL with each user's email address to start Setup and prepopulate user email addresses in the sign-in window.
    
  ```
  odopen://sync?useremail=youruseremail@organization.com
  ```

If you want to auto-configure a SharePoint site to be synced, you can use the URL below as a guide to build the path to the SharePoint site you want to sync automatically. Replace HERE with the correct values for each component of the URL.
  
> [!NOTE]
> Replace special characters like the period (.), hyphen (-), and at sign (@) with the corresponding encoded values. For example, if the URL includes a hyphen, replace the hyphen with its encoded value, **%2D**. Additionally, you will need Client Side Object Model (CSOM) knowledge to query the team site to determine the appropriate SiteID, WebID and ListID to build the appropriate URL. 
  
```
odopen://sync/?siteId=SiteID_HERE&amp;webId=WebID_HERE&amp;listId=ListID_HERE&amp;userEmail=UserEmail_HERE&amp;webUrl=WebURL_HERE"
```

- Run the following command using System Center Configuration Manager (SCCM) script: 
    
  ```
  %localappdata%\Microsoft\OneDrive\OneDrive.exe 
  ```

    It starts the OneDrive process. If users haven't set up any accounts, it displays OneDrive Setup. To display OneDrive Setup specifically to users who haven't set up an account for your organization, use the command line parameter: 
    
  ```
   /configure_business:<tenantId>
  ```

> [!NOTE]
> When you use System Center Configuration Manager, make sure you run OneDrive.exe with User permissions (not as an Administrator). > For help finding your tenant ID, see [Find your Office 365 tenant ID](find-your-office-365-tenant-id.md). 
  
## Step 3: Set your update ring (Optional)
<a name="cad"> </a>

To delay updates to the OneDrive sync client, and control their deployment to your users, you can switch from the Production update ring to the Enterprise update ring. For more information about the update rings and how the sync client checks for updates, see [The OneDrive sync client update process](sync-client-update-process.md).
  
To set the update ring using Group Policy, enable the **Delay updating OneDrive.exe until the second release wave** setting. For more information about this setting, see [Use Group Policy to control OneDrive sync client settings](use-group-policy.md).
  
## See also
<a name="cad"> </a>

[Restrictions and limitations when you sync files and folders using the new OneDrive sync client](https://go.microsoft.com/fwlink/?LinkId=717734)

