---
title: "Create a custom dictionary"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 07/07/2015
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
ms:assetid: c686f4f8-deda-4e15-8fbb-b1e130f2c6d5
description: "Learn about word breakers, normalizations and thesaurus files, supported and unsupported entries, and supported languages."
---

# Create a custom dictionary

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]

A custom dictionary is a file that an administrator creates to specify tokens that the word breaker of a particular language should treat as indivisible at index time and at query time. Custom dictionary files are not provided with the product. You must create a separate custom dictionary for each language for which you want to modify the behavior of a word breaker.


> [!NOTE]
> A custom dictionary for a given language applies to all Search service applications in the server farm.



In this article:

  - Reasons to use a custom dictionary

  - Rules for creating a custom dictionary

  - Create a custom dictionary

  - Copy the custom dictionary to each application server

  - Stop and restart the SharePoint Server Search 14 service

  - Perform a full crawl

  - Supported languages

## Reasons to use a custom dictionary

To know whether you must have a custom dictionary and what entries it should contain, you must understand the behavior of word breakers. The indexing system uses word breakers to break tokens when it indexes crawled content, and the query processor uses word breakers in queries. In each case, if a custom dictionary exists that supports the language and dialect of the word breaker that is being used, the search system checks for the word in the custom dictionary before it determines whether to use a word breaker for that word. If the word does not exist in the custom dictionary, the word breaker performs its usual actions, which might result in breaking a token into multiple tokens. If the token exists in the custom dictionary, the word breaker does not perform any actions on that token. The following two examples describe typical word breaker behavior and how an entry in the custom dictionary can affect that behavior.

  - A word breaker might break the token “IT\&T” immediately before and after the ampersand (&), resulting in the three tokens “IT”, “&”, and “T”. However, if the token “IT\&T” is in the custom dictionary of the same language as the word breaker that is being used, the word breaker does not break that token (at crawl time or query time). If “IT\&T” is in the custom dictionary, and if a document does not contain "IT" or "T" but does contain "IT\&T", a query that contains "IT" or "T" but not "IT\&T" does not return that document in the results set.

  - Terms like Chemical Abstracts Service (CAS) registry numbers can be affected by word breakers. For example, word breakers typically split numbers that appear before or after a hyphen or other special character from the rest of the number. For example, the CAS registry number for oxygen is 7782-44-7. After word-breaker processing, this CAS registry number is broken into three parts: the numbers 7782, 44, and 7. Adding the CAS registry numbers that appear in a corpus to a custom dictionary directs the search system to index each number without breaking it into parts.

## Normalizations and thesaurus files

Named-entity normalizations, such as date normalizations, that are ordinarily applied by word breakers are not applied to terms that are in custom dictionaries. Instead, all terms that are in custom dictionaries are treated as a match. This is especially important if you have words or numbers in a thesaurus file. For example, if the CAS registry number 7782-44-7 is part of an expansion set in the thesaurus and the word breaker breaks that number at the hyphens into three separate numbers, the expansion set of which that number is a part might not work as expected. In this case, adding the CAS registry number 7782-44-7 to the custom dictionary of the appropriate language resolves the problem. For information about how to use thesaurus files, see [Create and deploy a thesaurus in SharePoint Server](create-and-deploy-a-thesaurus.md).

## Rules for creating a custom dictionary

