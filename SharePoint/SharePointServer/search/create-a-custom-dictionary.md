---
title: "Create a custom dictionary"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 07/07/2015
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms:assetid: c686f4f8-deda-4e15-8fbb-b1e130f2c6d5
description: "Learn about word breakers, normalizations and thesaurus files, supported and unsupported entries, and supported languages."
---

# Create a custom dictionary

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

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


<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Supported</th>
<th>Not supported</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>dogfood</p></td>
<td><p>dog food</p></td>
</tr>
<tr class="even">
<td><p>3#</p></td>
<td><p>#3</p></td>
</tr>
<tr class="odd">
<td><p>For#sale</p></td>
<td><p>For|sale</p></td>
</tr>
<tr class="even">
<td><p>ASP.NET</p></td>
<td><p></p></td>
</tr>
<tr class="odd">
<td><p>IT&amp;T</p></td>
<td><p></p></td>
</tr>
<tr class="even">
<td><p>(2-Methoxymethylethoxy)propanol</p></td>
<td><p></p></td>
</tr>
<tr class="odd">
<td><p>34590-97-8</p></td>
<td><p></p></td>
</tr>
<tr class="even">
<td><p>C7H1603</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>


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

8.  In the **Save in** list, browse to the folder that contains the word breakers. By default, this folder is %ProgramFiles%\\Microsoft Office Servers\\14.0\\Bin for SharePoint Server 2010, %ProgramFiles%\\Microsoft Office Servers\\15.0\\Bin for SharePoint Server 2013 and %ProgramFiles%\\Microsoft Office Servers\\16.0\\Bin for Sharepoint Server 2016 and SharePoint Server 2019.
    

    > [!NOTE]
    > Custom dictionary files can be used only if they are stored in this folder in the local file system. They cannot be used if they are only stored in a SharePoint site, for example.



9.  Click **Save**.

10. If there are no other crawl servers or query servers in the farm, go to Stop and restart the SharePoint Server Search 14 service. Otherwise, go to the next procedure, “Copy the custom dictionary to each application server in the farm”.

## Copy the custom dictionary to each application server

There must be a copy of the custom dictionary on each application server in the farm.

**To copy the custom dictionary to each application**

1.  Verify that the user account that is performing this procedure is a member of the Administrators group on each application server (that is, each crawl server or query server) in the farm.

2.  On each application server in the farm, copy the new custom dictionary file to the folder that contains the word breakers. By default, this folder is %ProgramFiles%\\Microsoft Office Servers\\14.0\\Bin for SharePoint Server 2010, %ProgramFiles%\\Microsoft Office Servers\\15.0\\Bin for SharePoint Server 2013 and %ProgramFiles%\\Microsoft Office Servers\\16.0\\Bin for Sharepoint Server 2016 and SharePoint Server 2019.
    

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


