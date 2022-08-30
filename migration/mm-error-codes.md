---
title: "Migration Manager error codes"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- SPMigration
search.appverid: MET150
description: Migration Manager error codes
---

# Migration Manager transaction error codes

</br></br>

|Error code|Description |User action|
|:-----|:-----|:-----|
|MACCESSDENIED|User denied access.|Check permissions and try again.|
|MACCESSTOKENNULL|Failed to execute request as connector authorization failed.|Unexpected error. Try again.|
|MAUTHACCESSTOKEN|Connector authorization failure. Failed to get access token.|Unexpected error. Try again.|
|MAUTHACCESSTOKENINVALID|Connector authorization failure. The API request failed because the access token is invalid or expired.|Retry.|
|MAUTHCALLERNOTAUTHENTICATED|Connector authorization failed. The service is not allowing to connect as it does not recognize the caller.|Try again.|
|MAUTHMOVERAPP|Mover Application in Users Admin Account/tenant needs to be authorized.|To authorize this connector, you need to grant permissions to the Mover application. Try again.|
|MAUTHNOCODE|Connector authorization failed as auth code is not provided.|Try again.|
|MAUTHNOEMAIL|Connector authorization failure. Failed to get email from claim.|Unexpected error. Try again.|
|MAUTHNOIDTOKEN|Connector authorization failure. Failed to get ID token from access token.|Unexpected error. Try again.|
|MAUTHNOTENANT|Connector authorization failed; no tenant/enterprise ID found. Tenant = Enterprise. Tenant is the term in MS/Azure and Enterprise is used by Box and others.|Try again.|
|MAUTHREFRESHTOKEN|Connector authorization failure. Failed to get refresh token.|Try again.|
|MAUTHUSERNOTADMIN|Connector authorization failed; user does not have admin role.|Check permissions and try again.|
|MAZUREUPLOAD|Failed to submit the migration job to Migration API after the files were uploaded to the Azure blob.| Try again.|
|MBADREQUEST|Bad request when operating on source or destination item.|Unexpected error.  Try again.|
|MCONNECTORNOTFOUND|Connector not found in database.|Check connector settings.  Try again.|
|MCORRELATE|Collection correlates missing source listing.|Confirm source location, try again.|
|MDESTINATIONNOTWRITABLE|You do not have write access to the destination. |Check permissions and try again.|
|MDUPLICATE|Duplicate. This file already exists in your destination location.|Confirm file is in destination already.|
|MEMPTYMETADATA|Unable to find metadata. |Try again.|
|MEXPORTFILERESTRICTED|This file is restricted, and can’t be migrated from the source.|Check to see if this file has legal restrictions such as copyright claims.|
|MEXPORTFILEUNSUPPORTED|Unsupported file type. |You cannot migrate this file from the source.|
|MEXPORTFILEUNSUPPORTEDMIMETYPE|Unsupported file type.|You cannot migrate this file from the source. Check file at source.|
|MFAILEDGETROOTITEM|Failed to get root folder listing. This is set in both Google and Office365 connector|Try again.|
|MFILEIMPORT|This file type is not supported in the destination location. |Check source file.|
|MFILELOCKED|"File is locked, and cannot download or get metadata. |Unlock file.  Try again.|
|MFILENAMELENGTH|Filename exceeds maximum allowable length. |Rename file and try again.|
|MFILESIZEINCORRECT|Downloaded file is smaller than expected.|Check file for size and compare.  Try again.|
|MGETFOLDERACLS|Failure to get shared folder membership. |Check folder permissions and try again.|
|MHTTPCONNECTION|Connection failure.|Check your network and try again.|
|MINVALIDEMAIL|Invalid user email; unable to find user with that email. |Check user name and try again.|
|MINVALIDPAGESIZE|The page size for connector pagination must be greater than zero.|Try again.
|MINVALIDPARENTID|Item has no parent ID. Id-based connectors require the item to have a parent id.|Check file and try again.|
|MINVALIDPATH|Path is invalid.|Check path and try again.|
|MINVALIDRESPONSE|Invalid response from API call. |Try again.|
|MITEMPATHLENGTH|Item path exceeds length restrictions.|Check file path for length and try again.|
|MLARGEFILESIZEEXPORT|File exceeds maximum size for export from the source.|Check file size.|
|MLARGEFILESIZEIMPORT|File exceeds maximum allowed size for import into destination. |Check file size. |
|MLISTGROUP|API request to list groups for connector failed.| This may be caused by an invalid or throttling. Try again. |
|MLISTING|Folder listing failed.|Try again.|
|MLISTUSER|Failure to get user listing. This may be caused by an invalid requestor throttling. | Try again. |
|MLOCKACQ|Failed to acquire lock within timeout period and obtain new access token.|Try again.|
|MNONDESTRUCTIVEOPTIONENABLED| Unable to delete file or folder.|Try again.|
|MNOPARENT|Item does not have a parent item.|Check file and try again.|
|MNOTAFILE|The path refers to something that isn't a file.|Check the path and correct as necessary. Try again.|
|MNOTAFOLDER|The path refers to something that isn't a folder.|Check the path and correct as necessary.  Try again.|
|MNOTFOUND|Item not found.|Check file and try again.|
|MNOTIMPLEMENTED|Method not implemented for connector. |Try again.|
|MNOTPERMITTED|Cannot traverse to the folder level; cannot perform actions outside a users folder.|Check permissions and try again.|
|MNOTUSERORTEAMDRIVE|Confirm that the name of the item in the source service matches what you have in the task's source path. Note: Google Suite allows invisible characters to be added to item names. We advise that your rename the item in the source service to ensure there's no invisible characters and then use that same name in the task source path.|
|MOWNERNOTFOUND|The original owner was removed or its information was not found.|Reassign ownership of the file.|
|MPATHMALFORMED|Invalid path format. | Check your source and try again.|
|MSERVICENOTAVAILABLE|Service unavailable.|Try again.|
|MSETITEMPERMISSION|Failed to set permission. Failure may be caused by throttling.|Try again.|
|MSOURCENOTREADABLE|Unable to read the source directory. |Confirm source location. Try again.|
|MSTORAGEQUOTAREACHED|Storage quota exceeded for connector.|Increase storage limit and try again.|
|MTHROTTLE|API requests made by connector are getting throttled.|Try again.|
|MUNVERIFIEDPARENT|Item does not have a verified parent item. |Check file and try again.|
|MUPDATEITEMPERMISSION|Failed to remove permissions. |Try again.|
|MUSERCOUNT|Unexpected failure to get user count. |Try again.|
|MUSERFORBIDDEN|The current user does not have permission to access the file or folder.|Check permissions and try again.|
|MUSERINFONOTFOUND|User account info not found.|Check user info and try again.|
|MUSERNOTFOUND|User is not found; either it is disabled or deleted.|Check user and correct as necessary. Try again.|
|MUSERQUOTAREACHED|User quota limit reached.|Learn more: [Microsoft Graph error resonses and resource types](/graph/errors) |
|MZEROBYTEFILESIZEIMPORT|You cannot import a 0 byte file to a connector.|Check file and try again.|
|PFAIL|Failed to set permission|Check permissions and try again.|
|PFAILUNSUP|Unsupported file permissions not set.|Check permissions and try again.|
|PSUCCESS|Set permission successfully|
|PUNSUP|Unable to set permissions.|Check permission settings and try again.|
