---
title: Configure the OneDrive for Business modern user experience
ms.prod: SHAREPOINT
ms.assetid: 94d4fecf-3250-42aa-8230-5890790e24db
---


# Configure the OneDrive for Business modern user experience
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2016-11-15* **Summary:** Learn how to turn the OneDrive for Business modern user experience on or off in SharePoint Server 2016.As part of the November 2016 public update for SharePoint Server 2016 (Feature Pack 1), a new modern user experience for OneDrive for Business is included. This modern user experience is turned on automatically when you install the public update. However, you can use Microsoft PowerShell to toggle the user experience off and on if you need to.The OneDrive for Business modern user experience requires an active  [Software Assurance](https://www.microsoft.com/en-us/licensing/licensing-programs/software-assurance-default.aspx) contract at the time it is enabled, either by installation of the PU or by manual enablement. If you don't have an active Software Assurance contract at the time of enablement, then you must turn the OneDrive for Business modern user experience off. **Turn the OneDrive for Business modern user experience off**Make sure you have  [permissions to administer SharePoint Server with Windows PowerShell](https://technet.microsoft.com/EN-US/library/ee806878%28v=office.16%29.aspx), and log in to a server in your SharePoint farm. Open the SharePoint 2016 Management Shell as administrator and run the following script:


```

$Farm = Get-SPFarm
$Farm.OneDriveUserExperienceVersion = [Microsoft.SharePoint.Administration.OneDriveUserExperienceVersion]::Version1
$Farm.Update()

```

 **Turn the OneDrive for Business modern user experience on**Make sure you have  [permissions to administer SharePoint Server with Windows PowerShell](https://technet.microsoft.com/EN-US/library/ee806878%28v=office.16%29.aspx), and log in to a server in your SharePoint farm. Open the SharePoint 2016 Management Shell as administrator and run the following script:


```

$Farm = Get-SPFarm
$Farm.OneDriveUserExperienceVersion = [Microsoft.SharePoint.Administration.OneDriveUserExperienceVersion]::Version2
$Farm.Update()

```


