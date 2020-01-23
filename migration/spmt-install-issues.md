---
title: Troubleshooting SPMT installation issues
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: troubleshooting
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Troubleshoot common installation errors in the SharePoint Migration Tool."
---
# Troubleshooting SPMT installation issues

If you are having trouble installing the SharePoint Migration Tool, this article provides information on the possible causes and steps to correct the problem.

If after troubleshooting you still are experiencing problems, consider downloading and installing the public preview (beta) of SPMT. It contains the latest updates and fixes.</br>
[Download SPMT Public Preview](https://spmtreleasescus.blob.core.windows.net/betainstall/default.htm) 

## **Common issues**

If you are having issues loading the SharePoint Migration tool, here are a few items that are commonly forgotten.

|**Item**|**Requirement**|
|:-----|:-----|
|System architecture| Must be x64|
|.Net version |Must be 4.6.2 or higher. See [How to determine which versions are installed](https://docs.microsoft.com/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed)|
|Microsoft Visual C++ 2015 Redistributable for X64.|SPMT is trying to add all the redistributions in packages, but missing some system dlls. Trying to install the package might help to resolve all the dependencies. Download: [Microsoft Visual C++ 2015 Redistributable Update 3 RC](https://www.microsoft.com/download/details.aspx?id=52685).|
|Anti-virus| Stop 3rd party anti-virus software on your computer prior to installation.


### Government cloud support

If you are on a government cloud, you must first take these steps:

1. Open microsoft.sharepoint.migration.common.dll.config.
2. Change the value of **SPOEnvironmentType** to 2.  

~~~XML
    <appSettings>
        <clear />
        <add key="SPOEnvironmentType" value="2" />
    </appSettings>
/configuration>

~~~

>[!Note]
>"0" = Worldwide consumer cloud
>"1" = Government Cloud computing
>"2" = Government Cloud computing high and DoD



2.  Double-click "microsoft.sharepoint.migrationtool.advancedapp.exe" to start SPMT.


### **Check to make sure all system prerequisites have been installed**

#### Requirements for best performance

|**Component**|**Recommendation**|
|:-----|:-----|
|CPU |64-bit quad core processor or better|
|RAM |16 GB |
|Local Storage|Solid state disk: 150 GB free space|
|Network card|1 Gbps|
|Operating system |Windows Server 2012 R2 or Windows 10 client  <br/> .NET Framework 4.6.2 |
|Microsoft Visual C++ 2015 Redistributable|Required for OneNote migration.|

</br>

#### Minimum requirements (expect slow performance)

|**Component**|**Requirement**|
|:-----|:-----|
|CPU  |64-bit 1.4 GHz 2-core processor or better |
|RAM|8 GB|
|Local Storage|Hard disk: 150 GB free space|
|Network card|High-speed Internet connection|
|Operating system|Windows Server 2008 R2, Windows 7 updated or better  <br/> .NET Framework 4.6.2|
|Microsoft Visual C++ 2015 Redistributable|Required for OneNote migration.|
   

## **Install errors**

|**Error**|**Suggested action**|
|:-----|:-----|
|"Application SharePoint Migration Tool is already installed from another location".|An unfinished installation may be the cause of this error. Uninstall the tool and then reinstall.|

</br></br>

## Required Endpoints

The following table lists the required endpoints for using the SharePoint Migration Tool.</br>


|**Required Endpoint**|**Why**|
|:-----|:-----|
|https://<spam><spam>secure.aadcdn.microsoftonline-p.<spam><spam>com|Authentication|
|https://<spam><spam>login.microsoftonline.<spam><spam>com|Authentication|
|https://<spam><spam>api.office.<spam><spam>com|Office 365 APIs for content move and validation|
|https://<spam><spam>graph.windows.<spam><spam>net|Office 365 APIs for content move and validation|
|https://<spam><spam>spmtreleasescus.blob.core.windows.<spam><spam>net|Installation|
|https://<spam><spam>*.queue.core.windows.<spam><spam>net|Migration API Azure requirement|
|https://<spam><spam>*.blob.core.windows.<spam><spam>net|Migration API Azure requirement|
|https://<spam><spam>*.pipe.aria.microsoft.<spam><spam>com|Telemetry/update|
|https://<spam><spam>*.sharepoint.<spam><spam>com|Destination for migratrion|




