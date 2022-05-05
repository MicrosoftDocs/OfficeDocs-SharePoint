---
title: "Create an audience for SharePoint Server"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 8/14/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 91ab0b2c-8bb8-41e9-b662-324c661eb35f
description: "Learn how to use a Microsoft PowerShell script to create an audience."
---

# Create an audience for SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]

Learn how to use a Microsoft PowerShell script to create an audience.
  
## Create an audience by using a Microsoft PowerShell script

1. Verify that you meet the following minimum requirements:
    
  - See [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps&preserve-view=true).
    
  - You must read [about_Execution_Policies](/previous-versions//dd347641(v=technet.10)).
    
2. Copy the following variable declarations, and paste them into a text editor such as Notepad. Set input values specific to your organization. You will use these values in step 3. Save the file, and name it Audiences.ps1.
    
  ```
  ## Settings you may want to change for Audience Name and Description ## 
  $mySiteHostUrl = https://www.my.contoso.com
  $audienceName = "<Input name of audience>"
  $audienceDescription = "<Input description for audience>"
  $audienceRules = @()
  $audienceRules += New-Object Microsoft.Office.Server.Audience.AudienceRuleComponent("AccountName", "Contains", "jdoe")
  #Create an OR group operator between the two audience rules.
  $audienceRules += New-Object Microsoft.Office.Server.Audience.AudienceRuleComponent("", "OR", "")
  $audienceRules += New-Object Microsoft.Office.Server.Audience.AudienceRuleComponent("AccountName", "Contains", "jlew")
  
  ```

3. Copy the following code, and paste it into Audiences.ps1 beneath the variable declarations from step 2.
    
  ```
  #Get the My Site Host's SPSite object
  $site = Get-SPSite $mySiteHostUrl
  $ctx = [Microsoft.Office.Server.ServerContext]::GetContext($site)
  $audMan = New-Object Microsoft.Office.Server.Audience.AudienceManager($ctx)
  #Create a new audience object for the given Audience Manager
  $aud = $audMan.Audiences.Create($audienceName, $audienceDescription)
  $aud.AudienceRules = New-Object System.Collections.ArrayList
  $audienceRules | ForEach-Object { $aud.AudienceRules.Add($_) }
  #Save the new Audience
  $aud.Commit()
  #Compile the new Audience
  $upa = Get-SPServiceApplication | Where-Object {$_.DisplayName -eq "User Profile Service Application"}
  $audJob = [Microsoft.Office.Server.Audience.AudienceJob]::RunAudienceJob(($upa.Id.Guid.ToString(), "1", "1", $aud.AudienceName))
  
  ```

> [!NOTE]
> You can use a different file name, but you must save the file as an ANSI-encoded text file with the extension .ps1. 
  
4. Click SharePoint Management Shell.
    
5. Change to the directory to which you saved the file.
    
6. At the PowerShell command prompt, type the following command:
    
  ```
  ./Audiences.ps1 
  ```

For additional information about PowerShell scripts and .ps1 files, see [Running Windows PowerShell Scripts](/previous-versions/windows/it-pro/windows-powershell-1.0/ee176949(v=technet.10)).
  
For additional information about how to create audiences, see [AudienceRuleComponent class](/previous-versions/office/sharepoint-server/ms578007(v=office.15)).
