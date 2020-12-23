---
title: "Install the previous OneDrive sync client with Office and SharePoint"
ms.reviewer: 
ms.author: v-lsaldanha
author: Lovina-Saldanha
manager: dansimp
audience: Admin
f1.keywords:
- NOCSH
ms.topic: get-started-article
ms.service: one-drive
localization_priority: Normal
description: "In this article, you'll learn how to install the previous OneDrive sync client with Office and SharePoint."
---

# Install the previous OneDrive sync client with Office and SharePoint
> [!IMPORTANT]
> Support for the old OneDrive for Business sync app with SharePoint Online will end on January 11, 2021.
If you see this icon :::image type="content" source="media/cloud.png" alt-text=""::: OneDrive for business old icon on the right corner of your taskbar, read [this article](https://support.microsoft.com/en-us/office/upgrade-to-the-new-onedrive-sync-app-from-old-groove-exe-80156db5-5399-4c8b-bb2e-f5c2f2a4c31d) to learn more.

The previous OneDrive sync app lets users sync their OneDrive for work or school library, or Microsoft SharePoint or Microsoft 365 team site libraries, to their local computer. Here you can find the Click-to-Run installers for all supported languages of the previous OneDrive sync app (groove.exe).

> [!NOTE]
> This article is not intended for the current version of OneDrive (onedrive.exe). This article only applies to the previous OneDrive (groove.exe). In most cases, we recommend that you use onedrive.exe rather than groove.exe. For more information about the current version, see [Sync files with OneDrive in Windows](https://support.microsoft.com/en-us/office/sync-files-with-onedrive-in-windows-615391c4-2bd3-4aae-a42a-858262e42a49).
> To determine which OneDrive sync app you're using, see [Which OneDrive app?](https://support.microsoft.com/en-us/office/which-onedrive-app-19246eae-8a51-490a-8d97-a645c151f2ba)

If you have any Office 2016 application installed, such as Skype for Business 2016, you must have the 2016 version of OneDrive for work or school installed (see instructions below).

> [!NOTE]
> Office 2019 uses the onedrive.exe version, which is bundled with the software.
> If you run OneDrive with **Office 2010**, we recommend that you remove the SharePoint Workspace component from Office 2010. If you have a business requirement to run both SharePoint Workspace and OneDrive, upgrade Office 2010 to [Service Pack 2 (SP2)](https://support.microsoft.com/en-us/help/2687455/description-of-office-2010-service-pack-2) before you install OneDrive. This provides the best compatibility.
> If you run OneDrive on a **Mac**, see [Sync files with OneDrive on Mac OS X](https://support.microsoft.com/en-us/office/sync-files-with-onedrive-on-mac-os-x-d11b9f29-00bb-4172-be39-997da46f913f).
> For complete system requirements info, see [System requirements for Office](https://www.microsoft.com/en-us/microsoft-365/microsoft-365-and-office-resources).

## Installation instructions for Office 2016
For Office 2016, you will need to use a custom installation of Office 2016 to extract OneDrive.

### Let us fix this for you
To have us create a custom installation of Office 2016 to extract OneDrive, click [Download](https://aka.ms/diag_odbinstall).

In the **File Download** dialog box, select **Run** or **Open**, and then follow the steps in the easy fix wizard.

> [!NOTE]
> This wizard is in English only. However, the automatic fix also works for other language versions of Windows.
> If you aren't on the computer that has the problem, save the Fix it solution to a flash drive or a CD, and then run it on the computer that has the problem.

### Let me fix it myself
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

