---
ms.date: 11/09/2022
title: "SharePoint Migration Tool assessment risk errors "
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
- seo-marvel-mar2020
description: "Learn about the risk assessment errors in the SharePoint Migration Tool (SPMT)."
--- 

# SharePoint Migration Tool (SPMT) scan assessment error codes

The scan assessment feature is available only in SPMT 4.0 which is currently in public preview. To download, see [SPMT 4.0 public preview](https://aka.ms/spmt-beta-page).
To learn more about scan assessment, see [Scan and assess a SharePoint Server site with SPMT](/sharepointmigration/spmt-scan)].

|Error Code	|Description|User Action / Explanation|
|:-----	|:-----	|:-----	|:-----|
|FEATURE_UNSUPPORTED|Feature {0} is not supported|SPMT does not support custom features. Example, uploading a solution to SharePoint is a custom feature.|
|UNKNOWN_CONTENT_TYPE||SPMT does not support custom content types. |
|WORKFLOW_UNSUPPORTED|Workflow {0} in {1} is not supported|SPMT does not support custom workflows, and only some out of the box (OOTB) workflows.  Once SharePoint Designer workflow migration is enabled, only a few OOTB are not supported.| 
|LIST_TEMPLATE_UNSUPPORTED|List template is not supported|SPMT does not support hidden taxonomy lists and style libraries. However, this limitation doesn’t impact term store or site migration.|
|THICKET_FOLDER_UNSUPPORTED	|Thicket folder {0} is not supported|Folders that end with **_file** or **_files** are treated as a thicket folder, which can't be created in SharePoint Online. Rename the folder to ***Files**. SharePoint creates a hidden linked folder (thicket) to store the additional content, which cannot exist in the HTM file when you save a file as an HTM that contains content such as graphics. To avoid the confusion of mixing the thicket folder with the user-created folders, SharePoint doesn't allow these folders to be created.|
|PAGE_UNSUPPORTED|	Web part {0} is not supported|SPMT doesn’t support custom pages.  The exceptions are wiki and web part pages.|
|CUSTOM_SOLUTION_UNSUPPORTED|Solution {0} is not supported|	SPMT doesn’t support custom solutions.|	
|SITE_LOAD_FAILURE|	Invalid site URL '{0}'	|Check your SharePoint Server ULS log, or SPMT scan log for more details, then try again.  This unknown error occurs when loading site info. This error is not a  credential issue.|
|WEB_LOAD_FAILURE|Could not get web information in site '{0}'|Check your SharePoint Server ULS log, or SPMT scan log for more details, then try again.  This unknown error occurs when loading site info. This error is not a  credential issue.|
|SITE_USER_ERROR|Cannot access site groups|Check your SharePoint Server ULS log, or SPMT scan log for more details, then try again.  This unknown error occurs when fetching site users.|
|SITE_GROUP_ERROR|Cannot access site users|Check your SharePoint Server ULS log, or SPMT scan log for more details, then try again.  This unknown error occurs when fetching site groups.|
|TERM_STORE_ERROR|Fail to scan the source term store|Check your SharePoint Server ULS log, or SPMT scan log for more details, then try again.  This unknown error occurs when fetching term store info (term groups, term sets or terms).|
|LIST_LOAD_FAILURE|	Could not get list information	|Check your SharePoint Server ULS log, or SPMT scan log for more details, then try again.  This unknown error occurs when loading list info. This error is not a credential issue.|
|LIST_ITEM_LOAD_FAILURE|Populate list item meta info failed	|Check your SharePoint Server ULS log, or SPMT scan log for more details, then try again.  This unknown error occurs when fetching list items|
|CANNOT_ACCCESS	|Cannot access|	Check your SharePoint Server ULS log, or SPMT scan log for more details. If the auth is expired, then reauth and rescan. Also check if the user has permission on this site, web, or list.|
|LOOKUP_LIST_IN_UNKNOWN_WEB|Lookup column {0} in {1} refers to unknown list out of current scan scope.|Find the lookup list and include it within the migration scope by .json file.|
|LOOKUP_LIST_IN_PARENT_WEB|	Lookup column {0} in {1} refers to list in its parent web.|You need to migrate the parent web and the current site.|
|LIST_TARGET_AUDIENCE_ENABLED|Target audience is enabled. This list may be skipped during migration.|There's no 'audience targeting setting' in SharePoint Online.  Turn on the migration setting 'Skip list with audience targeting enabled' to skip this list. Otherwise, it's still migrated but the audience targeting is missing.|
|ITEM_COUNT_EXCEED_LIMIT|File count '{0}' exceeds limit '{1}'|SharePoint can store up to 30 million items per list. If item count exceeds 30 million, migration will fail. To learn more, see: [Manage large lists and libraries](https://support.microsoft.com/office/b8588dae-9387-48c2-9248-c24122f07c59)|
|ITEM_COUNT_EXCEED_INDEX_LIMIT|	File count '{0}' is too large to create index|	SharePoint Online has 20,000 index creation limit. If the item count exceeds 20,000, then adding column index is prohibited in that library. SPMT will give a warning in that case but won’t block migration.|
|LIST_VIEW_EXCEED_LIMIT	|The list view shows more than {0} items.| You may run into a list view threshold error in the classic experience.	SharePoint Online has a 5, 000 list view limit. This threshold is a barrier of efficient searching but won’t impact migration.|
|UNIQUE_PERMISSION_EXCEED_LIMIT|	Unique permissions per list should remain below {0} in total	|The supported limit of unique permissions for items in a list or library is 50,000. However, the recommended general limit is 5,000. Making changes to more than 5,000 uniquely permitted items at a time takes longer. Reduce the number of uniquely permitted items in a list or library.  Learn more: [Error when breaking SharePoint inheritance](/sharepoint/troubleshoot/lists-and-libraries/error-share-break-inheritance)|
|LIST_VIEW_LOOKUP_EXCEED_LIMIT	|The number of people, lookup, and managed metadata columns exceed list view lookup threshold. Please modify the resource throttling setting in the admin center.|	Displaying or querying 12 or more columns of the following types can cause scan failure: people, lookup, and managed metadata. Go to central admin, then select **Manage web application**.  Select the web application and then the drop-down **Resource Throttling** beneath *General Settings*.  Increase the value of **List View Lookup Threshold**.|
|PAGES_BLOCKED_COZ_NO_SCRIPT	|Web files might be blocked if custom script is disallowed in SharePoint admin center settings page.|	Turn on the migration setting 'Temporarily allow migration of scripts' (takes effect immediately) or go to Admin center and classic settings page.  Choose *allow users to run custom script* (can take up to 24 hours)   Learn more:  [Allow or prevent custom scripts](/sharepoint/allow-or-prevent-custom-script)|
