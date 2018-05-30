---
title: "Redirect Windows known folders to OneDrive"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 5/21/2018
ms.audience: Admin
ms.topic: get-started-article
ms.prod: office-online-server
localization_priority: Normal
ms.collection: Strat_OD_admin
search.appverid:
- ODB160
- ODB150
- GOB150
- GOB160
ms.assetid: e1b3963c-7c6c-4694-9f2f-fb8005d9ef12
description: "Learn how to redirect users' Documents folders or other known folders to OneDrive. "
---

# Redirect Windows known folders to OneDrive

This article is for IT admins managing the OneDrive sync client in a Windows Server enterprise environment that uses Active Directory Domain Services. (If you're not an IT admin and want to automatically sync your Documents folder with OneDrive, see [Sync your Documents folder with OneDrive](https://support.office.com/article/0f4ddfd3-4a72-4013-9d94-181dab6be19a).)
  
There are two primary advantages of redirecting Windows known folders (such as Documents) to the OneDrive for Business sync location for the users in your domain:
  
- Your users can continue using their Documents and other similar folders. They don't have to change their daily work habits to use OneDrive.
    
- Using OneDrive for your documents gives you a backup of your data in the cloud and gives you access to your documents from any device.
    
For these reasons, we recommend setting up folder redirection if you're an enterprise or large organization. Small or medium businesses may also find this useful, but keep in mind you'll need some experience with Group Policy and data migration to follow the procedures below.
  
## How it works

Here's an overview of what we'll be configuring in this article:
  
1. We'll set a policy at the domain level to make sure users all sync to the same folder when they install the OneDrive sync client.
    
2. We'll set additional policies to redirect the Documents folder to that sync location.
    
When users sign in on their computers, Group Policy will detect if the OneDrive folder exists in the specified location. If the folder doesn't exist (for example, if the user hasn't set up the sync client yet or if this is the first time they've signed in on the computer), the Documents folder will not be redirected. If the folder does exist, the Documents folder will be redirected to the OneDrive folder.
  
Once the Documents folder has been redirected, shortcuts to Documents - such as those in File Explorer - will point to the new location. However, the original folder and its contents will remain at its previous location under %userprofile%\Documents. You can then migrate any files from the original folder to OneDrive, and delete the original folder if desired.
  
## Before you begin

There are a number of things to consider in determining if redirecting known folders to OneDrive is a good solution for your organization:
  
- OneDrive has some [restrictions around file naming, file size, and file type](https://go.microsoft.com/fwlink/p/?LinkId=717734), that you should review before deploying new OneDrive sync client. Keep in mind that your users may try to use files of these types with OneDrive, or the OneDrive sync client may try to sync them when you redirect users' Documents folders.
    
- If your users have used the Documents folder as an installation location for some legacy applications, the applications may no longer work after the folder has been redirected. If your organization uses legacy applications that were not written to support folder redirection, be sure to test them before redirecting folders to OneDrive.
    
- If your users' Documents folders contain items with a very high frequency of updates - such as databases, web servers, or Outlook OST files - we recommend not redirecting these folders to OneDrive. While such files should continue to function normally, the high frequency of sync activity due to constantly changing files may cause network and performance issues.
    
If you're already redirecting known folders to a different location--for example, a network share--or if you have already deployed the new OneDrive sync client, then there are some additional planning considerations:
  
- If known folders are currently redirected to a network share or other location, you will need to migrate the data from that location to OneDrive after you redirect the known folders to OneDrive.
    
- After you redirect known folders to OneDrive using the procedures in this article, existing files in known folders will remain on users' computers and need to be manually moved to each user's OneDrive folder. We suggest using [xcopy](https://go.microsoft.com/fwlink/?linkid=871856) or [robocopy](https://go.microsoft.com/fwlink/?linkid=871855) scripting as an automated way of moving the files for your users. 
    
- To redirect known folders to OneDrive, users must be syncing their OneDrive files to the default location (%userprofile%\OneDrive -  _\<TenantName\>_). Known folders can't be redirected to a different location.
    
- If your users have a large amount of data that will be uploaded to OneDrive, you may want to stage your deployment to limit the impact on your network.
    
## Prerequisites and baseline environment

The procedures in this article require a particular existing configuration to exist in order to work. Check these prerequisites before you get started:
  
- Make sure you installed the [OneDrive for Business Group Policy objects](use-group-policy.md) on your domain. 
    
- Make sure any existing OneDrive users in your organization are syncing their files to the default sync location (%userprofile%\OneDrive -  _\<TenantName\>_). Users who are syncing files to a different location will not have their known folders redirected to OneDrive.
    
- All of the procedures in this article are performed in your domain Group Policy editor. You need to be a domain administrator to perform these procedures.
    
## Redirecting known folders to OneDrive

The first step in redirecting known folders to OneDrive is to make sure users sync their OneDrive to the default location when they set up the sync client. We do this through a domain policy.
  
 **To prevent users from changing the location of their OneDrive folder**
  
1. In your domain Group Policy editor, under **User Configuration\Policies\Administrative Templates\OneDrive**, double-click **Prevent users from changing the location of their OneDrive folder**.
    
2. Select the **Enabled** option, and then click **OK**.
    
The next step is to create an environment variable for the OneDrive folder. Group Policy won't let us redirect known folders directly to a different location under %userprofile%, so we need to create a new environment variable that contains the location of the folder under %userprofile%.
  
We'll use item-level targeting in this environment variable to prevent folders from being redirected until the folder has been created by the sync client.
  
 **To create an environment variable for the OneDrive folder**
  
1. In your domain Group Policy editor, under **User Configuration\Preferences\Windows Settings**, right-click **Environment**, click **New**, and then click **Environment Variable**.
    
2. In the **Name** box, type OneDriveSync.
    
3. In the **Value** box, type %userprofile%\\<SyncFolder\>.
    
     _\<SyncFolder\>_ is the name of your default folder. For example, **OneDrive - Contoso**.
    
4. On the **Common** tab, select the **Item-level targeting** check box, and then click **Targeting**.
    
5. In the Targeting Editor, click **New Item**, and then click **File Match**.
    
6. Choose **Folder exists** from the **Match type** drop down list. 
    
7. In the **Path** box, type %userprofile%\\<SyncFolder\> (the same path that you used in step 3). 
    
8. Click **OK**.
    
9. Click **OK**.
    
Now it's time to configure the known folders redirection itself.
  
Note that we do not support having existing content automatically migrated by Group Policy to the OneDrive folder. (See the warning in the procedure below). With automatic file migration, there is a potential for data loss in cases where there are files in both locations that have matching file names.
  
 **To redirect Documents folders to OneDrive**
  
1. In your domain Group Policy editor, under **User Configuration\Policies\Windows Settings\Folder Redirection**, right-click **Documents** and click **Properties**.
    
2. From the **Settings** drop down list, choose **Basic - Redirect everyone's folder to the same location**.
    
3. Under **Target folder location**, choose **Redirect to the following location**.
    
4. In the **Root Path** box, type %OneDriveSync%\Documents.
    
5. On the **Settings** tab, clear the **Move the contents of Documents to the new location** check box. 
    
    > [!NOTE]
    > Leaving this setting enabled could result in data loss when the contents of the Documents folder is merged with the OneDrive folder, if there are files with the same name in both locations. 
  
6. Click **OK**.
    
We've now set the Documents folder to redirect to the OneDrive folder. You can also easily redirect related known folders - Picture, Music, or Videos - by having them follow the redirection of the Documents folder. If you want to do this, use the following procedure.
  
 **To redirect related folders to the OneDrive folder**
  
1. In your domain Group Policy editor, under **User Configuration\Policies\Windows Settings\Folder Redirection**, right-click the related folder that you want to redirect - **Pictures**, **Music**, or **Videos** - and click **Properties**.
    
2. In the **Setting** drop down list, choose **Follow the Documents folder**.
    
3. Click **OK**.
    
Now that folder redirect has been configured, users' known folders will be redirected to their OneDrive folder once their OneDrive sync client has been set up. Once the redirect is in place, you'll need to migrate the user's data from the original location on their local disk to the OneDrive folder.
  
Keep in mind that as new users and computers come online over time, users may still save files to their Documents folder before they configure the OneDrive sync client, and these files would then need to be moved to the OneDrive folder after the redirect takes place.
  

