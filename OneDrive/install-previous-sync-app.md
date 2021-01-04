---
title: "Install the previous OneDrive sync app"
ms.reviewer: garezni
ms.author: kaarins
author: kaarins
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
ms.topic: get-started-article
ms.service: one-drive
localization_priority: Normal
description: "In this article, you'll learn how to install the previous OneDrive sync app (Groove.exe) for use with SharePoint Server."
---

# Install the previous OneDrive sync app 

If your organization still uses SharePoint Server 2016 or earlier, users will need to use the previous OneDrive for Business sync app (Groove.exe) to sync files. This article provides links to the Click-to-Run installers for all supported languages of the previous OneDrive sync app. If your organization uses SharePoint Server 2019, users should use the new OneDrive sync app (OneDrive.exe). [Learn more](/sharepoint/install/new-onedrive-sync-client). 

> [!IMPORTANT]
> Support for the previous OneDrive for Business sync app (Groove.exe) will end on January 11, 2021. On February 1, 2021, users will no longer be able to sync OneDrive or SharePoint files in Microsoft 365 by using Groove.exe. Groove.exe will continue to work only for files in SharePoint Server. [Learn how to transition to the new sync app](transition-from-previous-sync-client.md)

## Installation instructions for Office 2016

For Office 2016, you need to use a custom installation of Office 2016 to extract OneDrive. [Download a wizard to do this]()

> [!NOTE]
> Office 2019 includes the new OneDrive sync app (OneDrive.exe).

### Download the easy fix wizard

