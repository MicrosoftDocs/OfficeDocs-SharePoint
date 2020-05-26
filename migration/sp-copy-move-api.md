# SharePoint and OneDrive Copy and Move API ( CreateCopyJobs)

## API Documention
The following API description is based upon use of the SharePoint Client Side Object Model (CSOM). We recommend using NuGet packages when you reference CSOM in your solution. You can find latest version of the SharePoint Online CSOM package from the NuGet library using the ID, Microsoft.SharePointOnline.CSOM.

>[!Note]
> The CreateCopyJob API is deprecated.

## Methods
CreateCopyJobs
This method creates a new copy or move job allows customer to copy or move a file or folder from one site in SharePoint/OneDrive/Team to another site. 

### Syntax
```cs
public List<SPCopyMigrationInfo> CreateCopyJobs(Uri[] exportObjectUris, Uri destinationUri, SPCopyMigrationOptions options)
```
   

### Parameter
|**Parameter**|**Description**|
|:-----|:-----|
|exportObjectUris|URL for the files or folders of a list which user want to copy or move|
|destinationUri|URL for the destination location|

SPCopyMigrationOptions
```cs
public bool IgnoreVersionHistory { get; set; }
```
Determine source version history should be copied or moved to the destination. 
</br>

```cs
public bool IsMoveMode { get; set; }
```
For move operation, please set this parameter to true 
</br>
```cs
public bool AllowSchemaMismatch { get; set; }
```
This allows the item to move even if the target has mismatched schema definition to the source list.
</br>
```cs
public bool AllowSmallerVersionLimitOnDestination { get; set; }
```

This allows the move to take place if the target file has smaller version . By default it’s disallowed to prevent data loss.
</br>
```cs
public SPMigrationNameConflictBehavior NameConflictBehavior { get; set; }
```
If name conflict occurs at target site, the default reports a failure.
</br>
```cs
 public bool IncludeItemPermissions { get; set; }
```
if specified, will the user ID in 
</br>
```cs
public SPMoveAndShareFileInfo MoveAndShareFileInfo { get; set; }
```

For move, specified the IDs of the users and can share file operation 

</br>
```cs
public bool BypassSharedLock { get; set; }
```
This indicates whether file with a share lock can still be moved in a move job

</br>
```cs
public string[] ClientEtags { get; set; }
```
If set, and the source eTag doesn’t match the eTag specified the copy and move won’t take place. If leaves NULL, no check will take place
</br>
```cs
public bool MoveButKeepSource { get; set; }
```
Once set, this move operation is similar to copy. The file will move to destination but the source content will not be deleted
</br>
```cs
public bool ExcludeChildren { get; set; }
```
For this operation, only the root level folder of the URL is being copied. The sub folders or files within the folder will not be moved or copied
</br>
### Output

|**Output parameter**|**Description**|
|:-----|:-----|
|JobID/GUID|Return a unique Job ID associated with this asynchronous read|
|SourceListItemUniqueIds |	Return the source |
|JobQueueUri	|URL for accessing Azure queue used for returning notification of copy and moveprocess|
|EncryptionKey|	AES256CBC encryption key used to decrypt messages from job/manifest queue|


```cs
public Uri JobQueueUri { get; set; } 
```
The reporting features are the same as they are for CreateMigrationJob. Logging is provided to track the status of the createCopyJobs. By default, blob queue permissions and settings are set to "all access”. It will provide job status : Job start, Job end, Job error information . 

### Limitations

Currently, the following limitations are:

|What|Limitation|
|:-----|:-----|
|File size|A file must be less than 2 GB.|
|Number of items|No more than 30,000 items in a job.|
|Total size of job| Job size not to exceed 100 GB.|