A custom dictionary is a Unicode-formatted file. Each entry must be on a separate line, separated by a carriage return (CR) and line feed (LF). When you add entries to a custom dictionary, consider the following rules to avoid unexpected results:

  - Entries are not case-sensitive.

  - The pipe character (|) cannot be used.

  - White space cannot be used.

  - The number sign character (\#) cannot be used at the beginning of an entry but it can be used within or at the end of an entry.

  - Except for the pipe, number sign, and white-space characters previously mentioned, any alphanumeric characters, punctuation, symbols, and breaking characters are valid.

  - The maximum length of an entry is 128 (Unicode) characters.

The following table shows examples of supported and unsupported entries.

**Table 1 – Examples of supported and unsupported entries for custom dictionary files**


| Supported | Not supported |
| --- | --- |
| dogfood | dog food |
| 3# | #3 |
| For#sale | For\|sale |
| ASP.NET |  |
| IT&amp;T |  |
| (2-Methoxymethylethoxy)propanol |  |
| 34590-97-8 |  |
| C7H1603 |  |


The maximum limit to the number of entries in a custom dictionary is 10,000. There are no settings available to change this limit. However, we recommend that the total file size of a custom dictionary file does not exceed 2 gigabytes (GB). In practice, we suggest that you limit the number of entries to a few thousand.

## Create a custom dictionary

Use the following procedure to create a custom dictionary.

**To create a custom dictionary**

1.  Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.

2.  Log on to a crawl server.

3.  Open a new file in a text editor.
    
    Type the words that you want in the custom dictionary according to the rules stated in Rules for creating a custom dictionary earlier in this article.

4.  On the **File** menu, click **Save As**.

5.  In the **Save as type** list, select **All Files**.

6.  In the **Encoding** list, select **Unicode**.

7.  In the **File name** box, type the file name in the following format: Custom*NNNN*.lex, where “Custom” is a literal string, *NNNN* is the four-digit hexadecimal code of the language for which you are creating the custom dictionary, and lex is the file name extension. For a list of valid file names for supported languages and dialects, see Supported languages later in this article.

8.  In the **Save in** list, browse to the folder that contains the word breakers. By default, this folder is %ProgramFiles%\\Microsoft Office Servers\\14.0\\Bin for SharePoint Server 2010, %ProgramFiles%\\Microsoft Office Servers\\15.0\\Bin for SharePoint Server 2013 and %ProgramFiles%\\Microsoft Office Servers\\16.0\\Bin for SharePoint Server 2016 and SharePoint Server 2019.
    

    > [!NOTE]
    > Custom dictionary files can be used only if they are stored in this folder in the local file system. They cannot be used if they are only stored in a SharePoint site, for example.



9.  Click **Save**.

10. If there are no other crawl servers or query servers in the farm, go to Stop and restart the SharePoint Server Search 14 service. Otherwise, go to the next procedure, “Copy the custom dictionary to each application server in the farm”.

## Copy the custom dictionary to each application server

There must be a copy of the custom dictionary on each application server in the farm.

**To copy the custom dictionary to each application**

1.  Verify that the user account that is performing this procedure is a member of the Administrators group on each application server (that is, each crawl server or query server) in the farm.

2.  On each application server in the farm, copy the new custom dictionary file to the folder that contains the word breakers. By default, this folder is %ProgramFiles%\\Microsoft Office Servers\\14.0\\Bin for SharePoint Server 2010, %ProgramFiles%\\Microsoft Office Servers\\15.0\\Bin for SharePoint Server 2013 and %ProgramFiles%\\Microsoft Office Servers\\16.0\\Bin for SharePoint Server 2016 and SharePoint Server 2019.
    

    > [!NOTE]
    > Custom dictionary files can be used only if they are stored in this folder in the local file system. They cannot be used if they are only stored in a SharePoint site, for example.



## Stop and restart the SharePoint Server Search 14/15/16 service on each application server

You must restart the SharePoint Server Search 14 (for SharePoint Server 2010), SharePoint Server Search 15 (for SharePoint Server 2013) or SharePoint Server Search 16 (for SharePoint Server 2016 and SharePoint Server 2019)  service on each application server in the farm.


> [!IMPORTANT]
> Do not use the Services on Server page in Central Administration to stop and start the service. Doing so removes the service and deletes the index and the associated configuration. Instead, follow these steps.



**To stop and restart the SharePoint Server Search 14/15/16 service on each application server**

1.  Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.

2.  On the **Start** menu, point to **All Programs**, point to **Administrative Tools**, and then click **Services**.

3.  Right click the **SharePoint Server Search 14** (for SharePoint Server 2010), **SharePoint Server Search 15** (for SharePoint Server 2013) or **SharePoint Server Search 16** (for SharePoint Server 2016 and SharePoint Server 2019) service and then click **Properties**. The **Properties** dialog appears.

4.  Click **Stop**. After the service stops, click **Start**.

5.  Ensure that the **Startup type** is not set to **Disabled**.

6.  Repeat this procedure for each application server (that is, each crawl server and each query server) in the farm.

## Perform a full crawl

To apply the custom dictionary to the content index, you must perform a full crawl of the content that contains the tokens that you added to the custom dictionary. For information about performing a full crawl, see [Manage crawling in SharePoint Server](manage-crawling.md).

## Supported languages

The following table indicates the languages and dialects for which SharePoint Server 2010 supports custom dictionaries. You cannot create a custom dictionary for the language-neutral word breaker. The table includes the language code identifier (LCID) and language hexadecimal code for each supported language and dialect. The first two numbers in the hexadecimal code represent the dialect and the last two numbers represent the language. For languages that do not have separate word breakers for separate dialects, the first two numbers in the language hexadecimal code are always zeros.

**Table 2 - Supported languages**


| Language / dialect | LCID | Language hexadecimal code |
| --- | --- | --- |
| Arabic | 1025 | 0001 |
| Bengali | 1093 | 0045 |
| Bulgarian | 1026 | 0002 |
| Catalan | 1027 | 0003 |
| Croatian | 1050 | 001a |
| Danish | 1030 | 0006 |
| Dutch | 1043 | 0013 |
| English | 1033 | 0009 |
| French | 1036 | 000c |
| German | 1031 | 0007 |
| Gujarati | 1095 | 0047 |
| Hebrew | 1037 | 000d |
| Hindi | 1081 | 0039 |
| Icelandic | 1039 | 000f |
| Indonesian | 1057 | 0021 |
| Italian | 1040 | 0010 |
| Japanese | 1041 | 0011 |
| Kannada | 1099 | 004b |
| Latvian | 1062 | 0026 |
| Lithuanian | 1063 | 0027 |
| Malay | 1086 | 003e |
| Malayalam | 1100 | 004c |
| Marathi | 1102 | 004e |
| Norwegian_Bokmaal | 1044 | 0414 |
| Portuguese | 2070 | 0816 |
| Portuguese_Braz | 1046 | 0416 |
| Punjabi | 1094 | 0046 |
| Romanian | 1048 | 0018 |
| Russian | 1049 | 0019 |
| Serbian_Cyrillic | 3098 | 0c1a |
| Serbian_Latin | 2074 | 081a |
| Slovak | 1051 | 001b |
| Slovenian | 1060 | 0024 |
| Spanish | 3082 | 000a |
| Swedish | 1053 | 001d |
| Tamil | 1097 | 0049 |
| Telugu | 1098 | 004a |
| Ukrainian | 1058 | 0022 |
| Urdu | 1056 | 0020 |
| Vietnamese | 1066 | 002a |