1. [Download the easy fix wizard](https://aka.ms/diag_odbinstall).
2. In the **File Download** dialog box, select **Run** or **Open**, and then follow the steps on the screen.

> [!NOTE]
> This wizard is in English only. However, the automatic fix also works for other language versions of Windows.
> If you aren't on the computer that has the problem, save the Fix it solution to a flash drive or a CD, and then run it on the computer that has the problem.

### Create a custom installation manually

To use a custom installation of Office 2016 to extract OneDrive, follow these steps:

1. Download the [Office Deployment Tool](https://www.microsoft.com/en-us/download/details.aspx?id=49117), and then save the file to your desktop.
2. From your desktop, double-click **OfficeDeploymentTool.exe**, and then extract the files to your desktop. 
   The following files will be displayed on your desktop:

    - Setup.exe

    - Configuration.xml

3. Create a file named **AddODB.txt** as follows:

    a. Start Notepad, and then paste the following text into a new file:
```
        <Configuration>
          <Add SourcePath="http://officecdn.microsoft.com/pr/492350f6-3a01-4f97-b9c0-c7c6ddf67d60/" OfficeClientEdition="32" >
            <Product ID="O365BusinessRetail">
              <Language ID="en-us" />
              <ExcludeApp ID="Access" />
              <ExcludeApp ID="Excel" />
              <ExcludeApp ID="Lync" />
              <ExcludeApp ID="OneNote" />
              <ExcludeApp ID="Outlook" />
              <ExcludeApp ID="PowerPoint" />
              <ExcludeApp ID="Publisher" />
              <ExcludeApp ID="Word" />
            </Product>
          </Add>
          <Display Level="None" AcceptEULA="TRUE" />
        </Configuration>
```
> [!NOTE]
- > This file will install the 32-bit English-US version of OneDrive. If you have to have the 64-bit version, change the text in the second line that reads OfficeClientEdition="32" to the following: **OfficeClientEdition="64"**
- > If you have to have a language other than English-US, change the Language ID="en-us" text to the following:
**Language ID="<ll-cc>"**
> To find the appropriate value of the <ll-cc> placeholder to match your language, go to the following Microsoft website:
> [Language identifiers](https://docs.microsoft.com/DeployOffice/office2016/language-identifiers-and-optionstate-id-values-in-office-2016?redirectedfrom=MSDN#bkmk_languageidentifiers)

    b. Save the file to your desktop, and name it **AddODB**.

4. Open a command prompt as an administrator as follows:

    a. Select **Start**.

    b. In the **Start Search** box, type **cmd**, and then press Ctrl+Shift+Enter.

    c. If the **User Account Control** dialog box appears, confirm that the action displayed is what you want, and then select **Continue**.

5. At the command prompt, type the following commands, and press **Enter** after typing each one:
```
    `cd /d %userprofile%\desktop setup.exe /configure AddODB.txt`
```
    > [!NOTE]
    > The installation occurs silently in the background and can take 20 minutes or more to complete, depending on the speed of your Internet connection. Don't close the Command Prompt window during the installation.
    > When the installation is completed, a new command line appears at the command prompt.

6. Select **Start**. In the **Start Search** box, type **OneDrive**, and then start OneDrive.

    > [!NOTE]
    > After you set up OneDrive, you may not see the sync icon overlays (that is, the green check marks or red crosses) on files and folders. You must restart your computer to enable the sync icon overlays to reappear.

7. Close the command prompt. You can now safely delete the following files from your desktop:

    - OfficeDeploymentTool.exe

    - Setup.exe

    - Configuration.xml

    - AddODB.txt

## Installation instructions for Office 2013
To install the OneDrive sync app, follow the steps below.

    > [!NOTE]
    > If you have Office Professional Plus 2013, Office 365 Enterprise E3, Office 365 Midsize Business, or Office 365 Small Business Premium, then you already have the OneDrive sync app installed.

1. Uninstall any earlier versions of OneDrive for work or school.

2. Select one of the installer links below to download the OneDrive for work or school installer for your language and system edition. If you are already running a 32-bit or 64-bit edition of Office, you must select the same edition type for OneDrive for work or school.

|Language version   |32-bit download link  |64-bit download link |
|-------------------|----------------------|---------------------|
|Arabic             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Bulgarian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Chinese (Simplified)             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Chinese (Traditional)             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Croatian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Czech             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Danish             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Dutch            |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|English             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Estonian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Finnish             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|French             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) | |\
|German             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Greek             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Hebrew             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Hindi             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Hungarian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Indonesian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Italian             |\
|Japanese             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Kazakh             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Korean             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Latvian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Malay(Malaysia)             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Norwegian(Bokmal)            |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Polish             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Portuguese(Brazil)             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Portuguese(Portugal)             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Romanian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Russian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Serbian(Latin)             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Slovak             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Slovenian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Spanish             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Swedish             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Thai             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Turkish             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Ukrainian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\
|Vietnamese             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |\

3. Run the downloaded file to start the Setup program.

4. Follow the instructions to complete the installation.

5. If you are asked to provide a license key, enter **3V9N8-W93CC-FQPB8-Y9WVF-TVGJ3**.

6. Open your personal OneDrive for work or school document library (or open any SharePoint 2013 or Microsoft 365 website document library), then select **Sync** to sync the libraries.

    > [!NOTE]
    > The OneDrive sync app ships together with two components that are not selected for installation by default. We recommend that you do not change these default settings.

## Uninstalling the OneDrive sync app
To uninstall the OneDrive sync app:

1. Select **Start**, and then select **Control Panel**.

2. Select **Programs**.

3. Under **Programs and Features**, select **Uninstall a program**.

4. In the list of currently installed programs, right-click **OneDrive**, and then select **Uninstall**.

## References
[Configure syncing with the new OneDrive sync app](https://docs.microsoft.com/sharepoint/install/new-onedrive-sync-client)

[OneDrive for Windows](https://www.microsoft.com/microsoft-365/onedrive/download)

[Description of Office 2010 Service Pack 2](https://support.microsoft.com/help/2687455/description-of-office-2010-service-pack-2)

[Service Pack 2 for Microsoft Office 2010 (KB2687455) 32-Bit Edition](https://support.microsoft.com/help/2687455/description-of-office-2010-service-pack-2)

