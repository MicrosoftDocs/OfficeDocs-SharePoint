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

If your organization still uses SharePoint Server 2016 or earlier, users can't use the new OneDrive sync app (OneDrive.exe) to sync files. They need to use the previous OneDrive for Business sync app (Groove.exe). This article helps you install Groove.exe. If your organization uses SharePoint Server 2019, users should use the new OneDrive sync app (OneDrive.exe). [Learn more](/sharepoint/install/new-onedrive-sync-client)

> [!IMPORTANT]
> Support for the previous OneDrive for Business sync app (Groove.exe) with Microsoft 365 will end on January 11, 2021. Groove.exe will continue to work for files in SharePoint Server. [Learn how to transition to the new sync app](transition-from-previous-sync-client.md)

## Install Groove.exe with Office 2016

The previous sync app (Groove.exe) is no longer installed by default with Office 2016 Click-to-run. You need to use a custom installation to extract OneDrive.

### Use the installation wizard

1. [Download the OneDrive for Business 2016 installation wizard](https://aka.ms/diag_odbinstall).
2. Select **Run** or **Open**, and then follow the steps on the screen.

> [!NOTE]
> This wizard is in English only, but works if Office is installed in other languages. 

### Create a custom installation manually

1. Download the [Office Deployment Tool](https://www.microsoft.com/en-us/download/details.aspx?id=49117), and then save the file to your desktop.
2. From your desktop, double-click **OfficeDeploymentTool.exe**, and then extract the files to your desktop. 
   The following files will be displayed on your desktop:

    - Setup.exe
    - Configuration.xml

3. Create a file named **AddODB.txt** as follows:

    a. Start Notepad, and then paste the following text into a new file:

    ```XML
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
   > This file will install the 32-bit English-US edition of OneDrive. To install the 64-bit edition, change the value of OfficeClientEdition to 64. To install OneDrive in a different language, change the Language ID to a different language tag (ll-CC) by referring to the list of [Language identifiers](/DeployOffice/office2016/language-identifiers-and-optionstate-id-values-in-office-2016).

    b. Save the file to your desktop, and name it **AddODB**.

4. Open a command prompt as an administrator as follows:

    a. Select **Start**.

    b. In the **Start Search** box, enter **cmd**, and then press Ctrl+Shift+Enter.

    c. If the **User Account Control** dialog box appears, confirm that the action displayed is what you want, and then select **Continue**.

5. At the command prompt, run the following commands, and press **Enter** after each one.

    ```DOS
    cd /d %userprofile%\desktop setup.exe /configure AddODB.txt
    ```
   > [!NOTE]
   > The installation occurs silently in the background and can take 20 minutes or more to complete, depending on the speed of your Internet connection. Don't close the Command Prompt window during the installation. When the installation is completed, a new command line appears at the command prompt.

6. Select **Start**. In the **Start Search** box, type **OneDrive**, and then start OneDrive.

    > [!NOTE]
    > After you set up OneDrive, you might not see sync icons on files until you restart your computer.

7. Close the command prompt. You can now safely delete the following files from your desktop:

    - OfficeDeploymentTool.exe
    - Setup.exe
    - Configuration.xml
    - AddODB.txt

## Install Groove.exe with Office 2013

To install the previous OneDrive for Business sync app with Office 2013, follow these steps.

   > [!NOTE]
   > If you have Office Professional Plus 2013, Office 365 Enterprise E3, Office 365 Midsize Business, or Office 365 Small Business Premium, then you already have the OneDrive sync app installed.

1. Uninstall any earlier versions of the previous OneDrive for Business sync app.

2. Select one of the installer links below to download the installer for your language and system edition. If the 32-bit or 64-bit edition of Office is already installed, you must select the same edition for OneDrive.

|Language  |32-bit download link  |64-bit download link |
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
|Italian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&language=it-it&platform=x86&token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&taxregion=pr&source=olsfcrequest&version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&language=it-it&platform=x64&token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&taxregion=pr&source=olsfcrequest&version=o15ga) |\
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

    > [!NOTE]
    > The OneDrive sync app ships together with two components that are not selected for installation by default. We recommend that you do not change these default settings.