<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Language / dialect</th>
<th>LCID</th>
<th>Language hexadecimal code</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Arabic</p></td>
<td><p>1025</p></td>
<td><p>0001</p></td>
</tr>
<tr class="even">
<td><p>Bengali</p></td>
<td><p>1093</p></td>
<td><p>0045</p></td>
</tr>
<tr class="odd">
<td><p>Bulgarian</p></td>
<td><p>1026</p></td>
<td><p>0002</p></td>
</tr>
<tr class="even">
<td><p>Catalan</p></td>
<td><p>1027</p></td>
<td><p>0003</p></td>
</tr>
<tr class="odd">
<td><p>Croatian</p></td>
<td><p>1050</p></td>
<td><p>001a</p></td>
</tr>
<tr class="even">
<td><p>Danish</p></td>
<td><p>1030</p></td>
<td><p>0006</p></td>
</tr>
<tr class="odd">
<td><p>Dutch</p></td>
<td><p>1043</p></td>
<td><p>0013</p></td>
</tr>
<tr class="even">
<td><p>English</p></td>
<td><p>1033</p></td>
<td><p>0009</p></td>
</tr>
<tr class="odd">
<td><p>French</p></td>
<td><p>1036</p></td>
<td><p>000c</p></td>
</tr>
<tr class="even">
<td><p>German</p></td>
<td><p>1031</p></td>
<td><p>0007</p></td>
</tr>
<tr class="odd">
<td><p>Gujarati</p></td>
<td><p>1095</p></td>
<td><p>0047</p></td>
</tr>
<tr class="even">
<td><p>Hebrew</p></td>
<td><p>1037</p></td>
<td><p>000d</p></td>
</tr>
<tr class="odd">
<td><p>Hindi</p></td>
<td><p>1081</p></td>
<td><p>0039</p></td>
</tr>
<tr class="even">
<td><p>Icelandic</p></td>
<td><p>1039</p></td>
<td><p>000f</p></td>
</tr>
<tr class="odd">
<td><p>Indonesian</p></td>
<td><p>1057</p></td>
<td><p>0021</p></td>
</tr>
<tr class="even">
<td><p>Italian</p></td>
<td><p>1040</p></td>
<td><p>0010</p></td>
</tr>
<tr class="odd">
<td><p>Japanese</p></td>
<td><p>1041</p></td>
<td><p>0011</p></td>
</tr>
<tr class="even">
<td><p>Kannada</p></td>
<td><p>1099</p></td>
<td><p>004b</p></td>
</tr>
<tr class="odd">
<td><p>Latvian</p></td>
<td><p>1062</p></td>
<td><p>0026</p></td>
</tr>
<tr class="even">
<td><p>Lithuanian</p></td>
<td><p>1063</p></td>
<td><p>0027</p></td>
</tr>
<tr class="odd">
<td><p>Malay</p></td>
<td><p>1086</p></td>
<td><p>003e</p></td>
</tr>
<tr class="even">
<td><p>Malayalam</p></td>
<td><p>1100</p></td>
<td><p>004c</p></td>
</tr>
<tr class="odd">
<td><p>Marathi</p></td>
<td><p>1102</p></td>
<td><p>004e</p></td>
</tr>
<tr class="even">
<td><p>Norwegian_Bokmaal</p></td>
<td><p>1044</p></td>
<td><p>0414</p></td>
</tr>
<tr class="odd">
<td><p>Portuguese</p></td>
<td><p>2070</p></td>
<td><p>0816</p></td>
</tr>
<tr class="even">
<td><p>Portuguese_Braz</p></td>
<td><p>1046</p></td>
<td><p>0416</p></td>
</tr>
<tr class="odd">
<td><p>Punjabi</p></td>
<td><p>1094</p></td>
<td><p>0046</p></td>
</tr>
<tr class="even">
<td><p>Romanian</p></td>
<td><p>1048</p></td>
<td><p>0018</p></td>
</tr>
<tr class="odd">
<td><p>Russian</p></td>
<td><p>1049</p></td>
<td><p>0019</p></td>
</tr>
<tr class="even">
<td><p>Serbian_Cyrillic</p></td>
<td><p>3098</p></td>
<td><p>0c1a</p></td>
</tr>
<tr class="odd">
<td><p>Serbian_Latin</p></td>
<td><p>2074</p></td>
<td><p>081a</p></td>
</tr>
<tr class="even">
<td><p>Slovak</p></td>
<td><p>1051</p></td>
<td><p>001b</p></td>
</tr>
<tr class="odd">
<td><p>Slovenian</p></td>
<td><p>1060</p></td>
<td><p>0024</p></td>
</tr>
<tr class="even">
<td><p>Spanish</p></td>
<td><p>3082</p></td>
<td><p>000a</p></td>
</tr>
<tr class="odd">
<td><p>Swedish</p></td>
<td><p>1053</p></td>
<td><p>001d</p></td>
</tr>
<tr class="even">
<td><p>Tamil</p></td>
<td><p>1097</p></td>
<td><p>0049</p></td>
</tr>
<tr class="odd">
<td><p>Telugu</p></td>
<td><p>1098</p></td>
<td><p>004a</p></td>
</tr>
<tr class="even">
<td><p>Ukrainian</p></td>
<td><p>1058</p></td>
<td><p>0022</p></td>
</tr>
<tr class="odd">
<td><p>Urdu</p></td>
<td><p>1056</p></td>
<td><p>0020</p></td>
</tr>
<tr class="even">
<td><p>Vietnamese</p></td>
<td><p>1066</p></td>
<td><p>002a</p></td>
</tr>
</tbody>
</table>


