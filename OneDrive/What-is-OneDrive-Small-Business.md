---
title: OneDrive planning basics
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: get-started-article
ms.service: one-drive
localization_priority: Normal
ms.collection: Strat_OD_admin
description: "Learn about OneDrive in your small business."
---

# OneDrive planning basics

Small business deployment guide: Part 1 of 2

OneDrive for Business is a robust but simple-to-use cloud storage platform for small businesses, enterprises, and everything in between. Unlike other cloud storage providers, most of the advanced enterprise-focused features in OneDrive are available for every subscription type, enabling organizations to use OneDrive in whatever way benefits them the most. This guide focuses on the deployment and configuration options that make the most sense for small businesses looking to use OneDrive. From there, these organizations can select whatever additional management capabilities they require. For the full deployment guide, which contains other methods of deploying, configuring, and managing OneDrive, see [OneDrive feature overview](onedrive-feature-overview).

## Getting started with OneDrive

OneDrive is effective in even the largest enterprises, but it still has a small, easy-to-implement footprint that small businesses can take advantage of. After all, small businesses are often at highest risk for losing files on failed devices because few are concerned with centralized storage and backups. By using OneDrive, however, your small business can keep files safe, and your users can easily access them from all their devices.

To get started with OneDrive, follow these steps:

1.  **Review basic OneDrive information.** Start by reviewing the introductory OneDrive information available at the [OneDrive help center](https://support.office.com/onedrive). You’ll get answers to many of your questions, including the OneDrive experience and how it works.

2.  **Set up a Microsoft Office 365 subscription.** You must set up an Office 365 subscription to use OneDrive, but you aren’t required to purchase all the applications in the Office 365 suite. To get started, follow the steps in [Set up Office 365 for business](https://support.office.com/article/set-up-office-365-for-business-6a3a29a0-e616-4713-99d1-15eda62d04fa).

3.  **Add OneDrive licenses.** Review your plan options in [Compare OneDrive for Business plans](https://products.office.com/onedrive-for-business/compare-onedrive-for-business-plans), and then add the licenses you need.

When you’ve completed these tasks, you’re ready to plan for, deploy, and configure the OneDrive sync client and applications. To do that, complete these three simple steps:

1.  **Plan for adoption.** For small businesses, planning for user adoption can be as simple as individually showing your users how to use OneDrive. Often, small business customers don’t consider this step for new applications, and that can negatively affect the application’s success. The section [Adopt OneDrive](#_Adopt_OneDrive) provides helpful resources for OneDrive adoption.

2.  **Install and configure.** Sync clients are available for the Windows and macOS operating systems that provide a seamless experience for users interacting with their files. Most small businesses start by installing the sync client on their users’ devices, and then consider the OneDrive mobile apps later. In fact, you may already have the OneDrive client on your devices. Devices running the Windows 10 operating system and devices running Windows or macOS with Microsoft Office 2016 or later will have the OneDrive sync client already. For information about how to install and configure the OneDrive sync client and apps, see the section [Install and configure OneDrive](#_Install_and_configure).

3.  **Manage OneDrive.** For many small businesses, managing OneDrive is optional. You could simply install and configure OneDrive and leave it at that. If you want to use advanced features of OneDrive or add device sharing or access restrictions, however, you can easily manage those and other settings in the OneDrive admin center. For more information about managing OneDrive, see the section [Manage OneDrive](#_Manage_OneDrive).

## Key OneDrive features for small businesses

Unlike most other cloud storage providers, OneDrive not only provides robust features to small businesses out of the box, but it also makes most of its advanced features available to them. This gives small businesses the flexibility to use advanced features based on the needs of their organization. 

The features listed in this section address common customer concerns or specific compliance requirements, or provide unique functionality available only in OneDrive. For a full list of features available across OneDrive plans, see [Microsoft OneDrive](https://onedrive.live.com/about).

> [!NOTE]
> The information in this section is for awareness purposes only and is not required to install and use OneDrive.

### OneDrive Files On-Demand

OneDrive Files On-Demand enables users to view, search for, and interact with files stored in OneDrive from within File Explorer, without downloading all the files to their device. The feature provides a seamless look and feel for both OneDrive and local files without taking up space on the local hard drive. As shown in the following screenshot, files that have not been downloaded have a cloud icon for their status. For those files that have been downloaded, the status shows a green checkmark.

![Screenshot of Windows Explorer with some OneDrive files that have been downloaded and others that are only in the cloud](media/What-is-OneDrive-Small-Business_image1.png)

By default, files are downloaded only when you need to access them. However, if you plan to access a file while disconnected from the internet, simply make the file available offline by right-clicking it, and then selecting **Always keep on this device**. Alternatively, if you want to free space on your device and remove the downloaded copy of a file, right-click the file, and then select **Free up space**. The following screenshot shows the right-click menu for OneDrive files on a device running Windows.

![Screenshot of the OneDrive right-click menu, with options for "Always keep on this device" and "Free up space"](media/What-is-OneDrive-Small-Business_image2.png)

For more information about OneDrive Files On-Demand, see [Learn about OneDrive Files On-Demand](https://support.office.com/article/0e6860d3-d9f3-4971-b321-7092438fb38e).

### Modern attachments

OneDrive integrates with Microsoft Outlook to enable easy sharing of OneDrive files that appear just like email attachments. This feature provides a familiar sharing experience but centralizes storage of attachments in OneDrive. This allows your users to all collaborate on the same file instead of sending different versions bach and forth in email. In addition, you can configure sharing permissions on the files directly from within the Outlook client.

![Screenshot of Outlook with a modern attachment and the right-click menu showing permissions options](media/What-is-OneDrive-Small-Business_image3.png)

To reduce the potential for confusion when users choose to add a copy versus a link to attached OneDrive files, you can set the default behavior of the Outlook client, as demonstrated in [How to control default attachment state when you attach a cloud file in Outlook 2016](https://support.microsoft.com/help/4011261/how-to-set-attachment-preference-for-attaching-a-cloud-file-in-outlook).

### Files Restore

The OneDrive Files Restore feature lets users restore files to any point over the past 30 days. To select the desired recovery time, OneDrive presents you with a histogram that shows file activity so that you can determine which recovered time meets your needs. From there, simply select the file history entry to which you want to restore, and all changes after that point will be rolled back.

![Screenshot of the Restore my OneDrive page in Office 365](media/What-is-OneDrive-Small-Business_image4.png)

In addition, because the histogram shows individual activity on a file, you can use this feature to quickly view your files’ modification history. For more information about this feature, see [Announcing New OneDrive for Business feature: Files Restore](https://techcommunity.microsoft.com/t5/OneDrive-Blog/Announcing-New-OneDrive-for-Business-feature-Files-Restore/ba-p/147436).

### Recycle bin

OneDrive has a recycle bin similar to the one available on the Windows desktop. Deleted files are moved to the recycle bin and kept for a designated time before being permanently deleted. For work or school accounts, deleted files are purged after 93 days unless configured otherwise. For a demonstration of how the recycle bin works, see [Restore deleted files or folders in OneDrive](https://support.office.com/article/restore-deleted-files-or-folders-in-onedrive-949ada80-0026-4db3-a953-c99083e6a84f).

## Known Folder Move

Known Folder Move enables users to select Windows known folders, such as their desktop, Documents, or Pictures, to automatically synchronize to OneDrive. You can add this feature during the initial setup of OneDrive or after it has been configured. This capability provides a simple migration option for users looking to add known folders to their existing list of synchronized folders. For more information about Known Folder Move, see [Protect your files by saving them to OneDrive](https://support.office.com/article/protect-your-files-by-saving-them-to-onedrive-d61a7930-a6fb-4b95-b28a-6552e77c3057).

## Adopt OneDrive

User adoption is important to the overall success of any new application. Ideally, to feel that you have maximized your investment in Office 365 and OneDrive, you need to maximize user engagement with them. For small businesses, driving user adoption can be as simple as introducing users to OneDrive when you’re installing it or showing them any of the videos available at the [Office 365 Training Center](https://support.office.com/office-training-center?redirectSourcePath=%252fen-gb%252farticle%252foffice-training-center-b8f02f81-ec85-4493-a39b-4c48e6bc4bfb).

Personally showing your users how to save and share documents in OneDrive tends to be the most effective option for driving adoption, given that you’ll likely be performing manual installations. The primary value proposition for small businesses is file availability and redundancy. A document saved on local storage can be lost with a device; a document saved to OneDrive cannot. Simply having this discussion with your users beforehand, coupled with demonstrating the application’s ease of use, can drive positive outcomes for this effort.

For information about a more formal Microsoft 365 user adoption strategy, see the [Microsoft 365 End User Adoption Guide](https://fto365dev.blob.core.windows.net/media/Default/DocResources/en-us/Microsoft%20365%20User%20Adoption%20Guide.pdf). For more information about driving user engagement through a similar, more formal process, see [Success Factors for Office 365 End User Engagement](https://fto365dev.blob.core.windows.net/media/Default/DocResources/en-us/Resources/Office365_AdoptionBrochure_v2.0_Screen.pdf). You can also contribute to or comment on adoption-related ideas in the [Driving Adoption Tech Community](https://techcommunity.microsoft.com/t5/Driving-Adoption/ct-p/DrivingAdoption).


## Get started

When you're ready to start installing and configuring the OneDrive sync client and mobile apps, see Part 2, [OneDrive QuickStart guide for small businesses](One-Drive-Quickstart-Small-Business.md).

## See also

[Get started with OneDrive](https://support.office.com/article/Get-started-with-OneDrive-c7f31921-e2e5-4b00-959a-cc9ad6297de7)

[Why use OneDrive to store your docs](https://support.office.com/article/e55c4fa8-1e03-4d75-956b-924620bdfa2d)

[GDPR Compliancy with OneDrive and SharePoint](https://techcommunity.microsoft.com/t5/Microsoft-OneDrive-Blog/GDPR-Compliancy-with-OneDrive-and-SharePoint/ba-p/191126)

[Microsoft OneDrive Blog](https://techcommunity.microsoft.com/t5/OneDrive-Blog/bg-p/OneDriveBlog)

[OneDrive UserVoice](https://onedrive.uservoice.com/)

[OneDrive for Business Tech Community](https://techcommunity.microsoft.com/t5/OneDrive-for-Business/ct-p/OneDriveforBusiness)
